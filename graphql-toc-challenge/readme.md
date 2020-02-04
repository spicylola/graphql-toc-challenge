Getting started
---------------
To do this project, you will need to install Python3, Pip3.

First you'll need to get the source of the project.

```bash
# Get the example project code
git clone https://github.com/spicylola/graphql-toc-challenge.git
cd graphql-toc-challenge
```

```bash
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



