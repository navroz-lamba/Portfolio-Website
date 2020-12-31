from flask import request
import psycopg2
import os
from dotenv import load_dotenv

# to the credentials from .env
load_dotenv()

def fetch_content(content_type):
    '''
    Function to pick the appropriate table in database
    Args: content_type = str; the content that should be queried from the databases
    Returns: df_row = contains results from sql query
    '''
    import dj_database_url
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)   
    # connect to database
    DATABASE_URL = os.getenv('DATABASE_URL_heroku')
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    print(cur)

    # select everything from the titles database
    if content_type == 'title':
        cur.execute("SELECT content FROM titles_en")
        db_row = cur.fetchall()
        # close database connection
        conn.close()
    elif content_type == 'portfolio':
        cur.execute("SELECT * FROM portfolio_en")
        db_row = cur.fetchall()
        # close database connection
        conn.close()
    elif content_type == 'skills':
        cur.execute("SELECT * FROM skills_en")
        db_row = cur.fetchall()
        # close database connection
        conn.close()

    return db_row


def get_title_content(page):
    '''
    Function to get the relevant content for the html page
    Args: page = str; name of the html page
    Returns: title_text = str; content for the html page
    '''
    db_row = fetch_content('title')

    # assign content to variable
    if page == 'index':
        title_text = db_row[0][0]
    elif page == 'portfolio':
        title_text = db_row[1][0]
    elif page == 'about':
        title_text = db_row[2][0]

    return title_text


def get_portfolio_content():
    '''
    Function to get the portfolio projects from the database
    Returns: zipped
    '''

    db_row = fetch_content('portfolio')

    # instantiate a list to save all projects in
    project_list = []
    # iterate through all the projects in the database
    for project in db_row:
        one_project = []
        # add the title, description, skills and image name
        one_project.extend(project[1:5])
        # instantiate list for links
        links = []
        if project[6] != 'NaN':
            links.append(["Web App", project[6]])
        if project[5] != 'NaN':
            links.append(["Code", project[5]])
        one_project.append(links)

        # assign single project to entire project_list
        project_list.append(one_project)

    # create list of lists that contains pairs of projects
    if len(project_list) % 2 == 0:
        pass
    else:
        project_list.append(['placeholder'])
    iterator = iter(project_list)
    zipped = zip(iterator, iterator)

    return zipped


def get_skill_content():
    '''
    Function to get the skills from the database
    Returns: skill_list
    '''

    db_row = fetch_content('skills')

    # instantiate a dict to save all projects in
    skill_dict = {}

    # iterate through all the skills in the database
    for skill in db_row:
        if skill[1] in skill_dict.keys():
            skill_dict[skill[1]].append(list(skill[2:5]))
        else:
            skill_dict[skill[1]] = [list(skill[2:5])]

    return skill_dict

# def get_privacy_legal_notice():
#     '''
#     Function to get variables necessary for privacy and legal notice pages
#     Args: None
#     Returns: address_one, address_two, email = str
#     '''

#     try:
#         import config
#         address_one = config.address_one
#         address_two = config.address_two
#         email = config.email

#     except:
#         address_one = os.environ['ADDRESS_ONE']
#         address_two = os.environ['ADDRESS_TWO']
#         email = os.environ['EMAIL']

#     return address_one, address_two, email
