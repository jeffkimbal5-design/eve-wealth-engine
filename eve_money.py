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
