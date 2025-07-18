# Maths Test

This project provides an app where users can take a simple test on linear equations.

The app can be accessed at https://maths-test.onrender.com

## Local Development

To run this project on your local machine, clone the repo to your machine and create a python virtual environment. You can clone the repository with the following command:
```bash
git clone https://github.com/joe-willmott/maths-test.git
```

The only library required to run this app locally is flask, currently pinned at version 3.1.1. To install this dependency, create a virtual environment from the requirements.txt file, or run the following command in the terminal:
```powershell
pip install flask==3.1.1
```

Once you have all dependencies installed, you can run the app locally by running either of the following commands in the terminal:
```powershell
python -m flask run
```
```powershell
python app.py
```

Both of these commands should work as long as the main app file is named app.py.

Once the app is running locally, you should see a URL in the terminal. It should look something like http://127.0.0.1:5000/

Follow this URL to see your app running in a web browser. As you make changes to your code locally, if you save your files and refresh the web page, the page should be updated to reflected the latest code changes.

## Deployment

If you have made changes locally which you would like to deploy, you should commit your changes to your cloned repo and push the changes to GitHub. Make sure to provide a clear and concise commit message so that other contributors can easily see past changes.

There is currently only one branch (main) for this repo, so you can push the changes directly to the main branch. However, there would ideally be a staging branch connected to a GUI which you could push the changes to first for testing.

Alternatively, you could create a development branch and connect it to a new GUI using the hosting instructions below. Then you could deploy changes to the development branch and test the GUI before merging the development branch with the main branch.

## Hosting

The app is hosted using render.com.

There is an extra dependency required for hosting the app, called gunicorn. This is currently pinned at version 23.0.0 and can be installed using the following command:
```powershell
pip install gunicorn==23.0.0
```

You should not need to install this library to run the app locally, but it is included in the requirements.txt file so that render.com installs it prior to redeploying the live app.

The app goes to sleep when not in use, so it may take some time to start up when visiting the page. Redeploying the app makes it start up, so you can test very quickly after the app is fully deployed.

## Using the App

Go to https://maths-test.onrender.com

Click the 'Start the test' button.

Each question requires the user to provide the missing value (x) in the equation.

If the user gives the correct answer, their score increases by 1. If they give an incorrect or invalid answer, their score remains unchanged and they move onto the next question.

There are 10 questions in total, and the user receives a score out of 10 and a percentage at the end of the test.

## About the Code

The app uses flask's session functionality to create session-level variables:
* score
* question_count
* answer
* question

When using session-level variables, the app must use a secret_key. his is defined in app.py.

There are 3 routes in the app:
* "/"
* "/question"
* "/result"

The "/" route is the home page and uses the index.html template. This page simply contains a welcome title and a button to start the test.

When the button is clicked, it takes the user to the "/question" page. The app uses flask's url_for function to get the URL for the "question" function. This allows the route names to be dynamic, as long as the function within each route remains the same.

When the "question" page is loaded, it calls the question() function with a GET method. If the number of questions answered is less than the maximum number of questions, currently set at 10, it will generate a question and render the question.html template with the question and feedback strings as parameters. At this point, feedback is just an empty string. When the function generates a question, calls the generate_equation() function in "scripts/helper_functions.py". This function takes no inputs but returns a tuple of 2 items: the question string and the correct answer. After the equation is generated, the question() function stores the question and answer in session-level variables.

When the user clicks the 'Submit' button on the "/question" page, it will submit the answer they've inputted. This button triggers the question() function with a POST method. The function recognises the POST method and compares the user input to the answer stored in the session-level variable. It marks the answer, catching value errors if the input can't be converted to an integer, and stores the feedback in the feedback variable, which is subsequently displayed on the "/question" page when the page is re-rendered.

If the number of questions answered is greater than or equal to the maximum number of questions, it will redirect the user to the "/result" page.

The "/result" page uses the result.html template and shows a score out of 10 and, their score converted to a percentage. It also shows a link to take them back to the home page to restart the test.

The percentage is calculated in the result() function withing the "/result" route. it uses the session-level variable "score" and the maximum number of questions, currently set at 10. It will convert the percentage to an integer if it's a whole number, otherwise it will show as a float. This is just for readability.

All templates use the same styles.css file as a stylesheet.

The app runs with debugging enabled to help troubleshoot any potential issues
