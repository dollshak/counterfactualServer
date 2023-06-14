# Counter Factual Comperator

## About
This is the README file for the counterfaactual explanations comperator system.

## Usage
In this section we provide an explanation of how to use the application's features. 
### Add New Algorithm
In Order to add you own counterfactual algorithm, one's must support our algorithm interface as described below:
### Algorithm Interface
**initAlgo(model, arg_lst, feature_list)** 
this function receives 3 arguments:
1. model - the actual ML model we would like to work with. *NOTICE - model is guaranteed to have .predict method.*
2. arg_lst - argument to the counterfactual algorithm, in a dictionary object. mapped as <argument_name , value>
3. feature_list - model's data feature list ordered

 initAlgo should initiate and return an algorithm class object that supports the method:
<br> 
 explain(self, model_input: returns an explanation for the given model with a given input - *model_input*
 <br>
 results must return in the order of the feature_list initAlgo received
 <br>
 for exmaple, for a given weather forecasting model with 3 features: humadity, temperature, date - *model_input* would be: [0.3, 25,25/12]
 
 #### Algorithm Interface Implementation Example:
 ![image](https://github.com/dollshak/counterfactualServer/assets/62897121/00beade9-f3cf-4767-aad0-eb281be34706)


 ### Add New Algorithm using the App
 To add new algorithm one must:
 1. upload the algorithm code file (currently supports .py only)
 2. add algorithm params - *NOTICE - algorithm param names should be exaclty as expected in initAlgo*. it is recommnded to give an explanation of the inputs and thier meaning. default value is optional and isn't a requirement
 3. write a Description: write a short description of your algorithm to help others understand and learn from it.
 4. write output exmaple description: Describe what is the expected output of the algorithm.
 5. write additional info: here one should write informationfor who ever want to learn further of the algorithm, this is the place to write a github link,  website url, email and more.
 6. choose type to support, whether the algorithm supports classification models, regression models or both.
 7. Click on the add button.
 
 
 ### Run Algorithms.
 In order to run your algorithm:
 1. In the home screen click on the run algorithms button.
 2. Choose the algorithms you'd like to run
 3. Add parameters to each of the algorithms you chose
 4. Choose whether you want to limit the algorithm running time or not. if time is limited and couldn't finish in time, no results will be returned from the    respective algorithm.
 5. Upload the model
 6. Upload model inputs as a json file including dictionary object including:
`{
"names": <ordered list of feature names>,
"values" : <ordered input values> 
}`
7.Click on the run button.

### Edit Algorithms
In order to edit an algorithm:
1. In the home screen click on the edit algorithm button.
2. Choose the algorithm you would like to edit.
3. Fill the fields you would like to edit.
4. Click on the save button.

