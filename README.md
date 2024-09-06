# simple-flask-app
mlops-class-activity

# Simple Flask App

This project is a simple Flask application with a linear regression model. The app provides an HTML front-end and a REST API to interact with the model.

## Installation

1. Clone the repository:
    bash
    git clone https://github.com/your-username/simple-flask-app.git
    cd simple-flask-app
    
2. Create a virtual environment and activate it:
    bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    
3. Install the dependencies:
    bash
    pip install -r requirements.txt
    

## Usage

1. Run the Flask application:
    bash
    python app.py
    
2. Visit `http://127.0.0.1:5000/` in your browser to view the HTML page.
3. Use a tool like Postman to send POST requests to `http://127.0.0.1:5000/predict`.

## Deployment

This project is deployed on Vercel. Follow these steps to deploy it yourself:

1. Push your code to GitHub.
2. Import the repository into your Vercel dashboard.
3. Set up the project using the Python/Flask framework.
4. Vercel will provide a deployment link.


