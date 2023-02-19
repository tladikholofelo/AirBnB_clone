<h1 align="center">AirBnB Clone - The Console</h1>

<p align="center">
  <img src="https://github.com/Adeniyii/AirBnB_clone/blob/main/assets/hbnb_logo.png" alt="HolbertonBnB logo">
</p>

## Description
The AirBnB clone deploys a simple copy of the [AirBnB](https://www.airbnb.com/) website as the first step towards building a complete full web application, integrating database storage, a back-end API and front-end interface.

The first step is to manipulate a powerful storage system that can manage (create, update, destroy, etc) objects via a __console / command interpreter__.

## Console
The console is a __command interpreter__ that manipulates data without a visual interface, like in a Shell (ideal for development and debugging). This storage engine gives an abstraction between objects, and how they are stored and persisted. It also easily allows the changing of the type of storage without updating all of the codebase. 

The objects can be managed in a limited specific use-case to:
* Create a new object (ex: a new User or a new Place)
* Retrive an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Environment
- All files have been developed and tested on an Ubuntu 20.04 LTS machine using `python3 (version 3.8.3)`.
 <!-- Style guidelines -->
* All files have been coded using:
  * [pycodestyle (version 2.8.*)](https://pypi.org/project/pycodestyle/)
  * [PEP8](https://pep8.org/)

## Installation

Clone this repository:
```bash
git clone https://github.com/tladikholofelo/AirBnB_clone.git
```
Access the __AirBnb_clone__ directory:
```bash
cd AirBnB_clone
```
Run the console:
```bash
 ./console.py
```

## Usage

* Start the console in interactive mode:
```bash
$ ./console.py
(hbnb)
```

* Use `help` to see a list of the available commands:
```bash
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
```

Command | Description | Example
------- | ----------- | -------
all | Prints all string representations of all instances of a given class. If no class is passed, all classes are printed | ```(hbnb) all``` or ```(hbnb) all <class>```
count | Prints the number of instances of a given class | ```(hbnb) <class name>.count()```
create | Creates a new instance of a given class. The class id is printed and the instance is saved to the file file.json | ```(hbnb) create <class>```
destroy | Deletes an instance of a given class with a given id | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
help | Displays a list of the available help commands | ```(hbnb) help <command>```
quit | Quits the console | ```(hbnb) quit```
show | Prints the string representation of an instance based on the class name and id | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
update | Updates an instance based on a dictionary representation of attribute names and values | ```(hbnb) update <class> <id> <attribute name> "<attribute value>"``` or ```(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")```

## Execution

### Interactive mode:
```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit
$
```

### Non-interactive mode:
```bash
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
```

## Testing
Unittests for the project are defined in the [tests](./tests) folder.

### Run all test files:
```bash
$ python3 unittest -m discover tests
```

### Run a single test file:
```bash
$ python3 -m unittest tests/test_models/test_base_model.py
```

### Run tests in non-interactive mode: 
```bash
$ echo "python3 -m unittest discover tests" | bash
```

## Authors

> [Kholofelo Tladi](https://github.com/tladikholofelo) and
> [Emmanuel Oluwatosin Akinwande](https://github.com/Morakinyo75)

## Acknowledgments
To see the fundamental background of the AirBnB Clone project, visit the [Wiki](https://github.com/ralexrivero/AirBnB_clone/wiki).
