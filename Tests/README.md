# Login Automation Test Suite

## Overview
This suite provides a robust, secure, and maintainable login automation test using Python, pytest, and requests. It is designed for DevOps pipelines with full git integration, test reporting, and best practices in credential management.

## Features
- Parameterized login tests (positive/negative)
- Secure credential handling (via environment variables or .env)
- Robust error handling and logging
- JUnit XML test report for CI/CD integration
- Comprehensive documentation and troubleshooting guide

## Setup Instructions
1. **Clone the repo**
    ```bash
    git clone https://github.com/lakshmi1212/AgenticAI.git
    cd AgenticAI/Tests
    ```
2. **Install dependencies**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install pytest requests python-dotenv
    ```
3. **Configure credentials**
    - Copy `.env.template` to `.env` and fill in your login details:
      ```bash
      cp .env.template .env
      # Edit .env with your LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
      ```
    - Alternatively, set environment variables:
      ```bash
      export LOGIN_URL=https://your-app.com/api/login
      export LOGIN_EMAIL=your-email@example.com
      export LOGIN_PASSWORD=your-secure-password
      ```

## Running Tests
```bash
pytest --junitxml=results.xml login_test.py
```
- Results are available in `results.xml` for integration with CI/CD systems.

## Git Integration Workflow
```bash
git add login_test.py .env.template README.md
git commit -m "Add login automation test suite"
git push origin main
```

## Troubleshooting Guide
- **Network errors:** Check connectivity and LOGIN_URL correctness; review logs for details.
- **Authentication failures:** Verify credentials in your .env or environment variables; ensure your account is active.
- **Unexpected test errors:** Review logs and test output; validate the login endpoint and parameters.
- **Git errors:** Confirm remote URL and branch; ensure you have push access.

## Maintenance Procedures
- Update dependencies: `pip install -U -r requirements.txt` (if requirements.txt is used)
- Change credentials: Edit `.env` or update environment variables.
- Extend tests: Add more scenarios to `test_login` or create new test functions.

## Recommendations and Future Improvements
- Integrate with CI/CD (e.g., GitHub Actions)
- Add support for 2FA, CSRF, or SSO if required
- Expand for additional test cases and advanced reporting (HTML)
- Modularize for multi-user and multi-environment support

## Support & Resources
- [pytest documentation](https://docs.pytest.org/)
- [requests documentation](https://docs.python-requests.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

**Security Notice:** Never commit `.env` files or hardcoded secrets to version control. Always use environment variables or secure vaults in production/CI.
