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

user input will consist of only one folder, in this folder, I will want to open the area-titles file, then I will split the file by line
and have it check if it is an FIPS that I want.


when the user wants the 2021.annual.singlefile.csv the file will be opened and split.
I will then check if it is the FIPS that I want, and it will give me any line with the desired vaulues for 
area_fips, industry_code, and own_code.
If numeric data must be coverted, dont use eval

I will not want to include FIPS that begin with the letter c and All state wides will end with 000 


for reports:

open(file given):
for every line in file given
if FIPS starts with a C, or, ends with 000, 
continue
else:
append it to the rpt

for annual singlefile

open(file given)
for every line
if fips starts with c or ends with 000, (%1000?)
contiunue
elif industry code is 10 and own_code is 0:
add to industries portion
elif indusrty code is 5112 snd own_code is 5: 
add it to software publishing industry
else: append it to the rpt

These functions above will both take one parameter from the user and open the file.

Good input would require a valid folder to be given,
bad input because of too few arguments will call a usage function which will simply be there to tell the user how to use the function
bad input because of a file that cannot be opened will give the user the default error message.


## Phase 2: Implementation (tag name `implemented`)
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] More or less working code.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan
*   [ ] Tag the last commit in this phase `implemented`

I had to learn how to use a dictionary. I didnt understand how to put the 2021.singlefile in each of the file, I had to
ask the tutooring center for help. I had issues with splitting the data up correctly but I learned how to do it the right way.


## Phase 3: Testing and Debugging (tag name `tested`)
*(30% of your effort)*

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
*   [ ] Tag the last commit in this phase `tested`
test one, difference with UT_all_Industries:
the count for the number of areas in the file is off for both "All" and "soft". I don't know the cause yet. 
I checked to see if it was because one of the area-titles was off, but it had the correct number of FIPS numbers.
I will put a print statement under all of the 'continues' to see if a line was skipped that shouldn't have bee.
I also am guessing that some of the files are the wrong section.
I realized that that was not the issue, The issue is with all the other fields, Now I will check on my algorithms that compair 
the data. 

I found out that I was extracting the wrong data from the singlefile. I fixed the data I was taking out.

test two: giving the program wrong parameters.
I will start by testing the program with no file given then a mispelled file.

With a mispelled file, Open raises an error.
with a no file, usage message is raised.


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

Checked in Gitlab, all commits are there as they should be. I clonned the repository over to my laptop earlier today and It worked 
great, then I pushed all changes and pulled them on my desktop. All files worked as expected.

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

I think my code is easy to read, I asked my brother in law to reformat it with me and he taught me a few ways to format it and make it shorter.

I dont fully understand how the report works from the dictionary. I know how to use the key in the dictionary but I am not quite sure how the dictionary for the report got all the data.

I think it would take me 3 hours to find the cause, There are a lot of interdependant lines in the file that make it hard to debug.

I think my documentation makes sense to other people adn myself, however; I wish I worked harder on it and put more detail into it.

I think it would be dificult to add a feature into this, there are a lot of codes that depend on eachother and changing things would be hard, but doable.

This code will need to be changed to work with next years data types. They would be easy changes, but it wouldnt work without them.
