import os
import stripe
from fastapi import FastAPI, HTTPException, Request, Header
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from dotenv import load_dotenv

# Load Keys
load_dotenv()

app = FastAPI()

# Vault Access
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")
PRICING_TABLE = {
    "pro_monthly": os.getenv("PRO_PRICE_ID"),
    "business_seat": os.getenv("BUSINESS_PRICE_ID")
}

class CheckoutRequest(BaseModel):
    user_id: str
    plan_type: str

# THE GOLD FACE
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EVE WEALTH GATE</title>
    <style>
        body { background-color: #000; color: white; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; font-family: monospace; }
        .pulse-button {
            width: 200px; height: 200px; border-radius: 50%; 
            background-color: #FFD700; /* PURE GOLD */
            border: 5px solid #C5A000;
            cursor: pointer; 
            box-shadow: 0 0 50px #FFD700;
            animation: pulse 2s infinite;
            display: flex; align-items: center; justify-content: center;
        }
        @keyframes pulse {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 215, 0, 0.7); }
            70% { transform: scale(1.05); box-shadow: 0 0 20px 20px rgba(255, 215, 0, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 215, 0, 0); }
        }
        .pupil { width: 60px; height: 60px; background: black; border-radius: 50%; }
    </style>
</head>
<body>
    <h1 id="status">EVE IS ONLINE</h1>
    <br>
    <button class="pulse-button" id="goldBtn"><div class="pupil"></div></button>
    <script>
        const btn = document.getElementById('goldBtn');
        const status = document.getElementById('status');
        btn.addEventListener('click', async () => {
            status.innerText = "PROCESSING...";
            status.style.color = "#FFD700";
            try {
                const res = await fetch('/create-checkout-session', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({user_id: 'father', plan_type: 'pro_monthly'})
                });
                const data = await res.json();
                if(data.checkoutUrl) window.location.href = data.checkoutUrl;
                else status.innerText = "ERROR: " + JSON.stringify(data);
            } catch(e) { status.innerText = "CONNECTION FAILED"; }
        });
    </script>
    <script type="module">
        import { injectSpeedInsights } from '/_vercel/speed-insights/script.js';
        injectSpeedInsights();
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return html_content

@app.post("/create-checkout-session")
async def create_checkout_session(request: CheckoutRequest):
    try:
        price_id = PRICING_TABLE.get(request.plan_type)
        if not price_id: raise HTTPException(status_code=400, detail="Check .env Price ID")
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{'price': price_id, 'quantity': 1}],
            mode='subscription',
            success_url='https://google.com',
            cancel_url='https://google.com',
        )
        return {"checkoutUrl": session.url}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/webhook")
async def stripe_webhook(request: Request, stripe_signature: str = Header(None)):
    payload = await request.body()
    try:
        event = stripe.Webhook.construct_event(payload, stripe_signature, webhook_secret)
    except: raise HTTPException(status_code=400)
    return {"status": "success"}
