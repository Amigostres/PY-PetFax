from flask import Flask 


def create_app(): 
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:02132003@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False             

    from . import models
    from flask_migrate import Migrate
    models.db.init_app(app)
    migrate = Migrate(app, models.db)


    # the period means this location
    from . import pet
    from . import fact
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    return app
