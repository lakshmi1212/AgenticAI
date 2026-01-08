# Math Operations Module

This repository provides basic math operations (addition, subtraction) and automated tests using pytest.

## Usage

```
from src.math_operations import add, subtract

result_add = add(2, 3)
result_subtract = subtract(5, 2)
print(f"Addition: {result_add}, Subtraction: {result_subtract}")
```

## Running Tests

Install dependencies:

```
pip install -r default/requirements.txt
```

Run all tests:

```
python -m pytest tests/ -v --tb=short
```

## CI/CD Workflow

The CI workflow is defined in `.github/workflows/ci.yml` and runs tests on push and pull request events to the main branch.
