/* Local replacement for the retired SlayerOffice PHP source viewer. */
(() => {
  const source = document.documentElement.outerHTML;
  const panel = document.createElement('div');
  panel.style.cssText = 'position:fixed;inset:20px;z-index:2147483647;overflow:auto;background:white;color:black;padding:20px;border:2px solid #333;text-align:left';
  const close = document.createElement('button');
  close.textContent = 'Close source';
  close.addEventListener('click', () => panel.remove());
  const code = document.createElement('pre');
  code.textContent = source;
  panel.append(close, code);
  document.body.append(panel);
})();
