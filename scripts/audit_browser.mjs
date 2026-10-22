#!/usr/bin/env node
// Isolated, offline rendering of saved responses. No requests reach the network.
import { chromium } from 'playwright';
import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const manifest = JSON.parse(await fs.readFile(process.argv[2], 'utf8'));
const output = manifest.output;
const width = 1280;
const height = 900;
const maxHeight = 50000;
const sha = value => crypto.createHash('sha256').update(value).digest('hex');
const [browserDir, screenshotDir] = [path.join(output, 'browser'), path.join(output, 'screenshots')];
await fs.mkdir(browserDir, { recursive: true });
await fs.mkdir(screenshotDir, { recursive: true });
const launch = { headless: true, args: ['--disable-background-networking'] };
if (manifest.executablePath) launch.executablePath = manifest.executablePath;
const browser = await chromium.launch(launch);
const resourceFiles = [...new Set(Object.values(manifest.resources).flatMap(map => Object.values(map).map(item => item.file)))].sort();
const dependencies = [];
for (const file of resourceFiles) dependencies.push([file, sha(await fs.readFile(file))]);
const configuration = sha(JSON.stringify({ width, height, maxHeight, browser: browser.version(),
  script: sha(await fs.readFile(fileURLToPath(import.meta.url))), dependencies, resources: manifest.resources }));
let completed = 0;
let reused = 0;
let stopped = false;
process.on('SIGINT', () => { stopped = true; });
process.on('SIGTERM', () => { stopped = true; });

function originalResource(url) {
  const parsed = new URL(url);
  parsed.hash = '';
  let item = manifest.resources.original[parsed.href];
  if (item) return item;
  // HTTP/HTTPS and www variants of the captured first-party resource identify
  // the same saved asset. Query strings remain significant except ?ver=.
  if (['justaddwater.dk', 'www.justaddwater.dk'].includes(parsed.hostname)) {
    parsed.protocol = 'http:';
    parsed.hostname = 'justaddwater.dk';
    item = manifest.resources.original[parsed.href];
    if (item) return item;
    if ([...parsed.searchParams.keys()].every(k => k === 'ver')) {
      parsed.search = '';
      return manifest.resources.original[parsed.href];
    }
  }
  return undefined;
}

async function render(row, side) {
  const context = await browser.newContext({ viewport: { width, height }, deviceScaleFactor: 1,
    locale: 'en-GB', timezoneId: 'Europe/Copenhagen', serviceWorkers: 'block', reducedMotion: 'reduce',
    acceptDownloads: false });
  const info = { browser: browser.version(), viewport: { width, height }, blocked: [], reconstructed: [], jsErrors: [],
    consoleErrors: [], requests: 0, methodsBlocked: [] };
  const blocked = new Map();
  const reconstructed = new Set();
  const page = await context.newPage();
  page.on('pageerror', error => info.jsErrors.push(error.message));
  page.on('console', message => { if (message.type() === 'error') info.consoleErrors.push(message.text()); });
  page.on('dialog', dialog => dialog.dismiss());
  context.on('page', popup => { if (popup !== page) popup.close().catch(() => {}); });
  await context.routeWebSocket('**', socket => socket.close());
  await context.route('**/*', async route => {
    const request = route.request();
    info.requests++;
    if (!['GET', 'HEAD'].includes(request.method())) {
      info.methodsBlocked.push({ url: request.url(), method: request.method() });
      await route.abort('blockedbyclient');
      return;
    }
    const url = new URL(request.url());
    let item;
    if (side === 'original') item = originalResource(url.href);
    else if (url.hostname === 'archive.test') {
      const decoded = decodeURIComponent(url.pathname);
      item = manifest.resources.clone[decoded];
      if (!item && !decoded.endsWith('/')) item = manifest.resources.clone[decoded + '/'];
    }
    if (item) {
      if (item.provenance === 'recovered-image') reconstructed.add(url.href);
      await route.fulfill({ path: item.file, contentType: item.contentType, status: item.status,
        headers: { 'Access-Control-Allow-Origin': '*', 'Cache-Control': 'no-store' } });
    } else {
      blocked.set(url.href, { url: url.href, resourceType: request.resourceType(),
        reason: side === 'clone' && url.hostname === 'archive.test' ? 'missing-local-resource' : 'not-in-offline-capture' });
      await route.abort('blockedbyclient');
    }
  });
  try {
    const target = side === 'original' ? row.url : 'http://archive.test' + manifest.basePath + row.path;
    info.url = target;
    await page.goto(target, { waitUntil: 'load', timeout: 15000 });
    // Force lazy images to load locally. Finite waits protect the batch from old
    // scripts; any incompletely decoded image is recorded, not silently passed.
    await page.evaluate(async () => {
      document.querySelectorAll('img').forEach(img => img.loading = 'eager');
      await Promise.race([Promise.all([...document.images].map(img => img.decode().catch(() => {}))), new Promise(r => setTimeout(r, 1500))]);
      await Promise.race([document.fonts.ready, new Promise(r => setTimeout(r, 1000))]);
    });
    const metrics = await page.evaluate(() => {
      const box = el => {
        const r = el.getBoundingClientRect();
        return { x: Math.round(r.x), y: Math.round(r.y), width: Math.round(r.width), height: Math.round(r.height) };
      };
      const label = el => el.id ? '#' + el.id : el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/).join('.') : '');
      const overflow = [];
      for (const el of document.querySelectorAll('body *')) {
        if (['SCRIPT', 'STYLE', 'LINK', 'META'].includes(el.tagName)) continue;
        const r = el.getBoundingClientRect();
        const style = getComputedStyle(el);
        if (r.width > 0 && r.height > 0 && style.visibility !== 'hidden' && (r.right > innerWidth + 2 || r.left < -2)) {
          overflow.push({ element: label(el), ...box(el), text: el.textContent.trim().slice(0, 100) });
        }
      }
      const geometry = {};
      for (const selector of ['body', '#page', '#header', '#content', '#sidebar', '#footer', '.entry']) {
        const el = document.querySelector(selector);
        if (!el) continue;
        const css = getComputedStyle(el);
        geometry[selector] = { ...box(el), background: css.backgroundColor, backgroundImage: css.backgroundImage,
          color: css.color, font: css.font, textAlign: css.textAlign };
      }
      return {
        encoding: document.characterSet,
        renderedText: document.body.innerText,
        height: Math.max(document.documentElement.scrollHeight, document.body.scrollHeight),
        width: Math.max(document.documentElement.scrollWidth, document.body.scrollWidth),
        brokenImages: [...document.images].filter(img => !img.complete || img.naturalWidth === 0).map(img => ({ url: img.currentSrc || img.src, alt: img.alt })),
        enabledArchivedControls: [...document.querySelectorAll('.archive-form input:not(:disabled),.archive-form textarea:not(:disabled),.archive-form select:not(:disabled),.archive-form button:not(:disabled)')].map(label),
        overflow: overflow.slice(0, 30), overflowTotal: overflow.length, geometry,
        forms: [...document.forms].map(f => ({ id: f.id, action: f.action, method: f.method, enabled: [...f.elements].filter(e => !e.disabled).length }))
      };
    });
    Object.assign(info, metrics);
    info.truncated = metrics.height > maxHeight || metrics.width > width;
    info.screenshot = 'screenshots/' + row.id + '-' + side + '.jpg';
    await page.screenshot({ path: path.join(output, info.screenshot), type: 'jpeg', quality: 90,
      animations: 'disabled', caret: 'hide', clip: { x: 0, y: 0, width, height: Math.min(maxHeight, metrics.height) },
      captureBeyondViewport: true, timeout: 20000 });
  } catch (error) {
    info.error = error.message;
  } finally {
    info.blocked = [...blocked.values()];
    info.reconstructed = [...reconstructed];
    info.jsErrors = [...new Set(info.jsErrors)];
    info.consoleErrors = [...new Set(info.consoleErrors)];
    await context.close();
  }
  return info;
}

async function worker() {
  while (manifest.rows.length && !stopped) {
    const row = manifest.rows.shift();
    const file = path.join(browserDir, row.id + '.json');
    const signature = sha(configuration + row.path + row.url + row.source_sha256 + row.clone_sha256);
    let previous;
    try { previous = JSON.parse(await fs.readFile(file, 'utf8')); } catch {}
    let reusable = previous?.signature === signature && !previous.original?.error && !previous.clone?.error;
    if (reusable) {
      for (const side of ['original', 'clone']) {
        try { await fs.access(path.join(output, previous[side].screenshot)); } catch { reusable = false; }
      }
    }
    if (reusable) reused++;
    else {
      const result = { signature, source_sha256: row.source_sha256, clone_sha256: row.clone_sha256,
        captured_at: new Date().toISOString(), original: await render(row, 'original'), clone: await render(row, 'clone') };
      await fs.writeFile(file + '.tmp', JSON.stringify(result, null, 2));
      await fs.rename(file + '.tmp', file);
    }
    completed++;
    if (completed % 25 === 0) console.log(`Browser comparison: ${completed} done (${reused} reused), ${manifest.rows.length} queued`);
  }
}

try {
  await Promise.all(Array.from({ length: Math.max(1, Math.min(8, manifest.workers)) }, worker));
  console.log(`Browser comparison complete: ${completed} pairs (${reused} reused).`);
} finally {
  await browser.close();
}
if (stopped) process.exitCode = 130;
