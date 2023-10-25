<div align="center">
  
<h1> AirBnB clone - The console </h1>

> This repository contains the "AirBnB clone - The console" project for Holberton School.

</div>

<div align="center">

![sea-horse](https://user-images.githubusercontent.com/110431271/229328604-b8c19c26-54e9-48d6-946f-91b0337deece.png) ════════════════════ ![sea-horse](https://user-images.githubusercontent.com/110431271/229328604-b8c19c26-54e9-48d6-946f-91b0337deece.png) ════════════════════ ![sea-horse](https://user-images.githubusercontent.com/110431271/229328604-b8c19c26-54e9-48d6-946f-91b0337deece.png)

</div>

<br>

## Table of contents
* [About](#about)
* [Resources](#resources)
* [Requirements](#requirements)
* [Files](#files)
* [Usage](#usage)
* [Authors](#authors)

## About
The project its part of a greater project about construct our own AirBnB Clone to learn a get deeper into Python lenguage. In this repository, you can find a basic console for the web in where we do:
* The Console
* Web Static
* MySQL Storage
* Web framework - templating
* RESTful API
* Web dynamic
This objective is given us by Holberton School as a pair programming project of the second trimester.

## Resources
<h2>Concepts<h2>
* <a href="https://intranet.hbtn.io/concepts/66" target="blank">Python packages</a>
* <a href="https://intranet.hbtn.io/concepts/74" target="blank">AirBnB clone</a>
<h2>Videos<h2>
* <a href="https://www.youtube.com/watch?v=QTwmCB_AWqI" target="blank">Overview</a>
* <a href="https://www.youtube.com/watch?v=jeJwRB33YNg" target="blank">The Console</a>
* <a href="https://www.youtube.com/watch?v=ZwCD8cNZk9U" target="blank">ORM</a>
* <a href="https://www.youtube.com/watch?v=LrQhULlFJdU" target="blank">RESTful API</a>
<h2>HBNB Playlist<h2>
* <a href="https://www.youtube.com/playlist?list=PLlLHfkTcnvmPOp6jv_89tRpJUMFrP-Wbi" target="blank">HBNB videos</a>
<h2>Concepts to learn<h2>
* <a href="https://docs.python.org/3.4/library/unittest.html#module-unittest" target="blank">Unittest</a>
* Python packages concept page
* Serialization/Deserialization
* `*args, **kwargs`
* `datetime`

## Requirements
<h2>Python Scripts<h2>
*Allowed editors: vi, vim, emacs
*All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
*All your files should end with a new line
*The first line of all your files should be exactly #!/usr/bin/python3
*A README.md file, at the root of the folder of the project, is mandatory
*Your code should use the pycodestyle (version 2.7.*)
*All your files must be executable
*The length of your files will be tested using wc
*All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
*All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
*All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
*A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

<h2>Python Unit Tests<h2>
*Allowed editors: vi, vim, emacs
*All your files should end with a new line
*All your test files should be inside a folder tests
*You have to use the unittest module
*All your test files should be python files (extension: .py)
*All your test files and folders should start by test_
*Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
*All your tests should be executed by using this command: python3 -m unittest discover tests
*You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
*All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
*All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
*All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").*MyClass.my_function.__doc__)')
*We strongly encourage you to work together on test cases, so that you don’t miss any edge case

Execution
Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

<details>
<summary><h2>Files</h2></summary>
        
## Files
|Files|
|---|
|[console.py](#console.py)|
<h3>In "models" folder:<h3>
|[amenity.py](#amenity.py)|
|[base_model.py](#base_model.py)|
|[city.py](#city.py)|
|[place.py](#place.py)|
|[review.py](#review.py)|
|[state.py](#state.py)|
|[user.py](#user.py)|
<h3>In "engine" folder inside "models"<h3>
|[file_storage.py](#file_storage.py)|

<a name="console.py"></a>
<h3><a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/console.py">console.py</a></h3>
The command interpreter 
<a name="amenity.py"></a>
<h3><a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/amenity.py">amenity.py</a></h3>
.
<a name="base_model.py"></a>
<h3><a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/base_model.py">base_model.py</a></h3>
.
<a name="city.py"></a>
<h3><a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/city.py">city.py</a></h3>
.
<a name="place.py"></a>
<h3><a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/place.py">place.py</a></h3>
.
<a name="review.py"></a>
<h3><a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/review.py">review.py</a></h3>
.
<a name="state.py"></a>
<h3><a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/state.py">state.py</a></h3>
.
<a name="user.py"></a>
<h3><a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/user.py">user.py</a></h3>
.
<a name="file_storage.py"></a>
<h3><a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/engine/file_storage.py">file_storage.py</a></h3>
.

</details>

## Usage
Placeholder

<div align="center">

## Authors
  
&ensp;[<img src="https://img.shields.io/badge/Nitsu47-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">](https://github.com/Nitsu47)
&ensp;[<img src="https://img.shields.io/badge/LuciaPuppo897-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">](https://github.com/LuciaPuppo897)

<br>

![sea-horse](https://user-images.githubusercontent.com/110431271/229328604-b8c19c26-54e9-48d6-946f-91b0337deece.png) ════════════════════ ![sea-horse](https://user-images.githubusercontent.com/110431271/229328604-b8c19c26-54e9-48d6-946f-91b0337deece.png) ════════════════════ ![sea-horse](https://user-images.githubusercontent.com/110431271/229328604-b8c19c26-54e9-48d6-946f-91b0337deece.png)

<br>

Last updated: Oct 25, 2023

</div>