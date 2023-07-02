from flask import (Blueprint, render_template)
import json

bp = Blueprint('pet', __name__, url_prefix="/pets")
pets = json.load(open("pets.json"))
# print(pets)


@bp.route('/')
def index(): 
    return render_template("index.html", pets=pets)

@bp.route('/profile/<id>')
def animal_profile(id):
    for pet in pets:
        #so for some reason parameters are a String datatype by default ("bruh")
        if pet['pet_id'] == int(id):
            return render_template("profile.html", pet = pet )

            