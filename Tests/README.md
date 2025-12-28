# Login Automation Test Suite

## Overview
This project provides a secure, maintainable Python pytest script for login validation. Credentials and login URL are managed via environment variables. Test results can be exported as JUnit XML for CI/CD integration.

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI/Tests
   ```
2. **Install dependencies**:
   - Python 3.8+
   - Install required packages:
     ```
     pip install pytest requests
     ```

3. **Set environment variables**:
   - On Linux/macOS:
     ```
     export LOGIN_URL=https://your-app.com/login
     export LOGIN_EMAIL=your-email@example.com
     export LOGIN_PASSWORD=your-password
     ```
   - On Windows (cmd):
     ```
     set LOGIN_URL=https://your-app.com/login
     set LOGIN_EMAIL=your-email@example.com
     set LOGIN_PASSWORD=your-password
     ```

## Running Tests
- Run all login tests and generate JUnit XML report:
  ```
  pytest --junitxml=report.xml login_test.py
  ```
- To run with HTML report (requires pytest-html):
  ```
  pip install pytest-html
  pytest --html=report.html login_test.py
  ```

## Git Integration Workflow
- Initialize git repo (if not already):
  ```
  git init
  git add login_test.py README.md
  git commit -m "Add login automation test suite"
  git branch -M main
  git remote add origin https://github.com/lakshmi1212/AgenticAI.git
  git push -u origin main
  ```

## Troubleshooting
- **Network errors**: Check your internet connection and LOGIN_URL value.
- **Authentication failures**: Ensure LOGIN_EMAIL and LOGIN_PASSWORD are correct.
- **Missing environment variables**: Confirm all required variables are set.
- **Git push errors**: Check your access permissions and branch name.

## Maintenance
- Update dependencies regularly.
- Rotate credentials as per your security policy.
- Extend tests by adding more cases to `login_test.py`.

## Recommendations & Future Improvements
- Integrate with CI/CD (e.g., GitHub Actions, Jenkins).
- Add support for 2FA, CSRF tokens, or token-based authentication if required.
- Modularize for additional test cases and multi-user scenarios.
- Implement advanced reporting and notifications.

## Support
- For issues, refer to this README or open an issue in the repository.
- Community resources: [pytest docs](https://docs.pytest.org/), [requests docs](https://docs.python-requests.org/)
