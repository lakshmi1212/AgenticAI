# Login Automation Test Suite

## Overview
Automated login validation using Python, pytest, and requests for secure and robust authentication testing. Credentials are securely managed via environment variables or a `.env` file.

## Setup Instructions
1. **Clone Repository**
   ```bash
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI/Laks
   ```
2. **Install Dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install pytest requests python-dotenv
   ```
3. **Configure Credentials**
   - Copy `.env.template` to `.env` and fill in your values:
     ```
     cp .env.template .env
     ```
   - Or export credentials as environment variables:
     ```bash
     export LOGIN_URL=https://your-app.example.com/login
     export LOGIN_EMAIL=your-email@example.com
     export LOGIN_PASSWORD=your-password
     ```

## Running the Tests
- Run all tests:
  ```bash
  pytest login_test.py --tb=short --junitxml=results.xml
  ```
- For HTML reports (optional):
  ```bash
  pip install pytest-html
  pytest login_test.py --html=report.html
  ```

## Git Integration
- All test assets are versioned in git. Standard workflow:
  ```bash
  git add login_test.py .env.template README.md
  git commit -m "Add login automation test suite"
  git push origin main
  ```

## Troubleshooting
- **Missing credentials**: Ensure all required environment variables are set or `.env` is properly configured.
- **Network errors**: Check connectivity and LOGIN_URL.
- **Authentication failures**: Verify credentials.
- **Git errors**: Confirm git remote and branch.
- See logs in test output for more details.

## Extending Tests
- Add more test cases to the `pytest.mark.parametrize` in `login_test.py`.
- Modularize for additional authentication scenarios (e.g., 2FA, CSRF).

## Maintenance
- Update dependencies with `pip install --upgrade -r requirements.txt` (if used).
- Review and rotate credentials regularly.
- Update scripts as authentication flow evolves.

## Support & Resources
- [Pytest Documentation](https://docs.pytest.org/)
- [Requests Library](https://docs.python-requests.org/)
- [GitHub Actions](https://docs.github.com/en/actions)

## Recommendations
- Integrate with CI/CD (e.g., GitHub Actions) for automated pipeline execution.
- Expand test suite for multi-user and advanced scenarios.
- Monitor test results and maintain audit logs.
