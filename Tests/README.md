# Login Automation Test Suite

## Overview
Automated login validation using Python, pytest, and requests. Credentials are managed securely via environment variables.

## Setup Instructions
1. Install Python 3.11
2. Clone the repository
3. Copy `Tests/.env.template` to `.env` and fill in your credentials
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests
```bash
pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
```

## Configuration
- Credentials and login endpoint are set via environment variables.
- See `.env.template` for required variables.

## Troubleshooting
- **Network errors**: Check your LOGIN_URL and network connectivity.
- **Authentication failures**: Verify credentials in your .env file.
- **Git errors**: Ensure you have proper permissions and your token is valid.

## Maintenance
- Update dependencies in `requirements.txt` as needed.
- Extend tests by adding more cases to `login_test.py`.
- Keep secrets out of version control.

## Future Improvements
- Integrate with CI/CD pipelines (.github/workflows/ci.yml)
- Support for additional authentication methods
- Advanced reporting and test data management
