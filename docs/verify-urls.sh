#!/bin/sh
# Run `hugo --gc` first. Checks every front-matter `url:` has public/<url>/index.html.
cd "$(dirname "$0")/.." || exit 1
checked=0; missing=0
for f in content/posts/*.md content/pages/*.md; do
  u=$(grep -m1 '^url:' "$f" | sed 's/^url: *"\{0,1\}//; s/"\{0,1\} *$//')
  [ -z "$u" ] && continue
  checked=$((checked+1))
  [ -f "public${u%/}/index.html" ] || { echo "MISSING $u ($f)"; missing=$((missing+1)); }
done
echo "checked=$checked missing=$missing"
[ "$missing" -eq 0 ]
