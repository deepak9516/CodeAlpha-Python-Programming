import re

#Read the file
with open(r"Task 3 (Task Automation with Python Scripts)\input.txt","r") as file:
    content = file.read()

#Extract emails
emails = re.findall(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",content
    )

#save emails to another file
with open("email.txt","w") as file:
    for email in emails:
        file.write(email + "\n")
        
        
        
        
print("Emails extracted successfully!")
print("Total emails found: ",len(emails))