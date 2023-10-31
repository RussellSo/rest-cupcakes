from flask import Flask, render_template, request, jsonify, redirect
import requests
from models import SQLAlchemy, connect_db, db, Cupcake
from forms import addCupcake

app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///cupcakes_db'
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.config["SQLALCHEMY_ECHO"] = True
connect_db(app)
app.config['SECRET_KEY'] = 'cupcakes'

#note: essentially - returning a list of objects - objects were returned from a serialize instance method
@app.route('/')
def home():
    cupcakes = Cupcake.query.all()
    form = addCupcake()

    return render_template('index.html', cupcakes=cupcakes, form=form)

@app.route('/api/cupcakes')
def get_cupcakes_list():
    """ api with full database of cupcakes"""
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(all_cupcakes)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    """ api route that retrieves a single cupcake"""

    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=['POST'])
def add_cupcake():
    flavor= request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']

    # form = addCupcake()

    # if form.validate_on_submit():
    #     flavor = form.flavor.data
    #     size = form.size.data
    #     rating = form.rating.data
    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating)
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake = new_cupcake.serialize())
    return(response_json, 201)

@app.route('/api/cupcakes/<int:id>', methods =['PATCH'])
def edit_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)

    # db.session.query(Cupcake).filter_by(id=id).update(request.json) ## request.json is a dictionary - updates whole obj but throws error is new info is added

    cupcake.flavor = request.json.get('flavor', cupcake.flavor) # if flavor was updated, then get that. otherwise set it to what i was defaulted at.
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id).delete()
    return jsonify({'msg': "deleted"})


