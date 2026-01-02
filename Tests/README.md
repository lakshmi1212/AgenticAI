# Login Automation Test Suite

This repository contains a robust, secure, and maintainable login automation solution using Python and pytest.

## Features
- Validates login endpoint using credentials from environment variables
- Generates JUnit XML reports for CI/CD integration
- Robust error handling and logging
- Secure credential management

## Setup Instructions

1. **Python Installation**
   - Install Python 3.11 from [python.org](https://www.python.org/downloads/release/python-3110/)

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   - Copy `Tests/.env.template` to `.env` and update with your credentials
   - Export variables before running tests:
     ```bash
     export LOGIN_URL=https://your-login-endpoint.example.com/api/login
     export LOGIN_EMAIL=your-email@example.com
     export LOGIN_PASSWORD=your-secure-password
     ```

## Usage

Run the login test:
```bash
pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
```

## Test Results
- JUnit XML report is generated at `Tests/login_test_results.xml`
- Logs are output to console; customize as needed in `login_test.py`

## Troubleshooting Guide
- **Network errors**: Ensure endpoint is reachable and credentials are correct.
- **Authentication failures**: Verify email/password, check for 2FA or additional security requirements.
- **Missing environment variables**: Ensure all required variables are exported.
- **Git errors**: Confirm repository access and permissions.

## Maintenance Procedures
- Update dependencies in `requirements.txt` as needed
- Extend `login_test.py` for additional test cases or endpoints
- Manage credentials securely, never commit `.env` files

## Recommendations & Future Improvements
- Integrate with CI/CD pipeline using `.github/workflows/ci.yml`
- Support for multi-user and advanced authentication (2FA, OAuth)
- Modularize for extensibility

## Support Resources
- [pytest documentation](https://docs.pytest.org/en/stable/)
- [requests documentation](https://requests.readthedocs.io/en/latest/)
- GitHub repository issues

## License
MIT
