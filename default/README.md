# Login Automation Solution

## Overview
Automated login validation using Python, pytest, and requests. Integrates with DevOps pipelines and GitHub for robust, secure, and maintainable QA automation.

## Features
- Secure credential management via environment variables
- Positive/negative login test cases
- Robust error handling and reporting
- Ready for CI/CD integration (GitHub Actions)

## Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI
   ```
2. Copy and configure environment variables:
   ```sh
   cp .env.template .env
   # Edit .env and set LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
   ```
3. Install dependencies:
   ```sh
   python3.11 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Running Tests
```sh
pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
```

## CI/CD Integration
- Ready for GitHub Actions (see .github/workflows/ci.yml)

## Maintenance
- Update test scripts in `Tests/`
- Manage credentials securely in `.env`
- Extend tests for additional scenarios as needed

## Troubleshooting
- Ensure all environment variables are set
- Check network connectivity to LOGIN_URL
- Review pytest output and logs

## Contact
For support, contact the repository maintainer.