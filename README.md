# flask_test_project

For initial seatup up, you will require connection strings for your database and broker in either the .env file or config.py
Then set up the venv with command: 
python3 -m venv venv 
source venv/bin/activate
install the requirement.txt : pip3 install -r requirement.txt
run the run.py with desired host along with celery worker command:
celery -A app.celery worker --loglevel=info

