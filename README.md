# Recruitersspace
[website] (https://recruitersspace.herokuapp.com)
[recruiter login] (https://recruitersspace.herokuapp.com/login)

Information Capture and Dissemination Environment

Abstract—To establish a recruitment system where the applicants can submit their profile details electronically which can be accessed by the recruiters through a dedicated portal to ease the process of recruitment.
I.	PART I
A.	ARCHITECTURE DESIGN
Architectural design is one of the most integral part of the software system development phase. The architectural design is majorly concerned with how a system is structured and organized. It also takes into account of how the system should behave according to the functional and non-functional requirements.
The architectural model is developed using a block diagram which basically illustrates how the system is organized and structured. The blocks used in the models defined a particular component or part of the system which is then refined into more blocks introduced in them which describes sub-components. The arrows between the blocks define the relationship between the components or the direction of the flow of data between components.
Fig [1] shows the architecture design of our application (recruiter’s space) using UML diagram. 
 ![image](https://user-images.githubusercontent.com/64001052/148626663-0ec4f8fb-478f-4245-98d5-db74fa47dd29.png)


Fig. 1: Architecture design of Recruiter’s space
B.	SOFTWARE PROCESS
The architectural design presented in this delivered is developed on the basis of the system and user requirements that were included in deliverable 1 and deliverable 2. The requirements or functionalities mentioned in the user stories in previous deliverables such as account creation, login, applicant profile view, filter applicant’s profile etc. are used to design this architecture model.
Initially, the applicant is requested to fill a form to create applicant’s profile. Upon successful submission of the form, all the details that the applicant enters is stored into the data base. On the other hand, the recruiter can access all the applicant profiles stored in the database. The recruiter can also filter or sort all the application suitable to the recruiter’s needs. All the above mentioned functionalities are in phase with the user and system requirements mentioned in the previous deliverables
Fig [2] presents the activity diagram of our application (recruiter’s space) which clearly depicts the activities involved in our software system and the data processes.
![image](https://user-images.githubusercontent.com/64001052/148626677-a8bb0d54-3f8c-448a-ad5c-dd8da42577a7.png)

 
Fig. 2: Activity Diagram of Recruiter’s space


C.	ARCHITECTURE DESIGN REVISIONS:
The architecture design and system design of our ICDE application are in parallel with the user and system requirements in the previous deliverables. Therefore, no revisions are applicable to our architecture design.

D.	MVC ARCHITECTURE
 ![image](https://user-images.githubusercontent.com/64001052/148626688-701754d4-6b3e-4b3a-9800-5ff6b51547d2.png)

Fig. 3: MVC Architecture of Recruiter’s space

The Model view controller (MVC) shown in Fig [3] for our application is a software design pattern used for developing user interfaces. It divides the program logic into three interrelated elements. i.e.
●	Model
●	View
●	Controller
MVC separates the architecture component and is designed in order to handle specific development aspects of an application. MVC separates the business logic and presentation layer from each other. Nowadays, MVC architecture is used for both web development and designing mobile applications.

Model:
The model is responsible for getting and manipulating the data, Usually, Model interacts with the database. In our case it is a PostgreSQL database. Model responds to the request from the view and also responds. Model also performs data operations to the data in the database. For example, the recruiter whenever wants to find an applicant from a specific department, he can just apply a filter of the specific department.




View:
View is actually a user interface, it is what the user sees on the web browser and how they interact with the web page. View consists of HTML and CSS along with the dynamic values from the controller, the structure of the data is accessed and the information contained within is used to render the HTML content of the page the user ultimately sees in the browser. In our project we have used the Flask framework for the view components.

Controller:
Controller acts as broker in between the model and view. The controller will request the model to get some data from the database and then the controller will take the data and load it to the view. The data retrieved from the model is usually added to a data structure (like link/dictionary) and structure is what we see in the view. 
Controller takes in user input such as Applicant data or recruiters login credentials. This will happen when the applicant clicks on the submit button after filling out the form or it could happen when the recruiter registers himself which is a post request. 

E.	LAYERED ARCHITECTURE
 ![image](https://user-images.githubusercontent.com/64001052/148626707-d6ce7bea-1ec7-419a-a259-000d31099054.png)

Fig. 4: Layered architecture of Recruiter’s space

In Layer architecture shown in fig [4], layers are stacked on the top of one and another. Layers from top to bottom can communicate with each other. 

In our case we have 4 layered architecture patterns as shown in figure.

1.	User interface layer:
This layer interacts with the applicant and recruiter. Through web applications such as forms, login/sign in for recruiter. It is the top most visible layer in the application. It defines how our application appears to the user. We used the Flask framework for this layer.



2.	User communication layer 
This layer provides the user interface functionality that is delivered through the web browser. It allows applicants to fill the data and recruiter to log-in and sign-in, this layer also ensures that the operations of recruiter and applicant are separated. 

3.	Functionality Layer 
The 3rd layer provides the functionality of the application, for example, a recruiter can Filter the list with any keyword, department, or name. Recruiter can also download CSV by clicking on the generate records button, and there is also an option of statistics where the recruiter can view the statistics of how many students of a particular department or skill set have registered.

4.	Database Layer
Finally, the lowest layer contains tables and data managed by the application. Operations such as search, insert, delete, and update are executed here.

F.	PROS AND CONS OF DESIGN
For the development of Recruiter’s Space, we made some decisions which are:

Database:
From our two options of RDBMS and non-RDMBS, we have opted for PostgreSQL which is an open-source relational database management system. The data is stored in a tabular form and is easy to grasp. Due to its flexible nature, it saves a lot of time in updating values and is simple to use. In case of our ICDE, the details related to each of our applicants are same so the best choice was to use RDBMS. As for PostgreSQL, Heroku directly provides free Postgres service, with a variety of management commands for better control and execution. We just have to provide DATABASE_URL configuration variable to our application configuration. Although they have different pricing options, we are using the standard version which is free of cost.
Also, we are using SqlAlchemy as an ORM so that python classes are easily translated to tables in relational databases.

Framework:
In python, Flask and Django are the two web development frameworks available. We have opted for Flask because it involves minimal coding, is lightweight and is easy to deploy in production. Moreover, to display data on html page, stored in database related to a particular applicant, we have used to jinja templates, available only in Flask. Due to these reasons, Flask was an obvious choice over Django Framework.






Python:
We have chosen python as our programming language because it is an open source language that works with a vast sets of libraries, and all the coding information needed is available on the internet. It is simple and easy to understand and offers dynamic typing capabilities. Mainly, it is used as a backend programming language 

GUI design:
We are using HTML/CSS/BOOTSTRAP for content and layout design of our website.

Message exchange style:
To provide communication standards between computer systems on the web, we are using Representational state transfer which is an architectural style.
We are using GET and POST in our ICDE.

Message exchange format:
Due to its easy use and integration we are using JSON (Java script object notation) format to exchange information between clients and servers.

II.	PART II
A.	SOFTWARE METRICS
The estimation of countable software attributes is called software metrics. Apart from measuring software performance, these metrics also help in estimating productivity and other properties and planning work items. It is one of the methods managements adopts to track software development progress and to set future targets. There are two types of software metrics, internal and external metrics. Internal metrics are of great significance for the developer for example lines of code. While the external metrics include properties like reliability, usability and functionality and is important for the user. Table I shows partition of tasks achieved so far and their metric values. It gives information about task name, Lines of code, granularity level and number of units.

B.	GRANUALITY OF COMPONENTS
Analyzing the right amount of granularity in a model is imperative to make sure the model is elaborative as per requirement without distorting the data. Therefore, it is vital to understand the concept of granularity and its application. When discussing granularity, a major barrier we come across is a lack of understanding and consistent language. Although, some research has been done to explain granularity in the context of engineering design, different terminologies have been used to explain this by different communities. The following section explains some important concepts and their usage in model granularity. It provides a different viewpoint on granularity and can be useful in measuring granularity levels.


CLASSES/OBJECTS

•	RegistrationForm(FlaskForm)
•	User(db.Model)
•	Candidates(db.Model)
•	RegistrationControls(db.Model)

METHODS
•	counter()
•	freqs()
•	registrations()
•	view_details()
•	interview_selection()
•	filter_by()
•	search_by()
•	president_controls()
•	statistics()
•	delete()
•	load_user()
•	page_not_found()
•	login()
•	login_pos()
•	signup()
•	signup_post()
•	logout()

PACKAGES
•	RECRUITERSSPACE

LIBRARIES

•	Flask.WTForms
•	Flask_sqlalchemy
•	Flask_login
•	Flask_migrate
•	Flask.templating
•	Werkzeug.security


FRAMEWORK
•	FLASK

PLATFORMS
•	Windows

REFERENCES’
[1] Sommerville, Software Engineering, Pearson, 2015.
[2]https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/






 
