# Fixes for DVSA Vulnerabilities

## Lesson 10 - Unhandled Exceptions

### Fix Applied
- Added input validation to prevent missing key errors
- Wrapped logic to avoid unhandled exceptions
- Returned safe error messages instead of raw stack traces

### Additional Fix
- Updated order-manager.js to prevent forwarding raw Lambda errors

### Result
- API no longer exposes:
  - stack traces
  - file paths
  - internal function names
