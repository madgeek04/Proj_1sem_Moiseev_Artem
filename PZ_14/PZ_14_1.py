import tldextract
print(*[tldextract.extract(i).fqdn for i in open('spisok.txt').read().split('\n')], sep='\n')
