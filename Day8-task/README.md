# Task 8 – Simple CLI Calculator
 AI-Driven Development – 30-Day Challenge

## 📝 Overview
For this task, we built a **Simple CLI Calculator** using **SpecKitPlus**, following 5 core commands. The calculator was created by following these steps:

1. `/sp.constitution` – Defined the project idea and scope: *"Simple calculator with basic operations"*  
2. `/sp.specify` – Defined input and output: *"calculator: input expr (string) → output result (number)"*  
3. `/sp.plan` – Planned the logic: *"take expression, validate, evaluate, return number"*  
4. `/sp.tasks` – Broke down the tasks:  
   1. Receive input  
   2. Validate expression  
   3. Evaluate safely  
   4. Return result  
5. `/sp.implement` – Implemented the calculator using the above plan  



##  How It Was Built
The calculator was created by following these steps:


# Initialize SpecKitPlus project
specify init calculator
cd calculator

# Execute the 5 core commands in the prompt to define & implement the calculator
/sp.constitution "simple calculator with basic operations"
/sp.specify "calculator: input expr (string) output result number"
/sp.plan "take expression validate evaluate return number"
/sp.tasks "1 receive input 2 validate expression 3 evaluate safely 4 return result"
/sp.implement "implement calculator in five core commands"

##  How to Run

python -m src.calculator.main

