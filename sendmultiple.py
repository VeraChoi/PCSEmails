import sendgrid
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To
import csv

to_emails = [
]

info_start = 2; #Write the row number where student information begins here

#write the name of the file containing the information in the quotations of open('')
with open('sample2.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  for row in csv_reader:
        if line_count <info_start: 
           line_count+=1
        else:  
          emailnum=19 #Edit this variable to match the column number of the emails
          namenum=18 #Edit this to match the column number of the names
          to_emails.append(To(email=row[emailnum],
              name=row[namenum],
              dynamic_template_data={
              #This is where you can add unique info to emails. To add a unique word or component, write a name for the component and the column number in the format
              #'name':row[column_number],
              #Just as shown below. Please note that column numbers begin from 0.
              #Several unique component have already been created. If the column number for any information changes, change the number in the brackets to match.
              #To include these unique components in the emails, edit them into the corresponding template on SendGrid under Email API>Dynamic Templates>SendEmails.
              #Click edit code, then write the name of the component in double braces. For example,
              #Dear {{name}}, you are signed up for {{class}}.
              'name':row[namenum],
              'id':row[14], #This denotes the login for the repl accounts of java students
              'password':row[15], #This is the repl passwords for java students
              'scratchid':row[16], #This is the scratch id for scratch students
              'scratchpass':row[17], #This is the scratch password for scratch students
              'class':row[5], #This is the activity of the student
              'start':row[7],#This is the date of the first class
              'teacher': "Teacher name",#Add row[col_number] in place of Teacher name once a column containing the teacher is added to the file
              'student':row[3], #This is the student name
              'subject':("A message from Penguin Coding School about "+ row[5] + ' starting ' +row[7]) #This is the subject of the email
              }))
          line_count += 1


message = Mail(
  #Write the email which the SendGrid account is linked to below, followed by the name of the sender (both should be in quotations)
    from_email=('info@penguincodingschool.com', 'Penguin Coding School'),
    to_emails=to_emails,
    is_multiple=True)

#Each template has a template id. Multiple versions can be linked to one template, but only one can be active at the same time. 
#Copy and paste the template id below in quotations. 
message.template_id = 'd-28ef7a8d055146ca961db1729c7ba3ef' 



try:
    sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
