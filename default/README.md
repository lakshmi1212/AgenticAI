# Automated Login Validation with Python, pytest, requests

## Project Overview
Automated login validation using Python, pytest, and requests. Credentials are managed securely via environment variables. Full git integration and DevOps-ready.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI
   ```
2. Install Python 3.11 and dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.template` to `.env` and fill in your credentials:
   ```bash
   cp .env.template .env
   # Edit .env with your LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
   ```
4. Export environment variables (or use a tool like `python-dotenv`):
   ```bash
   export $(grep -v '^#' .env | xargs)
   ```

## Running Tests
```bash
pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
```

## Configuration Steps
- Store credentials in `.env` (never commit secrets).
- Use environment variables for CI/CD integration.

## Usage Guidelines
- Edit `.env` for different login endpoints and users.
- View test results in XML for integration with CI/CD.

## Maintenance Procedures
- Update `Tests/login_test.py` for new test cases.
- Update `.env.template` if environment variables change.
- Extend tests for additional scenarios (2FA, CSRF, etc).

## File Structure
- `Tests/login_test.py` - Main login automation script
- `.env.template` - Environment variable template
- `requirements.txt` - Python dependencies
- `README.md` - Documentation
- `login_test.metadata.json` - Metadata for DevOps integration
- `.github/workflows/ci.yml` - CI/CD workflow (to be generated)

## Security
- No hardcoded secrets; all credentials via environment variables.
- Secure error handling and logging.
