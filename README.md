# URL-shortener
This is a URL shortener web application. To run the project, do thos instructions:
- make a git repository and clone the project into `URL-shortener` directory:
  ```
  git init
  git clone https://github.com/JavadZahedi/URL-shortener
  ```
- open `URL-shortener` directory
  `cd URL-shortener`
- install `virtualenv` on your system if you haven't install it.
  `sudo apt-get install virtualenv`
- make a virtual environment
  `virtualenv <virtual_environment_name>`
- activate the virtual environment
  `source <virtual_environment_name>/bin/activate`
  you can deactivate it by running `deactivate` on the command line
- install pip3 on your system or virtual environment
  `sudo apt-get install pip3`
- install required libraries and packages on your virtual environment
  `pip3 install -r requirements.txt`
- open `myproject` directory
  `cd myproject`
- run `./manage.py runserver` on command line to run the server.
- now, the server has been ran on 8000 port of the localhost.
