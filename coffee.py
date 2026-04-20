import flask
import json


file=open("me.json","r")
allcoffee=json.load(file)
print(allcoffee)
file.close()

app=flask.Flask("COFFEE APP")

@app.route("/" ,methods=["get","post"])

def HOME():
    return flask.render_template("HOME🧋.HTML",allcoffeessss=allcoffee)


#add coffee

@app.route("/ADD" ,methods=["get","post"])

def ADD():
    if flask.request.method=="POST":
        coffee=flask.request.form.get("coffee")
        description=flask.request.form.get("description")
        ingridients=flask.request.form.get("ingridients")

        print (flask.request.files)
        print("*********************************************")


        image=flask.request.files.get("image")
        image.save("static/images/"+image.filename)


        print(coffee)
        print(description)
        print(ingridients)

        newcofffee={
            "name":coffee,
            "description":description,
            "ingridients":ingridients,
            "imagename":image.filename
        }
        allcoffee.append(newcofffee)
        #save all the coffffeeeeeeeeeeeeessssssssssszzzzzzzzz!!!!!!!!!!!!!!!!!!bobotea
        file=open("me.json","w")
        json.dump(allcoffee,fp=file,indent=4)
        file.close()

      



    return flask.render_template("ADD COFFEE.HTML")










app.run()