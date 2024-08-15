#app - lab doof. - NataliaML - iv cohorte gracosoft - bd no sql eval. 2
from flask import Flask, redirect, request, render_template, url_for, flash
from db import userCollection, indicationCollection, categoryCollection, examServiceCollection
from bson.objectid import ObjectId
##
app = Flask(__name__, template_folder="./templates")

# --- LIST ---

#LIST - INDICATIONS
@app.route("/indications", methods=["GET"])
def indications():
    indicaciones = indicationCollection.find()
    return render_template("listIndication.html.jinja", indicaciones=indicaciones)

#LIST - CATEGORIES
@app.route("/categories", methods=["GET"])
def categories():
    categorias = categoryCollection.find()
    return render_template("listCategory.html.jinja", categorias=categorias)

#LIST - EXAMS & SERVICES
@app.route("/exams", methods=["GET"])
def exams():
    examenes = examServiceCollection.find()
    return render_template("listExam.html.jinja", examenes=examenes)

# ---------------------------------- CRUD INDICATIONS -------------------------------
## *** CREATE INDICATION ***
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

## *** UPDATE INDICATION ***
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

## *** DELETE INDICATION ***
@app.route("/deleteI/<id>", methods=["GET"])
def deleteIndication(id):
    oid = ObjectId(id)
    indicationCollection.delete_one({'_id': oid})
    indicaciones = indicationCollection.find()
    return render_template("listIndication.html.jinja", indicaciones=indicaciones)

# -------------------------------- CRUD CATEGORIES -------------------------------"
## *** CREATE CATEGORY ***
@app.route("/c", methods=["GET", "POST"])
def addCategory():
    if request.method == "POST":

        name = request.form['categName']
        description = request.form['categDescription']

        category = {
            'name' : name,
            'description' : description
        }

        print("Category: ", category)

        categoryCollection.insert_one(category)
        categorias = categoryCollection.find()
        return render_template("listCategory.html.jinja", categorias=categorias)
    return render_template("createCategory.html.jinja")

## *** UPDATE CATEGORY ***
@app.route("/updateC/<id>", methods=["GET", "POST"])
def updateCategory(id):
    oid = ObjectId(id)
    category = categoryCollection.find_one({'_id': oid})
    if request.method == "POST":
        new_category = request.form
        category = categoryCollection.replace_one({'_id': oid},
                                        {
                                            'name' : new_category['categName'],
                                            'description' : new_category['categDescription'],
                                        })
        return redirect(url_for('categories'))
    return render_template("updateCategory.html.jinja", categX=category)

## *** DELETE CATEGORY ***
@app.route("/deleteC/<id>", methods=["GET"])
def deleteCategory(id):
    oid = ObjectId(id)
    categoryCollection.delete_one({'_id': oid})
    categorias = categoryCollection.find()
    return render_template("listCategory.html.jinja", categorias=categorias)

## ### ---- ###
@app.route("/showCategOptions", methods=["GET"])
def sendCategory():
    categorias = categoryCollection.find()
    indicaciones = indicationCollection.find()
    return render_template("createExam.html.jinja", categorias=categorias, indicaciones=indicaciones)

# ---------------------------------- CRUD EXAM & SERVICES -------------------------------"
@app.route("/e", methods=["GET", "POST"])
def addExam():
    listCat = categoryCollection.find()
    listIndi = indicationCollection.find()
    if request.method == "POST":

        name = request.form['examCode']
        categoriesX = request.form['categories']
        typeOfSample = request.form['typeOfSample']
        price = request.form['priceExam']
        indicationX = request.form['indications']

        exam = {
            'name' : name,
            'categoriesX' : categoriesX,
            'typeOfSample' : typeOfSample,
            'price' : price,
            'indicationX' : indicationX
        }

        print("Exam: ", exam)

        examServiceCollection.insert_one(exam)
        examenes = examServiceCollection.find()
        return render_template("listExam.html.jinja", examenes=examenes)
    return render_template("createExam.html.jinja", categoriasList=listCat, indicacionesList=listIndi)

## *** UPDATE CATEGORY ***
@app.route("/updateE/<id>", methods=["GET", "POST"])
def updateExam(id):
    listCat = categoryCollection.find()
    listIndi = indicationCollection.find()
    oid = ObjectId(id)
    exam = examServiceCollection.find_one({'_id': oid})
    if request.method == "POST":
        new_exam = request.form
        exam = examServiceCollection.replace_one({'_id': oid},
                                        {
                                            'name' : new_exam['examCode'],
                                            'categoriesX' : new_exam['categories'],
                                            'typeOfSample' : new_exam['typeOfSample'],
                                            'price' : new_exam['priceExam'],
                                            'indicationX' : new_exam['indications'],
                                        })
        return redirect(url_for('exams'))
    return render_template("updateExam.html.jinja", examX=exam, categoriasList=listCat, indicacionesList=listIndi)


##OJO!! PROBAR Y CORREGIR ESTO: EN EL UPDATEEXAM.HTML

"""
            <select name="categories" id="categoryOptions">
                {% for c in categoriasList %}
                    {%if c.name.value=={{examX.categoryX.value}}%}
                        <option value="{{c.name}}"> {{c.name}}</option>
                    {%endif%}
                {% endfor %}
            </select>
            <div>
                <label for="typeOfSample">Sample type: </label><br>
                <input type="string" name="typeOfSample" placeholder="Type of sample here">
                <br>
            </div>
            <div>
                <label for="priceExam">Type of sample: </label><br>
                <input type="string" name="priceExam" placeholder="Price "in Bs" ">
                <br>
            </div>
            <label for="indication"> Indication: </label><br>
            <select name="indications" id="indicationOptions">
                {% for indiX in indicacionesList %}
                    <option value="{{indiX.codeIndic}}"> {{indiX.codeIndic}}</option>
                {% endfor %}
            </select>
"""
"""
    <div id="infoExam">
        <h1> {% block title %} Exam & Service: {% endblock %}</h1>
        <a href="{{url_for('addExam')}}"> Add an exam </a>
        <h3> Exams List: </h3>
    </div>
    <div id="examListCont">
        <ul>
            {% for e in examenes %}
                <li>
                    <p>{{e.code}}</p>
                    <a href="/updateC/{{c._id}}">Update</a>
                    <a href="/deleteC/{{c._id}}">Delete</a>
                </li>
            {% endfor %}
        </ul>
    </div>
"""
#LIST - EXAMS GENERAL
# CRUD EXAMS --

# CONSULT CATALOGUE
# SEE REPORT

if __name__ == "__main__":
    app.run(debug=True)


"""
     <!--
            <a href="{{ url_for('categories') }}"> Categories</a>
            <a href="{{ url_for('exams') }}"> Exams & Services</a>
            <a href="{{ url_for('showCatalogue') }}"> Consult catalogue</a>
            <a href="{{ url_for('showReport') }}"> See Report</a>
        -->
"""