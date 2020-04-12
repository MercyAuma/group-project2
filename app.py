# Flask is a Python web developpement framework to build web applications. It comes with jinja2, a templating language for Python, and Werkzeug, a WSGI utility module.
# PostgreSQL is an open source relational database system which, as its name suggests,
# uses SQL.
# SQLAlchemy is an Object Relational Mapper (ORM), it is a layer between
# object oriented Python and the database schema of Postgres.


import os
from flask import Flask
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from datetime import datetime
from datetime import timedelta

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
from config import (POSTGRES_URL,POSTGRES_USER,POSTGRES_PW,POSTGRES_DB)


# Remove tracking modifications # Enable debugging
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['Debug']=True

# connect to the postgress database
# DB_URL = 'postgresql+psycopg2://postgres:Mercydb1@localhost:{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL


db = SQLAlchemy(app)

engine = create_engine(DB_URL)
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Dataset = Base.classes.Master_Dataset




# create route that renders index.html template

# Your models.py file should include the definition of classes 
# which define the models of your database tables.
#  Such classes inherit from the class db.Model where db is your SQLAlchemy object. 
#  Further, you may want to define models implementing custom methods, 
#  like an home-made __repr__ or a json method to format objects or 
#  export it to json. It could be helpful to define a base model which will lay the ground for all your other models:



@app.route("/")
def index():
# Render_template: This function allows us to display to the user a dynamic web page they can interact with. We can send data to be dyanmically shown on that page via parameters.Request: From Python in some apps it is imperative to retrieve data from a form or querystring. We use request from Flask to do this.
# Mail: Useful for sending email from your Python application using the SMTP protocol.
# Request: From Python in some apps it is imperative to retrieve data from a form or querystring. We use request from Flask to 
    return render_template("index.html")




@app.route("/data")
def data():

   # Create our session (link) from Python to the DB
    session = Session(engine)

    results=session.query(Dataset.state,Dataset.county).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    
    data_list = []
    for row in results:
        data_dict={}
        data_dict["state"] = row.state
        data_dict["county"] = row.county
        data_dict["county_name"]=county_name
        data_dict["Date"] =occurence_date
        data_dict["Confirmed_cases"] =confirmed
        data_dict[ "Confirmed_deaths"] =deaths
        data_dict["recovered"] =recovered
        data_dict["ICU_Beds"] =icu_beds
        data_dict["Populataion"] = population
        data_dict["ID"]=id

        data_list.append(data_dict)
        
        # data_dict["age"] = age
        # data_dict["sex"] = sex
        # data_list.append(data_dict)

        # Create a dictionary from the row data and append to a list of all_passengers
    # all_passengers = []
    # for name, age, sex in results:
    #     passenger_dict = {}
    #     passenger_dict["name"] = name
    #     passenger_dict["age"] = age
    #     passenger_dict["sex"] = sex
    #     all_passengers.append(passenger_dict)

    # return jsonify(all_passengers)



        

    # data = [{

    # "county_id": county,
    # "state_name":state,
    # "county_name":county_name,
    # # "Date":occurence_date,
    # "Confirmed_cases":confirmed,
    # "Confirmed_deaths":deaths,
    # "recovered":recovered,
    # "ICU_Beds":icu_beds,
    # "Populataion": population,
    # "ID":id
    # }]

    # close session
    session.close()

    return jsonify(data_list)

    # return redirect("/")

if __name__ == "__main__":
    app.run()
