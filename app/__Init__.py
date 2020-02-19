from flask import Flask
from manage import app

 app=Flask(__name__)
 app.run(debug=True)