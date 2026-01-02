# Login Automation Tests

Automated login validation using Python, pytest, and requests.

## Setup Instructions

1. **Python Installation:**
   - Requires Python 3.11
   - Install dependencies: `pip install -r requirements.txt`

2. **Environment Configuration:**
   - Copy `Tests/.env.template` to `.env` and fill in your credentials.
   - Export environment variables or use a tool like `python-dotenv`.

   ```bash
   export LOGIN_URL=https://your-login-endpoint.com/api/login
   export LOGIN_EMAIL=your-email@example.com
   export LOGIN_PASSWORD=your-password
   ```

## Running the Test

```bash
pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
```

## Troubleshooting Guide

- **Network Errors:** Check LOGIN_URL and network connectivity.
- **Authentication Failures:** Verify LOGIN_EMAIL and LOGIN_PASSWORD.
- **Environment Variables Not Set:** Ensure variables are exported or set in your CI/CD pipeline.
- **Git Errors:** Confirm repository permissions and PAT validity.

## Maintenance Procedures

- Update dependencies in `requirements.txt` as needed.
- Extend `login_test.py` for more test cases (2FA, negative tests).
- NEVER commit actual secrets to git.

## Recommendations for Future Improvements

- Integrate with CI/CD for automated test runs.
- Add multi-user and negative test cases.
- Enhance reporting (HTML, Slack notifications).

## Support Resources

- [pytest Documentation](https://docs.pytest.org/en/stable/)
- [requests Documentation](https://docs.python-requests.org/en/latest/)
- GitHub Issues in this repository.

## Escalation Procedures

- If you encounter persistent issues, escalate to DevOps/Security team with logs and error details.
