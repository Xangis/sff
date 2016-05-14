#!/bin/bash
wget --spider -l100 --recursive --no-verbose --output-file=wgetlog.txt http://sffdb.com
sed -n "s@.\+ URL:\([^ ]\+\) .\+@\1@p" wgetlog.txt | sed "s@&@\&amp;@" > sedlog.txt
cat sedlog.txt |sort|uniq > sitemap.txt
wc sitemap.txt
rm sedlog.txt wgetlog.txt
diff sitemap.txt templates/sitemap.txt

