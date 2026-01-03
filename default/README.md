# Login Automation Test Suite

This repository provides a robust, secure, and maintainable login automation solution using Python, pytest, and requests. It is fully integrated with DevOps practices, ready for CI/CD pipelines, and supports secure credential management via environment variables.

## Features
- Automated login validation with positive and negative test cases
- Secure credential handling using environment variables
- Pytest-based reporting and error handling
- Ready for GitHub Actions CI integration
- Modular and extensible for future test cases

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI
   ```
2. **Python Installation:**
   - Python 3.11 is required. Download from [python.org](https://www.python.org/downloads/release/python-3110/)
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables:**
   - Copy `.env.template` to `.env` and fill in your credentials:
     ```
     cp .env.template .env
     # Edit .env with your LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
     ```
   - Load environment variables (Linux/macOS):
     ```bash
     export $(grep -v '^#' .env | xargs)
     ```
   - On CI/CD, set secrets via your platform's secret management.

## Usage Guidelines
- **Run tests locally:**
  ```bash
  pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
  ```
- **Test Results:**
  - JUnit XML report generated at `Tests/login_test_results.xml`.
- **Troubleshooting:**
  - Ensure all environment variables are set and valid.
  - Check network connectivity to login endpoint.
  - Review error messages in pytest output.

## Maintenance Procedures
- Update dependencies in `requirements.txt` as needed.
- Extend test cases in `Tests/login_test.py` for additional scenarios.
- Manage credentials securely: never commit secrets to the repo.
- For CI/CD, update `.github/workflows/ci.yml` for pipeline changes.

## Repository Structure
```
AgenticAI/
├── Tests/
│   └── login_test.py
├── .env.template
├── README.md
├── requirements.txt
├── login_test.metadata.json
└── .github/
    └── workflows/
        └── ci.yml
```

## Security & Compliance
- No hardcoded secrets in code
- Credentials passed via environment variables
- Error handling for network and authentication issues
- Compliant with PEP8 and QA best practices

## Extending & Customization
- Add more tests to `Tests/login_test.py`
- Parameterize additional environment variables for other endpoints
- Integrate with more CI/CD platforms as needed

## Contact
For support or contributions, open an issue or pull request on GitHub.
