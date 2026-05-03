# DVSA Vulnerability Discovery and Remediation Project

This repository contains my work for the DVSA (Damn Vulnerable Serverless Application) security project. The objective of this project is to identify, exploit, analyze, and fix security vulnerabilities in a cloud-based serverless application deployed on AWS.

---

## 🔍 Project Overview

In this project, multiple real-world security vulnerabilities were discovered in a serverless architecture using AWS services such as Lambda, API Gateway, S3, and DynamoDB. Each vulnerability was analyzed by:

- Understanding intended system behavior
- Exploiting the weakness
- Evaluating the security impact
- Applying backend fixes
- Verifying the mitigation

---

## 🚨 Covered Vulnerabilities

The following vulnerabilities were identified and remediated:

- Lesson 1 & 9: Injection / Unsafe Processing
- Lesson 2: Broken Authentication
- Lesson 3: Sensitive Data Exposure
- Lesson 4: Insecure Cloud Configuration
- Lesson 5: Broken Access Control
- Lesson 6: Denial of Service (DoS)
- Lesson 7: Over-Privileged IAM Roles
- Lesson 8: Business Logic Vulnerability
- Lesson 10: Unhandled Exceptions

Each lesson includes:
- Exploitation steps
- Evidence (screenshots / logs)
- Root cause analysis
- Fix implementation
- Verification after fix

---

## 🛠 Tools Used

- AWS (Lambda, API Gateway, S3, CloudWatch, IAM)
- curl
- python3
- jq
- Browser DevTools

---

## 📁 Repository Structure

Each lesson is organized in a separate folder:

- `/lesson 1`
- `/lesson 2`
- `/lesson 3 - Sensitive Data Exposure`
- ...
- `/lesson 10 - Unhandled Exceptions`

Each folder contains a full vulnerability report following a structured format.

---

## 🧠 Key Learnings

- Importance of backend validation and secure design
- Misconfigurations in cloud environments can lead to serious risks
- Proper IAM policies are critical for security
- Error handling must not expose internal system details
- Business logic vulnerabilities can be as dangerous as technical flaws

---

## 📌 Description

This repository includes:
- Exploitation steps for each vulnerability
- Screenshots demonstrating proof of exploitation
- Root cause and security analysis
- Backend fixes and configuration improvements
- Verification of mitigation effectiveness

All work was performed in a controlled educational environment.

---
