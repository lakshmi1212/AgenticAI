# Login Automation Solution

## Overview
Automated login validation using Python, pytest, and requests. Secure credential management via environment variables. Ready for DevOps pipelines and CI/CD integration.

## Features
- Secure credential handling (.env.template)
- Positive and negative login test cases
- Robust error handling and reporting
- Git integration and metadata

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI
   ```
2. **Install Python 3.11**
3. **Create and activate a virtual environment:**
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Configure environment variables:**
   - Copy `.env.template` to `.env` and fill in your credentials.
   - Export variables or use a tool like `python-dotenv`.

## Configuration Steps
- Set `LOGIN_URL`, `LOGIN_EMAIL`, and `LOGIN_PASSWORD` in your environment or `.env` file.

## Usage Guidelines
- Run tests:
  ```bash
  pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
  ```
- Review results in the output XML file.

## Maintenance Procedures
- Update credentials in `.env.template` as needed.
- Extend `Tests/login_test.py` for additional scenarios.
- Update dependencies in `requirements.txt`.

## Security Notice
- Do **not** commit real credentials.
- Use environment variables for all secrets.

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

## CI/CD Integration
- Workflow file: `.github/workflows/ci.yml` (to be generated)
- On push, pull request, or manual dispatch, tests are executed automatically.

## Contact
For issues or contributions, open a GitHub issue or pull request.
