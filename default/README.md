# Login Automation Solution

## Overview
This project provides a robust, secure, and maintainable Python pytest script for validating login functionality via API. It uses environment variables for credential management and is fully integrated with DevOps best practices and Git version control.

## Features
- Automated login validation using pytest and requests
- Secure credential handling via environment variables (.env.template)
- Robust error handling and logging
- Ready for CI/CD pipeline integration
- Comprehensive documentation and metadata

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI
   ```
2. **Create your environment file:**
   Copy `.env.template` to `.env` and fill in your credentials:
   ```bash
   cp .env.template .env
   # Edit .env and provide LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
   ```
3. **Install dependencies:**
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. **Run the tests:**
   ```bash
   pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
   ```

## Configuration
- All secrets and sensitive credentials must be provided via environment variables (see `.env.template`). Never commit real secrets to the repo.

## Maintenance
- Update scripts and dependencies as required.
- Extend `Tests/login_test.py` for additional test cases (e.g., negative tests, 2FA, CSRF).
- Review commit history and CI/CD results for quality assurance.

## Support
For issues or enhancements, please open a GitHub issue in this repository.
