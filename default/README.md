# Login Automation QA Solution

## Overview
Automated login validation using Python, pytest, and requests. Credentials and endpoint are securely managed via environment variables for robust, maintainable, and secure DevOps integration.

## Folder Structure
- Tests/login_test.py         # Main pytest script for login validation
- .env.template              # Example environment config (do NOT commit secrets)
- requirements.txt           # Python dependencies
- README.md                  # Documentation and setup guide
- .github/workflows/ci.yml   # CI pipeline (to be generated)
- login_test.metadata.json   # Metadata for automation and integration

## Setup Instructions
1. **Python Installation**: Requires Python 3.11
2. **Clone the repository**:
   ```bash
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI
   ```
3. **Create and configure your .env file**:
   ```bash
   cp .env.template .env
   # Edit .env and fill in LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the test**:
   ```bash
   pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
   ```

## Configuration Steps
- All credentials are parameterized via environment variables. Never commit real secrets.
- See `.env.template` for required variables.

## Usage Guidelines
- Run tests locally or integrate with CI/CD pipeline.
- Inspect results in `Tests/login_test_results.xml` or pytest output.
- Troubleshoot by verifying environment variables and endpoint accessibility.

## Maintenance Procedures
- Update `Tests/login_test.py` to extend for new scenarios (e.g., 2FA, CSRF).
- Update `requirements.txt` as dependencies change.
- Regenerate `.env.template` if new secrets are required.

## Quality Assurance
- Code adheres to PEP8 and QA automation best practices.
- Credentials are never hardcoded.
- All network and authentication errors are robustly handled.

## Extensibility
- Easily add new test cases using pytest parameterization.
- Modular structure for future enhancements and scalability.
