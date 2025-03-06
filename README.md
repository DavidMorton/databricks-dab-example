# Skeleton for deploying Databricks Apps using DAB

## Intro

This repo has a blank starter template for deploying a reflex.dev website via a Databricks DAB. The site itself is pretty simple, being that it's the default template for reflex.dev applications, but it can be extended or changed to do whatever you need.

## Quick Tour

### databricks.yml

The root folder contains the databricks.yml file that defines the bundle. You'll notice that it has no deployment target hardcoded into it. There's a reason for this that we'll get around to later. The main takeaway from this is that it references the resources folder, which contains one other YAML script, which, in this case, deploys the website. Should you need other resources deployed, you would add additional YAML files into this resources folder. 

### app folder

The app folder contains the actual application itself, starting with the config file for the reflex.dev application (which you can find more information about on the [reflex.dev](https://reflex.dev/) home page).

You'll also find a requirements.txt file within the folder where you can include all your dependencies to be installed via PyPi. 

### .github folder

The github folder contains the action necessary to deploy the application. You'll notice there is neither a target workspace, nor a workspace token in this file. For security reasons, these values will be set within the action's secrets.

## Setting this up

### Viewing the GitHub Action

First, fork this repo into your own environment, or copy it to a new repo. As this is a personal repository of mine, you'll have no access to perform any deployments from this repo. 

Once you've created a new repo in GitHub containing the contents of this repo, go to the Repository's Actions tab in the UI. It's here where you'll be able to see the GitHub action that resides within the .github directory. You can view the deployment script here, and modify it if you'd like.

### Fetching a databricks token for deployment

1. In Databricks, visit the workspace to which you'd like to deploy your app.
1. In the upper right corner, click the icon with your initial or photo on it, and go to Settings.
1. On the settings page, navigate to Developer on the right panel. 
1. Next to "Access Tokens", you'll see a button to manage your access tokens. Click it.
1. Generate a new token. Set the lifetime of the token to something that works for you. 
1. Once your token has been generated, copy it. You won't see it again after you dismiss the dialog.

### Adding token to Github

1. Back in your GitHub repo, navigate to the repo Settings
1. On the left panel, navigate to Secrets and variables, followed by Actions.
1. Create a new repository secret. Name it DATABRICKS_TOKEN, and for the value, paste the token you generated above.
1. Copy the hostname (without any URL path) of your Databricks workspace. You should be able to get this from your browser's navigation bar.
1. Create a new repository secret. Name it DATABRICKS_HOST, and paste the hostname in as the value. Remember to exclude any part of the URL following the domain name. 

### Running the action

1. In your GitHub repo, navigate to the actions tab. You should see a failed action run from earlier in the list of workflow runs. It failed because, when you first checked in the files, you were lacking the necessary secrets in GitHub to connect to the databricks workspace. Click into the failed run. 
1. Near the top right of the page, you should see a button that says "Re-run all jobs". Click it. If all goes well, this should deploy the application for you.

### Verifying the app is deployed

1. Back in your Databricks workspace, on the left panel, navigate to Compute.
1. Click into the Apps tab.
1. Click the name of the app in the list.

You should see the current status of the app, whether it's running or not. From here you can also examine the logs in case something failed. 

*NOTE: AT THE TIME OF WRITING, THIS APP CRASHES INITIALLY. CLICK THE DEPLOY BUTTON ON THE TOP RIGHT, AND THE SECOND TIME, AND EACH SUBSEQUENT TIME AFTER, IT SHOULD WORK FINE* 



