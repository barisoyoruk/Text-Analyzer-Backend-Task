from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
import json

from textAnalyzer import analyzeText

class TextAnalyzerHandler(BaseHTTPRequestHandler):
	def set_response(self, status_code = 200):
		self.send_response(status_code)
		self.send_header('Content-Type', 'application/json')
		self.end_headers()

	def do_POST(self):
		try:
			if self.path == '/analyze':
				ctype, pdict = cgi.parse_header(self.headers.get('Content-Type'))

				# Library related issue
				if type(pdict['boundary']) != 'bytes':
					pdict['boundary'] = bytes(pdict['boundary'], "ascii")
				

				if ctype == 'multipart/form-data':
					postvars = cgi.parse_multipart(self.rfile, pdict)
				elif ctype == 'application/x-www-form-urlencoded':
					length = int(self.headers.get('Content-Length'))
					postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
				else:
					postvars = {}

				try:
					text = postvars['text'][0].replace('\\n', '\n')	# JSON does not allow new line char '\ns'. We should replace manually
				except:
					self.set_response(400)
					error_str = 'Error: Text is not given'
					self.wfile.write(error_str.encode(encoding='utf_8'))
					return

				try:
					filters = json.loads(postvars['analysis'][0])
				except:
					filters = None

				response_str = json.dumps(analyzeText(text, filters))
				self.set_response(200)
				self.wfile.write(response_str.encode(encoding='utf_8'))

			else:
				self.set_response(400)
				error_str = "Error: Unknown URL for POST request. Only /analyze acceptable"
				self.wfile.write(error_str.encode(encoding='utf_8'))
		except Exception as e:
			self.set_response(400)
			error_str = "Error: " + str(e)
			self.wfile.write(error_str.encode(encoding='utf_8'))


def main():
	try:
		PORT = 8080
		server = HTTPServer(('', PORT), TextAnalyzerHandler)
		server.serve_forever()
	except KeyboardInterrupt:
		server.socket.close()

if __name__ == '__main__':
        main()
