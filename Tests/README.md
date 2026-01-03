# Login Automation Test Suite

## Overview
Automated login validation using Python, pytest, and requests. Credentials managed via environment variables for security. Ready for DevOps integration.

## Setup Instructions
1. Install Python 3.11.
2. Clone the repository.
3. Copy `Tests/.env.template` to `.env` and fill in your credentials.
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
- Set the following environment variables:
  - LOGIN_URL
  - LOGIN_EMAIL
  - LOGIN_PASSWORD

## Usage
Run the test suite:
```bash
pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
```

## Maintenance
- Update credentials in `.env` as needed.
- Extend `login_test.py` for additional test cases.
- Ensure compliance with coding standards and security best practices.

## CI/CD Integration
- Ready for GitHub Actions via `.github/workflows/ci.yml` (see metadata for details).

## Troubleshooting
- Ensure all environment variables are set.
- Review error messages in test output.
- For network errors, check connectivity and API health.
