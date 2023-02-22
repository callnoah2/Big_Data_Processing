# Software Development Plan

## Phase 0: Requirements Analysis (tag name `analyzed`)
*(20% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Re-write the instructions in your own words.
    *   If you don't do this, you won't know what you're supposed to do!
    *   Don't leave out details!
*   [ ] Explain the problem this program aims to solve.
    *   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.
*   [ ] List all of the data that is used by the program, making note of where it comes from.
    *   Explain what form the output will take.
*   [ ] List the algorithms that will be used (but don't write them yet).
*   [ ] Tag the last commit in this phase `analyzed`
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*


For this assignment, I will need to start by hard coding a few fiels into my program. I Don't know how to do that
I will use these files that are now hardcoded into my program to process the data.
To process the data, I Will open each file and read it one line at a time, However, I cannot use .read or .readline()
I also need to add the parts of the lists to a dictionary

For Area-titles.CSV, I will need to decide what FIPS codes to use by using the area_fips field.
Then I will need to split each line of this file into exactly two fields.
Keep track of the FIPS areas that may be icluded in a dictionary
TREAT THESE CODES LIKE STRINGS
After discarding all unwanted FIPS areas, I should have 3,463 areas left.

For 2021.annual.singlefile.csv, I will need to hardcode the file into my program.
This program should skip over all of the lines of the file that the customer does not want. 

If industry_code == 10 and own_code == 0, the data should be added to all industries

if industry_code == 5112 and own_code == 5 It should fo to the softwear publishing indusrty.


The Goal of this program is to sort through all FIPS and decide which ones are wanted.
It will also look through each line of a file provided to see if it is wanted
wanted items will be printed out to the user.

from the last project, I already know how to open the files and print them, I also know how to split files by line
but I need to split files by line without using .split I think I will do this with a loop to iterate throught each line
I also know how to check for information wanted, I can do this with if statments.
A challenge I can forsee is needing to split each file without using the .split function
I will also need to find out what FIPS area codes are unwanted. but once that is done, it will be easy to remove unwanted ones


All data in this code either is hardcoded into the program, or it is found in the /data folder.
in the data folder, there are other folders for different areas and different elements of the areas
This data consists of an area-titles comma sperated file
this file contains the area_fips, and the area title.
they also have an output file to show me what it Should look like.
They also have a README	file, this file shows how to get the data set full copy.
all data is in a string format, the output should also be in string format

Algorithms will be used to read each file line by line and check if it is a wanted line.
another algortithm will be used to split CSV files,


## Phase 1: Design (tag name `designed`)
*(30% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
*   [ ] Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
*   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occur to you, and use them later when testing
*   [ ] Tag the last commit in this phase `designed`
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*


## Phase 2: Implementation (tag name `implemented`)
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] More or less working code.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan
*   [ ] Tag the last commit in this phase `implemented`


## Phase 3: Testing and Debugging (tag name `tested`)
*(30% of your effort)*

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
*   [ ] Tag the last commit in this phase `tested`


## Phase 4: Deployment (tag name `deployed`)
*(5% of your effort)*

Deliver:

*   [ ] Tag the last commit in this phase `deployed`
*   [ ] Your repository is pushed to GitLab.
*   [ ] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [ ] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 5: Maintenance

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [ ] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Assignment Reflection Survey** on Canvas.