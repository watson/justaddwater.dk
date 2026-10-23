"""Find browser resource references without treating ordinary links as loads."""
import re

CSS_URL = re.compile(r'url\(\s*([\'\"]?)(.*?)\1\s*\)', re.I)
CSS_IMPORT = re.compile(r'@import\s+([\'\"])(.*?)\1', re.I)
RESOURCE_LINK_RELS = {
    'stylesheet', 'preload', 'modulepreload', 'prefetch', 'preconnect',
    'dns-prefetch', 'icon', 'apple-touch-icon', 'apple-touch-icon-precomposed',
    'mask-icon', 'manifest', 'import',
}


def css_urls(css):
    # Comments contain examples and obsolete browser hacks, not dependencies.
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    return [match[2] for pattern in (CSS_URL, CSS_IMPORT) for match in pattern.finditer(css)]


def resource_urls(tag):
    """Return (attribute, URL) pairs for loads and connection hints on one tag."""
    attrs = ['background']
    if tag.name in ('img', 'script', 'iframe', 'frame', 'embed', 'audio', 'video', 'source', 'track'):
        attrs.append('src')
    if tag.name == 'input' and tag.get('type', '').lower() == 'image':
        attrs.append('src')
    if tag.name == 'video':
        attrs.append('poster')
    if tag.name == 'object':
        attrs.extend(('data', 'codebase'))
    if tag.name == 'applet':
        attrs.extend(('code', 'codebase', 'archive'))
    if tag.name in ('image', 'feimage', 'use', 'base'):
        attrs.extend(('href', 'xlink:href'))
    if tag.name == 'html':
        attrs.append('manifest')
    if tag.name == 'link' and RESOURCE_LINK_RELS.intersection(rel.lower() for rel in tag.get('rel', [])):
        attrs.append('href')
    result = [(attr, tag[attr]) for attr in attrs if tag.get(attr)]
    for attr in ('srcset', 'imagesrcset'):
        if tag.get(attr):
            result.extend((attr, candidate.split()[0]) for candidate in tag[attr].split(',') if candidate.strip())
    if tag.name == 'meta' and tag.get('http-equiv', '').lower() == 'refresh':
        match = re.search(r';\s*url\s*=\s*(.*)', tag.get('content', ''), re.I)
        if match:
            result.append(('refresh', match[1].strip().strip('\'\"')))
    return result
