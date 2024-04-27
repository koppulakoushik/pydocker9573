from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import os

app = Flask(__name__)


#app.config['MYSQL_HOST'] = os.environ['mysql_host']
app.config['MYSQL_HOST'] = "mysql"
#app.config['MYSQL_PORT'] = 3706
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "my-secret-pw"
app.config['MYSQL_DB'] = "flaskapp"


mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')
     
if __name__ == '__main__':
    app.run(host="0.0.0.0")