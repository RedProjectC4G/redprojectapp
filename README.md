# redprojectapp
Red project flask app

Install:
  pip3 install -r requirements.txt
  brew install postgres
  docker run --name redpostgres -e POSTGRES_PASSWORD=admin -e POSTGRES_USER=admin -e POSTGRES_DATABASE=red_development -p5432:5432 -d postgres:9.6
Run local: FLASK_ENV=dev ./manage.py run

Add a azure remote to git: git remote add azure https://reddeploy@redprojectintakeapp.scm.azurewebsites.net/redProjectIntakeApp.git
