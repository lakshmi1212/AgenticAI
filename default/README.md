# Login Automation QA Solution

## Project Overview
Automated Python pytest script for login validation. Integrates with DevOps pipelines and version control for robust, secure authentication testing.

## Setup Instructions
1. **Python Installation**: Ensure Python 3.11 is installed.
2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Environment Variables**:
    - Copy `.env.template` to `.env` and fill in actual values for `LOGIN_URL`, `LOGIN_EMAIL`, and `LOGIN_PASSWORD`.
    - Use a secure secrets manager or CI/CD environment for production.

## Configuration Steps
- Store credentials securely. Never commit `.env` with real secrets.
- Update `login_test.py` for additional test cases as needed.

## Usage Guidelines
- Run tests:
    ```bash
    pytest Tests/login_test.py --maxfail=1 --disable-warnings -v
    ```
- View detailed logs in test output.
- For CI/CD integration, configure secrets in pipeline settings.

## Maintenance Procedures
- Update dependencies in `requirements.txt` as needed.
- Extend `Tests/login_test.py` for new scenarios.
- Rotate credentials regularly and audit for security.

## Repository Structure
- `Tests/login_test.py`: Automated login test
- `.env.template`: Environment variable template
- `requirements.txt`: Python dependencies
- `README.md`: Project documentation
- `login_test.metadata.json`: Metadata for automation and integration

## Quality Assurance
- Follows PEP8 coding standards
- Credentials handled via environment variables
- Robust error handling and logging
- Ready for DevOps pipeline integration
