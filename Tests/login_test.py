#!/usr/bin/env python3
"""
pytest-based login automation script using requests.
Credentials and login URL are loaded from environment variables for security.

Required env vars:
  - LOGIN_URL
  - LOGIN_EMAIL
  - LOGIN_PASSWORD

Usage:
  pytest Tests/login_test.py --junitxml=Tests/login_test_results.xml
"""
import os
import pytest
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO