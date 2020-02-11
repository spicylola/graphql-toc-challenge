Getting started
---------------
To do this project, you will need to install Python3, Pip3.
Getting started if you want this repo locally
---------------
To run locally, you will need to have Python3, Pip3, Postgres, Docker, and Docker-Compose installed.

Make Sure to Download a version of Python 3.4 or greater to already have Pip installed/
***Python3 Installation, download the version for your OS:** https://www.python.org/downloads/

**Pip: It should already come with your Python installation.** 


First you'll need to get the source of the project.

```bash
# Get the example project code
git clone https://github.com/spicylola/graphql-toc-challenge.git
cd graphql-toc-challenge
```

```bash
pip install virtualenv
pip install --upgrade pip
alias python=/usr/local/bin/python3
python3 -m pip install --upgrade --force pip
# Create a virtualenv in which we can install the dependencies
virtualenv venv
source venv/bin/activate
```

Now we can install our dependencies:

```bash
pip install -r requirements/base.txt
```

```bash
cd graphql-toc-challenge
export FLASK_APP=__init__.py
flask run
```


Now head on over to
[http://127.0.0.1:5000/graphql](http://127.0.0.1:5000/graphql)

and run queries!

For this Challenge, You will do a Graphql query and Mutation!
------------------
Query Challenge:
You will have the opporunity to generate good fortune to some lucky client! In order to do this, in /graphql-toc-challenge/schema.py, you will create a resolver method in the Query object, that will pick three random fortune quotes from the fortunes.txt file and return this as a response to the client.  There is already an example provided for you that returns the entire list of fortune quotes. 
Good Resource for random sample function in Python:
https://www.geeksforgeeks.org/python-random-sample-function/

**BONUS** Mutation Challenge:
You will modify the Bootstrap Cover template to display your new fortune. You can do this by mutating the h1 tag in the HTML file and any html element with the class "lead". 

GOOD LUCK!



