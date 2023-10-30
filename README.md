<div align="center">

![AirBnB_Clone](https://github.com/Nitsu47/holbertonschool-AirBnB_clone/assets/135637506/5a5595cc-8f00-4613-9834-78b2b19f4015)

</div>

<div align="center">
  
<h1> AirBnB clone - The console </h1>

This repository contains the "AirBnB clone - The console" project for Holberton School.

</div>

<div align="center">

════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
</div>

<br>

## Table of contents
* [About](#about)
* [Resources](#resources)
* [Requirements](#requirements)
* [Files](#files)
* [Usage](#usage)
* [Authors](#authors)

<details>
<summary><h2>About</h2></summary>

The project its part of a greater project about construct our own AirBnB Clone to learn a get deeper into Python lenguage. In this repository, you can find a basic console for the web in where we do:
* The Console
* Web Static
* MySQL Storage
* Web framework - templating
* RESTful API
* Web dynamic
This objective is given us by Holberton School as a pair programming project of the second trimester.

</details>

<details>
<summary><h2>Resources</h2></summary>

<h3>Concepts</h3>
  
* <a href="https://intranet.hbtn.io/concepts/66" target="blank">Python packages</a>

* <a href="https://intranet.hbtn.io/concepts/74" target="blank">AirBnB clone</a>

<h3>Videos</h3>
  
* <a href="https://www.youtube.com/watch?v=QTwmCB_AWqI" target="blank">Overview</a>

* <a href="https://www.youtube.com/watch?v=jeJwRB33YNg" target="blank">The Console</a>

* <a href="https://www.youtube.com/watch?v=ZwCD8cNZk9U" target="blank">ORM</a>

* <a href="https://www.youtube.com/watch?v=LrQhULlFJdU" target="blank">RESTful API</a>

<h3>HBNB Playlist</h3>
  
* <a href="https://www.youtube.com/playlist?list=PLlLHfkTcnvmPOp6jv_89tRpJUMFrP-Wbi" target="blank">HBNB videos</a>

<h3>Concepts to learn</h3>
  
* <a href="https://docs.python.org/3.4/library/unittest.html#module-unittest" target="blank">Unittest</a>

* Python packages concept page

* Serialization/Deserialization

* `*args, **kwargs`

* `datetime`

</details>

<details>
<summary><h2>Requirements</h2></summary>

<h2>Python Scripts</h2>

* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

<h2>Python Unit Tests</h2>

* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* All your test files and folders should start by test_
* Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
* All your tests should be executed by using this command: python3 -m unittest discover tests
* You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").*MyClass.my_function.__doc__)')
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

</details>

<details>
<summary><h2>Files</h2></summary>
        
|Out Folders|
|---|
|[console.py](#console.py): The command-line interpreter for interacting with the AirBnB clone project. It allows users to manage and interact with the project's data and models through a command-line interface|
|[models](#models): contains all the basic models|
|[tests](#tests): Contains tests for the console and models|

|In "models" folder:|
|---|
|[engine](#engine): Contains essential modules for data storage and retrieval, including 'file_storage.py'|
|[amenity.py](#amenity.py): Amenity model, which represents the services or amenities available in a rental property. It includes attributes for features such as a pool, Wi-Fi access, and parking facilities.|
|[base_model.py](#base_model.py): Provides common attributes and methods that are inherited by other models, facilitating data management|
|[city.py](#city.py): City model in which we can establish the city in where the rental property is. ex: New York|
|[place.py](#place.py): Place model in which we can establish the city in where the rental property is. ex: EE.UU|
|[review.py](#review.py): Review model to stablish the reviews sections of a publication|
|[state.py](#state.py): State model to establish the State in where the rental property is. ex: Florida|
|[user.py](#user.py): User model to establish a User for the Publicator or the possible Buyer|

|In "engine" folder inside "models"|
|---|
|[file_storage.py](#file_storage.py): Responsible for storing and retrieving data|

<a name="models"></a>
<a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/tree/master/models"></a>
<a name="tests"></a>
<a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/tree/master/models/engine"></a>
<a name="console.py"></a>
<a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/console.py"></a>
<a name="engine"></a>
<a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/tree/master/models/engine"></a>
<a name="amenity.py"></a>
<a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/amenity.py"></a>
<a name="base_model.py"></a>
<a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/base_model.py"></a>
<a name="city.py"></a>
<a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/city.py"></a>
<a name="place.py"></a>
<a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/place.py"></a>
<a name="review.py"></a>
<a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/review.py"></a>
<a name="state.py"></a>
<a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/state.py"></a>
<a name="user.py"></a>
<a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/user.py"></a>
<a name="file_storage.py"></a>
<a href="https://github.com/Nitsu47/holbertonschool-AirBnB_clone/blob/master/models/engine/file_storage.py"></a>

</details>

<details>
<summary><h2>Usage</h2></summary>

For the first, if you doesn´t have installed yet 'git', write this command:
```
sudo apt-get install git
```
For the next, clone this repository with:
```
git clone https://github.com/Nitsu47/holbertonschool-AirBnB_clone.git
```
Now, to execute the console, put:
```
./console.py
```
After it you can view the prompt '(hbnb)' and star to put commands!!

<h2>Here you have a list of the aviable commands:</h2>

quit and EOF - these commands exit the console.

help - displays the list of commands to read help. If you use ```help command_name``` it displays the help for the specified command.

create - when you put ```create class_name``` it creates an instance for the specified class and prints it´s id.

destroy - when you put ```destroy class_name instance_id``` it deletes the specified instance based on the class name and instance id.

show - when you put ```show class_name instance_id``` it shows (prints) the string representation of the respective instance based on the class name and instance id.

all - when you put ```all class_name``` it prints the string representation of all instances of the respective specified class.

update - when you put ```update class_name instance_id attribute "value"``` updates an specified attribute based on the class name and instance id

</details>

<div align="center">

## Authors
  
&ensp;[<img src="https://img.shields.io/badge/Nitsu47-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">](https://github.com/Nitsu47)
&ensp;[<img src="https://img.shields.io/badge/LuciaPuppo897-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">](https://github.com/LuciaPuppo897)

<br>

════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

<br>

Last updated: Oct 30, 2023
