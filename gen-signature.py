import hmac
import hashlib
with open('payload.json', 'rb') as f:
    payload = f.read()
secret = "your_secret"
signature = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
print(f"sha256={signature}")