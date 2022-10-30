from flask import Flask, render_template

web = Flask(__name__)

# CONTENT = [
#     {
#         'id': 1,
#         'title': 'Our Services',
#         'body':''
#     },
#     {
#         'id':2,
#         'title': 'OUR SECURITY POLICY'
#         'body':''
#     },
#     {
#         'id':3,
#         'title': 'FACILITIES',
#         'body':''
#     },
#     {
#         'id':4,
#         'title': 'OUR NETWORK & SYSTEMS',
#         'body':''
#     },
#     {
#         'id':5,
#         'title': 'OUR PEOPLE',
#         'body':''
#     },
#     {
#         'id':6,
#         'title': OUR CONFIDENTIALITY,
#         'body':""
#     },
#     {
#         'id':7,
#         'title': 'OUR CURRENT CLIENTELE',
#         'body':''
#     },
#     {
#         'id':8,
#         'title': 'OUR CURRENT FEE MODEL',
#         'body':''
#     }
# ]

@web.route("/")
def website():
    return render_template("home.html")

if __name__ =="__main__":
    web.run(debug = True)