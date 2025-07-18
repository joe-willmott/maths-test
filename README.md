# Maths Test

This project provides an app where users can take a simple test on linear equations.

The app can be accessed at https://maths-test.onrender.com

## Local Development

To run this project on your local machine, clone the repo to your machine and create a python virtual environment.

The only library required to run this app locally is flask, currently pinned at version 3.1.1. To install this dependency, create a virtual environment from the requirements.txt file, or run the following cammand in the terminal:
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

There is currently only one branch (main) for this repo, so you can push the changes directly to the main branch. However, there would ideally be a staging branch connected to a GUI which you could pudh the changes to first for testing.

Alternatively, you could create a development branch and connect it to a new GUI using the hosting instructions below. Then you could deploy changes to the development branch and test the GUI before merging the developemnt branch with the main branch.

## Hosting

The app is hosted using render.com.

There is an extra dependency required for hosting the app, called gunicorn. This is currently pinned at version 23.0.0 and can be installed using the following command:
```powershell
pip install gunicorn==23.0.0
```

You should not need to install this library to run the app locally, but it is included in the requirements.txt file so that render.com installs it prior to redeploying the live app.

The app goes to sleep when not in use, so it may take some time to start up when visiting the page. Redeploying the app makes it start up, so you can test very quickly after the app is fully deployed.
