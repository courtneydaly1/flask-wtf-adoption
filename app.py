"""Flask app"""

from flask import Flask, url_for, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app= Flask(__name__)

app.config['SECRET_KEY']= 'shhhSecret!'
app.config["SQLALCHEMY_DATABASE_URI"]= "postgresql:///pet_adoption"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False

connect_db(app)
db.create_all()

toolbar=DebugToolbarExtension(app)


"""Routes"""

@app.route('/')
def list_of_pets():
    
    pets= Pet.query.all()
    
    return render_template('pet_list.html', pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet"""
    
    form = AddPetForm()
    
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet= Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        
        flash(f"{new_pet.name} has been added!")
        return redirect(url_for('list__of_pets'))  
    else:
        return render_template("add_pet_form.html", form=form)  
    
@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    """edit an existing pet"""
    
    pet= Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.notes= form.notes.data
        pet.photo_url=form.photo_url.data
        pet.available=form.available.data
        db.session.commit()
        
        flash (f"{pet.name} has been updated!")
        
    else:
        return render_template('edit_pet_form.html', form=form, pet=pet)
    
@app.route('/api/pets/<int:pet_id>', methods=['POST'])
def get_pet_api(pet_id):
    """get info on oet through JSON"""
    
    pet=Pet.query.get_or_404(pet_id)
    info= {'name':pet.name, "age":pet.age}
    
    return jsonify(info)
        
                
        
        

