from flask import render_template, request
from . import app 
from . import helper


@app.route('/index')
@app.route('/')
def index_en():
    title_text = helper.get_title_content('index')

    return render_template('index.html',
                            title_text=title_text,
                            title="DATA SCIENCE & Machine Learning",
                            id="index")


@app.route('/about')
def about_en():
    title_text = helper.get_title_content('about')

    skills = helper.get_skill_content()

    return render_template('/about.html',
                            title_text=title_text,
                            skills=skills,
                            title="ABOUT ME",
                            id="about")
