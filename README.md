Folder Structure
project-root/
 ├─ run/
 │   ├─ docker-compose.yml
 │   └─ (other service files)
 ├─ src/
 
Make sure the docker-compose.yml file is inside the run folder.

How to Run the Project

Follow these steps to start the application using Docker:

1️ Open Command Prompt (CMD) and navigate to the run folder

2️ Build and start all containers
docker-compose up --build

This command will:

Build all Docker images


3️ Open the application in the browser

Once the container startup completes successfully, open your browser and visit the local URL shown in the terminal.

Typically:

http://localhost:3000

then it will lead to app
