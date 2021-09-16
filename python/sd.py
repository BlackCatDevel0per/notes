# Simple file download script
import requests

def download(url, out=None, bar=None):
  r = requests.get(url, allow_redirects=True)
  if out==None:
    outfile=url.split("/")
    out=outfile[-1]
  fn = open(out, 'wb')
  fn.write(r.content)
  fn.close()
  ###

