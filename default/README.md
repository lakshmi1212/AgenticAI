# Login Automation Solution

## Project Overview
Automated Python pytest script for login validation and git integration. This solution ensures robust, secure, and maintainable login test automation ready for DevOps pipelines.

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI
   ```
2. **Install Python 3.11 and dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure environment variables:**
   - Copy `.env.template` to `.env` and fill in your values for `LOGIN_URL`, `LOGIN_EMAIL`, and `LOGIN_PASSWORD`.
   - Export variables manually or use a tool like `python-dotenv`.

## Configuration Steps
- Store credentials securely using environment variables.
- Never commit secrets to the repository.
- Update `.env.template` for new variables as needed.

## Usage Guidelines
- Run the login test:
  ```bash
  pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
  ```
- Results are saved as JUnit XML for CI/CD integration.
- Interpret results based on pytest output and XML report.

## Maintenance Procedures
- Update scripts in `Tests/` for new login scenarios or API changes.
- Update dependencies in `requirements.txt` as needed.
- Regenerate `.env.template` when adding new config options.

## File Structure
- `Tests/login_test.py` – Main login automation test
- `.env.template` – Environment variable template
- `README.md` – Project documentation
- `requirements.txt` – Python dependencies
- `.github/workflows/ci.yml` – CI pipeline (to be generated)
- `login_test.metadata.json` – Metadata for automation and integration

## Quality Assurance
- Code is PEP8 compliant
- Credentials are not hardcoded
- Error handling and logging implemented
- Test covers positive login scenario

## Extending Automation
- Add more test functions to `Tests/login_test.py` for negative and edge cases
- Modularize code for reusability
- Integrate with CI/CD via GitHub Actions
