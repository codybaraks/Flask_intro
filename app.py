from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/team')
def Team():
    return render_template('Team.html')

@app.route('/connect')
def Connect():
    return  render_template('Connect.html')

@app.errorhandler(404)
def error_page(e):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
