#install flask environment ----------------------------------------------------------------------------
python3 -m venv venv

#activate environment --------------------------------------------------------------------------------
source venv/bin/activate

#install django ----------------------------------------------------------------------------------------
pip3 install django

#check files installed --------------------------------------------------------------------------------
pip freeze

#start project
django-admin startproject config . -------------------------------------------------------------------

#start App ---------------------------------------------------------------------------------------------
python3 manage.py runserver
(all commands are to be run as above after manage.py)

#create structure for project  
 static folder
templates folderimg
css folder
js folder
gitignore

#to create App
python3 manage.py startapp <name of app>

#make sure you create urls.py file inside of the app folder (only if you're going to create vies on it)

#install SQLAlchemy -----------------------------------------------------------------------------------
pip install SQLAlchemy

#site info -------------------------------------------------------------------------------------------
http://127.0.0.1:5000

#Database info

#soft delete - made to deactivate account without deleting it.
is_active:inactive

# Install Crispy Forms

    Run in your terminal -> pip install crispy_bootstrap5

# run pip3 freeze > requirements.txt - this will create a requirements .txt file that shows all the dependancies for your file.

#to create a file to add info to database
python3 manage.py makemigrations --empty posts
