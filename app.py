#app - lab doof. - NataliaML - iv cohorte gracosoft - bd no sql eval. 2
from flask import Flask, redirect, request, render_template, url_for, flash
from db import userCollection, indicationCollection, categoryCollection, examServiceCollection
from bson.objectid import ObjectId
#from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
##
app = Flask(__name__, template_folder="./templates")

"""login_manager = LoginManager()
login_manager.init_app(app)"""

# --- LIST ---
examFiltList = [] #filtered list

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

#START - MAIN PAGE
@app.route("/main", methods=["GET"])
def showMain():
    return render_template("mainPage.html.jinja")

#START - BASE
@app.route("/", methods=["GET"])
def showBase():
    return render_template("base.html.jinja")
"""
# ------------ LOGGIN & REGISTER (SADLY NOR WORKING)------------------

@app.route("/login", methods=["GET", "POST"])
def logginUser():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        user = userCollection.find_one({'username': username, 'password': password})
        if user:
            flash('Welcome!', 'message')
            return render_template("base.html.jinja")
        else:
            flash('Error! Invalid username or password', 'error')
    return render_template("logginUser.html.jinja")


@app.route("/register", methods=["GET", "POST"])
def registerUser():
    if request.method ==  "POST":

        user = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if user: 
            if email:
                if password:
                    userX = {
                        "username": user,
                        "email": email,
                        "password": password
                    }
                    userCollection.insert_one(userX)
                    return redirect(url_for('logginUser'))
        else:
            flash('Err0r, fill data to complete', 'error')
    return render_template('registerUser.html.jinja')

"""
# ---------------------------------- CRUD INDICATIONS -------------------------------
## *** CREATE INDICATION ***
@app.route("/indicationC", methods=["GET", "POST"])
def addIndication():
    if request.method == "POST":

        codeIndic = request.form['indicationCode']
        description = request.form['indicationDescription']

        indication = {
            'codeIndic' : codeIndic,
            'description' : description
        }
        #print("Indication: ", indication)
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

        #print("Category: ", category)

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
# ---------------------------------- CRUD EXAM & SERVICES -------------------------------"
## *** ADD EXAM ***
@app.route("/e", methods=["GET", "POST"])
def addExam():
    listCat = categoryCollection.find()
    listIndi = indicationCollection.find()
    if request.method == "POST":
        codeExam = request.form['examCode']
        name = request.form['examName']
        categoriesX = request.form['categories']
        typeOfSample = request.form['typeOfSample']
        price = request.form['priceExam']
        indicationX = request.form['indications']

        exam = {
            'codeExam' : codeExam,
            'name': name,
            'categoriesX' : categoriesX,
            'typeOfSample' : typeOfSample,
            'price' : price,
            'indicationX' : indicationX
        }
        #print("Exam: ", exam)
        examServiceCollection.insert_one(exam)
        examenes = examServiceCollection.find()
        return render_template("listExam.html.jinja", examenes=examenes)
    return render_template("createExam.html.jinja", categoriasList=listCat, indicacionesList=listIndi)
## *** UPDATE EXAM ***
@app.route("/updateS/<id>", methods=["GET", "POST"])
def updateExam(id):
    listCat = categoryCollection.find()
    listIndi = indicationCollection.find()
    oid = ObjectId(id)
    exam = examServiceCollection.find_one({'_id': oid})
    if request.method == "POST":
        new_exam = request.form
        exam = examServiceCollection.replace_one({'_id': oid},
                                        {
                                            'codeExam' : new_exam['examCode'],
                                            'name' : new_exam['examName'],
                                            'categoriesX': new_exam['category'],
                                            'typeOfSample' : new_exam['typeOfSample'],
                                            'price' : new_exam['priceExam'],
                                            'indication': new_exam['indication'],
                                        })
        return redirect(url_for('exams'))
        #'categoriesX' : new_exam['categories'], 'indicationX' : new_exam['indications'],
    return render_template("updateExam.html.jinja", examX=exam, categoriasList=listCat, indicacionesList=listIndi)
## *** DELETE EXAM ***
@app.route("/deleteS/<id>", methods=["GET"])
def deleteExam(id):
    oid = ObjectId(id)
    examServiceCollection.delete_one({'_id': oid})
    examenes = examServiceCollection.find()
    return render_template("listExam.html.jinja", examenes=examenes)

## *** DETAILED EXAM ***
@app.route("/detailedServ/<id>", methods=["GET"])
def getExam(id):
    oid = ObjectId(id)
    serviceX = examServiceCollection.find_one({'_id': oid})
    return render_template("detailedExam.html.jinja", examen=serviceX)

## ### ---- FILTERS - SPECIFIC LIST - (CATALOGUE & REPORT) ###
# CONSULT CATALOGUE
@app.route("/filter", methods=["GET", "POST"])
def showCatalogue():
    categories = categoryCollection.find()
    if request.method == "POST":
        catfilter = request.form.get('categoryFilter')
        samplefilter = request.form.get('sampleFilter')
        print("Filtro categoria: ", catfilter, "Sample filter: ", samplefilter)
        
        examFiltList = examServiceCollection.find({'categoriesX': catfilter, 'typeOfSample': samplefilter})
        print("Exams list: ", examFiltList)
        if catfilter:
            examFiltList = examServiceCollection.find({'categoriesX': catfilter})
        elif samplefilter:
            #examFiltList = [exam for exam in examFiltList if exam['typeOfSample'] == samplefilter]
            examFiltList = examServiceCollection.find({'typeOfSample': samplefilter})
        else:
            examFiltList = examServiceCollection.find()
    else:
        examFiltList = examServiceCollection.find()
        #
    return render_template("catalogueExam.html.jinja", categorias=categories, exams=examFiltList)
# SEE REPORT
@app.route("/report", methods=["GET"])
def showReport():
    #
    categNewList = [] 
    top = 0 
    mostCommonIndic = {}
    #
    intervalE = {
        'first':0,
        'second':0,
        'third':0,
        'fourth':0,
        'fifth':0,
    }
    # ---- EXAMS BY PRICE RANGES (0 TO 500+) ----
    for exam in examServiceCollection.find(): 
        if float(exam['price']) <= 100: 
            intervalE['first'] += 1 
        elif float(exam['price']) <= 200: 
            intervalE['second'] += 1 
        elif float(exam['price']) <= 300: 
            intervalE['third'] += 1 
        elif float(exam['price']) <= 500: 
            intervalE['fourth'] += 1 
        elif float(exam['price']) > 500: 
            intervalE['fifth'] += 1 
    # ---- MOST COMMON INDICATION ----
    for indic in indicationCollection.find(): 
        i = 0 
        for examX in examServiceCollection.find(): 
            if examX['indicationX'] == indic['description']: 
                i += 1 
        if i > top: 
            top = i 
            mostCommonIndic = {'code': indic['codeIndic'], 'description': indic['description']}  
    # ---- EXAMS REGISTERED IN EACH CATEGORY ----
    for cat in categoryCollection.find(): 
        i = 0 
        for exam in examServiceCollection.find(): 
            if exam['categoriesX'] == cat['name']: 
                i += 1 
        categNewList.append({'name': cat['name'], 'num': str(i)}) 
    #
    return render_template("reportExam.html.jinja", categNewList=categNewList, intervalE=intervalE, mostCommonIndic=mostCommonIndic)

@app.route("/video", methods=["GET"])
def showVideo():
    return render_template("videoBase.html.jinja")



if __name__ == "__main__":
    app.run(debug=True)


"""
    from collections import Counter
from flask import Flask, request, render_template, flash, redirect, url_for
from db import examCollection, userCollection, categoryCollection, indicationCollection
from bson.objectid import ObjectId
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from random import randint
from collections import defaultdict

app = Flask(__name__, template_folder="./templates")
app.config['SECRET_KEY'] = "twiceot9"
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
    user = userCollection.find_one({'_id': ObjectId(user_id)})
    if user:
        user_obj = User()
        user_obj.id = str(user['_id'])
        return user_obj
    return None

#Initial page
@app.route("/", methods=["GET"])
def showHome():
    return render_template("home.html.jinja")

#User login and register
@app.route("/register", methods=["GET", "POST"])
def registerF():
    if request.method ==  "POST":

        user = request.form['username']
        pw = request.form['password']

        user = {
            "username": user,
            "password": pw
        }
        
        userCollection.insert_one(user)
        return redirect(url_for('loginF'))
    return render_template('userRegister.html.jinja')

@app.route("/login", methods=["GET", "POST"])
def loginF():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        user = userCollection.find_one({'username': username, 'password': password})
        if user:
            user_obj = User()
            user_obj.id = str(user['_id'])
            login_user(user_obj)
            return redirect(url_for('showMenu'))
        else:
            flash('Invalid username or password', 'error')

    return render_template("login.html.jinja")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('showMainPage'))
"""