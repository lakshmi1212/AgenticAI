# Login Automation Test Suite

## Overview
This project provides a robust, secure, and maintainable automated login validation solution using Python, pytest, and requests. It is designed for seamless integration with DevOps pipelines and GitHub workflows.

## Features
- Automated login validation via HTTP POST
- Environment variable-based credential management (no hardcoded secrets)
- Positive and negative test cases
- Logging and error handling
- JUnit XML and HTML reporting support
- Ready for CI/CD integration

## Setup Instructions
1. **Clone the repository:**
   ```sh
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI/Laks
   ```
2. **Python environment:**
   - Python 3.8+ required
   - Install dependencies:
     ```sh
     pip install pytest requests pytest-html
     ```
3. **Configure credentials:**
   - Copy `.env.template` to `.env` and update values, or set environment variables directly:
     ```sh
     export LOGIN_URL=https://your-app.com/login
     export LOGIN_EMAIL=your_email@example.com
     export LOGIN_PASSWORD=your_password_here
     ```
   - Alternatively, use a tool like `python-dotenv` to load from `.env`.

## Usage
- **Run tests:**
  ```sh
  pytest --maxfail=2 --disable-warnings --junitxml=results.xml login_test.py
  ```
- **HTML report:**
  ```sh
  pytest --html=report.html login_test.py
  ```
- **Test Results:**
  - Reports are generated as `results.xml` (JUnit XML) and/or `report.html`.

## Git Integration Workflow
- Initialize (if needed): `git init`
- Add files: `git add login_test.py .env.template README.md`
- Commit: `git commit -m 'Add login automation test suite'`
- Push: `git push origin main`

## Troubleshooting Guide
- **Missing credentials:** Ensure environment variables are set or `.env` is configured.
- **Network errors:** Check connectivity and login URL.
- **Authentication failures:** Verify email and password are correct; check for account lockout or 2FA.
- **Git errors:** Ensure you have push access and correct branch.
- **Test failures:** Review `results.xml` or `report.html` for detailed errors.

## Maintenance Procedures
- Update dependencies as needed (`pip install -U ...`).
- Extend tests for new login scenarios by editing `login_test.py`.
- Rotate credentials regularly and avoid committing secrets.

## Recommendations & Future Improvements
- Integrate with GitHub Actions for automated testing on push/PR.
- Add support for advanced authentication (2FA, CSRF, SSO).
- Modularize for multi-user and multi-endpoint testing.
- Enhance reporting and notification (Slack/email alerts).
- Schedule regular test runs and dependency updates.

## Support & Resources
- Refer to [pytest documentation](https://docs.pytest.org/)
- For CI/CD: [GitHub Actions](https://docs.github.com/en/actions)
- Community: [Python Requests](https://docs.python-requests.org/en/master/)

## License
MIT
