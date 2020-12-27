from flask import render_template, request
from . import app 
from . import helper


@app.route('/index')
@app.route('/')
def index():
    title_text = helper.get_title_content('index')

    return render_template('index.html',
                            title_text=title_text,
                            title="DATA SCIENCE & MACHINE LEARNING",
                            id="index")


@app.route('/portfolio')
def portfolio():
    # get all projects from the database
    zipped = helper.get_portfolio_content()

    # get the title content for the portfolio page
    title_text = helper.get_title_content('portfolio')

    return render_template('/portfolio.html',
                            title_text=title_text,
                            title="PROJECT PORTFOLIO",
                            id="portfolio",
                            projects=zipped)


@app.route('/about')
def about():
    title_text = helper.get_title_content('about')

    skills = helper.get_skill_content()

    return render_template('/about.html',
                            title_text=title_text,
                            skills=skills,
                            title="ABOUT ME",
                            id="about")
