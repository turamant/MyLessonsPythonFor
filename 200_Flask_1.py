from flask import Flask, jsonify, request

# Initialise the app
app = Flask(__name__)


# Define what the app does
@app.route("/greet/<it>")
def index(it: str):
    response = {"1": "Capture first name & last name",
                "2": "If either is not provided: respond with an error",
                "3": "If first name is not provided and second "
                     "name is provided: respond with \"Hello Mr. <second-name>!\"",
                "4": "If first name is provided but second name"
                     " is not provided: respond with \"Hello, <first-name>!\"",
                "5": "If both names are provided: respond with a "
                     "question, Is your name <fist-name> <second-name>",
                }
    return jsonify(response[it])


@app.get("/greet")
def my_response():
    response = {"1": "Capture first name & last name",
                "2": "If either is not provided: respond with an error",
                "3": "If first name is not provided and second "
                     "name is provided: respond with \"Hello Mr. <second-name>!\"",
                "4": "If first name is provided but second name"
                     " is not provided: respond with \"Hello, <first-name>!\"",
                "5": "If both names are provided: respond with a "
                     "question, Is your name <fist-name> <second-name>",
                }
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
