# Lesson 2 - Broken Authentication

## Vulnerability Summary
The DVSA backend failed to verify JWT signatures and trusted payload fields such as `username` and `sub`.

## Impact
An attacker can:
- Modify a valid token
- Impersonate another user
- Access victim order data

## Steps to Reproduce

1. Capture attacker token using DevTools
2. Capture victim token
3. Decode tokens to extract identity
4. Modify attacker token payload to impersonate victim
5. Send forged request using curl
6. Retrieve victim order list
7. Retrieve full victim order details

## Result
The attacker successfully accessed the victim’s data using a forged JWT token.

## Files
- `commands.txt` → commands used for exploitation and verification
- `jwt_decode.py` → script to decode JWT tokens
- `jwt_forge.py` → script to forge JWT tokens
- `screenshots/` → proof of exploitation
