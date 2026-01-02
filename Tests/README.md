# Login Automation Test Suite

## Overview
Automated login validation using Python, pytest, and requests. Credentials are managed securely via environment variables. Includes robust error handling and logging.

## Setup Instructions
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI
   ```
2. **Install Python 3.11 and pip:**
   Ensure Python version is 3.11. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. **Configure Secrets:**
   - Copy `Tests/.env.template` to `.env` and fill in LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD.
   - Export secrets to environment variables or use a tool like `python-dotenv`.

## Running Tests
```sh
pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
```

## Test Results
- Results are saved in `Tests/login_test_results.xml` (JUnit format).
- Detailed logs in `Tests/login_test.log`.

## Troubleshooting
- **Network Errors:** Check internet connection and LOGIN_URL.
- **Authentication Failures:** Verify credentials and endpoint.
- **Git Errors:** Confirm access rights and remote settings.

## Maintenance
- Update scripts as needed, add new test cases in `Tests/`.
- NEVER commit `.env` with secrets.
- Review dependencies in `requirements.txt` regularly.

## Security Notes
- No credentials are hardcoded; always use environment variables.
- Sensitive files (e.g., `.env`) should be excluded from git.

## Recommendations
- Integrate with CI/CD via `.github/workflows/ci.yml`.
- Extend for multi-user, 2FA, and advanced reporting as needed.

## Support & Escalation
- For persistent issues, review logs and consult documentation.
- Escalate to DevOps or security for unresolved authentication problems.
