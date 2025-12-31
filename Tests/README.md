# Login Automation Test Suite

## Overview
Automated login validation using Python 3.11, pytest, and requests. Credentials are securely managed via environment variables. Designed for easy integration with DevOps pipelines and CI/CD.

## Setup Instructions
1. **Clone the repo** and navigate to the root directory:
   ```sh
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI
   ```
2. **Install Python 3.11** (recommended) and dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. **Configure credentials:**
   - Copy `Tests/.env.template` to `.env` and fill in your values.
   - Or, export environment variables directly:
     ```sh
     export LOGIN_URL=https://your-app.example.com/login
     export LOGIN_EMAIL=your_email@example.com
     export LOGIN_PASSWORD=your_password
     ```

## Running the Tests
From the project root:
```sh
pytest Tests/login_test.py --tb=short --junitxml=login_results.xml
```
- Results are output in standard pytest format and JUnit XML for CI/CD integration.

## Git Integration Workflow
- All test scripts and config templates are version-controlled.
- Standard git actions:
  ```sh
  git add Tests/login_test.py Tests/.env.template Tests/README.md requirements.txt login_test.metadata.json
  git commit -m "Add robust login automation test suite"
  git push origin main
  ```

## Troubleshooting Guide
- **Network errors:** Check your LOGIN_URL and internet connectivity.
- **Authentication failures:** Verify LOGIN_EMAIL and LOGIN_PASSWORD are correct and active.
- **Timeouts:** Ensure the target service is up and reachable.
- **Environment variables not set:** Use `.env` or export them in your shell.
- **Git errors:** Confirm you have push access and your branch is up-to-date.

## Maintenance & Extensibility
- Update `login_test.py` to support additional test cases or endpoints.
- Add more pytest test functions for advanced scenarios (e.g., 2FA, CSRF).
- Update `requirements.txt` as new dependencies are added.
- Review logs and JUnit XML for test results and diagnostics.

## Recommendations
- Integrate with CI/CD (e.g., GitHub Actions) for automated test execution.
- Store secrets securely (never commit actual secrets).
- Expand for multi-user and advanced auth flows as needed.

## Support & Resources
- [pytest documentation](https://docs.pytest.org/)
- [requests documentation](https://docs.python-requests.org/)
- For issues, open a GitHub issue or contact your DevOps team.
