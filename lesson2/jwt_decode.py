import os, json, base64

def decode(token):
    payload = token.split(".")[1]
    payload += "=" * (-len(payload) % 4)
    return json.loads(base64.urlsafe_b64decode(payload.encode()))

token = input("Enter JWT: ")
data = decode(token)

print("Username:", data.get("username"))
print("Sub:", data.get("sub"))
