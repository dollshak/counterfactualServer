# Counterfactual Explanations Comperator
## Implementing and expanding the system
### Adding a new Engine to handle more executables files
In order to add new engine one must do the following:
1. Add a new class which implements the EngingAPI.py class.
2. In the function get_cf_results of the class Engin4Controller.py add an if condition (or equivalent) to handle the case of each possible 
file (.py file of any other file)

### Supporting more input types
In order to support more input types (e.g image)
1. Add a new class which implements the InputHandlerAbstract.py
2. In the function _get_handler of the class InputOutputController.py add an if condition (or equivalent) to handle the case of each possible 
input.

## Maintaining the system
### General Instructions:
As the project is an open source - new features and updates will be pushed using pull requests.
in order to get access to the either of the repositories (Client or Server). please contact:
<br>
Ido Livne - idoliv@post.bgu.ac.il
<br>
Raz Bamnloker - razbam@post.bgu.ac.il
<br>
Shaked Dollberg - Dollshak@post.bgu.ac.il
<br>
### The Database
The DB has capacity of 5GB - that should be more than enough for any amount of different algorithms. In case of reaching the limit, deleting from the DB the latest LUT.
database details:
1. mongoDB -> log in using the regular website - https://account.mongodb.com/account/login?nds=true
2. user Email - sridbliv@gmail.com
3. password - 321vilbdirs

### Client Side  - 
The client repository can be found here - https://github.com/dollshak/counterfactualClient

