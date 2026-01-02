# Login Automation Test Suite

## Overview
Automated login validation using Python, pytest, and requests. Validates both successful and failed login attempts. Designed for secure, maintainable, and robust test automation with DevOps integration.

## Setup Instructions
1. **Python Installation:**
   - Requires Python 3.11
2. **Install Dependencies:**
   - `pip install -r requirements.txt`
3. **Configure Environment Variables:**
   - Copy `Tests/.env.template` to `.env` and fill in actual values for:
     - `LOGIN_URL`
     - `LOGIN_EMAIL`
     - `LOGIN_PASSWORD`
     - `INVALID_PASSWORD`
   - Use a tool like [python-dotenv](https://pypi.org/project/python-dotenv/) or export variables in your shell.

## Usage Guidelines
- Run tests:
  ```bash
  pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
  ```
- Review results in the generated XML file.

## Troubleshooting Guide
- **Network Errors:** Ensure LOGIN_URL is correct and accessible.
- **Authentication Failures:** Verify credentials in .env.
- **Missing Environment Variables:** Ensure all required secrets are set.
- **Git Errors:** Confirm repository access and token validity.

## Maintenance Procedures
- Update test scripts as authentication logic changes.
- Regenerate `.env.template` if required secrets change.
- Extend test cases in `login_test.py` for additional scenarios.

## Recommendations for Future Improvements
- Integrate with CI/CD pipelines (see .github/workflows/ci.yml)
- Add multi-user and advanced negative test cases
- Enhance reporting (HTML, notifications)

## Support Resources
- [pytest documentation](https://docs.pytest.org/)
- [requests documentation](https://docs.python-requests.org/)
- [GitHub Actions](https://docs.github.com/en/actions)
