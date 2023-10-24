from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "CNS-user": generate_password_hash("CNS-password"),
}

@auth.verify_password
def verify_password(username, password):
    print(f"username: {username}")
    print(f"password: {password}")
    if username in users and \
            check_password_hash(users.get(username), password):
        return "200"
    else:
        return "401"

@app.route('/')
@auth.login_required
def index():
    print("successfullly authenticated")
    return "200"

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="140.112.30.37", port=9701)
    # app.run()