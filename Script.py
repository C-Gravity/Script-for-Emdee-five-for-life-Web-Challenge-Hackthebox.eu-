import requests
import hashlib
import re


url="http://docker.hackthebox.eu:32190/"
r=requests.session()
out=r.get(url)
outl=re.search(r"<h3 align='center'>(\w*)</h3>",out.text)

outll=hashlib.md5(outl.group(1).encode('utf-8')).hexdigest()

print("sending md5 :-{}".format(outll))

data={'hash': outll}
out = r.post(url = url, data = data)

print(out.text)
