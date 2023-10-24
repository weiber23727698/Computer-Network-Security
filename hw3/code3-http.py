from flask import Flask, request, Response
from functools import wraps

app = Flask(__name__)

# Dictionary to store valid usernames and passwords
users = {
    "CNS-user": "CNS-password"
}

# Decorator function for authentication
def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.authorization

        if not auth or not check_credentials(auth.username, auth.password):
            return authenticate_error()
        
        return func(*args, **kwargs)
    
    return wrapper

# Check if the provided credentials are valid
def check_credentials(username, password):
    print(f"username: {username}")
    print(f"password: {password}")
    return username in users and users[username] == password

# Response for authentication error
def authenticate_error():
    return Response(
        "Could not verify your access level for that URL.\n"
        "You have to login with proper credentials", 
        401, 
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

@app.route('/')
@authenticate
def index():
    print("successfullly authenticated")
    return "200"

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="140.112.30.37", port=9701)
    # app.run()
