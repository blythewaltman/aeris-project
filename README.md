# Aeris Project

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Endpoints](#endpoints)
6. [Docker Deployment](#docker-deployment)

## Introduction

Welcome to the Aeris Project, a Flask-based web application designed to analyze concentration time series data. This project utilizes the Flask web framework in Python and provides endpoints for computing statistical measures and visualizing concentration data.

## Requirements

- Python 3.x
- Flask
- Docker

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/blythewaltman/aeris-project.git
   cd aeris-project
   ```

## Usage

### **To run the app locally**

1. Create and start a virtual environment to use an isolated Python environment.

2. Install the dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Set an environment variable for FLASK_APP:

   - **Linux and macOS:**

     ```bash
     export set FLASK_APP=webapp
     ```

   - **Windows (PowerShell):**

     ```powershell
     $env:FLASK_APP=webapp
     ```

   - **Windows (Command Prompt):**
     ```bash
     set FLASK_APP=webapp
     ```

4. Change into the folder that contains the Flask app.
   ```bash
   cd my_app
   ```
5. Start the Flask server with
   ```bash
   python -m flask run
   ```

## Endpoints

You can visit the following endpoints in the application

- `/get-mean` returns the mean of the concentration.
- `/get-std-deviation` returns the standard deviation of the concentra8on
- `get-sum` returns the sum of the concetration
- `get-image` returns png visualization of the concentration

## Docker Deployment

The easiest way to build and run the container is to open the project is Visual Studio Code and use the `F5` shortcut or the Run Without Debuggin command in the main pannel. This will automatically build the Docker image and run the Docker container.
