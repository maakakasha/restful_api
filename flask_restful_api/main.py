from flask import Flask
from flask_restful import Api, Resource

# initialize Flask instance application
app = Flask(__name__)
api = Api(app)

names = {
        "Mahmoud": {"age": 20, "gender": "male"},
         "Ali": {"age": 21, "gender": "male"},
         }

# creating an inheritence child of Resource
# Resource class for json data
class HelloWorld(Resource):
    def get(self, name):
        return names[name]
    
    def post(self):
        return {"data": "Yuppiii! Posted using post method"}

# creating a route
api.add_resource(HelloWorld, "/helloworld/<string:name>")

# runs the application
if __name__ == "__main__":
    app.run(debug=True)