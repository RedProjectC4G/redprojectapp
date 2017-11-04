# redprojectapp
Red project flask app

Install:
  pip3 install -r requirements.txt
  brew install postgres
  docker run --name redpostgres -e POSTGRES_PASSWORD=admin -e POSTGRES_USER=admin -e POSTGRES_DATABASE=red_development -p5432:5432 -d postgres:9.6
Run local: FLASK_ENV=dev ./manage.py run

Add a azure remote to git: git remote add azure https://reddeploy@redprojectintakeapp.scm.azurewebsites.net/redProjectIntakeApp.git

## Docker Dev Environment
The command `docker-compose up` will create two containers:
1. Web: runs the flask dev server
2. DB: Runs the postgres instance

You can also run `docker-compose up -d` to daemonize the process and free up your terminal for other usage. But that means you'll have to run `docker-compose -logs` to view any output from the containers (which can be useful for debugging).

Once the containers are running, migratations can be run using the following command: `docker-compose exec web python manage.py db upgrade`
