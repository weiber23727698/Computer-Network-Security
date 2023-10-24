from flask import Flask, request, redirect, make_response, Response

app = Flask(__name__)

# Dictionary to store valid usernames and passwords
users = {
    "CNS-user": "CNS-password"
}

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if check_credentials(username, password):
            response = make_response(redirect('/'))
            response.set_cookie('authenticated', 'true')
            return response
        else:
            response = make_response(redirect('/'))
            response.set_cookie('authenticated', 'false')
            return response

    # Handle GET request
    if request.method == 'GET':
        if request.cookies.get('authenticated') == 'true':
            print("Authenticated successfully!")
            return "200"
        else:
            return Response(
                "Could not verify your access level for that URL.\n"
                "You have to login with proper credentials", 
                401, 
                {'WWW-Authenticate': 'Basic realm="Login Required"'}
            )

# Logout route
@app.route('/logout')
def logout():
    response = make_response(redirect('/login'))
    response.set_cookie('authenticated', '', expires=0)
    return response

# Check if the provided credentials are valid
def check_credentials(username, password):
    print(f"username: {username}")
    print(f"password: {password}")
    return username in users and users[username] == password

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="140.112.30.37", port=8082)
    # app.run()
