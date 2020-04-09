from flask import Flask
from flask import render_template, request, redirect

import os
from flask_sqlalchemy import SQLAlchemy

pdir = os.path.dirname(os.path.abspath(__file__))
dbfile = "sqlite:///{}".format(os.path.join(pdir, "book.db"))


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbfile
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Book(db.Model):
    title = db.Column(db.String(89), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {} >".format(self.title)


@app.route("/")
@app.route("/index")
def index():
    return "Hello World!!"


@app.route("/home", methods=["GET", "POST"])
def home():
    if request.form:
      try:
        print(request.form.get("title"))
        book = Book(title=request.form.get("title"))
        db.session.add(book)
        db.session.commit()
        # return redirect('/')
      except Exception as e:
          print('Failed to add book')
          print(e)
    books = Book.query.all()
    return render_template("home.html", books=books)
    # return render_template("home.html")


@app.route("/delete", methods=["POST"])
def delete():
  try:
    deletetitle = request.form.get("deletetitle")
    book = Book.query.filter_by(title=deletetitle).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/home")
  except Exception as e:
          print('Failed to delete book')
          print(e)

@app.route("/update", methods=["POST"])
def update():
  try:
    newtitle = request.form.get("newtitle")
    oldtitle = request.form.get("oldtitle")
    print(newtitle + " old title " + oldtitle)
    book = Book.query.filter_by(title=oldtitle).first()
    book.title = newtitle
    db.session.commit()
    return redirect("/")
  except Exception as e:
          print('Failed to Update book')
          print(e)

if __name__ == "__main__":
    app.run(debug=True)
