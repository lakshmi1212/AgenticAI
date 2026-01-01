# Login Automation Test Suite

## Overview
Automated login validation using Python, pytest, and requests. Credentials are securely managed via environment variables for robust, secure, and maintainable testing.

## Setup Instructions
1. **Python Installation**:
   - Install Python 3.11.
2. **Install Dependencies**:
   - Run: `pip install -r ../requirements.txt` (from the Tests directory)
3. **Configure Environment Variables**:
   - Copy `.env.template` to `.env` and set values, or export variables:
     - LOGIN_URL
     - LOGIN_EMAIL
     - LOGIN_PASSWORD
   - Example:
     ```bash
     export LOGIN_URL=https://your-login-url.example.com/login
     export LOGIN_EMAIL=your.email@example.com
     export LOGIN_PASSWORD=your_secure_password
     ```

## Running the Test
- From the root directory, run:
  ```bash
  pytest Tests/login_test.py --maxfail=1 --disable-warnings --junitxml=login_test_results.xml
  ```
- Test results are output in JUnit XML format (`login_test_results.xml`).

## Git Integration Workflow
1. Initialize repo (if not already):
   ```bash
   git init
   git remote add origin https://github.com/lakshmi1212/AgenticAI.git
   ```
2. Add files:
   ```bash
   git add Tests/login_test.py Tests/README.md Tests/.env.template requirements.txt login_test.metadata.json
   ```
3. Commit and push:
   ```bash
   git commit -m "Add login automation test suite"
   git push origin main
   ```

## Troubleshooting
- **Network errors**: Check your internet and login URL.
- **Authentication failures**: Verify credentials and environment variable setup.
- **Git errors**: Ensure correct remote, branch, and permissions.
- **Log analysis**: Review logs/output for detailed error messages.

## Maintenance & Extensibility
- Update dependencies in `requirements.txt`.
- Extend test cases in `login_test.py` for additional scenarios.
- For advanced reporting and CI/CD, integrate with `.github/workflows/ci.yml`.

## Support & Resources
- [pytest documentation](https://docs.pytest.org/en/stable/)
- [requests documentation](https://docs.python-requests.org/en/latest/)
- [GitHub Actions](https://docs.github.com/en/actions)

## Recommendations
- Use CI/CD for automated test execution and result reporting.
- Never commit real secrets; use `.env.template` and environment variables.
- Expand tests for multi-user and negative scenarios as needed.
