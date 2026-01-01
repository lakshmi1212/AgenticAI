# Login Automation Test Suite

## Overview
Automated login validation using Python, pytest, and requests. Credentials are securely managed via environment variables. Results are suitable for DevOps pipelines and CI/CD integration.

## Setup Instructions
1. **Python & Dependencies:**
   - Install Python 3.11
   - Install dependencies: `pip install -r ../requirements.txt`
2. **Environment Variables:**
   - Copy `Tests/.env.template` to `.env` and set your credentials.
   - Export environment variables or use a tool like `python-dotenv`.
3. **Test Execution:**
   - Run tests: `pytest Tests/login_test.py --maxfail=1 --disable-warnings --tb=short --junitxml=Tests/report.xml`

## Secure Credential Management
- Never commit `.env` files containing real secrets.
- Use CI/CD secret stores (GitHub Actions secrets) for pipeline execution.

## Git Integration Workflow
- Initialize repo: `git init`
- Add files: `git add Tests/login_test.py Tests/.env.template Tests/README.md requirements.txt login_test.metadata.json`
- Commit: `git commit -m "Add login automation test suite"`
- Push: `git push origin main`

## Troubleshooting Guide
- **Network errors:** Check endpoint, credentials, and connectivity.
- **Authentication failures:** Verify credentials and endpoint format.
- **Git errors:** Ensure correct remote URL and branch.

## Maintenance Procedures
- Update dependencies in `requirements.txt` as needed.
- Review credentials and rotate secrets regularly.
- Extend `login_test.py` for additional test cases.

## Recommendations for Future Improvements
- Integrate with CI/CD (GitHub Actions, Jenkins).
- Add support for 2FA, CSRF tokens, and negative testing.
- Modularize for multi-user and multi-endpoint scenarios.
- Generate HTML test reports for enhanced visibility.

## Support Resources
- Python Docs: https://docs.python.org/3/
- Pytest Docs: https://docs.pytest.org/en/stable/
- Requests Docs: https://requests.readthedocs.io/en/latest/

---
*Project delivered by Senior QA Automation & DevOps Integrator.*
