from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("Hello from Python on Vercel!".encode('utf-8'))
        return
    
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        try:
            request_data = json.loads(post_data.decode('utf-8'))
        except:
            request_data = {"raw_data": post_data.decode('utf-8')}
        
        response_data = {
            "message": "POST request received successfully!",
            "timestamp": datetime.now().isoformat(),
            "method": "POST",
            "received_data": request_data,
            "status": "success"
        }
        
        self.wfile.write(json.dumps(response_data, ensure_ascii=False).encode('utf-8'))
        return 