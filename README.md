
<h1 align="center">Fampay Youtube API Task</h1>
<br>

This project is a simple backend application that is supposed to fetch YouTube videos with a predefined query and stores the results in the database (the database being PostgreSQL in this case).  


## Applicant Details :

#### Email : [akshatsharma2602@gmail.com](mailto:akshatsharma2602@gmail.com)
#### Linkedin : [https://www.linkedin.com/in/akshat-sharma-2602/](https://www.linkedin.com/in/akshat-sharma-2602/)
#### Github : [https://github.com/akshat2602](https://github.com/akshat2602)
#### Online Repo : [https://github.com/akshat2602/fampay-task](https://github.com/akshat2602/fampay-taskca)

## About the project :
-   PostgreSQL used as the primary database.
-   Superuser is already initialized with the credentials: Username- `admin`, Email- `admin@admin.com`, Password- `admin`
-   Integration with Django Rest Framework
-   API Documentation is configured using swagger.
-   Containerized using Docker and managed using docker-compose.
-   PEP-8 Coding guidelines followed.
-   Used Celery and Celery-beat for doing async API calls and scheduling tasks.

API endpoints have been developed to further display the data to the user:

### Endpoint URL - /list/video/
This endpoint will return a paginated response sorted in descending order of published date-time of the videos. We can sort the resposne in ascending order using a query param in the following format - 
`localhost:8000/list/video/?ordering=published_at`

### Endpoint URL - /search/video/
This endpoint will return a paginated response and can be used for searching on the title or the description of the video using query params in the following format.
`localhost:8000/search/video/?search=ate`


## Getting Started
To get a local copy of this template up and running on your machine, follow these simple steps.
### Prerequisites
- Docker
`curl -fsSL https://get.docker.com -o get-docker.sh`
`sudo sh get-docker.sh`

### Installation
- Clone the repo `git clone https://github.com/akshat2602/fampay-task.git`
- Change the current directory to the template `cd fampay-task`
- Build the docker containers`docker-compose -f docker-compose.dev.yml build` for the dev containers and `docker-compose -f docker-compose.prod.yml build` for the prod containers
- Run the docker containers`docker-compose -f docker-compose.dev.yml up` for the dev containers and `docker-compose -f docker-compose.prod.yml up` for the prod containers

## API Documentation
API documentation is done using swagger. Visit `http://localhost:8000/swagger` for API documentation.

## Technologies used
<a href="https://www.djangoproject.com/" target="_blank"><img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/> </a>
<a href="https://www.django-rest-framework.org/" target="_blank"> <img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray" /> </a>
<a href="https://www.docker.com/" target="_blank"><img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/> </a>
<a href="https://www.postgresql.org" target="_blank"> <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"/></a>
