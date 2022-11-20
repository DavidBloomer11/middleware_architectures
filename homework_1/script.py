import re
import json

#importing email
with open('email.txt') as f:
    email = f.read()
    f.close()


#extracting data from email

tour_id = re.findall(r'Tour id: "(.*?)"', email)
location = re.findall(r'Location: "(.*?)"', email)
person = re.findall(r'Person: "(.*?)"', email)

dictionary = {'tour_id':tour_id[0], 'location':location[0],'person':person[0]}

#output
print(json.dumps(dictionary))