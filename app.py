from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/skills")
def showskills():
    skills_list=["CSS","HTML","PYTHON"]
    return render_template("skills.html",skills=skills_list)

@app.route('/contact',methods=["GET","POST"])
def contact():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        return f"You are registred with email:{email}"
    return render_template("contact.html")
if __name__ == "__main__":
    app.run(debug=True)
