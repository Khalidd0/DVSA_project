# Lesson 1 - Event Injection

## Vulnerability Summary
The DVSA backend used unsafe deserialization (`node-serialize`) to process user input. This allowed attacker-controlled input to be executed as JavaScript code.

## Impact
An attacker can execute arbitrary code inside the Lambda function, leading to Remote Code Execution (RCE).

## Exploit Overview
A malicious payload containing `$$ND_FUNC$$` was sent to the `/order` endpoint. The backend executed the injected code, which wrote and read a file inside `/tmp` and printed the result in CloudWatch logs.

## Result
The CloudWatch logs showed:
FILE READ SUCCESS: You are reading the contents of my hacked file

This confirms successful code execution.
