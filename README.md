# Airflow project setup using WSL

This is an easy guide for setting up PostgreSQL and Apache Airflow on WSL (Windows Subsystem for Linux) with a predefined Airflow project structure. This guide covers installing PostgreSQL, creating a new database and user for Airflow, setting up an Airflow folder, creating a virtual environment, installing the necessary Python packages, and starting Airflow.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Step 1: Install PostgreSQL](#step-1-install-postgresql)
- [Step 2: Create Airflow Database and User](#step-2-create-airflow-database-and-user)
- [Step 3: Set Up the Airflow Project](#step-3-set-up-the-airflow-project)
- [Step 4: Create a Python Virtual Environment](#step-4-create-a-python-virtual-environment)
- [Step 5: Install Apache Airflow](#step-5-install-apache-airflow)
- [Step 6: Set the Environment Variables](#step-6-set-the-environment-variables)
- [Step 7: Initialize and Start Airflow](#step-7-initialize-and-start-airflow)
- [Optional: Automatically start PostgreSQL, Airflow webserver, and Airflow scheduler with WSL](#optional-automatically-start-postgresql-airflow-webserver-and-airflow-scheduler-with-wsl)

## Prerequisites
1. WSL installed on your Windows machine. If you haven't installed it yet, follow the [official WSL installation guide](https://docs.microsoft.com/en-us/windows/wsl/install-win10).
2. A Linux distribution installed on WSL (e.g., Ubuntu). You can download it from the Microsoft Store.

## Step 1: Install PostgreSQL

Open a new WSL terminal, and run the following commands to install PostgreSQL:

```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib libpq-dev
```

## Step 2: Create Airflow Database and User

Start the PostgreSQL service and create a new user and database for Airflow:

```
sudo service postgresql start
sudo -u postgres psql
```

Then, execute the following SQL commands:

```
CREATE USER YOUR_USERNAME PASSWORD 'YOUR_PASSWORD';
CREATE DATABASE airflow;
GRANT ALL PRIVILEGES ON DATABASE airflow TO YOUR_USERNAME;
\q
```

*Note*: Replace SET_YOUR_USERNAME and SET_YOUR_PASSWORD with your own values.

*Optional*: To restrict the connections to PostgreSQL database only to the local machine, edit the /etc/postgresql/12/main/pg_hba.conf file:

```
sudo vim /etc/postgresql/12/main/pg_hba.conf
```

Locate the line that looks like this:

```
host    all             all             0.0.0.0/0               md5
```

Change to:

```
host    all             all             0.0.0.0/0               reject
```

## Step 3: Set Up the Airflow project

Git clone Airflow project repo:

```
git clone https://github.com/ddervosj/airflow_project && cd airflow_project
```

## Step 4: Create a Python Virtual Environment

Install python3-venv and create a virtual environment for Airflow:

```
sudo apt-get install python3-venv
mkdir venvs
python3 -m venv ~/airflow_project/venvs/airflow_venv
```

Activate the virtual environment:

```
source ~/airflow_project/venvs/airflow_venv/bin/activate
```

## Step 5: Install Apache Airflow

Upgrade pip and setuptools, then install Apache Airflow and its dependencies:

```
pip install --upgrade pip setuptools
pip install apache-airflow apache-airflow-providers-docker psycopg2-binary
```

## Step 6: Set the Environment Variables

Add the following lines to your .bashrc file to set proper directories and secrets:

```
export AIRFLOW_HOME=path/to/the/airflow_project
export POSTGRESQL_USER=username
export POSTGRESQL_PASSWORD=password
```

Reload the terminal configuration and activate the virtual environment:

```
source ~/.bashrc
source ~/airflow_project/venvs/airflow_venv/bin/activate
```

## Step 7: Initialize and Start Airflow

Initialize the Airflow database:

```
airflow db init
```

Create a new Airflow admin user:

```
airflow users create --username admin --password <your_password> --firstname <your_firstname> --lastname <your_lastname> --role Admin --email <your_email>
```

Start the Airflow webserver and scheduler in separate terminals:

Terminal 1

```
airflow webserver
```

Terminal 2

```
airflow scheduler
```

Now, Airflow should be up and running. Access the Airflow web UI at <http://localhost:8080>.

That's it! You're ready to start developing Airflow DAGs.

## [Optional]: Automatically start PostgreSQL, Airflow webserver, and Airflow scheduler with WSL

Install tmux

```
pip install tmux
```

Grant passwordless sudo privileges for running PostgreSQL start command by editing visudo

```
sudo visudo
```

Add the following line at the end of the file:

```
your_wsl_username ALL=(ALL) NOPASSWD: /usr/sbin/service postgresql start
```

Make startup.sh script executable:

```
chmod +x startup.sh
```

Add startup.sh to .bashrc to execute upon WSL start:

```
source ${AIRFLOW_HOME}/startup.sh
```

That's it. Now PostgreSQL and Airflow will start automatically every time you launch WSL.

## Attaching to tmux sessions

In case you want to attach to a specific tmux session, run:

```
tmux attach-session -t session_name
```

Example of attaching webserver:

```
tmux attach-session -t airflow_webserver 
```

Inspired by:

https://medium.com/abn-amro-developer/apache-airflow-tutorial-part-2-complete-guide-for-a-basic-production-installation-using-e0e6a7541d2a 

https://medium.com/abn-amro-developer/data-pipeline-orchestration-on-steroids-apache-airflow-tutorial-part-1-87361905db6d
