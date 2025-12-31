# Login Automation Test Suite

This suite provides robust, secure, and maintainable login automation for modern QA and DevOps pipelines using Python, pytest, and requests.

## 🚀 Features
- Secure credential management (via environment variables)
- Positive and negative login validation
- Logging and robust error handling
- JUnit XML reporting for CI/CD
- Full git integration and maintainable codebase

---

## 1. Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package installer)
- pytest
- requests

### Install Dependencies
```sh
pip install pytest requests
```

### Environment Variables
Copy `.env.template` to `.env`, fill in your credentials, and export them:

```sh
cp .env.template .env
# Edit .env and set LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
export $(grep -v '^#' .env | xargs)
```

---

## 2. Running Tests

To execute the test suite and generate a JUnit XML report:

```sh
pytest Tests/login_test.py --junitxml=report.xml
```

### Test Cases
- **Positive:** Valid email/password should login successfully.
- **Negative:** Invalid credentials should result in HTTP 401 and error message.

---

## 3. Git Integration Workflow

The repo follows best practices for code and test asset management:

```sh
git init
git add Tests/login_test.py Tests/README.md Tests/.env.template
git commit -m "Add login automation test suite"
git push origin main
```

---

## 4. Troubleshooting Guide

| Issue | Solution |
|-------|----------|
| `Missing credentials or URL.` | Ensure LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD are exported in your shell |
| Network errors | Check connectivity, proxy, and VPN settings |
| Authentication failures | Verify credentials are correct |
| Git push errors | Ensure you have the correct repo access and branch |

- Review `report.xml` and pytest logs for detailed error information.
- Use `logging.INFO` output for diagnosis.

---

## 5. Maintenance & Extensibility
- Update test cases in `login_test.py` as needed
- Add more tests for edge cases, 2FA, CSRF, etc.
- Update dependencies regularly
- Rotate credentials securely

---

## 6. CI/CD Integration
- Integrate with GitHub Actions or your preferred CI tool
- Use JUnit XML report for test result publication

---

## 7. Security Best Practices
- Never commit real credentials
- Use environment variables or secure vaults for secrets
- Review code for PEP8 and QA standards compliance

---

## 8. Support & Escalation
- For issues, review logs and this README
- For advanced support, escalate to QA/DevOps lead
- Community resources: [pytest docs](https://docs.pytest.org/), [requests docs](https://docs.python-requests.org/)

---

## 9. Future Recommendations
- Add CI/CD pipeline for automated test execution
- Expand test coverage (multi-user, advanced auth)
- Add HTML reporting, Slack/email notifications
- Modularize tests for scalability
- Schedule regular reviews and dependency updates

---

**Author:** Senior QA Automation Engineer & DevOps Integrator
