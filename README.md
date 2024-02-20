# Services For Newcomers
# Developed by Pierre Dynamo Fotsing
This apllication runs on Python 3.12, Django 5.0 Framework. Sqlite3(later will be changed to MySQL server 8.3.0) database in the back-end and HTML, and CSS in the front-end.  

**Features:**  
The project is called online services for newcomers. It is and agenda and consist of the following features  
=>**Home page** that contains general information about the system.   
=>**Client page** – In this feature, the user (a newcomer) can register personal information.   
=>**Service page** – In this feature, the user (a newcomer) can choose services.   
=>**Appointment page** – In this feature, the user (a newcomer) can choose the available dates based on the selected services.   
=>**Appointments list page** – This feature, will provide an itemize list of appointments registered in the system.   
=>**Login/Logout System** – With this feature, the user can log-in and log-out of the system.   


**Steps to run the project on Windows:**

**Step One:** download and `extract/unzip` the **ServicesForNewcomers** folder.

**Step Two:** type the command `cd C:\FormationDjango\ServicesForNewcomers` change the current folder to the **ServicesForNewcomers** folder.

**Step Three:** type the command `pip install vitualenv` # This will install a virtual environment.

**Step Four:** type the command `_vitualenv venv_` # This will create the virtual environment with folder name venv.

**Step Five:** type the command `venv\Scripts\activate` # This will activate the virtual environment called venv.

**Step Six:** type `pip install django` # This will install Django Framework.

**Step Seven:** stay in the **ServicesForNewcomers** folder and type the command `code .` this will open VScode editor.

**Step Eight:** stay in the **ServicesForNewcomers** folder type `python manage.py makemigrations Agenda`  and press Enter key on the keyboard.

**Step Nine:** stay in the **ServicesForNewcomers** folder type `python manage.py migrate`  and press Enter key on the keyboard.

**Step Ten:** type `python manage.py runserver 8080` press Enter key on the keyboard # This will make the project to run on port 8080.    


**The result on your command line will look like be as follows:**  
(base) PS C:\FormationDjango\ServicesForNewcomers> virtualenv venv
created virtual environment CPython3.11.5.final.0-64 in 1205ms
  creator CPython3Windows(dest=C:\FormationDjango\ServicesForNewcomers\venv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\HP\AppData\Local\pypa\virtualenv)
    added seed packages: pip==23.3.2, setuptools==69.0.3, wheel==0.42.0
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
(base) PS C:\FormationDjango\ServicesForNewcomers>

(base) PS C:\FormationDjango\ServicesForNewcomers> venvs/Scripts/activate
(base) (venv) PS C:\FormationDjango\ServicesForNewcomers>

(base) (venv) PS C:\FormationDjango\ServicesForNewcomers> code .

(base) (venv) PS C:\FormationDjango\ServicesForNewcomers> python manage.py makemigrations Agenda
No changes detected in app 'Agenda'
(base) (venv) PS C:\FormationDjango\ServicesForNewcomers> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
(base) (venv) PS C:\FormationDjango\ServicesForNewcomers>

(base) (venv) PS C:\FormationDjango\ServicesForNewcomers> python manage.py runserver 8080
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 19, 2024 - 22:57:01
Django version 5.0.2, using settings 'ServicesForNewcomers.settings'
Starting development server at http://127.0.0.1:8080/
Quit the server with CTRL-BREAK.

[19/Feb/2024 22:57:19] "GET / HTTP/1.1" 200 53
Not Found: /favicon.ico
[19/Feb/2024 22:57:19] "GET /favicon.ico HTTP/1.1" 404 2237    

**Your web browser will display the following message:**

"Services for newcomers available soon ..."
