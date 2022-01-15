from flask import Flask,render_template,request
import os
import re
import json
import psycopg2

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("animation.html")

@app.route('/ynapmoc_amina')
def anima_comapny():
    print("in company")
    herokuCLI_command = 'heroku config:get DATABASE_URL -a anima-database-fe'
    DATABASE_URL = os.popen(herokuCLI_command).read()[:-1]

    # connect with database
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    # create cursor
    cursor = conn.cursor()

    # set SQL create table
    SQL_create_command = """
    SELECT * from anima_company
    """

    # execute SQL
    cursor.execute(SQL_create_command)
    data = cursor.fetchall()
    print(data[0][0])
    print(type(data[0]))
    print("in company!!!!")

    #print("in year")

    # commit change of database
    conn.commit()

    # close cursor
    cursor.close()
    # close connect
    conn.close()
    #return render_template("anima_company.html", data=data)
    return render_template("anima_company.html",data = json.dumps(data))

@app.route('/reaY')
def year():
    print("in year")
    herokuCLI_command = 'heroku config:get DATABASE_URL -a anima-database-fe'
    DATABASE_URL = os.popen(herokuCLI_command).read()[:-1]

    # connect with database
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    # create cursor
    cursor = conn.cursor()

    # set SQL create table
    SQL_create_command = """
    SELECT * from animation
    """
    # execute SQL
    cursor.execute(SQL_create_command)
    data = cursor.fetchall()
    #print(data)
    #print(type(data))

    # commit change of database
    conn.commit()

    # close cursor
    cursor.close()
    # close connect
    conn.close()
    #return render_template("year.html",data = data)
    return render_template("year.html",data=json.dumps(data))

if __name__ == '__main__':
    app.run()

