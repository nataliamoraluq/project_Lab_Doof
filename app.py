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

## CREATE INDICATION
@app.route("/", methods=["GET", "POST"])
def addIndication():
    if request.method == "POST":

        """
            {{el._id}}  -----> m._id
                {{el.nombre}}  -----> m.nombreProf
                -----> m.apellidoProf
                -----> m.idProf
                -----> m.nombreM
                -----> m.objetM
                -----> m.duracion
                -----> m.notaMin

                <div>
                <label for="indicationCode">Indication Code: </label><br>
                <input type="string" name="indicationCode" placeholder="Code here">
                <br>
            </div>
            <div>
                <label for="indicationDescription">Description of this indication: </label><br>
                <input type="string" name="indicationDescription" placeholder="Description here">
                <br>
            </div>
                
        """

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

## UPDATE
"""@app.route("/modificar/<id>", methods=["GET", "POST"])
def updateElement(id):
    oid = ObjectId(id)
    materia = collection.find_one({'_id': oid})
    if request.method == "POST":
        new_materia = request.form
        materia = collection.replace_one({'_id': oid},
                                        {
                                            'nombreProf' : new_materia['teacherFirstName'],
                                            'apellidoProf' : new_materia['teacherLastName'],
                                            'idProf' : new_materia['teacherId'],
                                            'nombreM' : new_materia['subjectName'],
                                            'objetM' : new_materia['subjectPurpose'],
                                            'duracion' : new_materia['durationSubject'],
                                            'notaMin' : new_materia['minimumPassingGrade'],
                                        })
        return redirect(url_for('subjects'))
    return render_template("updateSubject.html.jinja", subjectX=materia) """
## DELETE
@app.route("/delete/<id>", methods=["GET"])
def deleteElement(id):
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