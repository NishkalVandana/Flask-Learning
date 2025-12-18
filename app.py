from flask import Flask,render_template,request,redirect,url_for,flash
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

app.secret_key="secret"
@app.route('/contact',methods=["GET","POST"])
def contact():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        if not name:
            flash("Name is required")
            return redirect(url_for("contact"))
        if not email:
            flash("Email is required")
            return redirect(url_for("contact"))
        flash("Form submitted successfully")
        return redirect(url_for('success'))
    return render_template("contact.html")
@app.route('/success')
def success():
    return render_template("success.html")
if __name__ == "__main__":
    app.run(debug=True)
