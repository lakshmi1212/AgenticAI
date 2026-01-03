# Login Automation Solution

## Project Overview
Automated login validation using Python, pytest, and requests, fully integrated for DevOps pipelines.

## Setup Instructions
1. Install Python 3.11.
2. Clone this repository.
3. Create a `.env` file using `.env.template` and provide correct credentials.
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Export environment variables:
   ```bash
   export $(grep -v '^#' .env | xargs)
   ```

## Configuration Steps
- Edit `.env.template` with your LOGIN_URL, LOGIN_EMAIL, and LOGIN_PASSWORD.
- Never commit actual secrets to git; use environment variables or secret stores in CI/CD.

## Usage Guidelines
- Run tests with:
  ```bash
  pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
  ```
- Review `Tests/login_test_results.xml` for test outcomes.

## Maintenance Procedures
- Update test logic in `Tests/login_test.py` for new scenarios.
- Update dependencies in `requirements.txt` as needed.
- Rotate credentials securely and update `.env`.

## CI/CD Integration
- GitHub Actions workflow is provided in `.github/workflows/ci.yml`.
- Ensure secrets are set in repository settings for secure CI execution.

## Security Notes
- No secrets are hardcoded.
- All credentials handled via environment variables.

## Extensibility
- Modular test script for future test case additions.
- Scalable for expanded authentication scenarios (2FA, tokens, etc).
