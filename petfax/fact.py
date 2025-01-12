from flask import ( Blueprint, render_template, request, redirect ) 
from . import models

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new')
def new(): 
    return render_template('facts/new.html')




@bp.route('/', methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        submitter = request.form['submitter']
        fact = request.form['fact']

        new_fact = models.Fact(submitter=submitter,fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit()

        return redirect('/facts')

    elif request.method == 'GET':
        results = models.Fact.query.all()
        for result in results:
            print( result.fact_id, result.submitter, result.fact)

        return render_template('facts/index.html', facts = results)


@bp.route('/<factId>', methods=['PUT'])
def put_fact(factId):
    if request.method == 'PUT':
        model = models.Fact.query.get(factId)
        model.submitter = 'updated'
        models.db.session.add(model)
        models.db.session.commit()
