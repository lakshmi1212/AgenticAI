# Login Automation with Python, pytest, and requests

## Overview
Automated login validation using Python, pytest, and requests. Secure credential handling via environment variables. Integrates with DevOps pipelines and GitHub Actions.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI
   ```
2. **Python Installation:**
   - Install Python 3.11 from [python.org](https://www.python.org/downloads/release/python-3110/)

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables:**
   - Copy `.env.template` to `.env` and set your credentials and login URL.
   - Or, set environment variables directly:
     - `LOGIN_URL`
     - `LOGIN_EMAIL`
     - `LOGIN_PASSWORD`

## Usage Guidelines

Run the tests:
```bash
pytest Tests/login_test.py
```

### Test Results
- JUnit XML and HTML reports can be generated via pytest options.
- Test covers both successful and failed login scenarios.

## Maintenance Procedures
- Update credentials in `.env` as needed.
- Extend `Tests/login_test.py` for more test cases (e.g., 2FA, CSRF).
- Keep dependencies updated in `requirements.txt`.

## Troubleshooting
- Ensure environment variables are set and valid.
- Review error messages in pytest output for details.

## Security Notes
- **Never commit secrets to the repository.** Use `.env.template` for examples only.
- Credentials are loaded securely at runtime.

## Extensibility
- Modular test structure allows easy extension for more authentication scenarios.

---

© 2024 AgenticAI DevOps & QA Automation
