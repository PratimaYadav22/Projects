# LLMtoSQLText

In this project, I have leveraged the capabilities of Gemini LLM (Large Language Model) and Gemini Pro API to facilitate database querying through simple English language inputs. The goal was to enable users to express their queries in plain English, which are then translated into SQL queries by the LLM model. These SQL queries are subsequently executed on the database, and the results are provided to the user.

The project offers a user-friendly interface where individuals can input their queries using natural language. Behind the scenes, Gemini LLM processes these inputs, generates corresponding SQL queries, and interacts with the database using Gemini Pro API to retrieve the desired information.

1) install anaconda
2) create venv using below command.
   
conda create -p venv python==3.12 -y

To activate this environment, use                                                                                                                                                     
   $ conda activate C:\Users\prati\venv                                                                                                                                              

To deactivate an active environment, use
   $ conda deactivate


Additinal Information:
The project has Employees database.
