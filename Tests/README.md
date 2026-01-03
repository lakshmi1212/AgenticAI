# Login Automation Test Suite

## Overview
Automated login validation using Python, pytest, and requests. Credentials and endpoint are securely loaded via environment variables. Designed for DevOps pipelines and git integration.

## Setup Instructions
1. **Python 3.11** is required.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Copy `.env.template` to `.env` and fill in your actual values:
    ```bash
    cp Tests/.env.template Tests/.env
    # Edit Tests/.env with your credentials
    ```
4. Export environment variables (for local run):
    ```bash
    export $(cat Tests/.env | xargs)
    ```

## Running Tests
```bash
pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
```

## Test Results
- JUnit XML report is generated at `Tests/login_test_results.xml`.

## Troubleshooting
- **Network errors**: Ensure LOGIN_URL is reachable.
- **Authentication failures**: Double-check credentials in your `.env` file.
- **Missing environment variables**: Ensure all required variables are set.
- **Git errors**: Verify your git remote and permissions.

## Maintenance & Extensibility
- Update credentials in `.env` as needed.
- Extend `login_test.py` for additional authentication scenarios.

## Recommendations
- Integrate with CI/CD pipelines (see `.github/workflows/ci.yml`).
- Modularize for multi-user and advanced reporting.
- Regularly update dependencies in `requirements.txt`.

## Support & Escalation
- Review logs and test reports for diagnostics.
- For advanced support, escalate to QA automation lead.
