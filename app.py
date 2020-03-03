from flask import Flask, render_template, request
from datetime import datetime
import forms
import mysql.connector
import copy

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost", database="formdata1", user="root", password="pr09r4mm3r"
)
mycursor = mydb.cursor(buffered=True)


@app.route("/form1", methods=["GET", "POST"])
def form1():
    form = forms.Form1Form()
    # if form is submitted
    if form.validate_on_submit():

        timestamp = datetime.now()
        # deepcopy the data to remove csrf_token
        data = copy.deepcopy(form.data)
        data.pop("csrf_token")

        # for creating the new columns
        for name in data.keys():
            try:  # check if the column_name is already in table
                mycursor.execute(f"SELECT {name} from `form1`;")
                mycursor.fetchone()
            except:  # if error | no column in table | create it | NOTE: varchar(15) => reduced the size for memory overflow
                mycursor.execute(f"ALTER TABLE `form1` add {name} varchar(20);")

        # insert into the table
        names = data.keys()
        values = data.values()

        mycursor.execute(
            f"INSERT INTO form1 ({', '.join(names)}) VALUES {tuple(values)};"
        )
        mydb.commit()

        # success message
        return "success"

    # sql1 = "select id from complaints_table order by no_of_complaints DESC limit 3;"
    # mycursor.execute(sql1)
    # records = mycursor.fetchall()
    # for GET request
    records = (0, 1, 2)
    return render_template("form1.html", form=form, records=records)


@app.route("/form2", methods=["GET", "POST"])
def form2():
    form = forms.Form2Form()

    # if form is submitted

    if form.validate_on_submit():
        # breakpoint()
        timestamp = datetime.now()
        # deepcopy the data to remove csrf_token
        data = copy.deepcopy(form.data)
        data.pop("csrf_token")

        # for creating the new columns
        for name in data.keys():

            try:  # check if the column_name is already in table
                mycursor.execute(f"SELECT {name} from `form2`;")
                mycursor.fetchone()
            except:  # if error | no column in table | create it | NOTE: varchar(15) => reduced the size for memory overflow
                mycursor.execute(f"ALTER TABLE `form2` add {name} varchar(15);")

        # insert into the table
        names = data.keys()
        values = data.values()

        mycursor.execute(
            f"INSERT INTO form2 ({', '.join(names)}) VALUES {tuple(values)};"
        )
        mydb.commit()

        # success message
        return "success"
    # breakpoint()
    # for GET request
    return render_template("form2.html", form=form)


@app.route("/form3", methods=["GET", "POST"])
def form3():
    form = forms.Form3Form()
    # if form is submitted
    if form.validate_on_submit():
        timestamp = datetime.now()
        # deepcopy the data to remove csrf_token
        data = copy.deepcopy(form.data)
        data.pop("csrf_token")

        # for creating the new columns
        for name in data.keys():

            try:  # check if the column_name is already in table
                mycursor.execute(f"SELECT {name} from `form3`;")
                mycursor.fetchone()
            except:  # if error | no column in table | create it | NOTE: varchar(15) => reduced the size for memory overflow
                mycursor.execute(f"ALTER TABLE `form3` add {name} varchar(15);")

        # insert into the table
        names = data.keys()
        values = data.values()

        mycursor.execute(
            f"INSERT INTO form3 ({', '.join(names)}) VALUES {tuple(values)};"
        )
        mydb.commit()

        # success message
        return "success"

    # for GET request
    return render_template("form3.html", form=form)


if __name__ == "__main__":
    app.secret_key = "secret"
    app.run(debug=True)
