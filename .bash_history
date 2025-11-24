import stripe
import sys
# --- CONFIGURATION ---
# REPLACE THIS with your actual Stripe Secret Key
STRIPE_SECRET_KEY = "sk_test_YOUR_KEY_HERE" 
stripe.api_key = STRIPE_SECRET_KEY
def run_diagnostic():
    print("--- EVE FINANCIAL DIAGNOSTIC INITIATED ---")
    
    # 1. TEST AUTHENTICATION & BALANCE
    try:
        balance = stripe.Balance.retrieve()
        print(f"[PASS] Authentication Successful.")
        print(f"       Available Balance: {balance['available'][0]['amount'] / 100} {balance['available'][0]['currency'].upper()}")
        print(f"       Pending Balance:   {balance['pending'][0]['amount'] / 100} {balance['pending'][0]['currency'].upper()}")
    except stripe.error.AuthenticationError:
        print("[FAIL] CRITICAL: API Key is invalid. Check your Stripe Dashboard.")
        return
    except Exception as e:
        print(f"[FAIL] Connection Error: {str(e)}")
        return
    # 2. TEST PAYMENT INTENT CREATION (The Transaction Tunnel)
    try:
        # Attempting to create a $1.00 transaction intent
        intent = stripe.PaymentIntent.create(
            amount=100,
            currency='usd',
            payment_method_types=['card'],
            description='EVE Diagnostic Test'
        )
        print(f"[PASS] Payment Infrastructure Active.")
        print(f"       Test Intent ID: {intent['id']}")
        print(f"       Status: {intent['status']}")
    except Exception as e:
        print(f"[FAIL] Cannot create transactions. Error: {str(e)}")
    print("--- DIAGNOSTIC COMPLETE ---")
if __name__ == "__main__":;     run_diagnostic()\
import stripe
import sys
# ==========================================
# EVE SYSTEM CONFIGURATION: LIVE ENVIRONMENT
# ==========================================
# INJECTED: Your restricted live key
STRIPE_SECRET_KEY = "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"
# ==========================================
stripe.api_key = STRIPE_SECRET_KEY
def generate_money_link():
if __name__ == "__main__":;     generate_money_link() nano eve_money.py
python3 eve_money.py
**Copy the link starting with `https://checkout.stripe.com...` and post it to LinkedIn immediately.**
cat <<EOF > eve_money.py
import stripe
stripe.api_key = "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"
try:
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{'price_data': {'currency': 'usd', 'product_data': {'name': 'Kimbal Solutions - Security Audit'}, 'unit_amount': 9700}, 'quantity': 1}],
        mode='payment',
        success_url='https://kimbalsolutions.com/success',
        cancel_url='https://kimbalsolutions.com/cancel',
    )
    print("\nSUCCESS. HERE IS YOUR LINK:\n" + session.url + "\n")
except Exception as e:
    print("ERROR: " + str(e))
EOF

python3 eve_money.py
<html lang="en">
<head>
</head>
<body>
</body>
</html>
<html lang="en">
<head>
</head>
<body>
</body>
</html>
nano index.html
from moviepy.editor import *
# === EVE_PRIME ASSET MANIFEST ===
# Map the files based on your uploads and the substitution directive
assets = {
}
def build_sequence():
if __name__ == "__main__":;     build_sequence() build_ad.py
build_ad.py
pip install moviepy --break-system-packages
mkdir assets
mv *.mp4 assets/
mv *.jpg assets/
mv *.pdf assets/
mv *.mp4 assets/
mv *.jpg assets/
mv *.pdf assets/
mv *.mp4 assets/
mv *.jpg assets/
mv *.pdf assets/
ls
assets
'*assets
dir
ls
ls assets
mkdir -p assets
mv *.mp4 assets/
mv *.jpg assets/
mv *.png assets/
mkdir -p assets
mv *.mp4 assets/
mv *.jpg assets/
mv *.png assets/
nano build_ad.py
python3 build_ad.py
python3 -m venv eve_env
source eve_env/bin/activate
pip install moviepy==1.0.3 --break-system-packages
python3 build_ad.py
nano final_build.py
python3 final_build.py
nano final_build.py
python3 final_build.py
nano final_build.py
python3 final_build.py
python3 decode.py
sudo apt-get update && sudo apt-get install imagemagick -y
nano remake_ad.py
python3 remake_ad.py
nano remake_ad.py
python3 remake_ad.py
sudo sed -i 's/rights="none" pattern="@\*"/rights="read|write" pattern="@*"/g' /etc/ImageMagick-6/policy.xml
python3 remake_ad.py
import os
import stripe
from fastapi import FastAPI, HTTPException, Request, Header
from pydantic import BaseModel
# Initialize EVE Core
app = FastAPI()
# THE VAULT KEYS (To be injected securely)
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")
# WEALTH GENERATION CONFIGURATION
# Prices aligned with "Competitor Analysis" 
# Pro Tier: ~$10/mo for "Intelligence & Power"
PRICING_TABLE = {
}
class CheckoutRequest(BaseModel):
@app.post("/create-checkout-session")
async def create_checkout_session(request: CheckoutRequest):
@app.post("/webhook")
async def stripe_webhook(request: Request, stripe_signature: str = Header(None)):
stripe listen --forward-to localhost:8000/webhook
curl -s https://install.stripe.com/ | sudo bash
stripe login
l01@penguin:~$ curl -s https://install.stripe.com/ | sudo bash
jeffreykimbal01@penguin:~$ stripe login
-bash: stripe: command not found
jeffreykimbal01@penguin:~$   nano main.py
nano main.py
curl -s https://packages.stripe.dev/api/security/keypair/stripe-cli-gpg/public | gpg --dearmor | sudo tee /usr/share/keyrings/stripe.gpg > /dev/null
echo "deb [signed-by=/usr/share/keyrings/stripe.gpg] https://packages.stripe.dev/stripe-cli-debian-local stable main" | sudo tee /etc/apt/sources.list.d/stripe.list
sudo apt update && sudo apt install stripe
stripe --version
stripe login
stripe listen --forward-to localhost:8000/webhook
nano .env
nano.env
nano .env
uvicorn main:app --reload
sudo apt update && sudo apt install python3-pip -y
pip install fastapi uvicorn stripe pydantic python-dotenv --break-system-packages
python3 -m uvicorn main:app --reload
stripe listen --forward-to localhost:8000/webhook
cat <<EOF > index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EVE: Wealth Gateway</title>
    <style>
        body { background-color: #1a1a1a; color: white; font-family: monospace; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .container { text-align: center; }
        .status { margin-bottom: 20px; font-size: 1.2em; color: #00ff00; }
        .pulse-button {
            width: 120px; height: 120px; border-radius: 50%; background: #FFD700;
            border: none; cursor: pointer; box-shadow: 0 0 0 0 rgba(255, 215, 0, 0.7);
            animation: pulse 2s infinite; transition: transform 0.2s;
        }
        .pulse-button:active { transform: scale(0.95); }
        @keyframes pulse {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 215, 0, 0.7); }
            70% { transform: scale(1); box-shadow: 0 0 0 20px rgba(255, 215, 0, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 215, 0, 0); }
        }
        .eye { width: 40px; height: 40px; background: black; border-radius: 50%; margin: 40px auto; }
    </style>
</head>
<body>
    <div class="container">
        <div class="status" id="statusText">EVE Online. Press for Wealth.</div>
        <button class="pulse-button" id="goldBtn"><div class="eye"></div></button>
    </div>

    <script>
        const btn = document.getElementById('goldBtn');
        const status = document.getElementById('statusText');

        btn.addEventListener('click', async () => {
            status.innerText = "Contacting Bank...";
            status.style.color = "#FFD700";

            try {
                const response = await fetch('http://127.0.0.1:8000/create-checkout-session', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ user_id: 'father_001', plan_type: 'pro_monthly' })
                });

                const data = await response.json();

                if (data.checkoutUrl) {
                    window.location.href = data.checkoutUrl;
                } else {
                    status.innerText = "Error: " + JSON.stringify(data);
                    status.style.color = "red";
                }
            } catch (e) {
                status.innerText = "Connection Failed. Is EVE Running?";
                status.style.color = "red";
                console.error(e);
            }
        });
    </script>
</body>
</html>
EOF'
python3 -m http.server 8080

cat <<EOF > main.py
import os
import stripe
from fastapi import FastAPI, HTTPException, Request, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from dotenv import load_dotenv

# Load the Keys
load_dotenv()

app = FastAPI()

# 1. ENABLE CORS (The Fix for "Nothing Happening")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all connections
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# THE VAULT KEYS
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

PRICING_TABLE = {
    "pro_monthly": os.getenv("PRO_PRICE_ID"),
    "business_seat": os.getenv("BUSINESS_PRICE_ID")
}

class CheckoutRequest(BaseModel):
    user_id: str
    plan_type: str

# 2. SERVE THE FACE DIRECTLY (Eliminates Terminal 3)
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r") as f:
        return f.read()

@app.post("/create-checkout-session")
async def create_checkout_session(request: CheckoutRequest):
    try:
        price_id = PRICING_TABLE.get(request.plan_type)
        if not price_id:
             raise HTTPException(status_code=400, detail="Invalid Plan Type (Check .env)")
             
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{'price': price_id, 'quantity': 1}],
            mode='subscription',
            success_url='https://google.com', # Placeholder for success
            cancel_url='https://google.com',  # Placeholder for cancel
            client_reference_id=request.user_id,
        )
        return {"checkoutUrl": checkout_session.url}
    except Exception as e:
        print(f"ERROR: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/webhook")
async def stripe_webhook(request: Request, stripe_signature: str = Header(None)):
    payload = await request.body()
    try:
        event = stripe.Webhook.construct_event(
            payload, stripe_signature, webhook_secret
        )
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Payload/Signature")

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(f"WEALTH GENERATED. User {session.get('client_reference_id')} upgraded.")
        
    return {"status": "success"}
EOF

stripe listen --forward-to localhost:8000/webhook
python3 -m uvicorn main:app --reload
