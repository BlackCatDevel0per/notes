# Simple file download script
import requests

def download(url, out=None, bar=None):
  r = requests.get(url, allow_redirects=True)
  if out==None:
    outfile=url.split("/")
    out=outfile[-1]
  open(out, 'wb').write(r.content)

