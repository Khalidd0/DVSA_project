# Lesson 2: Broken Authentication

## Description
The application fails to verify JWT signatures, allowing attackers to modify token payloads and impersonate other users.

## Impact
An attacker can access another user's order data by forging a token.

## Steps Summary
1. Capture attacker token
2. Capture victim token
3. Decode tokens
4. Modify payload
5. Send forged request
6. Retrieve victim data

## Result
Victim order data was successfully accessed using a forged token.
