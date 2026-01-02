# Login Automation Solution

## Overview
Automated login validation using Python, pytest, and requests. Credentials are securely managed via environment variables. Designed for robust QA and DevOps integration.

## Setup Instructions
1. **Clone Repository:**
    ```bash
    git clone https://github.com/lakshmi1212/AgenticAI.git
    cd AgenticAI
    ```
2. **Install Python (3.11 recommended):**
    Ensure Python 3.11 is installed.
3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Configure Environment Variables:**
    - Copy `Tests/.env.template` to `.env` and fill in your credentials.
    - Export the variables or use a tool like [python-dotenv](https://pypi.org/project/python-dotenv/) if desired.
    ```bash
    export LOGIN_URL=https://your-app.com/api/login
    export LOGIN_EMAIL=your@email.com
    export LOGIN_PASSWORD=your_password
    ```

## Running the Tests
```bash
pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
```
- Results are saved as JUnit XML for CI/CD integration.

## Troubleshooting Guide
- **Missing Environment Variables:** Ensure LOGIN_URL, LOGIN_EMAIL, and LOGIN_PASSWORD are set.
- **Network Errors:** Check network connectivity and endpoint URL.
- **Authentication Failures:** Verify credentials and check for account lockout or 2FA requirements.
- **Git Errors:** Ensure you have write access and correct credentials for git operations.
- **Response Not JSON:** Check if the endpoint is correct and returning expected data.

## Maintenance Procedures
- Update scripts in `Tests/` as needed.
- NEVER commit real secrets or `.env` files.
- Update `requirements.txt` when dependencies change.
- Extend tests by adding new pytest functions or fixtures in `login_test.py`.

## Enhancement Recommendations
- Integrate with CI/CD using `.github/workflows/ci.yml`.
- Add support for multi-user login scenarios and negative test cases.
- Modularize for advanced reporting and 2FA/multi-step authentication.

## Support & Resources
- [Pytest Documentation](https://docs.pytest.org/en/stable/)
- [Requests Documentation](https://docs.python-requests.org/en/latest/)
- For advanced issues, escalate to your QA/DevOps lead.
