import re
import tldextract
r = re.compile('\\S+')
g = [r.findall(i) for i in open('spisok.txt').readlines()]
for o in g:
    print(tldextract.extract(o[-1]).fqdn)
