# Lesson 10 - Unhandled Exceptions

## Summary
The application exposes internal error messages and stack traces when invalid input is provided.

## Impact
Attackers can gain insight into backend logic, file paths, and function behavior.

## Result
After fix, errors return safe generic messages without exposing internal details.
