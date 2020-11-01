# Historical Figures Repository
![CI/CD](https://github.com/jemutorres/historical-figures/workflows/CI/CD/badge.svg) 

Historical Figures Repository is an application to manage a repository of historical figures.

It has been coded in [Python3.8](https://www.python.org/downloads/release/python-380/), using the [FastAPI](https://fastapi.tiangolo.com/), [Pydantic](https://pydantic-docs.helpmanual.io/) and [Tortoise-ORM](https://github.com/tortoise/tortoise-orm) frameworks.

This application has been developed following the **Test Driven Development (TDD)** programming practice.

# Demo
A demo application is deployed in [Heroku](https://historical-figures-jemutorres.herokuapp.com/).

# Installation

Clone the repository. Use [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) to build and run the project.
```
docker-compose up -d --build
``` 

# Project Structure

    └── project             # Python project
        └── app
        │   ├── api         # API services
        │   ├── models      # ORM models
        │   ├── schemas     # API Schemas
        │   ├── scripts     # Application scripts
        │   └── tests       # Integration/Unit tests
        └── db              # Database service

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

# Interactive API docs
You could see [here](https://historical-figures-jemutorres.herokuapp.com/docs) the automatic interactive API documentation (provided by [Swagger UI](https://github.com/swagger-api/swagger-ui))

## Alternative API docs
Also, you could see [here](https://historical-figures-jemutorres.herokuapp.com/redoc) the alternative automatic documentation provided by [ReDoc](https://github.com/Rebilly/ReDoc)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)