import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

# Prefer env; fallback is your existing Stripe Payment Link from eve_1.py
PAYMENT_LINK = os.getenv(
    "STRIPE_PAYMENT_LINK",
    "https://buy.stripe.com/aFa6oI1cj2RVbZEbkN77O08",
).strip()

PRICE_LABEL = os.getenv("PRICE_LABEL", "$10.00 ACCESS")


def page(body: str, title: str = "EVE WEALTH GATE") -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <style>
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0; min-height: 100vh; display: flex; align-items: center; justify-content: center;
      background: #000; color: #fff; font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    }}
    .wrap {{ text-align: center; padding: 2rem; max-width: 28rem; }}
    h1 {{ letter-spacing: 0.2em; font-size: 1.25rem; margin: 0 0 1.5rem; color: #FFD700; }}
    .price {{ font-size: 1.75rem; margin: 0 0 2rem; }}
    .btn {{
      display: inline-block; text-decoration: none; color: #000; background: #FFD700;
      border: 3px solid #C5A000; padding: 1rem 2rem; font-weight: 700; font-size: 1.1rem;
      border-radius: 999px; box-shadow: 0 0 40px rgba(255, 215, 0, 0.45);
      transition: transform 0.15s ease, box-shadow 0.15s ease;
    }}
    .btn:hover {{ transform: scale(1.04); box-shadow: 0 0 60px rgba(255, 215, 0, 0.7); }}
    .sub {{ color: #888; margin-top: 1.5rem; font-size: 0.85rem; }}
    .eye {{
      width: 140px; height: 140px; border-radius: 50%; background: #FFD700; border: 5px solid #C5A000;
      margin: 0 auto 1.75rem; display: flex; align-items: center; justify-content: center;
      box-shadow: 0 0 50px #FFD700; animation: pulse 2s infinite;
    }}
    .pupil {{ width: 42px; height: 42px; border-radius: 50%; background: #000; }}
    @keyframes pulse {{
      0% {{ transform: scale(0.96); }}
      70% {{ transform: scale(1.04); }}
      100% {{ transform: scale(0.96); }}
    }}
  </style>
</head>
<body>
  <div class="wrap">{body}</div>
</body>
</html>"""


@app.get("/", response_class=HTMLResponse)
async def home():
    if not PAYMENT_LINK:
        return HTMLResponse(
            page(
                "<h1>EVE WEALTH GATE</h1>"
                "<p class='price'>Payment link not configured</p>"
                "<p class='sub'>Set STRIPE_PAYMENT_LINK in Vercel env.</p>"
            ),
            status_code=503,
        )
    body = f"""
    <div class="eye"><div class="pupil"></div></div>
    <h1>EVE IS ONLINE</h1>
    <p class="price">{PRICE_LABEL}</p>
    <a class="btn" href="/pay">PAY NOW</a>
    <p class="sub">Secure checkout powered by Stripe</p>
    """
    return HTMLResponse(page(body))


@app.get("/pay")
async def pay():
    if not PAYMENT_LINK:
        return HTMLResponse(page("<h1>Unavailable</h1><p class='sub'>No payment link configured.</p>"), status_code=503)
    return RedirectResponse(url=PAYMENT_LINK, status_code=302)


@app.get("/success", response_class=HTMLResponse)
async def success():
    body = """
    <h1>PAYMENT RECEIVED</h1>
    <p class="price">Thank you.</p>
    <p class="sub">EVE WEALTH GATE</p>
    """
    return HTMLResponse(page(body, title="Payment success"))


@app.get("/health")
async def health():
    return {"ok": True, "payments_configured": bool(PAYMENT_LINK)}
