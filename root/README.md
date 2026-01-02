# Login Automation Solution

## Overview
Automated login validation using Python, pytest, and requests. Credentials are securely managed via environment variables. Fully integrated for DevOps pipelines and git workflows.

## Setup Instructions
1. **Python Installation**: Install Python 3.11.
2. **Clone Repository**: `git clone https://github.com/lakshmi1212/AgenticAI.git`
3. **Environment Variables**:
    - Copy `root/.env.template` to `.env` and fill in your credentials.
    - Export variables or use a tool like `python-dotenv`.
    - Required: `LOGIN_URL`, `LOGIN_EMAIL`, `LOGIN_PASSWORD`
4. **Dependencies**:
    - Install with `pip install -r root/requirements.txt`

## Running Tests
- Run: `pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml`
- The script will log progress and errors.
- Test results are saved in JUnit XML format for CI integration.

## Troubleshooting
- **Network Errors**: Check internet connection and LOGIN_URL validity.
- **Authentication Failures**: Verify credentials, check for 2FA or additional security requirements.
- **Missing Environment Variables**: Ensure all required variables are set.
- **Git Issues**: Confirm remote access and branch permissions.

## Maintenance
- Update dependencies in `root/requirements.txt` as needed.
- Extend tests by adding new functions to `Tests/login_test.py`.
- Do not commit real secrets; always use `.env.template` for sharing.

## Recommendations
- Integrate with CI/CD using GitHub Actions.
- Modularize tests for multi-user and edge case support.
- Regularly update Python and package dependencies.

## Support
- See documentation for common issues and escalation procedures.
