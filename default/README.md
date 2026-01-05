# Login Automation Solution

## Project Overview
Automated Python pytest script for login validation, leveraging secure environment variable management and full git integration for DevOps pipelines.

## Key Features
- Secure credential handling via environment variables
- Robust error handling and test reporting
- Ready for CI/CD integration
- Comprehensive documentation and metadata

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI
   ```
2. **Install Python 3.11**
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables:**
   - Copy `.env.template` to `.env` and fill in your LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD.
   - Export variables or use dotenv loader as preferred.

## Configuration Steps
- Edit `.env.template` and provide the actual login endpoint, email, and password.
- Ensure environment variables are loaded before running tests.

## Usage Guidelines
- Run tests with:
  ```bash
  pytest Tests/login_test.py
  ```
- Review test output for pass/fail status and error details.

## Maintenance Procedures
- Update dependencies in `requirements.txt` as needed.
- Extend `Tests/login_test.py` for additional test cases.
- Maintain credential security—never commit real secrets.

## Quality Assurance
- Positive and negative test cases included.
- Network and authentication errors are handled gracefully.
- Code adheres to PEP8 and QA automation best practices.

## Deliverables
- `Tests/login_test.py` – Login test script
- `.env.template` – Environment variable template
- `requirements.txt` – Dependency list
- `README.md` – Documentation
- `login_test.metadata.json` – Metadata for pipeline integration

## Support
For issues or enhancements, open a GitHub issue or pull request.