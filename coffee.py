import flask

allcoffeessss=[]

app=flask.Flask("COFFEE APP")

@app.route("/" ,methods=["get","post"])

def HOME():
    return flask.render_template("HOME🧋.HTML",allcoffeessss=allcoffeessss)


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
        allcoffeessss.append(newcofffee)


        #to do:save



    return flask.render_template("ADD COFFEE.HTML")










app.run()