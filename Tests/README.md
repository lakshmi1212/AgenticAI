# Login Automation Test Suite

## Overview
Automated login validation using Python, pytest, and requests. Integrates with DevOps pipelines for secure, maintainable authentication testing.

## Setup Instructions
1. **Python Installation**: Requires Python 3.11
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Environment Configuration**:
   - Copy `Tests/.env.template` to `.env` and fill in values for:
     - LOGIN_URL
     - LOGIN_EMAIL
     - LOGIN_PASSWORD
     - INVALID_PASSWORD
   - Load environment variables before running tests (recommended: use `python-dotenv` or export manually).

## Usage
Run tests and generate JUnit XML report:
```bash
pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
```

## Configuration Steps
- Store sensitive credentials in environment variables (never commit secrets).
- Use `.env` files for local development. CI/CD should inject secrets securely.

## Troubleshooting Guide
- **Network errors**: Check LOGIN_URL, internet connectivity, and firewall settings.
- **Authentication failures**: Verify credentials, check for account lockout.
- **Git errors**: Ensure you have push access and correct branch.
- **JSON errors**: Ensure login endpoint returns valid JSON.

## Maintenance Procedures
- Update dependencies in `requirements.txt` as needed.
- Add new test cases to `Tests/login_test.py` for enhanced coverage.
- Rotate credentials regularly and audit access.

## Recommendations for Improvement
- Integrate with CI/CD (see `.github/workflows/ci.yml`).
- Extend for multi-user, 2FA, and advanced error scenarios.
- Modularize code for scalability.

## Support & Resources
- For issues, consult logs and error messages.
- Reach out to maintainers or DevOps team for advanced support.
