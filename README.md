# FundRegister
This project get a list of funds from fundcompare API and store it in a postgresql database. 
<br>
Then it get details of each fund from getfund API endpoint and
update the 3 required parameters for each fund. 
<br>
I have used celery for background processing and Django ORM for database connection.
<br>
We have three APIs
<br>
a. An API which gets registration number of a funds, fetch the fund info from database
and return it as a JSON object.
you can call this by this url:
http://127.0.0.1:8000/fund_by_regno/{reg_no}

b. An API which receives a string and searches for funds with similar name. The input string can be a substring of the fund name. 
you can call this by this url:
http://127.0.0.1:8000/fund_by_name/{name}

c. An API which saves all of the funds' information in a database. 
you can call this by this url:
http://127.0.0.1:8000/save_data

You can also see the documentation for this project which is wriiten with swagger by visiting this url:
http://127.0.0.1:8000/swagger-ui/

How to run this:
0. pip install requirements.txt
1. Run redis server by using this command:
redis-server
2. Running celery worker and see its output by this command:
celery -A FundRegister.celery worker -l info
3. Running the django project with this command:
python3 manage.py runserver

Note:
you can change the database of this project to sqlite just by commenting the existing DATABASES part of settings.py and uncomment the previous one.
If you choose to use postgresql database, remember to enter needed data in .env file which sould be in the same folder as settings.py.
The needed information:
SECRET_KEY=django_secret_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

