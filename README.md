# 3: Printing_Quotes

Programming Language: Python
Goal: To get comfortable using basic sequential operations (input, process, output) in creating programs.

Constraints:

  --Be sure the output contains the original string.
  --Use a single output statement to construct the output.
  --Use a built-in function of the programming language to determine the length of the string.

Understanding the Problem
  What are the features of this application (or program)?
    --Prompts for a quote and author
    --Display the quotation and author
  
  Problem Statement:
    Create a program that prompts for a quote and author and then prints output that shows the quotation and author as shown.
------------------------------------------------------------------------

Discover the Inputs, Processes, Outputs (IPO)
  Input:
    --quote
    --author
  
  Process:
    --prompts
    --prints
    
  Output:
    --quote
    --author
-------------------------------------------------------------------------

Test Plan
  Input:
    --quote: What is the quote? "be impatient with action, and patient with results"
    --author: Who said it? "Naval Ravikant"
  
  Expected Results:
    --Naval Ravikant says, "be impatient with action, and patient with results."
    
  Actual Results:
    --Naval Ravikant says, "be impatient with action, and patient with results."
--------------------------------------------------------------------------

Algorithm in Psuedocode
  1)Start
  2)Get a value for "quote" by prompting the user with the message 'What is the quote? '
  3)Get a value for "author" by prompting the user with the message 'Who said it? '
  4)Print the message ' "author" + says \" + "quote" + \" . '
  5)Stop
