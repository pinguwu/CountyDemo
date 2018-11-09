from flask import Flask, url_for, render_template, request, flash, Markup
import os
import json

app = Flask(__name__)


@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    try:
        stateSelected = request.args["states"]
        print(stateSelected)
        return render_template("index.html", states = get_state_options(counties), fun_fact = get_fun_fact(stateSelected))
    except:
        return render_template("index.html", states = get_state_options(counties))


def get_state_options(counties):
    los = []
    #is this los | |i || |_
    for county in counties:
        state = county["State"]
        TrueFalse = state in los
        if (TrueFalse == False):
            los.append(state)

    options = ""
    for state in los:
        options += Markup("<option value=\"" + state + "\">" + state + "</option>")


    return options

def get_fun_fact(states):
    state = states

    with open('county_demographics.json') as list_o_things:
        info = json.load(list_o_things)

        #highest median income i guess lmao

    most_under = info[0]["County"]
    state_most_under = info[0]["State"]
    percent = info[0]["Income"]["Median Household Income"]
    loas = {}
    for x in info:
        if (x["Income"]["Median Household Income"] > percent):
            most_under = x["County"]
            state_most_under = x["State"]
            percent = x["Income"]["Median Household Income"]
            loas[state_most_under] = percent
    
    return "This state has a median household income of: " + str(loas.get(state))


if __name__=="__main__":
    app.run(debug=True, port=36090)
