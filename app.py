from flask import Flask, render_template, request
from jinja2 import TemplateNotFound

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.context_processor
def inject_active_path():
    return dict(active_path=request.path)

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        return '<h1>Home</h1><p>Create templates/index.html to customize.</p>'

@app.route('/about')
def about():
    try:
        return render_template('about.html', title='About')
    except TemplateNotFound:
        return '<h1>About</h1><p>Create templates/about.html to customize.</p>'

@app.route('/events')
def events():
    try:
        return render_template('events.html', title='Events')
    except TemplateNotFound:
        return '<h1>Events</h1><p>Create templates/events.html to customize.</p>'

@app.route('/mentors')
def mentors():
    try:
        return render_template('mentors.html', title='Mentors')
    except TemplateNotFound:
        return '<h1>Mentors</h1><p>Create templates/mentors.html to customize.</p>'
    
@app.route('/scholarships')
def scholarships():
    try:
        return render_template('scholarships.html', title='Scholarships')
    except TemplateNotFound:
        return '<h1>Scholarships</h1><p>Create templates/scholarships.html to customize.</p>'    
    
@app.route('/contact')
def contact():
    try:
        return render_template('contact.html', title='Contact')
    except TemplateNotFound:
        return '<h1>Contact</h1><p>Create templates/contact.html to customize.</p>'

if __name__ == '__main__':
    app.run(debug=True)