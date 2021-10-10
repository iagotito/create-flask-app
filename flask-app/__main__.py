from urllib.parse import urlparse

from . rest import app

URL = "http://0.0.0.0:8000"

url = urlparse(URL)
host, port = url.hostname, url.port
app.run(host=host, port=port, debug=True)
