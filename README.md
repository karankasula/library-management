Requirements:
    -   python3.X
    -   Node
    -   yarn

Setup
    The first thing to do is to clone the repository:
    - git clone git@github.com:karankasula/library-management.git
    - cd library-management

Create a virtual environment to install dependencies in and activate it:
    - python3 -m venv venv
    - source venv/bin/activate

Then install the dependencies:
    - pip install -r requirements/base.txt

Migrate the models:
    - python manage.py migrate

Run the server
    - python manage.py runserver


Frontend:
Open seperate terminal:
    cd <project_path>/frontend

Install dependencies
    yarn install

Start Frontend
    yarn dev

Now on browser check http://localhost:8000/