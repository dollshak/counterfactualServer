# Counterfactual Explanations Comperator
## Implementing and expanding the system
### Adding a new Engine to handle more executables files
In order to add new engine one must do the following:
1. Add a new class which implements the EngingAPI.py class.
2. In the function get_cf_results of the class EngingController.py add an if condition (or equivalent) to handle the case of each possible 
file (.py file of any other file)

### Supporting more input types
In order to support more input types (e.g image)
1. Add a new class which implements the InputHandlerAbstract.py
2. In the function _get_handler of the class InputOutputController.py add an if condition (or equivalent) to handle the case of each possible 
input.

## Maintaining the system
### The Database
The DB has capacity of 5GB - when reaching the limit one should delete algorithms ( Except the basic ones : DiCE , Alibi , Wachter) or add more capacity.
