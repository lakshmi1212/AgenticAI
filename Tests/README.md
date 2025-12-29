# Login Automation Test Suite

## Overview
This suite provides robust, secure, and maintainable automated login validation using Python, pytest, and requests. It supports DevOps integration, secure credential management, and full git workflow compatibility.

## Features
- Python/pytest-based login automation
- Environment variable or .env-based credential parameterization
- Positive and negative test cases (success/failure)
- Robust error handling and logging
- JUnit XML/HTML test result reporting
- Git integration for version control and traceability

## Setup Instructions
1. **Clone Repo**
   ```sh
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI/Tests
   ```
2. **Install Python & Dependencies**
   - Python 3.8+
   - Install dependencies:
     ```sh
     pip install pytest requests python-dotenv
     ```
3. **Credential Configuration**
   - Copy `.env.template` to `.env` and fill with your login details, or set environment variables directly:
     ```sh
     cp .env.template .env
     # Edit .env with your LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
     ```
   - Alternatively, export environment variables:
     ```sh
     export LOGIN_URL=https://your-app/login
     export LOGIN_EMAIL=your@email.com
     export LOGIN_PASSWORD=your-password
     ```

## Running the Tests
Run all tests and generate JUnit XML report:
```sh
pytest login_test.py --junitxml=results.xml
```
- For HTML report (optional):
  ```sh
  pip install pytest-html
  pytest login_test.py --html=results.html
  ```

## Test Cases
- **test_login_success**: Valid credentials, expects HTTP 200 and success indicator.
- **test_login_failure**: Invalid password, expects HTTP 401/403/400 or failure indicator.

## Git Workflow
- Initialize repo: `git init`
- Add files: `git add login_test.py .env.template README.md`
- Commit: `git commit -m 'Add login automation test suite'`
- Push: `git push origin main`

## Troubleshooting
- **Missing credentials/URL**: Ensure environment variables or .env are set.
- **Network/auth errors**: Check server availability and credentials.
- **Git errors**: Verify access rights and remote branch existence.
- **Test fails unexpectedly**: Inspect logs in test output for error details.

## Maintenance
- Update credentials in .env or environment variables as needed.
- Extend `login_test.py` for new test cases (e.g., 2FA, lockout scenarios).
- Review logs and reports after each run.
- Update dependencies regularly (`pip list --outdated`).

## Recommendations & Future Improvements
- Integrate with CI/CD (e.g., GitHub Actions) for automated test execution on push/PR.
- Expand test suite for multi-user, 2FA, and advanced security scenarios.
- Modularize code for reuse and scalability.
- Monitor test pass rates and maintain commit history for traceability.

## Support
- For issues, review logs and consult README troubleshooting.
- Escalate to DevOps/QA lead if problems persist.
- Community: [pytest docs](https://docs.pytest.org/), [requests docs](https://docs.python-requests.org/)
