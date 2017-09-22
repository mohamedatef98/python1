import csv
persons=[]
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
    if person['name'].upper()[0]=="S" and person['name'].upper()[len(person['name'])-1] =="P":
        break
    person['email'] = input('Enter The email')
    person['mobile'] = input('Enter The mobile')
    person['university'] = input('Enter The university')
    person['major'] = input('Enter The major')
    persons.append(person)
    print("New Person added with name : "+person['name']+" and an email : "+person['email']+" and a mobile : "+person['mobile']+" at university : "+person['university']+" at the major : "+person['major'])

outputFile = open('names.csv', 'w')
with outputFile:
    writer = csv.DictWriter(outputFile, fieldnames=['name', 'email','mobile','university','major'])
    writer.writeheader()
    for person in persons:
        writer.writerow(person)


