# Login Automation Test Suite

## Overview
This project provides a secure, maintainable Python pytest script for automated login validation. Credentials and endpoint are managed via environment variables for security. Includes positive and negative test cases, robust error handling, logging, and automated integration with git.

## Setup Instructions
1. **Python Installation**
   - Requires Python 3.8 or newer (tested on 3.10).
2. **Install Dependencies**
   ```bash
   pip install pytest requests
   ```
3. **Configuration**
   - Copy `.env.template` to `.env` and fill in your credentials.
   - Export environment variables manually, or use a tool like `python-dotenv` (optional).
   ```bash
   export LOGIN_URL=https://your-app.example.com/api/login
   export LOGIN_EMAIL=youruser@example.com
   export LOGIN_PASSWORD=yourpassword
   ```

## Running Tests
```bash
pytest login_test.py --maxfail=1 --disable-warnings --junitxml=results.xml
```
- Test report will be saved as `results.xml` for CI integration.

## Git Integration
- Repository: [lakshmi1212/AgenticAI](https://github.com/lakshmi1212/AgenticAI)
- Branch: `main`
- Folder: `Tests1`
- To update:
  ```bash
  git pull
  git add Tests1/login_test.py Tests1/README.md Tests1/.env.template
  git commit -m "Update login automation test suite"
  git push origin main
  ```

## Troubleshooting Guide
- **Network errors**: Check connectivity, endpoint URL, proxy/firewall settings.
- **Authentication failures**: Verify credentials, ensure correct environment variable values.
- **Git errors**: Check remote URL and permissions.
- **Timeouts**: Adjust timeout in script if needed.

## Maintenance Procedures
- Update dependencies with `pip install --upgrade pytest requests`.
- Rotate credentials regularly; update `.env` and environment variables.
- Extend tests by adding more test cases or refactoring for modularity.
- For CI/CD integration, use GitHub Actions for automated test execution on push.

## Future Enhancements
- Add support for multi-user login scenarios.
- Integrate with advanced reporting (HTML, Allure).
- Expand to cover 2FA, CSRF tokens, or OAuth workflows.
- Modularize for scalability and easier maintenance.

## Support & Resources
- [Pytest Documentation](https://docs.pytest.org/en/latest/)
- [Requests Documentation](https://docs.python-requests.org/en/latest/)
- [GitHub Actions Guide](https://docs.github.com/en/actions)

---
**Security Note**: Do NOT commit `.env` with real secrets. Always use `.env.template` for sharing configuration structure.
