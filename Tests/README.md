# Login Automation Test Suite

## Overview
This suite validates login functionality using Python, pytest, and requests. Credentials and login URL are securely managed via environment variables.

## Setup Instructions
1. Install Python 3.11.
2. Clone this repository.
3. Copy `Tests/.env.template` to `.env` and fill in your login URL, email, and password.
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration Steps
- Edit `.env` (based on `.env.template`) to provide `LOGIN_URL`, `LOGIN_EMAIL`, and `LOGIN_PASSWORD`.
- NEVER commit your real secrets!

## Usage Guidelines
Run the test suite:
```bash
pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
```

## Troubleshooting
- Ensure environment variables are set.
- Check network connectivity and the login endpoint.
- Review error messages in test output for details.

## Maintenance Procedures
- Update test scripts as needed in `Tests/login_test.py`.
- Keep dependencies in `requirements.txt` up to date.
- Review and rotate credentials regularly.
