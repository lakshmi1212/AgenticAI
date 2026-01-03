# Login Automation Solution

## Overview
Automated login validation using Python, pytest, and requests. Credentials and login URL are securely managed using environment variables. Designed for integration with DevOps pipelines and GitHub Actions.

## Setup Instructions
1. **Clone the repository:**
   ```sh
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI
   ```
2. **Python Installation:**
   - Requires Python 3.11
   - Install dependencies:
     ```sh
     pip install -r requirements.txt
     ```
3. **Environment Configuration:**
   - Copy `.env.template` to `.env` and fill in your credentials:
     ```sh
     cp .env.template .env
     ```
   - Edit `.env` to provide `LOGIN_URL`, `LOGIN_EMAIL`, and `LOGIN_PASSWORD`.

## Usage Guidelines
- Run tests:
  ```sh
  pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
  ```
- Test results will be stored in `Tests/login_test_results.xml`.

## Troubleshooting
- Ensure all required environment variables are set.
- Check network connectivity to the login URL.
- Review logs for error details.

## Maintenance Procedures
- Update dependencies in `requirements.txt` as needed.
- Extend `Tests/login_test.py` for additional test cases.
- Securely manage and rotate credentials in `.env`.

## Security & Compliance
- No credentials are hardcoded in the test script.
- All sensitive information is managed via environment variables.
- Follows PEP8 and QA automation best practices.
