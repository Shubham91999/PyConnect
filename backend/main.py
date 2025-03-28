from flask import request, jsonify
from config import app, db
from model import Contact

# Route to show all the saved contacts in our application
@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all() # 
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

# Route to add a new contact in our application
@app.route("/create_contact", methods=["POST"])
def create_contact():
    # Breaking down the request object into required attributes
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    # Checking for nullness
    if not first_name or not last_name or not email:
        return (jsonify({
            "message": "You must enter first name, last name and email"
        }), 400)

    new_contact = Contact(first_name=first_name, last_name=last_name, email=email) # Create new Contact object if all entered
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "Contact created successfully"}), 201   # Status code 201 (Created) is more specific

# Route to update existing contact, identified by user ID
@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    # Lookout for db record using user_id
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "Contact Not Found!!!"}), 404   # Status code, 404 not found
    
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()

    return jsonify({"message": "User Updated Successfully!!!"}), 200

# Route for deleting contact based on ID
@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"messgae": "Contact Not Found"}), 404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "Contact Deleted Successfully!!!"}), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)

