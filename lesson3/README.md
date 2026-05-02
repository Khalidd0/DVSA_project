# Lesson 3 – Sensitive Data Exposure

## Summary
The DVSA application stores receipt data in an S3 bucket and exposes backend error messages when processing API requests. This leads to potential sensitive data exposure and information leakage.

## Vulnerability
- Sensitive Data Exposure
- Improper Error Handling

## Root Cause
The application:
- stores receipt files in S3 in a predictable structure
- does not properly protect sensitive data
- returns raw backend error messages to the user

## Exploitation Steps
1. User A creates and completes an order.
2. Receipt files are generated and stored in S3.
3. Direct access to the receipt file is attempted through the browser.
4. User B attempts to access User A’s order using the API.
5. The backend returns an error with internal stack trace details.

## Impact
An attacker can:
- identify storage structure of sensitive data
- gain insight into backend implementation
- use leaked information for further attacks

## Result
The system returned:
- AccessDenied when accessing S3 file directly
- backend error and stack trace when calling API
- internal file path `/var/task/get_order.py`

## Evidence

### Figure 1 – S3 Receipt Files
![S3](screenshots/figure1-s3-receipt-files.png)

### Figure 2 – Access Denied
![AccessDenied](screenshots/figure2-access-denied.png)

### Figure 3 – API Error Leakage
![Error](screenshots/figure3-api-stack-trace.png)

## Fix Overview
- hide internal error messages from users
- use generic error responses
- enforce strict access control on S3
- use pre-signed URLs for file access
- encrypt sensitive data at rest

## Video Demonstration
[Add your video link here]