# Login Automation Test Suite

## Overview
Automated Python pytest script to validate login functionality securely and reliably. Credentials are managed via environment variables for best security practices.

## Setup Instructions
1. Install Python 3.11.
2. Clone this repository.
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Copy `.env.template` to `.env` and fill in your credentials.
5. Export environment variables before running tests:
    ```
    export $(grep -v '^#' Tests/.env | xargs)
    ```

## Usage
Run the login test and generate a JUnit XML report:
```
pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
```

## Troubleshooting Guide
- **Network errors**: Check your internet connection and LOGIN_URL value.
- **Authentication failures**: Verify LOGIN_EMAIL and LOGIN_PASSWORD are correct.
- **Git errors**: Ensure your git credentials and permissions are set up.
- **Environment variable issues**: Use `printenv` or `echo $VAR` to verify values are set.

## Maintenance
- Update `.env` for new credentials as needed.
- Extend `login_test.py` for additional test cases.
- Update dependencies in `requirements.txt` when needed.

## Recommendations
- Integrate with CI/CD for automated feedback.
- Use secrets management tools for production credentials.
- Extend test coverage for edge cases and error handling.
