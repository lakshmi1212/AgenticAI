# Login Automation Test Suite

## Overview
Automated login validation with Python, pytest, and requests. Secure credential handling via environment variables. Robust error handling and DevOps-ready git integration.

## Setup Instructions
1. **Install Python 3.11** (recommended).
2. **Install dependencies**:
   ```bash
   pip install -r ../requirements.txt
   ```
3. **Configure environment variables**:
   - Copy `.env.template` to `.env` (do NOT commit `.env`).
   - Set values for `LOGIN_URL`, `LOGIN_EMAIL`, `LOGIN_PASSWORD`.
   - Or, export them directly in your shell.

## Running Tests
- From the `Tests/` directory:
  ```bash
  pytest login_test.py --maxfail=2 --disable-warnings --tb=short
  ```
- For JUnit XML (CI/CD integration):
  ```bash
  pytest login_test.py --junitxml=results.xml
  ```
- For HTML report (if plugin installed):
  ```bash
  pytest login_test.py --html=results.html
  ```

## Git Integration
- All test assets are under version control.
- Standard workflow:
  ```bash
  git add login_test.py .env.template README.md
  git commit -m 'Add login automation test suite'
  git push origin main
  ```

## Troubleshooting Guide
- **Network error**: Check your URL and network connectivity. Proxy/firewall issues can block requests.
- **Authentication failure**: Verify credentials. Check for typos and ensure user is registered.
- **Environment variables not set**: Ensure `.env` is sourced or variables are exported.
- **Git errors**: Confirm you have push access and correct remote URL.

## Maintenance & Extensibility
- Add new test cases to `login_test.py` with `@pytest.mark.parametrize`.
- Update `.env.template` if new secrets are required.
- Keep dependencies in `requirements.txt` up to date.

## Security Best Practices
- Never commit real secrets or `.env` files.
- Use CI/CD secret managers for pipeline integration.

## Recommendations
- Integrate with GitHub Actions for automated test execution.
- Extend for multi-user or 2FA flows as needed.
- Review and update test cases regularly to match auth logic.
