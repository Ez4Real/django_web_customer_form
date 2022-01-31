# Install pip first
python get-pip.py

# Then install virtualenv using pip3
pip3 install virtualenvwrapper-win

# Now create a virtual environment
virtualenv venv 

# VENV Activate
.\env\Scripts\activate.bat

Install requirements
pip install -r /path/to/requirements.txt

# Run project
manage.py runserver
