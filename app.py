from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import sqlite3
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#use of gemini model and sql query would be the response

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text


def execute_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


prompt=[
    """
    Act like you are an expert in converting the english questions or statement to SQL query!
    The sql database has the name EMPLOYEES and has the following columns -EMPLOYEE_ID INT, NAME VARCGAR(25), DEPT_NAME VARCHAR(25), DESIGNATION VARCHAR(10) 
    \n\n for example- \n Example 1 - how many entries of recorfs are present
    the sql command will be something like this SELECT COUNT(*) FROM EMPLOYEES;
    \n Example 2 - Tell me all the employees whose designation is Tech Lead and department name is Tech,
    The SQL command will be something like this select * from employees where designation ="Tech Lead" and dept_name = "Tech"
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]


#streamlit app

st.set_page_config(page_title="Let's retrieve any SQL query from you English lang")
st.header("Gemini app to retrieve SQL data")

question = st.text_input("Give your English Query here ",key="input")

submit = st.button("Ask the question")

#after clicking on submit

if submit:
    response= get_gemini_response(question,prompt)
    print(response)
    data=execute_sql_query(response,"employees.db")
    st.subheader("The response is: ")
    for row in data:
        print(row)
        st.header(row)


