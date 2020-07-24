PREREQUISITES:
- Python version 2.7, 3.5, 3.6, 3.7, or 3.8 (download here: https://www.python.org/downloads/)
- The SendGrid service, starting at the free level

CREATING AND LINKING AN API KEY:
Log in to SendGrid using Penguin Coding School's account. Then, at the bottom left under settings, click API keys (https://app.sendgrid.com/settings/api_keys).
Press "Create API Key" and save the key shown. 

Then, set the key as an environment variable following these instructions:
Mac
(Type this into your command line):
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env
SendGrid also supports local environment file .env. Copy or rename .env_sample into .env and update SENDGRID_API_KEY with your key.

Windows

Temporarily set the environment variable(accessible only during the current cli session):
(Type this into your command line)

set SENDGRID_API_KEY=YOUR_API_KEY

Permanently set the environment variable:

setx SENDGRID_API_KEY "YOUR_API_KEY"


To install sendgrid and all its dependancies, type 

pip install sendgrid

into your command line. These instructions, and further reference, can be found at (https://github.com/sendgrid/sendgrid-python#install-package)

DOWNLOADING THE FILE:

Download the file sendmultiple.py. Edit the file where the comments indicate (it should say sample2.csv) to represent your csv file containing the information you want to send. This file and sendmultiple.py should be in the same folder.
Edit the file where the comments indicate to match the template id of the email you are sending. Edit any dynamic information in the file by following the directions in the comments.

EDITING THE EMAIL:
The dynamic contents of the email can be added easily by editing sendmultiple.py where the comments indicate once added to your csv file. 
The layout of the email can be edited from the Dynamic Templates tab under Email API (https://mc.sendgrid.com/dynamic-templates) after logging in. Click edit, then edit code on the HTML block to edit this template. 
Alternatively, you can create a new template by clicking Create Dynamic Template and dragging an HTML module into the email. Follow the instructions in the file to add dynamic content, using the syntax {{info_name}} within the block to include it. 
If you choose to create a new template, edit sendmultiple.py where indicated to include the new template id. Each template may have multiple versions, but only one may be activated at once. In this situation, the template id remains the same, so the file does not need to be edited.


