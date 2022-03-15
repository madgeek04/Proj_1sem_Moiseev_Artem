import tldextract
print(*[tldextract.extract(i.split(' ')[-1]).fqdn for i in open('spisok.txt').read().split('\n')], sep='\n')
