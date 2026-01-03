# Login Automation Solution for DevOps Pipelines

## Overview
Automated login validation using Python, pytest, and requests. Secure, maintainable, and ready for CI/CD integration.

## Features
- Secure credential handling via environment variables
- Robust error handling and logging
- Pytest-based test automation
- Ready for GitHub Actions CI

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI
   ```
2. **Install Python 3.11 and pip.**
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables:**
   - Copy `.env.template` to `.env` and fill in your credentials.
   - Export variables or use a tool like `python-dotenv` (not required for this script).

## Running Tests
```bash
pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
```

## Configuration
- Required environment variables:
  - `LOGIN_URL`: Login endpoint URL
  - `LOGIN_EMAIL`: Login email
  - `LOGIN_PASSWORD`: Login password

## Maintenance
- Update dependencies in `requirements.txt` as needed.
- Extend `Tests/login_test.py` for more test scenarios.
- NEVER commit secrets to version control.

## CI/CD Integration
- Ready for GitHub Actions workflow (`.github/workflows/ci.yml`).

## Troubleshooting
- Ensure all required environment variables are set.
- Review logs for network or authentication errors.

## License
MIT
