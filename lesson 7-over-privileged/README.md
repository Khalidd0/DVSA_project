# Lesson 7 - Over-Privileged Function

## Summary
The Lambda function was assigned excessive permissions, allowing access to DynamoDB data.

## Impact
An attacker can use leaked credentials to access sensitive data.

## Result
After fix, access to DynamoDB was denied, proving least privilege enforcement.
