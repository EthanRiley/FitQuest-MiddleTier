# Flask Web App with SQL and Docker

This is a Flask web application that utilizes SQL as its backend database and Docker to manage and run all its containers. This README file will guide you through the setup and configuration process.

## Prerequisites

- Docker installed on your system
- Docker Compose installed on your system
- Python 3.x installed on your system

## Configuration

1. Clone the repository to your local machine:

git clone https://github.com/EthanRiley/FitQuest-MiddleTier


2. Navigate to the project folder:

cd flask-sql-docker

3. Build the Docker images:

docker-compose build

4. Create a `secrets` folder and add the password files:

mkdir secrets
echo 'your_password' > secrets/db_password.txt
echo 'your_root_password' > secrets/db_root_password.txt

Replace `your_password` and `your_root_password` with your desired passwords.

5. Update the `insert_script.py` file with the correct passwords:

- Open the `db/mock_data/insert_script.py` file in a text editor
- Replace the placeholder password on line 15 with the password you set in `db_password.txt` and `db_root_password.txt`
- Save and close the file

6. Install the mock data:

cd db/mock_data
python3 insert_script.py

7. Start the Docker containers:

docker-compose up

You can now access the AppSmith web application at `http://localhost:8080`.

## Stopping the Application

To stop the application, press `Ctrl+C` in the terminal where `docker-compose up` is running.

You can also stop the containers using the following command:

docker-compose down

