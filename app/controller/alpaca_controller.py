from flask import render_template, jsonify, json

# as the models file contains all the models, import what you need
from app.models import Alpaca, alapaca_model

class AlpacaController(object):

    # TODO: Implement Index
    # WHAT: Grabs data from model and uses it to display the relevant
    # alpacas from the database
    # CONDITIONS: If user specifies sex, then must filter the list
    # RETURN: Return formatted Alpaca's to use for the view
    def index(self, sex=None):
        results = alapaca_model.get_all(sex)
        return render_template("index.html", results=results, sex=sex)
    
    # TODO: Implement Profile
    # WHAT: Grabs the relevant Alpaca from the model and uses it to
    # display the profile for that alpaca from the database
    # RETURN: Return formatted Alpaca to use for the view
    def profile(self, name):
        results = alapaca_model.get(name)
        return render_template("profile.html", results=results, contact=json.dumps(results['contact']), hobbies=results['hobbies'])
    # TODO: Implement Search
    # WHAT: Uses the data recieved to find the Alpaca from the data
    # CONDITIONS: If user specifies nothing you can return everything or nothing!
    # that part if determined by you however if something is specified, it must
    # be a filtered list of alpacas
    # RETURN: Return formatted alpacas as a list using the
    # search criteria
    def search(self):
        pass

    # TODO: Implement Create
    # WHAT: Uses the data recieved to create an Alpaca model
    # REQUIREMENTS: Make a 'fake' save function in Alpaca that
    # Prints saving alpaca and then list the information recieved
    # and then give back a message stating what was saved
    # i.e Fred was created!
    # CONDITIONS:
    # RETURN: Return formatted message using the relevant information
    def create(self, name, sex, bio, dName, age, hobbiesList, contactList):
        alpaca = Alpaca(name, sex, bio, dName, age, hobbiesList, contactList)
        data = {'message': "successfully created the following user: " + name}
        print('saving alpaca', name, sex, bio, dName, age, hobbiesList, contactList)

        return jsonify(data)

    # TODO: Implement Delete
    # WHAT: Uses the data recieved to find the Alpaca from the data
    # and then deletes it
    # REQUIREMENTS: Make a 'fake' delete function in Alpaca that
    # Prints the alpaca that will be delted followed by deleting alpaca
    # and then list the information recieved and then give back a
    # message stating what was saved i.e Fred was deleted!
    # CONDITIONS:
    # RETURN: Return formatted message using the relevant information
    def delete(self):
        pass
    
alpaca_controller = AlpacaController()