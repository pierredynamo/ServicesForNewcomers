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


**Steps to run the project:**  
**Step One:** download and _extract/unzip_ the **ServicesForNewcomers** folder.    
**Step Two:** Open your _VScode editor_ and navigate to the **ServicesForNewcomers** folder.    
**Step Three:** type the command "_python -m venv venv_" # This will create the virtual environment with folder name venv.  
**Step Four:** type the command "_venv\Scripts\activate_" and press Enter key on the keyboard #_This will activate the virtual environment._   
**Step Five:** type "_python -m pip install Django_" # This will install Django Framework.  
**Step Six:** type "_cd Agenda_" and press Enter key on the keyboard # _This will change the directory to the appplication folder._    
**Step Seven:** type "_python manage.py makemigrations Agenda._"  and press Enter key on the keyboard.  
**Step Eight:** type "_python manage.py migrate._"  and press Enter key on the keyboard.  
**Step Nine:** type "_python manage.py runserver 8080_" press Enter key on the keyboard # _This will make the project to run on port 8080._    

**The result on your command line will look like be as follows:**  
PS C:\FormationDjango\ServicesForNewcomers\> python -m venv venv  
PS C:\FormationDjango\ServicesForNewcomers\> venv\Scripts\activate  
(venv) PS C:\FormationDjango\ServicesForNewcomers\> python -m pip install Django  
Collecting Django  
  Obtaining dependency information for Django from https://files.pythonhosted.org/packages/50/1b/7536019fd20654919dcd81b475fee1e54f21bd71b2b4e094b2ab075478b2/Django-5.0.2-py3-none-any.whl.metadata  
  Downloading Django-5.0.2-py3-none-any.whl.metadata (4.1 kB)  
Collecting asgiref<4,>=3.7.0 (from Django)  
  Obtaining dependency information for asgiref<4,>=3.7.0 from https://files.pythonhosted.org/packages/9b/80/b9051a4a07ad231558fcd8ffc89232711b4e618c15cb7a392a17384bbeef/asgiref-3.7.2-py3-none-any.whl.metadata  
  Using cached asgiref-3.7.2-py3-none-any.whl.metadata (9.2 kB)  
Collecting sqlparse>=0.3.1 (from Django)  
  Obtaining dependency information for sqlparse>=0.3.1 from https://files.pythonhosted.org/packages/98/5a/66d7c9305baa9f11857f247d4ba761402cea75db6058ff850ed7128957b7/sqlparse-0.4.4-py3-none-any.whl.metadata  
  Downloading sqlparse-0.4.4-py3-none-any.whl.metadata (4.0 kB)  
Collecting tzdata (from Django)
  Obtaining dependency information for tzdata from https://files.pythonhosted.org/packages/65/58/f9c9e6be752e9fcb8b6a0ee9fb87e6e7a1f6bcab2cdc73f02bb7ba91ada0/tzdata-2024.1-py2.py3-none-any.whl.metadata  
  Downloading tzdata-2024.1-py2.py3-none-any.whl.metadata (1.4 kB)  
Downloading Django-5.0.2-py3-none-any.whl (8.2 MB)  
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.2/8.2 MB 4.0 MB/s eta 0:00:00  
Using cached asgiref-3.7.2-py3-none-any.whl (24 kB)  
Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)  
Downloading tzdata-2024.1-py2.py3-none-any.whl (345 kB)  
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 345.4/345.4 kB 4.3 MB/s eta 0:00:00  
Installing collected packages: tzdata, sqlparse, asgiref, Django  
Successfully installed Django-5.0.2 asgiref-3.7.2 sqlparse-0.4.4 tzdata-2024.1  
 
(venv) C:\FormationDjango\ServicesForNewcomers\> python manage.py makemigrations Agenda  
(venv) C:\FormationDjango\ServicesForNewcomers\> python manage.py migrate   
(venv) C:\FormationDjango\ServicesForNewcomers\> python manage.py runserver 8080   

System check identified no issues (0 silenced).  
February 19, 2024 - 14:20:19  
Django version 5.0.2, using settings 'ServicesForNewcomers.settings'  
Starting development server at http://127.0.0.1:8080/  
Quit the server with CTRL-BREAK.    

**Your web browser will display the following message:**

"Services for newcomers available soon ..."
