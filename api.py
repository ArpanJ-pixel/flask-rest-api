from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource,Api,reqparse,fields,marshal_with,abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///database.db'
db=SQLAlchemy(app)
api=Api(app)

class usermodel(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),unique=True,nullable=False)
    email=db.Column(db.String(80),unique=True,nullable=False)

    def __repr__(self):
        return f"User(name={self.name}, email={self.email})"

user_args=reqparse.RequestParser()
user_args.add_argument('name',type=str,required=True,help='Name cannot be blank')
user_args.add_argument('email',type=str,required=True,help='email cannot be blank')

patch_args=reqparse.RequestParser()
patch_args.add_argument('name',type=str)
patch_args.add_argument('email',type=str)

user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String
}

class Users(Resource):
    @marshal_with(user_fields)
    def get(self):
        users=usermodel.query.all()
        return users

    @marshal_with(user_fields)
    def post(self):
        args=user_args.parse_args()
        existing_user=usermodel.query.filter_by(name=args['name']).first()
        if existing_user:
            abort(409,message='name already exist')
        existing_email=usermodel.query.filter_by(email=args['email']).first()
        if existing_email:
            abort(409,message='email already exist')
        user=usermodel(name=args["name"],email=args["email"])
        db.session.add(user)
        db.session.commit()
        users=usermodel.query.all()
        return users,201    #201 is default status for succesful request
    
class User(Resource):
    @marshal_with(user_fields)
    def get(self,id):
        user=usermodel.query.filter_by(id=id).first()
        if not user:
            abort(404,message="user not found")
        return user

    @marshal_with(user_fields)
    def patch(self,id):
            args=patch_args.parse_args()
            user=usermodel.query.filter_by(id=id).first()
            if not user:
                abort(404,message="user not found")
            if args['name'] is None and args['email'] is None:
                abort(400, message="At least one field must be provided")
            if args['name'] is not None:
                existing_user=usermodel.query.filter_by(name=args['name']).first()
                if existing_user and existing_user.id != id:
                    abort(409, message="Name already exists")
                user.name = args['name']
            if args['email'] is not None:
                existing_email=usermodel.query.filter_by(email=args['email']).first()
                if existing_email and existing_email.id != id:
                    abort(409, message="email already exists")
                user.email = args['email']
            db.session.commit()
            return user

    def delete(self,id):
            user=usermodel.query.filter_by(id=id).first()
            if not user:
                abort(404,message="user not found")
            db.session.delete(user)
            db.session.commit()
            return '',204            #for successful deletion
            #200 is default

api.add_resource(Users,'/api/users/')
api.add_resource(User,'/api/users/<int:id>')

@app.route('/')
def home():
    return '<h1> api </h1>'
if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)