# Login Automation Test Suite

## Overview
Automated login validation using Python 3.11, pytest, and requests. Credentials are securely handled via environment variables. Robust error handling, logging, and positive/negative test coverage included.

## Setup
1. **Install dependencies** (Python 3.11 required):
   ```sh
   pip install -r ../requirements.txt
   ```
2. **Configure environment variables:**
   - Copy `.env.template` to `.env` and fill in values (or export manually):
     - `LOGIN_URL` - Your login form endpoint URL
     - `LOGIN_EMAIL` - Your test user email
     - `LOGIN_PASSWORD` - Your test user password
   - Example:
     ```sh
     export LOGIN_URL=https://example.com/login
     export LOGIN_EMAIL=your@email.com
     export LOGIN_PASSWORD=yourpassword
     ```

## Usage
- Run all tests with JUnit report:
  ```sh
  pytest login_test.py --junitxml=report.xml
  ```
- Review logs for detailed errors and troubleshooting.
- Negative and positive test cases are included.

## Git Integration
- All test assets are versioned via git. To commit changes:
  ```sh
  git add login_test.py .env.template README.md
  git commit -m "Add robust login automation test suite"
  git push origin main
  ```

## Troubleshooting
- **Missing environment variables:** Ensure LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD are set.
- **Network/auth errors:** Check endpoint accessibility, credentials, and logs in pytest output.
- **Git errors:** Confirm remote access and branch.

## Maintenance
- Update test logic in `login_test.py` as needed.
- Add more tests for edge cases or new login flows.
- Rotate credentials regularly, never commit secrets.

## Recommendations
- Integrate with CI/CD for automated feedback.
- Extend for multi-user, 2FA, or advanced authentication scenarios.
- Use secrets management for production pipelines.

## Support
- For advanced issues, consult project maintainers or DevOps team.
