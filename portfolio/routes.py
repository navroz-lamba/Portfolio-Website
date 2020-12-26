from flask import render_template, request
from . import app 
from . import helper


@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():

    greeting = 'Welcome to My Data Science Portfolio Website'

    return render_template('/index.html',
                            greeting=greeting)


@app.route('/about', methods=['POST', 'GET'])
def about_en():

    if request.method == "POST":
      
        title_text = helper.get_title_content('about')

        skills = helper.get_skill_content()

        return render_template('/about.html',
                                title_text=title_text,
                                skills=skills,
                                title="ABOUT ME",
                                id="about")
