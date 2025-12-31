# Login Automation Test Suite

This suite provides robust, secure, and maintainable automated login validation using Python, pytest, and requests. It is designed for DevOps/CI integration and secure credential management.

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI
   ```
2. **Python Setup:**
   - Requires **Python 3.11**.
   - Install dependencies:
     ```sh
     pip install -r requirements.txt
     ```
3. **Environment Variables:**
   - Copy `.env.template` to `.env` and fill in your actual credentials.
   - Export environment variables (or use a tool like `python-dotenv`):
     ```sh
     export $(cat Tests/.env | xargs)
     ```
   - Required variables:
     - `LOGIN_URL` (e.g., https://your-app.example.com/api/login)
     - `LOGIN_EMAIL` (your valid email)
     - `LOGIN_PASSWORD` (your valid password)

## Running Tests

```sh
pytest Tests/login_test.py --junitxml=results.xml
```

- Results are shown in terminal and saved as JUnit XML for CI integration.

## Git Integration

- The test suite is versioned in git and ready for CI/CD pipelines (see `.github/workflows/ci.yml`).
- To commit changes:
  ```sh
  git add Tests/login_test.py Tests/.env.template Tests/README.md requirements.txt .github/workflows/ci.yml login_test.metadata.json
  git commit -m "Add robust login automation test suite"
  git push origin main
  ```

## Troubleshooting

- **Missing credentials:** Ensure all required environment variables are set.
- **Network errors:** Check connectivity and login URL.
- **Authentication failures:** Validate credentials, check for 2FA/CSRF requirements.
- **Git errors:** Check remote URL, branch, and permissions.

## Security

- Never commit real secrets or credentials.
- Use `.env` for local secrets only.
- All sensitive data is parameterized; no hardcoded credentials.

## Extending & Maintenance

- Add more test cases to `test_login` for additional scenarios.
- Update dependencies as needed in `requirements.txt`.
- For new features, create a new branch and pull request.

## CI/CD Recommendations

- Integrate with GitHub Actions (see `.github/workflows/ci.yml`) for automated testing on push/PR.
- Monitor test pass rates and code quality.

## Support

- For help, review logs and error messages, or consult your DevOps/QA team.

---

**Author:** Senior QA Automation & DevOps Integrator
