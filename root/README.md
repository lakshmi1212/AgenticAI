# Login Automation QA Solution

Automated login validation using Python, pytest, and requests. Credentials are securely parameterized using environment variables.

## Setup Instructions

1. **Install Python 3.11**
2. **Clone the repository:**
   ```bash
   git clone https://github.com/lakshmi1212/AgenticAI.git
   cd AgenticAI
   ```
3. **Create and activate a virtual environment:**
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration Steps

1. Copy `.env.template` to `.env` and fill in your credentials:
   ```bash
   cp .env.template .env
   # Edit .env with your LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD
   ```
2. Export environment variables:
   ```bash
   export $(grep -v '^#' .env | xargs)
   ```

## Usage Guidelines

Run the automated login test:
```bash
pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
```

- Results will be output in JUnit XML format for CI integration.
- Logging is enabled for troubleshooting.

## Maintenance Procedures

- Update credentials in `.env` as needed.
- Extend `Tests/login_test.py` for additional test cases.
- Update dependencies in `requirements.txt` if required.

## CI/CD Integration

- This solution is ready for GitHub Actions integration via `.github/workflows/ci.yml`.

## Troubleshooting

- Ensure all environment variables are set before running tests.
- Check logs for details on failures.
- Validate your login endpoint and credentials.

## Security Notes

- Never commit actual credentials to version control.
- Use environment variables for secrets in CI/CD.

---

**Deliverables:**
- Python pytest script: `Tests/login_test.py`
- Configuration: `.env.template`
- Documentation: `README.md`
- Requirements: `requirements.txt`
- Metadata: `login_test.metadata.json`
- CI workflow: `.github/workflows/ci.yml`

For support, open an issue in this repository.
