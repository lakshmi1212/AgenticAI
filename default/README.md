# Login Automation with Pytest & Requests

## Overview
Automated login validation using Python, pytest, and requests, integrated with DevOps best practices and git workflows.

## Features
- Secure credential handling via environment variables
- Robust error handling and logging
- Easy integration with CI/CD pipelines
- Test reporting (JUnit XML, etc.)

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI
   ```
2. **Install Python 3.11 and dependencies:**
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Configure Environment Variables:**
   - Copy `.env.template` to `.env` and fill in your credentials:
     ```
     cp .env.template .env
     # Edit .env with your LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
     ```
   - Export variables (if using shell):
     ```bash
     export $(cat .env | xargs)
     ```

## Usage
Run the login test:
```bash
pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
```

## CI/CD Integration
- The workflow file `.github/workflows/ci.yml` (to be added) will automate test execution on push, PR, and manual dispatch.

## Maintenance
- Update dependencies in `requirements.txt` as needed
- Extend `Tests/login_test.py` for more test cases
- NEVER commit real credentials; use `.env.template` for sharing config

## Troubleshooting
- Ensure all environment variables are set
- Check network connectivity to LOGIN_URL
- Review error output for details

## Security
- No credentials are hardcoded
- Environment variables are required for secrets
- Compliant with QA and DevOps security best practices

## File Structure
- `Tests/login_test.py`: Main login test
- `.env.template`: Example credentials file
- `requirements.txt`: Python dependencies
- `README.md`: Documentation
- `.github/workflows/ci.yml`: CI workflow (pending)
- `login_test.metadata.json`: Metadata for automation and integration
