# What I achieved
- create an endpoint to migrate the data from csv file
- create an endpoint to redeem the data
- the referral code can only be used once
- the referral code expires after 48hrs
- user is awarded points
- writing tests

# What I could have done better
- better error handling
- link the refereed user with a specific referral code
- full test coverage

# Requirements
- python 3
- pipenv
- Postgres

# SetUp the app locally
- git clone `https://github.com/Georgeygigz/backend-test`
- `cd backend-test`
- `pipenv shell` to create and activate virtual environment
- `pipenv install --skip-lock` to install dependencies and skip pipenv lock
- `touch .env` to create a .env file
- `cp .env_sample .env` to copy the environment variables from .env_sample to .env
- create a postgres db and replace the database details in .env file with your database details
- `source .env` to source the environment variables
- `flask db upgrade` to run migrations
- `python run.py` to start server

# Endpoints
 - `http://127.0.0.1:5000/api/v1/users/migrate` migrate the data. Users details will be migrated
 - `http://127.0.0.1:5000/api/v1/users/redeem/<referral_code>` migrate the data. Users details will be migrated

 # Run Test
 - `pytest`