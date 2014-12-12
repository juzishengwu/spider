#coding=utf-8
from wikitools import wiki, category
import sys

#category:
#   Is_a_medical_condition
#   Is_a_gene
#   Is_a_genoset
#   Is_a_medicine
#   Is_a_medical_condition
#   Topic
c = sys.argv[1] 
site = wiki.Wiki("http://bots.snpedia.com/api.php")
snps = category.Category(site, c)
for article in snps.getAllMembersGen(namespaces=[0]):
    print article.title.encode('u8')
