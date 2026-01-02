# Login Automation with Python & Pytest

## Overview
Automated login validation using Python, pytest, and requests. Credentials are securely managed via environment variables. Includes positive and negative test cases.

## Setup Instructions
1. Clone the repository.
2. Copy `Tests/.env.template` to `.env` and fill in actual values for:
   - LOGIN_URL
   - LOGIN_EMAIL
   - LOGIN_PASSWORD
   - INVALID_PASSWORD
3. Install Python 3.11 and dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests
```bash
pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
```

## Configuration
- All secrets are managed via environment variables. Never commit actual credentials.
- Update `.env` for different environments/users.

## Troubleshooting
- **Network errors**: Ensure LOGIN_URL is reachable.
- **Authentication failures**: Verify credentials and endpoint.
- **Git errors**: Ensure you have push access and correct branch.

## Maintenance
- Update scripts and `.env.template` for new test cases or credential changes.
- Extend tests for new authentication methods as needed.

## Support & Future Enhancements
- Integrate with CI/CD using GitHub Actions (`.github/workflows/ci.yml`).
- Modularize for multi-user or multi-endpoint scenarios.
- Add advanced reporting and test data management.

## Required Secrets
- LOGIN_URL
- LOGIN_EMAIL
- LOGIN_PASSWORD
- INVALID_PASSWORD
