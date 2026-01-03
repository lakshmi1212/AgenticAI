# Login Automation Solution

## Overview
Automated login validation using Python, pytest, and requests. Credentials are securely managed via environment variables. Fully integrated with Git and CI/CD pipelines.

## Setup Instructions
1. **Python Installation**: Ensure Python 3.11 is installed.
2. **Clone the Repository**:
   ```bash
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure Environment Variables**:
   - Copy `.env.template` to `.env` and fill in your credentials.
   - Export environment variables or use a dotenv loader.

## Configuration Steps
- Update `.env` with your login URL, email, and password.
- **Never commit secrets to source control.**

## Usage Guidelines
- Run tests:
  ```bash
  pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
  ```
- Results are saved in JUnit XML format for CI integration.

## Maintenance Procedures
- Update credentials in `.env` as needed.
- Extend `Tests/login_test.py` for new test cases.
- Keep dependencies up to date in `requirements.txt`.

## CI/CD Integration
- GitHub Actions workflow is provided in `.github/workflows/ci.yml`.

## Troubleshooting
- Ensure all environment variables are set.
- Check network connectivity to login URL.
- Review error messages in test output.

## Security
- Credentials are never hardcoded in code or committed to git.
- Handle secrets via environment variables or secure vaults.

## Extensibility
- Modular script design supports additional authentication flows and test cases.
