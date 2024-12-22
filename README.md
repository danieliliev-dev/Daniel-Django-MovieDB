### Movie Database Application (using Django framework)
---------------------------------------------------------------------------------------------------------------------------------------------------------
Hello and welcome to the movie database application! 

- This will be a different README than most, made for people with little experience with Python in general, thus containing more details and information, answering first to WHY and then HOW the project is made,
because if you find out WHY, you will manage to deal with the HOW :)
This project is built using Django framework from Python, SQLite as database and using a bit of HTML (hypertext markup language), WSGI (web server gateway interface and ASGI (asynchronous server gateway interface).

- Why Django, Why SQLite? Django follows the "batteries-included" philosophy, which means it comes with a lot of built-in functionality out of the box. This includes admin panel, database ORM (Object-Relational Mapping),
Forms Handling, URL (uniform resource locator) routing, Security Features: Built-in protections against common web vulnerabilities (like SQL injection, cross-site scripting (XSS), cross-site request forgery (CSRF), clickjacking, etc.

- This README will guide you through the installation processes, setting up the IDE (integrated developer environment) and eventually running the project.
Main purpose is to allow users to manage a movie database endpoints with features like viewing lists, searching, adding, and categorising movies.

---------------------------------------------------------------------------------------------------------------------------------------------------------

### 1. Prerequisites
Before starting, you will need the following:
- A computer with running operating system Windows, macOS, or Linux
- An active internet connection to download necessary packages
- Enough hard drive space and RAM to run the PyCharm app that we will use (See Section 2 for each OS and official link of producer JetBrains for exact specifications for all versions)

---------------------------------------------------------------------------------------------------------------------------------------------------------

### 2. Installing PyCharm (preferred IDE)
PyCharm is a form of Integrated Development Environment (IDE) used for Python development. Follow these steps to install PyCharm.
For free use - install the community edition:
PyCharm archived versions: https://www.jetbrains.com/pycharm/download/other.html
- Important notice - older versions of operating systems need older version of PyCharm - ex. Windows 7 and below can only run PyCharm 2019.3.5 and earlier versions
# For Windows:
-	Download PyCharm from PyCharm's official website.
-	Run the installer and follow the instructions. The default installation settings should be fine for most users.
-	After installation, launch PyCharm.
# For macOS:
-	Download PyCharm from PyCharm's official website.
-	Open the downloaded .dmg file and drag PyCharm to the Applications folder.
-	Open PyCharm from the Applications folder.
-	NOTE - you can run the same Python code on both Windows and Mac. You will need to create separate virtual environments on each:  https://docs.python.org/3/using/mac.html#
# For Linux:
-	Download PyCharm from PyCharm's official website.
-	Extract the .tar.gz archive and run the pycharm.sh script from the terminal to start PyCharm.
  
---------------------------------------------------------------------------------------------------------------------------------------------------------

### 3. Setting Up Your Python Environment
You will need to set up a Python environment to run the Django project. Here's how to do it:
3.1. Install Python (If not already installed)
Windows and macOS: Download and install Python from python.org
Linux (Ubuntu): Install Python using the following command in the terminal:
```sudo apt-get install python3 python3-pip```

### !!!VERY IMPORTANT!!!

Make sure to check the box that says "Add Python to PATH" during installation!
Otherwise when trying to install packages like pip you will encounter issues like: “not recognised as the name of a cmdlet, function, script file,
or operable program” and you will either have to reinstall the IDE or set the path manually to the for the environment variables. Here is how to do it on Windows:
Press Windows + R to open the Windows Run prompt.
- Type in ```sysdm.cpl``` and click OK.
- Open the Advanced tab and click on the Environment Variables button in the System Properties window.
- The Environment Variables window is divided into two sections. The sections display user-specific and system-wide environment variables. To add a variable, click the New… button under the appropriate section.
- Enter the variable name and value in the New User Variable prompt and click OK.

3.2. Install Virtualenv (Recommended)
Using a virtual environment ensures that you manage your project's dependencies separately from your global Python environment.

Why is installing a separate virtual environment important? Main reasons are:

3.2.1 Avoiding Dependency Conflicts
Each project may require different versions of libraries. By using a virtual environment, you isolate each project’s dependencies,
ensuring that updates or changes in one project’s dependencies do not break or interfere with others. Without virtual environments,
different projects could end up using incompatible versions of the same package.

3.2.2. Reproducibility
With a virtual environment, you can freeze the exact versions of dependencies you’re using into a requirements.txt file.
This makes it easy for others (or for you, at a later date) to recreate the same environment on another machine, ensuring that the project behaves exactly as it did originally.

3.2.3. Cleaner Global Environment
Without a virtual environment, installing packages globally can clutter your system's Python installation. Some packages may even require administrative access to install globally.
Virtual environments help keep your global environment clean and prevent any unnecessary changes to system-wide packages.

3.2.4. Easy Dependency Management
Managing dependencies in a virtual environment is more streamlined. You can install, update, or remove dependencies specific to a project without affecting the rest of the system.
It also makes it easier to manage different Python versions across different projects.

3.2.5. Collaboration
When collaborating with others, using a virtual environment ensures that everyone is working with the same dependencies and versions.
This reduces the chances of "it works on my machine" issues and makes the setup process for new contributors easier.

3.2.6. Security
By isolating project dependencies, you limit the exposure of a potential security vulnerability in a specific package to only the project that uses it. It minimizes the risk of a compromised global Python environment.
In summary, virtual environments provide better control over dependencies, maintain system stability, and allow for greater flexibility and collaboration when working on Python projects.

So, how to set up this virtual environment in our case with Pycharm?
3.2.6.1.Open your terminal (or PyCharm terminal)
3.2.6.2.Install virtualenv:
```pip install virtualenv```
3.2.6.3.Create a new virtual environment in your project folder:
```virtualenv venv```
3.2.6.4.Activate the virtual environment:
o	For Windows:
```venv\Scripts\activate```
o	For macOS/Linux:
```source venv/bin/activate```

---------------------------------------------------------------------------------------------------------------------------------------------------------

### 4. Setting Up the Django Project
4.1. Clone or Download the Project
Download or clone the repository containing the Django project files. If you have Git installed, you can clone it directly to your computer:
```git clone https://github.com/danieliliev-dev/moviedb.git```
```cd moviedb```
4.2. Install Project Dependencies
With your virtual environment active, install the necessary dependencies using pip:
```pip install django```
Otherwise you can go to the trigger button on top right on PyCharm (IDE and project settings > Settings > Python interpreter > and here add pip and Django with the plus icon.
If installed correctly in the Python packages tab you should be able to see Django, pip, asgrief and sqlparse.
For full documentation on installation of Django check here: https://docs.djangoproject.com/en/5.1/intro/install/

---------------------------------------------------------------------------------------------------------------------------------------------------------

### 5. Setting Up the Database
5.1.Apply Migrations
Django uses migrations to create the database schema. To set up the database, run the following command:
```python manage.py migrate```
5.2.Create a Superuser / Root User / Admin
To access the Django admin panel and manage the movies, create a superuser account by running the following command:
```python manage.py createsuperuser```
Follow the prompts to create your admin username, email, and password.

---------------------------------------------------------------------------------------------------------------------------------------------------------

### 6. Running the Project and starting the Development Server
Once your environment is set up, you can run the Django development server:
```python manage.py runserver```
This will start the server at http://127.0.0.1:8000/. Open this URL in your browser to see the application running.

Why do we see exactly this http://127.0.0.1:8000/ ?

When you see 127.0.0.1:8000 in your browser while developing a Django project, it refers to your local development server running on your own computer. Let’s break down what each part means:
127.0.0.1 (IP Address)
•	127.0.0.1 is the loopback IP address (also called localhost), which always refers to your own computer. It's like saying "this machine."
•	This address is used to test or develop applications locally, so when you access 127.0.0.1, you're talking to the server that’s running on your computer.
•	127.0.0.1 and localhost are interchangeable; both direct traffic to your local machine.
:8000 (Port Number)
•	The 8000 part is the port number, which specifies the specific process or application on your computer that should handle the request.
•	When you run a Django development server using the python manage.py runserver command, it by default starts on port 8000. This is why you typically see 127.0.0.1:8000.
•	Ports are used to identify specific services on a machine. For example, port 80 is commonly used for HTTP (web) traffic, but Django’s development server uses port 8000 by default.
•	You can change the port number by specifying it when starting the server, e.g., python manage.py runserver 8080, and then your URL would look like 127.0.0.1:8080.

Putting It Together:
When you see 127.0.0.1:8000:
•	127.0.0.1 tells your computer to connect to itself (your local machine).
•	8000 tells it to connect to the web server (Django’s development server) running on that port.
Why is This Used in Django?
When you’re developing with Django, the default web server is a lightweight development server that runs locally on your machine. It allows you to test and interact with your web application in real-time as you make changes.
•	The development server is not meant for production use because it’s not optimized for handling high traffic, but it’s great for building and testing your application on your own computer.
•	When you run python manage.py runserver, it binds to 127.0.0.1:8000 by default.
So, 127.0.0.1:8000 is a local address that Django's development server uses to allow you to view your project as you develop it. You will usually use this address until you're ready to deploy your project to a production server.

---------------------------------------------------------------------------------------------------------------------------------------------------------

### 7. Using the Movie Database Application
7.1. Viewing the movie list(s)
Go to the home page (http://127.0.0.1:8000/) to see a list of all movies in the database.
7.2. Displaying movie details
Click on any movie title to view detailed information, such as the title, description, release date, director, genre, and user ratings.
7.3. Searching movies
You can search for movies by title, director, or genre using the search bar available in the UI.
7.4. Adding movies
Go to the "Add Movie" page (http://127.0.0.1:8000/add/) to add a new movie. You will need to provide details like the movie's title, description, release date, director, genre, and an optional cover image.
7.5. Marking movies as favourites
You can mark a movie as your favourite by clicking on the "Favourite" button on the movie detail page.
7.6. Categorisation (genre, popularity, newest/oldest)
The movie categories page displays movies grouped by "Most Liked,""Newest," and "Genres." You can access the top movies in each category.

---------------------------------------------------------------------------------------------------------------------------------------------------------

### 8. Optional: Admin Panel
If you want to manage movies, users, and other data directly from the web interface, you can access the Django admin panel.
1.	Go to http://127.0.0.1:8000/admin/
2.	Log in with the superuser credentials you created earlier.
3.	You can add, edit, or delete movies from the admin panel.

---------------------------------------------------------------------------------------------------------------------------------------------------------

### 9. Stopping the Server
To stop the development server, press Ctrl + C in the terminal where the server is running.

---------------------------------------------------------------------------------------------------------------------------------------------------------

### 10. Additional Information
### Project Structure:
```
moviedb/
│
├── moviedb/                - Django project folder
│   ├── settings.py         - Project settings
│   ├── urls.py             - URL routing
│   ├── wsgi.py             - WSGI configuration
│   └── asgi.py             - ASGI configuration
│
├── movie/                  - Movie app folder
│   ├── models.py           - Movie model definition
│   ├── views.py            - Views for rendering pages
│   ├── urls.py             - URLs for the movie app
│   ├── templates          - Templates for HTML views
│   ├── static             - Static files (CSS, images)
│   └── forms.py            - Forms for movie creation
│
├── requirements.txt        - List of project dependencies
├── manage.py               - Django project management script
└── db.sqlite3              - SQLite database file
```
---------------------------------------------------------------------------------------------------------------------------------------------------------

### 11. Troubleshooting
If you encounter any issues, consider the following steps:
•	Ensure that you have activated your virtual environment.
•	Double-check that Django is installed in your environment by running pip freeze.
•	If you encounter any errors in the terminal, review the error message carefully. It usually provides helpful information on what's missing or incorrect.
For further Django documentation and help, visit Django's official documentation.
