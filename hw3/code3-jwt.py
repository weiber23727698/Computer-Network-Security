from flask import Flask, request, jsonify, Response
import jwt

app = Flask(__name__)

# Secret key for JWT
app.config['SECRET_KEY'] = 'your_secret_key'

# Dictionary to store valid usernames and passwords
users = {
    "CNS-user": "CNS-password"
}

# Login route
@app.route('/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if check_credentials(username, password):
        print("make token")
        token = jwt.encode({'username': username}, app.config['SECRET_KEY'], algorithm='HS256')
        return token #jsonify({'token': token})
    token = jwt.encode({}, app.config['SECRET_KEY'], algorithm='HS256')
    return Response(
        "Could not verify your access level for that URL.\n"
        "You have to login with proper credentials", 
        401, 
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

# Protected route
@app.route('/', methods=['GET'])
def index():
    print("index")
    token = request.headers.get('Authorization')
    print(token)
    if token != None:
        token = token.split(' ')[-1]
    if token:
        try:
            decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            username = decoded_token['username']
            print(f"Authenticated successfully as {username}")
            return "200"
        except:
            print("QQ")
            return Response(
                "Could not verify your access level for that URL.\n"
                "You have to login with proper credentials", 
                401, 
                {'WWW-Authenticate': 'Basic realm="Login Required"'}
            )

    return Response(
        "Could not verify your access level for that URL.\n"
        "You have to login with proper credentials", 
        401, 
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

# Check if the provided credentials are valid
def check_credentials(username, password):
    print(f"username: {username}")
    print(f"password: {password}")
    return username in users and users[username] == password

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="140.112.30.37", port=8082)
    # app.run()
