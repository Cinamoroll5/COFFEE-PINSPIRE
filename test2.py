import json

newcofffee={
            "name": 'chocochips',
            "description": 'tasty',
            "ingridients":"chocolate",
            "imagename":"choco eatt eat"
        }
#read the file

file=open("me.json","r")
allcoffee=json.load(file)
print(allcoffee)
file.close()
allcoffee.append(newcofffee)
#save all the coffffeeeeeeeeeeeeessssssssssszzzzzzzzz!!!!!!!!!!!!!!!!!!bobotea
file=open("me.json","w")
json.dump(allcoffee,fp=file,indent=4)
file.close()