# rachleff-list

Quickly see what years a company is on the list. Useful for diligence on later-stage private companies.

[About the list](https://blog.wealthfront.com/career-launching-companies-list/)

# Usage

## Check for a company

This company is in the list

```sh
(.venv)  % py src/main.py company-in-year hackerone --test
Hackerone found in years ['2019']
```

This company is not in the list

```sh
(.venv) % py src/main.py company-in-year apple --test
Apple not found
```

## Known problems

Most recent (2021) is not a pdf; store in repo as txt, or recreate with copy/past -> '2021.txt'

# Test

`PYTHONPATH=src pytest tests`

or use debug if VS Code.

# Dev

`mypy src`

# Install

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

# Reference

- [pytest docs](https://docs.pytest.org/en/6.2.x/example/index.html)
- [TDD with Python, 2E](https://learning.oreilly.com/library/view/test-driven-development-with/9781491958698/part01.html#part1)
- [Click docs](https://click.palletsprojects.com/en/8.0.x/#documentation)
