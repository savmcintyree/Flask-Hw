from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/favorite5')
def favorite5():
    artists = ['Taylor Swift', 'Phoebe Bridgers', 'Conan Gray','Gracie Abrams','Kevin Abstract']
    return render_template('favorite5.html', names=artists)