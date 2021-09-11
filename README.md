# rachleff-list

Quickly see what years a company is on the list. Useful for diligence on later-stage private companies.

## About the list

- US-based, privately held, have a revenue run rate by year end of between $20 million and $300 million, be on a trajectory to grow at a rate in excess of 50% for at least the next three or four years, and have compelling unit economics

- Survey of _Accel Partners, Addition, Andreessen Horowitz, Benchmark, Bond, Coatue, Dragoneer, Greylock Partners, Index Ventures, IVP, Kleiner Perkins Caufield & Byers, Matrix Partners, Redpoint, Ribbit Capital, Social Capital, Spark Capital, TCV, Tiger Global, Unusual Ventures_
- [More](https://blog.wealthfront.com/announcing-2021-career-launching-companies/)

# Usage

## Check for a company

This company is in the list

```sh
% ./src/rachleff check hackerone
Hackerone found in years ['2020', '2019']
% ./src/rachleff check flexport
Flexport not found
```

This company is not in the list

```sh
% py src/main.py check apple
Apple not found
```

## Known problems

Most recent (2021) is not a pdf; store in repo as txt, or recreate with copy/past -> '2021.txt'

# Test

`PYTHONPATH=src pytest tests`

or use debug if VS Code.

# Dev

# Install

## Running locally with alias

Prereqs:
pydantic

Set shell alias to path such as

```sh
alias rachleff-list='/{path_to_dir}/rachleff-list/src/main.py'
```

Give permissions to execute the file. For example:

```sh
% chmod a+x /{path_to_dir}/rachleff-list/src/main.py
```

## Development

```sh
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

Can check typing with:

```sh
mypy src
```

# Data notes

Dropped

- 2021
  - Too big
    - 23andme
    - Chime
    - Databricks
    - goPuff
    - Instacart
    - Marqueta
    - Payoneer
    - Samsara
    - Warby Parker
  - IPO
    - Asana
    - Affirm
    - Snowflake
    - Wish
