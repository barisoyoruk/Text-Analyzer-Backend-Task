from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
import json

from textAnalyzer import analyzeText


class TextAnalyzerHandler(BaseHTTPRequestHandler):
	def set_error(self):
		self.send_response(400)
		self.send_header('Content-Type', 'application/json')
		self.end_headers()

	def set_success(self):
		self.send_response(200)
		self.send_header('Content-Type', 'application/json')
		self.end_headers()

	def do_POST(self):
		if self.path == '/analyze':
			ctype, pdict = cgi.parse_header(self.headers.get('Content-Type'))
			pdict['boundary'] = bytes(pdict['boundary'], "ascii")
			if ctype == 'multipart/form-data':
				postvars = cgi.parse_multipart(self.rfile, pdict)
			elif ctype == 'application/x-www-form-urlencoded':
				length = int(self.headers.get('Content-Length'))
				postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
			else:
				postvars = {}

			try:
				text = postvars['text'][0]
			except:
				self.set_error()
				json_str = 'Text is not given'

			try:
				filters = json.loads(postvars['analysis'][0])
			except:
				filters = None
			json_str = json.dumps(analyzeText(text, filters))
			self.set_success()
			self.wfile.write(json_str.encode(encoding='utf_8'))

		else:
			self.set_error()
			json_str = "Unknown URL for POST request. Only /analysis acceptable"
			self.wfile.write(json_str.encode(encoding='utf_8'))


def main():
	#try:
		PORT = 8080
		server = HTTPServer(('', PORT), TextAnalyzerHandler)
		server.serve_forever()
	#except KeyboardInterrupt:
	#	serve.socket.close()

if __name__ == '__main__':
        main()
