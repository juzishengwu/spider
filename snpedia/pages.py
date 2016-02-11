#coding=utf-8
import sys, subprocess, time

page_list_fn = sys.argv[1]
for t in file(page_list_fn):
    title = t.strip()
    subprocess.call('python page.py %s'%title, shell=True)
    print title
    time.sleep(5)
