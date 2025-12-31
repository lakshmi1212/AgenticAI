# Login Automation Test Suite

## Overview
Automated login validation using Python 3.11, pytest, and requests. Credentials are handled securely via environment variables. Includes positive and negative test cases, robust error handling, and logging. Ready for DevOps and CI/CD integration.

---

## Setup Instructions

1. **Install dependencies:**
   - Python 3.11 required
   - `pip install -r requirements.txt`

2. **Configure environment variables:**
   - Copy `.env.template` to `.env` and fill in your credentials, or set the following variables directly in your shell or CI/CD system:
     - `LOGIN_URL`: Login endpoint (e.g., https://your-app.example.com/api/login)
     - `LOGIN_EMAIL`: Valid user email
     - `LOGIN_PASSWORD`: Valid user password

3. **Test execution:**
   - From the repo root:
     - `pytest Tests/login_test.py --tb=short --junitxml=login_test_results.xml`

---

## Git Integration Workflow

- Repo is managed via git on GitHub (`lakshmi1212/AgenticAI`, branch: `main`).
- Files are added/updated using automated tools for traceability.
- Typical workflow:
  1. `git add Tests/login_test.py Tests/.env.template Tests/README.md requirements.txt login_test.metadata.json`
  2. `git commit -m "Add/Update login automation test suite"`
  3. `git push origin main`

---

## Test Results & Reporting

- JUnit XML report: `login_test_results.xml` (for CI integration)
- View results in HTML with plugins like `pytest-html` (optional)

---

## Troubleshooting Guide

- **Network errors:**
  - Check your LOGIN_URL is reachable
  - Inspect logs for timeout or DNS errors
- **Authentication failures:**
  - Verify credentials are correct and not expired
  - Check if 2FA or Captcha is required (not supported in this script)
- **Git errors:**
  - Ensure you have correct permissions for the repo and branch
  - Check your git remote and branch configuration
- **Other issues:**
  - Use `pytest -s` for verbose logs
  - Review error messages in `login_test.py`

---

## Maintenance & Extension

- Update dependencies in `requirements.txt` as needed
- Add new test cases by extending the `@pytest.mark.parametrize` list
- For new authentication flows (2FA, SSO), modularize test logic
- Keep `.env` files out of git (`.gitignore`)

---

## Recommendations & Future Improvements

- Integrate with GitHub Actions/CI for automated pipeline runs
- Support for multi-user/role-based login validation
- Add advanced reporting (HTML, Slack, email notifications)
- Modularize for additional authentication mechanisms

---

## Support & Escalation

- Review this README and code comments first
- For advanced support, escalate to DevOps/QA lead or open a GitHub issue
- Community resources: [pytest docs](https://docs.pytest.org/), [requests docs](https://requests.readthedocs.io/en/latest/)
