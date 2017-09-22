import csv
persons=[]
fields = ['name', 'email','mobile','university','major']
id = 1
while 1:
    person={
            'name':'',
            'email':'',
            'mobile':'',
            'university':'',
            'major':''
            }
    person['name']=input('Enter The name')
    if person['name'].upper()=="STOP":
        break
    person['email'] = input('Enter The email')
    if person['email'].upper() == "STOP":
        person['email'] = ''
        persons.append(person)
        print("New Person added with name : "+person['name']+" and an email : "+person['email']+" and a mobile : "+person['mobile']+" at university : "+person       ['university']+" at the major : "+person['major'])
        break
    person['mobile'] = input('Enter The mobile')
    if person['mobile'].upper() == "STOP":
        person['mobile'] = ''
        persons.append(person)
        print("New Person added with name : "+person['name']+" and an email : "+person['email']+" and a mobile : "+person['mobile']+" at university : "+person       ['university']+" at the major : "+person['major'])
        break
    person['university'] = input('Enter The university')
    if person['university'].upper() == "STOP":
        person['university'] = ''
        persons.append(person)
        print("New Person added with name : "+person['name']+" and an email : "+person['email']+" and a mobile : "+person['mobile']+" at university : "+person       ['university']+" at the major : "+person['major'])
        break
    person['major'] = input('Enter The major')
    if person['major'].upper() == "STOP":
        person['major'] = ''
        persons.append(person)
        print("New Person added with name : "+person['name']+" and an email : "+person['email']+" and a mobile : "+person['mobile']+" at university : "+person       ['university']+" at the major : "+person['major'])
        break
    persons.append(person)
    print("New Person added with name : "+person['name']+" and an email : "+person['email']+" and a mobile : "+person['mobile']+" at university : "+person['university']+" at the major : "+person['major'])

outputFile = open('names.csv', 'w')
with outputFile:
    writer = csv.DictWriter(outputFile, fieldnames=fields)
    writer.writeheader()
    for person in persons:
        writer.writerow(person)

