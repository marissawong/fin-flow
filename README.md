# Fin Flow API

## Running locally
### Configuring
1. Create a new file called `.env.local`
2. Request the `DATABASE_URL` value

### Executing
#### MacOS
1. Inside folder `api`, run `pyenv exec python -m venv .venv`
2. A new folder `.venv` will be created
3. Run `source ./.venv/bin/activate` to activate your virtual environment
4. Run `pip install -r requirements.txt` to install required packages
5. Run `uvicorn app.main:app --reload` to start the API locally

#### Windows
1. Inside folder `api`, run `python -m venv .venv`
2. A new folder `.venv` will be created
3. Run `.venv/Scripts/activate` to activate your virtual environment
4. Run `pip install -r requirements.txt` to install required packages
5. Run `uvicorn app.main:app --reload` to start the API locally

## Structure
This project was developed and organized following the concepts of Domain-Driven Design (DDD).

### domain
- `/entities`: business objects
- `/repositories`: interfaces
- `/services`: domain logic involving multiple entities

### infrastructure
- `/repositories`: handles database transactions using [SQLAlchemy](https://www.sqlalchemy.org)

### application
- `/dto`: defines data transfer objects
- `/use_cases`: business logic that interacts with `repositories` and `services` for a single entity

### presentation
- `/api`: defines FastAPI routes (endpoints)