import pandas as pd
import numpy as np
import psycopg2
import os
from dotenv import load_dotenv

# to the credentials from .env
load_dotenv()

# read in all necessary Excel files
titles_en_df = pd.read_excel("database/titles_db_en.xlsx", engine='openpyxl')
portfolio_en_df = pd.read_excel("database/portfolio_db_en.xlsx", engine='openpyxl')
skills_en_df = pd.read_excel("database/skills_db_en.xlsx", engine='openpyxl')


# connect and create tables if they don't exist yet
DATABASE_URL = os.getenv('DATABASE_URL_heroku')
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS titles_en \
            (id SERIAL, page text, content text)")

cur.execute("CREATE TABLE IF NOT EXISTS portfolio_en \
            (id SERIAL, title text NOT NULL, description text, skills text, \
             image text, code text, blog_post text, project text, date date, tag text)")

cur.execute("CREATE TABLE IF NOT EXISTS skills_en \
            (id SERIAL, topic text, skills text, level integer, tooltip text)")

# select everything from the titles_en database
cur.execute("TRUNCATE titles_en RESTART IDENTITY")

for titles_en_row in titles_en_df.itertuples():
    cur.execute("INSERT INTO titles_en (page, content) VALUES (%s, %s)",
                [titles_en_row.page, titles_en_row.content])
    conn.commit()

# select everything from the portfolio database
cur.execute("TRUNCATE portfolio_en RESTART IDENTITY")

for portfolio_row in portfolio_en_df.itertuples():
    cur.execute("INSERT INTO portfolio_en (title, description, skills, image, code, blog_post, tag) \
                VALUES (%s, %s, %s, %s, %s, %s, %s)",
                [portfolio_row.title, portfolio_row.description,
                 portfolio_row.skills, portfolio_row.image, portfolio_row.code,
                 portfolio_row.blog_post, portfolio_row.tag])
    conn.commit()

# select everything from the skills database
cur.execute("TRUNCATE skills_en RESTART IDENTITY")

for skills_row in skills_en_df.itertuples():
    cur.execute("INSERT INTO skills_en (topic, skills, level, tooltip) VALUES (%s, %s, %s, %s)",
                [skills_row.topic, skills_row.skills, skills_row.level, skills_row.tooltip])
    conn.commit()

conn.close()