# Lesson 5 - Broken Access Control

## Summary
The public Lambda function could invoke an admin-only function due to excessive permissions.

## Impact
An attacker could mark an order as paid without completing billing.

## Result
Order state changed from unpaid to paid without legitimate workflow.
