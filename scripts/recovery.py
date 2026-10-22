"""Selected public material recovered from backups and original code embeds.

The private SQL dump and WordPress installation are never build inputs. Only
the reviewed snippets, asset files, and provenance in data/recovery.json ship.
"""
from datetime import datetime
from functools import lru_cache
import html
import json
from pathlib import Path
import re
from urllib.parse import quote_plus

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SHORTCODE = re.compile(r'\[code\b[^\]]*\].*?\[/code\]', re.I | re.S)
UNDO_URL = 'http://humanized.com/weblog/images/resources/undo/todo.html'
UNDO_PATH = '/archive-assets/demos/undo.html'
TABLE_DEMO = '/wp-content/uploads/2006/03/fixed-table-cells-notworking.html'
BUTTON_DEMO = '/wp-content/uploads/2008/11/ie7css-flaw-background-image-on-buttons.html'


@lru_cache
def recovery_data():
    return json.loads((ROOT / 'data/recovery.json').read_text())


@lru_cache
def video_players():
    return json.loads((ROOT / 'data/video-players.json').read_text())


def modernize_videos(soup):
    """Use native players for original IDs or owner-approved alternative uploads.

    Exact source matching also covers copies on index/category/archive pages.
    Retired providers without a native replacement keep their original markup.
    """
    replacements = {row['captured']: row['replacement'] for row in video_players()}
    for tag in reversed(soup.find_all(['object', 'iframe', 'embed'])):
        replacement = replacements.get(str(tag))
        if replacement:
            tag.replace_with(BeautifulSoup(replacement, 'html.parser').iframe)


def code_key(source):
    return ' '.join(html.unescape(source).split())


@lru_cache
def code_lookup():
    return {code_key(block['captured']): block for block in recovery_data()['code_blocks']}


def code_html(code, language='', key=''):
    css = ' class="language-' + html.escape(language, quote=True) + '"' if language else ''
    identifier = ' data-recovery-code="' + html.escape(key, quote=True) + '"' if key else ''
    return '<pre class="archive-code"' + identifier + '><code' + css + '>' + html.escape(code, quote=False) + '</code></pre>'


def restore_code(raw):
    """Escape known examples before an HTML parser can execute/rearrange them."""
    if isinstance(raw, bytes) and b'[code' not in raw.lower():
        return raw
    source = raw.decode('utf-8') if isinstance(raw, bytes) else raw
    pattern = r'(?P<open><(?:p|pre)\b[^>]*>\s*)?(?P<snippet>\[code\b[^\]]*\].*?\[/code\])(?P<close>\s*</(?:p|pre)>)?'

    def replace(match):
        block = code_lookup().get(code_key(match['snippet']))
        if block is None:
            return match[0]
        result = code_html(block['code'], block['language'], block['id'])
        # Some original shortcodes end midway through a prose paragraph.
        if match['open'] and match['open'].startswith('<p>') and not match['close']:
            following = source[match.end():].lstrip()
            if following and not following.startswith('<'):
                result += '<p>'
        return result

    return re.sub(pattern, replace, source, flags=re.I | re.S)


def restore_tag_lists(soup):
    """Reproduce SimpleTags 2.0 output for the two reviewed authoring typos."""
    lists = {row['captured']: row for row in recovery_data()['tag_lists']}
    for paragraph in soup.find_all('p'):
        if (not paragraph.string or paragraph.string.parent is not paragraph
                or paragraph.find_parent(['pre', 'code'])):
            continue
        row = lists.get(paragraph.string.strip())
        if row is None:
            continue
        small = soup.new_tag('small', attrs={'data-recovery-tags': str(row['post_id'])})
        small.append('Technorati Tags: ')
        for index, tag in enumerate(row['tags']):
            if index:
                small.append(', ')
            link = soup.new_tag('a', href='http://technorati.com/tag/' + quote_plus(tag), rel='tag')
            link.string = tag
            small.append(link)
        paragraph.clear()
        paragraph.append(small)


def restore_gists(soup):
    for script in list(soup.find_all('script', src=True)):
        gist = recovery_data()['gists'].get(script['src'])
        if gist is None:
            continue
        section = soup.new_tag('div', attrs={'class': 'archive-gist'})
        for index, file in enumerate(gist['files']):
            pre = soup.new_tag('pre', attrs={'class': 'archive-code', 'data-recovery-code': f'gist-{gist["post_id"]}-{index + 1}'})
            code = soup.new_tag('code')
            code.string = file['code']
            pre.append(code)
            section.append(pre)
            label = soup.new_tag('p', attrs={'class': 'archive-code-source'})
            label.append(file['name'] + ' · ')
            link = soup.new_tag('a', href=gist['url'] + '/' + gist['revision'])
            link.string = 'Original gist'
            label.append(link)
            section.append(label)
        if not gist['files']:
            note = soup.new_tag('p', attrs={'class': 'archive-note'})
            note.append('The original embedded code is no longer available. ')
            link = soup.new_tag('a', href=gist['url'])
            link.string = 'Original gist'
            note.append(link)
            section.append(note)
        script.replace_with(section)


def restore_local_forms(soup, path):
    # This example compares submit/button rendering; its "nothing" action was
    # a placeholder. Keep the original control types and their active styling,
    # but give them no form owner that could navigate or submit anything.
    if path == BUTTON_DEMO:
        for form in soup.find_all('form', action='nothing'):
            form.name = 'div'
            form.attrs = {'class': ['archive-local-form'], 'role': 'group'}


def restore_demos(soup, path):
    for frame in soup.find_all('iframe', src=UNDO_URL):
        frame['src'] = UNDO_PATH
        frame['title'] = 'Undo demonstration by Aza Raskin'
        frame['sandbox'] = 'allow-scripts'
        frame['loading'] = 'lazy'
    if path == TABLE_DEMO:
        soup.html['data-archive-demo'] = 'table-height'
        script = soup.new_tag('script', src='/archive-assets/demos.js', defer='defer')
        soup.head.append(script)


def restore_comments(soup, path):
    """Restore only owner-approved comments at their original permalinks."""
    for comment in recovery_data()['comments']:
        anchor = f'comment-{comment["id"]}'
        if comment['path'] != path or soup.find(id=anchor):
            continue
        content = soup.find(id='content')
        if content is None:
            raise ValueError('Recovered comment destination has no content: ' + path)
        comments = content.select_one('ol.commentlist')
        if comments is None:
            heading = soup.new_tag('h3', id='comments')
            heading.string = '1 Response'
            comments = soup.new_tag('ol', attrs={'class': 'commentlist'})
            respond = content.find(id='respond')
            if respond:
                respond.insert_before(heading)
                respond.insert_before(comments)
            else:
                content.append(heading)
                content.append(comments)
        item = soup.new_tag('li', id=anchor, attrs={'class': ['alt', comment['type']]})
        cite = soup.new_tag('cite')
        author = soup.new_tag('a', href=comment['author_url'], attrs={'class': 'url'})
        author.string = comment['author']
        cite.append(author)
        item.append(cite)
        item.append(' (Pingback):' if comment['type'] == 'pingback' else ' Says:')
        item.append(soup.new_tag('br'))
        metadata = soup.new_tag('small', attrs={'class': 'commentmetadata'})
        permalink = soup.new_tag('a', href='#' + anchor)
        date = datetime.fromisoformat(comment['date'])
        timestamp = soup.new_tag('time', datetime=date.isoformat())
        timestamp.string = f'{date:%B} {date.day}, {date:%Y at %H:%M}'
        permalink.append(timestamp)
        metadata.append(permalink)
        item.append(metadata)
        paragraph = soup.new_tag('p')
        # These reviewed comments contain plain text and bare URLs only.
        for part in re.split(r'(https?://\S+)', comment['content']):
            if part.startswith(('http://', 'https://')):
                link = soup.new_tag('a', href=part, rel='nofollow')
                link.string = part
                paragraph.append(link)
            else:
                paragraph.append(part)
        item.append(paragraph)
        comments.append(item)
        count = len(comments.find_all('li', recursive=False))
        heading = content.find(id='comments')
        if heading:
            heading.string = f'{count} Response' + ('s' if count != 1 else '')
    return soup
