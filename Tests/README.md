# Login Automation Test Suite

## Overview
Automated login validation using Python, pytest, and requests. This suite ensures authentication mechanisms are robust, secure, and ready for DevOps pipelines.

## Setup Instructions
1. **Python Installation**: Ensure Python 3.11 is installed.
2. **Clone Repository**: `git clone https://github.com/lakshmi1212/AgenticAI.git`
3. **Install Dependencies**: `pip install -r requirements.txt`
4. **Environment Variables**:
    - Copy `Tests/.env.template` to `.env` (do not commit `.env`)
    - Fill in LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
    - Export these variables in your shell or use a tool like `python-dotenv`

## Configuration Steps
- Store credentials securely (never commit secrets).
- Customize `LOGIN_URL` as needed for your environment.

## Usage Guidelines
- Run tests:
  ```bash
  pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
  ```
- Results are reported in JUnit XML for CI integration.
- Logging output provided for troubleshooting.

## Maintenance Procedures
- Update credentials in `.env` only as needed.
- Extend `login_test.py` for additional test cases or endpoints.
- Review code for security compliance before updates.

## Troubleshooting
- Ensure environment variables are set and accessible.
- Check network connectivity to LOGIN_URL.
- Review logs for error details.

## Extensibility
- Modular design allows easy extension for 2FA, CSRF, and other auth scenarios.
- Parameterization supports multiple test cases.

## Contact
- For issues, open a GitHub issue or contact the repo maintainer.
