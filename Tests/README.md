# Login Automation Test Suite

## Overview
This project delivers a robust, secure, and maintainable login automation solution using Python, pytest, and requests. It is designed for seamless integration with modern DevOps pipelines, using environment variables for credential security and producing JUnit XML test reports for CI/CD systems.

## Features
- Automated login validation (positive/negative cases)
- Secure credential management (no hardcoded secrets)
- Parameterization via environment variables
- Logging and error handling
- JUnit XML report generation
- Git integration and DevOps readiness

## Setup Instructions
1. **Clone the repository**
   ```sh
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI/Tests
   ```
2. **Install dependencies**
   - Python 3.8+
   - [pytest](https://docs.pytest.org/en/stable/): `pip install pytest`
   - [requests](https://docs.python-requests.org/en/master/): `pip install requests`

3. **Configure credentials**
   - Copy `.env.template` to `.env` and fill in the actual values:
     ```sh
     cp .env.template .env
     # Edit .env and set LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD, INVALID_PASSWORD
     ```
   - Export variables to your environment:
     ```sh
     set -a
     source .env
     set +a
     ```

4. **Run the tests**
   ```sh
   pytest login_test.py --junitxml=login_test_results.xml
   ```
   - Test results are output to `login_test_results.xml` for CI/CD integration.

## Git Integration Workflow
- Initialize repo: `git init` (if not already initialized)
- Add files: `git add login_test.py .env.template README.md`
- Commit: `git commit -m 'Add login automation test suite'`
- Push: `git push origin main`

## Test Reporting
- JUnit XML reports are generated for integration with GitHub Actions or other CI/CD systems.

## Maintenance Procedures
- Update test cases by editing `login_test.py`.
- Update credentials in `.env` as needed (never commit real secrets).
- Add new test cases via `@pytest.mark.parametrize`.
- Review logs and reports for troubleshooting.

## Troubleshooting Guide
| Issue                      | Diagnostic Steps                                      |
|----------------------------|------------------------------------------------------|
| Network error              | Check URL, internet connection, proxy/firewall logs   |
| Authentication failure     | Verify credentials, check for account lockout         |
| Git push error             | Validate git remote, branch, permissions              |
| Missing env variables      | Check `.env` file, ensure variables are exported      |
| Unexpected test failures   | Review `login_test_results.xml` and logs              |

## Recommendations for Future Improvements
- Integrate with GitHub Actions for CI/CD automation
- Add support for 2FA, CSRF tokens if required
- Extend test suite for multi-user and advanced scenarios
- Modularize code for reuse and scalability
- Implement advanced reporting (HTML, Slack notifications)

## Support
- Refer to [pytest documentation](https://docs.pytest.org/en/stable/)
- For advanced support, escalate to QA or DevOps leads

---
**Security Note:** Never commit real credentials to the repository. Use environment variables or secure vaults in CI/CD.
