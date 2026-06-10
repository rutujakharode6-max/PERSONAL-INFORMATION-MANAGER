import http.server
import socketserver
import urllib.parse

PORT = 5000

# Personal Data
NAME = "Maya Patel"
AGE = 22
CITY = "San Francisco"
HOBBY = "Coding"

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>✨ Personal Information Manager ✨</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0;
            color: #333;
        }
        .card {
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(10px);
            padding: 40px;
            border-radius: 24px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            max-width: 450px;
            width: 100%;
            text-align: center;
        }
        h1 { color: #4a4a4a; margin-bottom: 25px; font-size: 1.5em; }
        .input-group { margin-bottom: 20px; text-align: left; }
        label { display: block; margin-bottom: 8px; color: #555; font-weight: 600; }
        input[type="text"] {
            width: 100%; padding: 12px; border: 2px solid #e1e1e1; border-radius: 12px;
            box-sizing: border-box; font-size: 16px; transition: border-color 0.3s;
        }
        input[type="text"]:focus { outline: none; border-color: #a6c1ee; }
        button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; border: none; padding: 14px 20px; border-radius: 12px;
            cursor: pointer; font-size: 16px; font-weight: bold; width: 100%;
            margin-top: 10px; transition: transform 0.2s, box-shadow 0.2s;
        }
        button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(118, 75, 162, 0.4); }
        .profile-item {
            text-align: left; margin: 12px 0; font-size: 18px; padding: 10px 15px;
            background: white; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.02);
            display: flex; align-items: center; gap: 10px;
        }
        .success-msg { margin-top: 25px; color: #27ae60; font-weight: bold; font-size: 1.1em; }
    </style>
</head>
<body>
    <div class="card">
        {content}
    </div>
</body>
</html>
"""

FORM_CONTENT = """
        <h1>✨ WELCOME TO YOUR PROFILE ✨</h1>
        <p style="margin-bottom: 25px; color: #666;">Let's personalize your experience!</p>
        <form method="POST" action="/">
            <div class="input-group">
                <label>💚 What's your favorite food?</label>
                <input type="text" name="food" required autocomplete="off">
            </div>
            <div class="input-group">
                <label>💜 What's your favorite color?</label>
                <input type="text" name="color" required autocomplete="off">
            </div>
            <button type="submit">Personalize ✨</button>
        </form>
"""

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        html = TEMPLATE.replace('{content}', FORM_CONTENT)
        self.wfile.write(html.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        fields = urllib.parse.parse_qs(post_data)
        
        food = fields.get('food', [''])[0].strip().title()
        color = fields.get('color', [''])[0].strip().capitalize()
        
        age_months = AGE * 12
        
        result_content = f'''
        <h1 style="margin-bottom: 30px;">✨ Profile Updated! ✨</h1>
        <div class="profile-item">👤 <b>{NAME}</b></div>
        <div class="profile-item">🎂 {AGE} years old ({age_months} months)</div>
        <div class="profile-item">🏙️ Lives in {CITY}</div>
        <div class="profile-item">🎯 Enjoys {HOBBY}</div>
        <div class="profile-item">🍽️ Loves {food}</div>
        <div class="profile-item">🎨 Favorite color: {color}</div>
        
        <p class="success-msg">✓ Have a wonderful day! 🌟</p>
        <a href="/" style="display:inline-block; margin-top:20px; text-decoration:none; color:#764ba2; font-weight:bold;">← Start Over</a>
        '''
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        html = TEMPLATE.replace('{content}', result_content)
        self.wfile.write(html.encode('utf-8'))

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Server running beautifully at http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
