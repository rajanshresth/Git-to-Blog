import hmac
import hashlib
with open('payload.json', 'rb') as f:
    payload = f.read()
secret = "your_webhook_secret"  # must match your .env and GitHub webhook secret
signature = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
print(f"sha256={signature}")