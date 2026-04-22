# Lesson 1 and Lesson 9 - Event Injection & Vulnerable Dependencies

## Summary
The DVSA backend used an unsafe dependency (`node-serialize`) to process user input. This allowed attacker-controlled input to be executed as JavaScript code inside the Lambda function.

## Vulnerabilities
- Lesson 1: Event Injection (Code Injection)
- Lesson 9: Vulnerable Dependencies

## Root Cause
The application unserialized attacker-controlled input using `node-serialize`, which allows function execution through special payloads like `$$ND_FUNC$$`.

## Impact
An attacker can:
- execute arbitrary code in Lambda
- perform file operations
- potentially access AWS services

## Result
CloudWatch logs confirmed code execution:

FILE READ SUCCESS: You are reading the contents of my hacked file

## Fix Overview
- removed `node-serialize` usage
- replaced unsafe parsing with `JSON.parse`
- added allowlist validation for actions
