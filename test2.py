import json


file=open("me.json","r")
file.seek(0)
allcoffees=json.loads(file.read())
file.close()
print (type(allcoffees))
print(allcoffees)


newcofffee={
            "name": 'chocochips',
            "description": 'tasty',
            "ingridients":"chocolate",
            "imagename":"choco eatt eat"
        }
allcoffees.append(newcofffee)
file=open("me.json","w")
file.write(str(allcoffees))
file.flush()


file.close()