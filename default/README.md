# Login Automation Solution

## Overview
Automated Python login test using `pytest` and `requests` for robust authentication validation. Credentials are managed via environment variables for security. Full git integration, documentation, and metadata enable seamless DevOps pipeline integration.

## Repository Structure
```
.
├── Tests/
│   └── login_test.py
├── .env.template
├── README.md
├── requirements.txt
├── login_test.metadata.json
└── .github/
    └── workflows/
        └── ci.yml (to be added)
```

## Setup Instructions
1. **Clone Repository**
   ```bash
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI
   ```
2. **Install Python 3.11**
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure Environment Variables**
   - Copy `.env.template` to `.env`
   - Fill in `LOGIN_URL`, `LOGIN_EMAIL`, `LOGIN_PASSWORD`
   - Load variables (e.g., with `python-dotenv` or export manually):
     ```bash
     export $(grep -v '^#' .env | xargs)
     ```

## Usage
Run the login test:
```bash
pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
```

## CI/CD Integration
- GitHub Actions workflow file: `.github/workflows/ci.yml` (pending)
- Automated test execution on push/PR to `main` branch.

## Troubleshooting
- Ensure all required environment variables are set.
- Check network connectivity to the login endpoint.
- Review logs and JUnit XML report for errors.

## Maintenance
- Update credentials in `.env` (never commit secrets).
- Extend tests in `Tests/login_test.py` for additional scenarios.
- Update dependencies in `requirements.txt` as needed.

## Security
- No secrets are stored in code or git.
- Robust error handling and logging included.

## Contact
For issues, open a GitHub issue or contact the repository maintainer.
