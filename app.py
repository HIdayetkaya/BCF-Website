from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('home.html', title="Home")

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html', title="About Us")

if __name__ == '__main__':
    app.run(debug=True)
