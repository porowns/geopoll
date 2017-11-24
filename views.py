from flask import Flask, render_template, json, request

from models.table_whisperer import insert_new_user, account_sign_in

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('homepage.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST'])
def signUp():
    # read the posted values
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _pword = request.form['inputPassword']

    # validate values
    if _name and _email and _pword:
        insert_new_user(_name, _email, _pword)
        return json.dumps({'html': '<span>All fields good!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


@app.route('/showSignIn')
def showSignIn():
    return render_template('signin.html')


@app.route('/signIn', methods=['POST','GET'])
def signIn():
    _acc_name = request.form['inputAccName']
    _pword = request.form['inputPassword']

    if _acc_name and _pword:
        account_sign_in(_acc_name, _pword)
        return json.dumps({'html':'<span>All fields good!</span>'})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


if __name__ == '__main__':
    app.run()
