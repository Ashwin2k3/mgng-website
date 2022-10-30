from flask import Flask

web = Flask(__name__)

@web.route("/")
def website():
    return "mgng"

if __name__ =="__main__":
    web.run(debug = True)