#coding=utf-8
from wikitools import wiki, category, page
import sys

title = sys.argv[1]
site = wiki.Wiki("http://bots.snpedia.com/api.php")
pagehandle = page.Page(site, title)
snp_page = pagehandle.getWikiText()
#print snp_page.encode('u8')
open(title, 'w').write(snp_page.encode('u8'))
