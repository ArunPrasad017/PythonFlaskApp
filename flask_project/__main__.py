from flask_project.app import app

from flask_project import routes, models, oauth

"""
app.run(debug=True, host='flaskexample.com', ssl_context=(
    '/Users/aralagarsamy/Documents/python_project/stefano/stefano_base/Python-Project/flask_project/server.crt', 
    '/Users/aralagarsamy/Documents/python_project/stefano/stefano_base/Python-Project/flask_project/server.key')
)
"""

app.run(debug=True, host='flaskexample.com')