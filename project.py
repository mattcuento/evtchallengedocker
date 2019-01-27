
#import modules to get filepath, to open browser, opening url, creating a request handler, and creating a TCPServer
import webbrowser, urllib.request, http.server, socketserver

#creating vars to store local file name and url
url = "http://evtgit01.evtcorp.com/yrutenberg/Tech-Challenge/raw/master/evt-web.html"
file = "index.html"

#translating url into text
webpage = urllib.request.urlopen(url)
html = webpage.read()

#writing text to index.html file
with open(file, "wb") as text_file:
	text_file.write(html)

#auto open default browser to index.html
webbrowser.open_new_tab("http://localhost:8000")

#specifying local port number
PORT = 8000

#create the request handler
reqHandler = http.server.SimpleHTTPRequestHandler

#create the TCP server and pass in port and reqHandler
#returns the active port and begins running server, active on any IP
with socketserver.TCPServer(("0.0.0.0", PORT), reqHandler) as httpd:
	print("Active at port", PORT)
	httpd.serve_forever()
