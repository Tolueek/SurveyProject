User Data Collection Project

Overview

This project is a web application built using Flask that allows users to input their personal information and expenses. The data is stored in a MongoDB database. A Python or R class named "User" processes the collected data, which is then saved into a CSV file for further analysis. The final analysis and visualizations can be done in a Jupyter Notebook.

This project is hosted on AWS and can be accessed via the provided link.

Features

User data collection through a Flask web application.
MongoDB as the backend database for storing user data.
Data processing using a Python/R class.
Data export to a CSV file.
Data analysis and visualization using Jupyter Notebooks.
Technologies Used

Flask: Web framework for building the application.
MongoDB: NoSQL database for storing user data.
Python: Programming language for building the app and processing data.
Pandas: Python library for data manipulation and CSV operations.
Matplotlib/Seaborn: Python libraries for creating visualizations.
Jupyter Notebook: Interactive environment for data analysis.
AWS: Hosting environment for the application.
Prerequisites

Before running this project, make sure you have the following installed:

Python 3.x
MongoDB
Flask
Pandas
Matplotlib or Seaborn
Jupyter Notebook
To install the required Python packages, run the following:

pip install -r requirements.txt
Project Setup

1. Clone the Repository
First, clone this repository to your local machine:

git clone https://github.com/yourusername/user-data-collection-project.git
2. Set Up MongoDB
Ensure that MongoDB is installed and running on your system or use a cloud-based instance. You can install MongoDB from the official website.

3. Create a Virtual Environment
It's recommended to use a virtual environment to manage dependencies:

python3 -m venv myenv
source myenv/bin/activate  # On Windows, use 'myenv\Scripts\activate'
4. Install Dependencies
After setting up the virtual environment, install the required dependencies:

pip install -r requirements.txt
5. Run the Flask Application
To run the Flask application locally, use the following command:

FLASK_APP=app.py flask run --host=0.0.0.0 --port=5000
This will start the Flask web application on port 5000. You can access it by navigating to http://localhost:5000 in your web browser.

6. Accessing the Application on AWS
If your app is hosted on AWS, you can access it by navigating to the public IP or domain name of your EC2 instance.

File Structure

user-data-collection-project/
│
├── app.py                # Main Flask application
├── requirements.txt      # List of required Python libraries
├── user.py               # User class for data processing
├── data/                 # Folder to store collected data
│   └── user_data.csv     # CSV file for storing user data
├── templates/            # Folder for HTML templates
│   └── index.html        # Main page of the web app
├── static/               # Folder for static files (CSS, JS, images)
├── notebooks/            # Folder for Jupyter notebooks (analysis)
│   └── data_analysis.ipynb
└── README.md             # This README file
Application Workflow

User Input: Users enter their personal details and expense information through the web application.
Data Storage: The data is saved to a MongoDB database.
Data Processing: A Python or R class processes the user data, generating CSV files for analysis.
Data Analysis: A Jupyter notebook is used to analyze the data, generating visualizations that are saved as images or charts.
Web Deployment: The Flask application is hosted on AWS for public access.
Running the Analysis

To perform data analysis:

Open the Jupyter notebook located in the notebooks/ folder:
jupyter notebook notebooks/data_analysis.ipynb
Run the cells to load the CSV file, process the data, and generate visualizations.
Export the generated charts or analysis as needed.
Deployment on AWS

EC2 Instance Setup: Launch an EC2 instance with your preferred operating system.
Install Dependencies: Install Python, Flask, MongoDB, and other required packages on the EC2 instance.
Upload the Application: Use SCP, FTP, or Git to upload the application files to the EC2 instance.
Start the Flask Application: Run the Flask app on the EC2 instance:
FLASK_APP=app.py flask run --host=0.0.0.0 --port=5000
Configure Nginx (Optional): Use Nginx as a reverse proxy to route traffic to the Flask application.
Access the Application: Once deployed, you can access the application by using the public IP address or domain of the EC2 instance.
Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request. For any issues or feature requests, feel free to create an issue in the GitHub repository.

License

This project is licensed under the MIT License - see the LICENSE file for details.
