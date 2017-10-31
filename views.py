from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('homepage.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')



if __name__ == '__main__':
    app.run()
