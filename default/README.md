# Login Automation with Python, pytest, and requests

## Overview
Automated login validation using Python, pytest, and requests. Credentials are managed securely via environment variables. Designed for seamless integration into DevOps pipelines with full git and CI/CD support.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI
   ```
2. Create a Python virtual environment (recommended):
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy and configure environment variables:
   ```bash
   cp .env.template .env
   # Edit .env with your LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
   ```
5. Export environment variables:
   ```bash
   export $(grep -v '^#' .env | xargs)
   ```

## Usage Guidelines
Run the login tests:
```bash
pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
```

## Configuration Steps
- Edit `.env` for credentials (never commit secrets).
- Update `LOGIN_URL` for your API endpoint.

## Maintenance Procedures
- Update dependencies in `requirements.txt` as needed.
- Extend tests in `Tests/login_test.py` for additional scenarios.
- Regenerate metadata after changes.

## Troubleshooting
- Ensure environment variables are set.
- Check API endpoint connectivity.
- Review pytest output and XML report for errors.

## CI/CD Integration
- Ready for GitHub Actions workflow (.github/workflows/ci.yml).

## Security
- No hardcoded secrets. All credentials via environment variables.
- Robust error handling and logging in test script.

## Files
- Tests/login_test.py: Main test script
- .env.template: Environment variable template
- requirements.txt: Python dependencies
- README.md: Documentation
- login_test.metadata.json: Metadata for automation
- .github/workflows/ci.yml: CI/CD workflow