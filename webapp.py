from flask import Flask, url_for, render_template, request
import os
import json

app = Flask(__name__)


@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template("index.html", states = get_state_options(counties))


def get_state_options(counties):
    los = []

    for county in counties:
        state = county["State"]
        TrueFalse = state in los
        if (TrueFalse == False):
            los.append(state)

    options = ""
    for state in los:
        options += Markup("<option value=\"" + state + "\">" + s + "</option>")


    return options





if __name__=="__main__":
    app.run(debug=True, port=36090)
