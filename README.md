The frontend framework for the user interface is HTML,CSS
The backend framework is  Django and the technology used is Python  for the server-side logic.
PostgreSql database  is used to store user information, notes, and authentication details.
Before login,User should create an account in it.Authentication is the process of verifying the identity of a user or system. A common mechanism involves the use of usernames and passwords. When a user tries to access a secured area or resource, they provide their credentials, which are then validated against the stored values in the system. If the credentials match, the user is granted access.I Create a custom User model Customer that includes fields for the username, email,name,password,status and confirmpassword.
The additional feature which I had implemented in my project is that along with title and content upload and image field as Thumbnail is also addedd so that the user can easily identidfy their notes.
The another additional feature is the notes are displayed to their respective user only
I handle potential errors using forms.py.Django provides inbuilt forms which handles validations  automatically.
Thwe challenges that I have faced during the development process is that validation errorrs then I overcame using forms.py and Javascript.I also faced csrf token verification and operational errors I handled it by referencing Django documentation.
technical choices that I make in terms of technologies and frameworks:-
1)Django Framework:
Developers often choose Django as it is a robust and well-established Python web framework. Django provides a built-in authentication system, ORM (Object-Relational Mapping), form handling, and many other features that simplify and accelerate web application development.
2)Database Management System (DBMS):
Django supports multiple DBMS options, including PostgreSQL, MySQL, SQLite, and others. The choice of DBMS depends on factors such as scalability, data complexity, and the project's specific requirements. For larger and production-grade applications, developers might opt for PostgreSQL or MySQL for their performance and scalability advantages.
3)Frontend Technologies:
Developers have various options for frontend technologies when building a Django project. Common choices include HTML, CSS, JavaScript
4)Inbuilt forms and packages:
Django provides  forms.py -anbuilt validation mechanism handling and jazzmin package for admin panel customisation
