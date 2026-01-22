# openevolve_example
a minimal example of using OpenEvolve for a seminar presentation

There are four components to an OpenEvolve program

# ONE - config.yml
This contains all of the various parameters of the algorithm.  In particular it specifies what the server for the LLM and the model that will be used to generate new code and the model that will be used to evaluate whether that code is correct.
There are many other parameters that can be modified including the "temperature" indicating how creative you want the LLM to be when it generates answer.

# TWO - evaluator.py
This is a program that has a function evaluate that returns a dictionary with entries "combined_score".
That dictionary can also have separate individual scores and keep track of additional logged information about the evaluation.
This program calls evaluate("initial_program.py") and determines a score.

# THREE - initial_program.py

# FOUR - prompt.txt
This is the prompt that is sent to the LLM in order to

(1) tell it what you want it to generate

(2) why you want to generate it (provide motivation)

(3) details about what the output should look like

(4) restrictions on the output (that it should only change the code in the "evolve block") and

(5) (optional) encouragement! "I know you can do it! you are amazing!"
