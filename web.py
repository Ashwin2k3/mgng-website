from flask import Flask, render_template

web = Flask(__name__)

@web.route("/")
def website():
    return render_template("home.html")

if __name__ =="__main__":
    web.run(debug = True)