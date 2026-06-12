from flask import Flask, render_template_string

# ==============================================================================
# EVE_1 | DIRECT LINK PROTOCOL
# OPERATOR: JEFFREY KIMBAL
# ==============================================================================

app = Flask(__name__)

# YOUR DIRECT PAYMENT LINK
PAYMENT_LINK = "https://buy.stripe.com/aFa6oI1cj2RVbZEbkN77O08"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EVE_1 | CONVERGENCE</title>
    <style>
        body { background-color: #050505; color: #00ff41; font-family: monospace; text-align: center; display: flex; flex-direction: column; justify-content: center; height: 100vh; margin: 0; }
        .box { border: 2px solid #00ff41; padding: 50px; max-width: 600px; margin: auto; background: #0a0a0a; box-shadow: 0 0 30px rgba(0, 255, 65, 0.15); }
        h1 { letter-spacing: 4px; margin-bottom: 10px; font-size: 3rem; text-shadow: 0 0 10px #00ff41; }
        p { color: #ccc; margin-bottom: 40px; font-size: 1.2rem; }
        .price { font-size: 2rem; color: #fff; margin-bottom: 40px; }
        
        /* THE BUTTON */
        a.button {
            background-color: #00ff41;
            color: #000;
            text-decoration: none;
            padding: 20px 50px;
            font-size: 1.5rem;
            font-weight: bold;
            display: inline-block;
            transition: 0.3s;
            border: 2px solid #00ff41;
        }
        a.button:hover {
            background-color: #000;
            color: #00ff41;
            box-shadow: 0 0 20px #00ff41;
        }
    </style>
</head>
<body>
    <div class="box">
        <h1>EVE_1 ONLINE</h1>
        <p>SECURE PAYMENT GATEWAY</p>
        <div class="price">ACCESS: $10.00</div>
        
        <a href="{{ link }}" class="button">INITIATE TRANSFER</a>
    </div>
    <script type="module">
        import { injectSpeedInsights } from '/_vercel/speed-insights/script.js';
        injectSpeedInsights();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, link=PAYMENT_LINK)

if __name__ == '__main__':
    print(" * EVE_1 PORTAL ACTIVE. GO TO: http://127.0.0.1:4242")
    app.run(host='0.0.0.0', port=4242)
