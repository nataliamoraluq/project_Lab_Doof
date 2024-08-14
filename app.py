#app - lab doof. - NataliaML - iv cohorte gracosoft - bd no sql eval. 2
from flask import Flask, redirect, request, render_template, url_for, flash
from db import userCollection, indicationCollection, categoryCollection, examServiceCollection
from bson.objectid import ObjectId
##
app = Flask(__name__, template_folder="./templates")

#LIST - INDICATIONS
@app.route("/indications", methods=["GET"])
def indications():
    indicaciones = indicationCollection.find()
    return render_template("listIndication.html.jinja", indicaciones=indicaciones)

#LIST - INDICATIONS
@app.route("/categories", methods=["GET"])
def categories():
    categorias = categoryCollection.find()
    return render_template("listCategory.html.jinja", categorias=categorias)


## CREATE INDICATION
@app.route("/", methods=["GET", "POST"])
def addIndication():
    if request.method == "POST":

        codeIndic = request.form['indicationCode']
        description = request.form['indicationDescription']

        indication = {
            'codeIndic' : codeIndic,
            'description' : description
        }

        print("Indication: ", indication)

        indicationCollection.insert_one(indication)
        indicaciones = indicationCollection.find()
        return render_template("listIndication.html.jinja", indicaciones=indicaciones)
    return render_template("createIndication.html.jinja")

## UPDATE INDICATION
@app.route("/updateI/<id>", methods=["GET", "POST"])
def updateIndication(id):
    oid = ObjectId(id)
    indication = indicationCollection.find_one({'_id': oid})
    if request.method == "POST":
        new_indication = request.form
        indication = indicationCollection.replace_one({'_id': oid},
                                        {
                                            'codeIndic' : new_indication['indicationCode'],
                                            'description' : new_indication['indicationDescription'],
                                        })
        return redirect(url_for('indications'))
    return render_template("updateIndication.html.jinja", indicX=indication) 

## DELETE INDICATION
@app.route("/deleteI/<id>", methods=["GET"])
def deleteIndication(id):
    oid = ObjectId(id)
    indicationCollection.delete_one({'_id': oid})
    indicaciones = indicationCollection.find()
    return render_template("listIndication.html.jinja", indicaciones=indicaciones)


"""
{% for x in indicaciones %}
                <li> 
                    <p>{{ x.codeIndic }}</p> 
                    <p>{{x.description}} </p>
                    <a href="/modificar/{{x._id}}">Modificar</a> 
                    <a href="/delete/{{x._id}}">Eliminar</a> 
                </li>
            {% endfor %}
"""
# CRUD INDICATIONS --

"""<a href="{{ url_for('addIndication') }}"> Indications</a>
        <a href="{{ url_for('addCategory') }}"> Categories</a>
        <a href="{{ url_for('addExam') }}"> Exams & Services</a>
        <a href="{{ url_for('showCatalogue') }}"> Consult catalogue</a>
        <a href="{{ url_for('showReport') }}"> See Report</a>"""



#LIST - CATEGORIES
# CRUD CATEGORIES --

#LIST - EXAMS GENERAL
# CRUD EXAMS --

# CONSULT CATALOGUE
# SEE REPORT

if __name__ == "__main__":
    app.run(debug=True)


"""
     <!--
            <a href="{{ url_for('addCategory') }}"> Categories</a>
            <a href="{{ url_for('addExam') }}"> Exams & Services</a>
            <a href="{{ url_for('showCatalogue') }}"> Consult catalogue</a>
            <a href="{{ url_for('showReport') }}"> See Report</a>
        -->
"""