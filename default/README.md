# Login Automation Solution

## Overview
Automated Python pytest script for login validation with secure credential handling and full git integration. Designed for rapid feedback in DevOps pipelines.

## Setup Instructions
1. Clone the repository:
    ```bash
    git clone https://github.com/lakshmi1212/AgenticAI.git
    cd AgenticAI
    ```
2. Install Python 3.11.
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Copy `.env.template` to `.env` and fill in your credentials:
    ```bash
    cp .env.template .env
    # Edit .env and set LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
    ```
5. Export environment variables or use a tool like `python-dotenv`.

## Running Tests
```bash
pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
```

## CI/CD Integration
- The solution is ready for GitHub Actions integration via `.github/workflows/ci.yml`.

## Troubleshooting
- Ensure all environment variables are set before running tests.
- Check network connectivity to the LOGIN_URL.
- Review test logs and JUnit XML report for details.

## Maintenance
- Update scripts and credentials as needed.
- Extend `Tests/login_test.py` for additional test cases.

## Security Notice
- **Never commit real credentials to version control.** Use environment variables and `.env.template`.
