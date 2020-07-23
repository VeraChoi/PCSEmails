import sendgrid
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To
import csv

to_emails = [
]

info_start = 2; #Write the row number where student information begins here
with open('sample2.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  for row in csv_reader:
        if line_count <info_start: 
           line_count+=1
        else:
            
            to_emails.append(To(email=row[19],
              name=row[18],
              dynamic_template_data={
              #Enter the column number for each element in the brackets 
              'name':row[18],
              'id':row[14],
              'password':row[15],
              'scratchid':row[16],
              'scratchpass':row[17],
              'class':row[5],
              'start':row[7],
              'teacher': "Teacher name",
              'student':row[3],
              'subject':("A message from Penguin Coding School about "+ row[5] + ' starting ' +row[7])
              }))
            line_count += 1

message = Mail(
    from_email=('veraychoi@gmail.com', 'Me, SendGrid Vera'),
    to_emails=to_emails,
    is_multiple=True)
message.template_id = 'd-d091c8b666ff462794e1862b7430c9f9' 



try:
    sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)