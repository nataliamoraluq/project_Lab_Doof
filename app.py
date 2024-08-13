#app - lab doof. - NataliaML - iv cohorte gracosoft - bd no sql eval. 2
from flask import Flask, redirect, request, render_template, url_for, flash
from db import userCollection, indicationCollection, categoryCollection, examServiceCollection
from bson.objectid import ObjectId
##
app = Flask(__name__, template_folder="./templates")

@app.route("/subjects", methods=["GET"])
def indications():
    indicaciones = indicationCollection.find()
    return render_template("listIndication.html.jinja", indicaciones=indicaciones)


"""<a href="{{ url_for('addIndication') }}"> Indications</a>
        <a href="{{ url_for('addCategory') }}"> Categories</a>
        <a href="{{ url_for('addExam') }}"> Exams & Services</a>
        <a href="{{ url_for('showCatalogue') }}"> Consult catalogue</a>
        <a href="{{ url_for('showReport') }}"> See Report</a>"""

#LIST - INDICATIONS
# CRUD INDICATIONS --

#LIST - CATEGORIES
# CRUD CATEGORIES --

#LIST - EXAMS GENERAL
# CRUD EXAMS --

# CONSULT CATALOGUE
# SEE REPORT