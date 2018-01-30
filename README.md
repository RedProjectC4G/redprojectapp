# redprojectapp
Red project flask app

Install (pipenv):
  - pip3 install pipenv
  - pipenv install
  - pipenv shell
  - FLASK_ENV=dev python3 manage.py run

Install (Docker)
  - Install docker
  - docker-compose build
  - docker-compose up

Add a azure remote to git: git remote add azure https://reddeploy@redprojectintakeapp.scm.azurewebsites.net/redProjectIntakeApp.git

## Docker Dev Environment
The command `docker-compose up` will create two containers:
1. web: runs the flask dev server
2. mongo-db: Runs the mongo instance

You can also run `docker-compose up -d` to daemonize the process and free up your terminal for other usage. But that means you'll have to run `docker-compose -logs` to view any output from the containers (which can be useful for debugging).

Once the containers are running, setup the inital admin with: `docker-compose exec web python manage.py init_db`
