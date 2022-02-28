# MultiUserOpenRefine

![MultiUserOpenRefine](MUOR/static/images/logo.svg)

## Description
MultiUserOpenRefine is an extension to open-source tool that, in addition to all
the features described on [OpenRefine official website](https://openrefine.org/), allows creating user accounts, each providing
private workspace and leaving the convenience of running the basic OpenRefine
tool on a remote server.

Project is being developed at Adam Mickiewicz University in Poznań by students.

## Components
- Docker
- uWSGI
- NGINX
- Python with packages from requirements.txt

## How to run

1. Build docker image of OR (with privided script)
2. Set up NGINX with config from MUOR/configs/
3. Start uWSGI with .ini from MUOR/configs
4.  Set up server from MUOR folder



