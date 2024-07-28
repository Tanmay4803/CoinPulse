# Bitcoin-Alert-Application

 Introduction
This project is a Django-based web application designed to manage and send alerts. The solution includes endpoints for creating, reading, updating, and deleting alerts, and uses Docker for containerization.

Prerequisites
Docker
Docker Compose
Postman (for testing the API endpoints)
Steps to Run the Project
Clone the Repository

sh
Copy code
git clone <repository-url>
cd <repository-folder>
Navigate to the Project Directory

sh
Copy code
cd my_app
Remove Any Previous Database

sh
Copy code
docker compose down -v
Start the Database Container

sh
Copy code
docker compose up -d db
Build the Django Application

sh
Copy code
docker compose build djangoapp
Start the Django Application

sh
Copy code
docker compose up djangoapp
The server will be running on localhost at port 8000.

API Endpoints
Create an Alert
URL: localhost:8000/alerts/create/
Method: POST
Example Request Body:
json
Copy code
{
    "name": "tanmay saxena",
    "email": "tanmay4803@gmail.com",
    "current": "68000",
    "target": "67000"
}
Read All Alerts
URL: localhost:8000/alerts/readall/
Method: GET
Read a Specific Alert
URL: localhost:8000/alerts/read/<str:pk>
Method: GET
Update an Alert
URL: localhost:8000/alerts/update/<str:pk>
Method: PUT
Example Request Body:
json
Copy code
{
    "name": "updated name",
    "email": "updatedemail@gmail.com",
    "current": "69000",
    "target": "68000"
}
Delete an Alert
URL: localhost:8000/alerts/delete/<str:pk>
Method: DELETE
Database Configuration
The application uses PostgreSQL as its database. The configuration details are:

Host: localhost
Port: 5432
User: postgres
Password: postgres
Database: postgres
You can connect to the database using TablePlus or any other database client with the above details.

Running the Alert Trigger Script
There is a Python script located at management/commands/bitcoin.py that can be run to see the trigger alerts.

Steps to Run the Script
Open the terminal in VS Code.
Navigate to the project directory.
Run the following command:
sh
Copy code
python manage.py bitcoin
The output of the script execution can be observed in the VS Code terminal. A screenshot of the output is attached for reference.

Example Dataset
When you provide a dataset for creating an alert, its JSON format should be as follows:

json
Copy code
{
    "name": "tanmay saxena",
    "email": "tanmay4803@gmail.com",
    "current": "68000",
    "target": "67000"
}
Conclusion
This README provides the necessary steps to set up, run, and interact with the Django application for managing alerts. For any additional information or queries, refer to the documentation or contact the project maintainer.
