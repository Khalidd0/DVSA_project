## Lesson 7 - Over-Privileged Function

### Fix Applied
- Removed excessive permissions from Lambda execution role
- Removed DynamoDB full access
- Removed wildcard S3 access
- Replaced SES full access with limited send-only permissions

### IAM Changes
Before:
- dynamodb:* (full database access)
- s3:* (all buckets)
- ses:* (full email control)

After:
- s3:GetObject only for receipts bucket
- ses:SendEmail and SendRawEmail only

### Result
- DynamoDB scan is denied after fix
- AWS credentials can no longer be abused
