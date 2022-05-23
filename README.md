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

## Administrator manual
1. Build docker image of OR (with provided script)
2. Set up NGINX with config from MUOR/configs/
3. Start uWSGI with .ini from MUOR/configs
4. Set up server from MUOR folder

## User manual
To use the application, go into the [MultiUserOpenRefine official website](https://randomsec.projektstudencki.pl).
### Creating an account
1. On application home screen there is an option to log in or to create an account. Click on the _Create an account_ button
to move to the next screen.
![Home screen](MUOR/static/images/user-manual/Zrzut%20ekranu%202022-05-23%20o%2014.50.29.png)
2. Fill in the username and password, as well as email. The password can't be related to user personal information and has
to contain alphanumeric characters. Click the _Sign Up_ button to proceed.
![Registration screen](MUOR/static/images/user-manual/Zrzut%20ekranu%202022-05-23%20o%2014.51.25.png)
### Logging in
1. After successful registration, the user will be redirected to the login screen. Fill in username and password and
click the _Log in_ button to enter the application.
![Login screen](MUOR/static/images/user-manual/Zrzut%20ekranu%202022-05-23%20o%2014.51.43.png)
2. Wait a couple of seconds while the private user session is launched.
![Login screen](MUOR/static/images/user-manual/Zrzut%20ekranu%202022-05-23%20o%2014.51.58.png)
### Using the application
After being redirected to the **OpenRefine** home screen, the user can perform every action available in the original
application. All the instructions are described on [OpenRefine official website](https://openrefine.org/). To log out, 
click the _Logout_ button on top of the screen.
![Login screen](MUOR/static/images/user-manual/Zrzut%20ekranu%202022-05-23%20o%2014.52.10.png)