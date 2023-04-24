#!/bin/bash

# Activate the virtual environment
source ${AIRFLOW_HOME}/venvs/airflow_venv/bin/activate

# Start PostgreSQL
sudo service postgresql start

# Start a new detached tmux session for the Airflow webserver
tmux new-session -d -s airflow_webserver "airflow webserver"

# Start a new detached tmux session for the Airflow scheduler
tmux new-session -d -s airflow_scheduler "airflow scheduler"

# Deactivate the virtual environment
deactivate
