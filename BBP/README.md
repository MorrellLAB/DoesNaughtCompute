<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Access Slides
---

Go to this link: https://swipe.to/6340r

![](https://raw.githubusercontent.com/MorrellLAB/DoesNaughtCompute/master/BBP/images/Write_Less_Code_Cartoon.png)

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Becoming a Better Programmer
---

#### Chaochih Liu and Peter Morrell

July 8<sup>th</sup>, 2016

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Part 1: Write Less Code!

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Write Less Code!
---

Remove unnecessary code!

- Takes up extra storage
- Clutters revision control histories
- Gets in the way of development
- Uses code space

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Quality vs. Quantity
---

Writing more code does not mean more software!

<!-- software improvements could mean removing code -->

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Why does this matter?
---

- More code to read and understand
- More work to modify
- More places for bugs
- Duplicated code is difficult to troubleshoot

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Code Duplication
---

Strongly advise against: cut-and-paste coding...

...especially if code is copied with slight changes

<!-- show example code, maybe in R -->

***

<!-- Exercises color scheme -->
<!-- background: #063852 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Discussion Question
---

How different does a section of code have to be before it is justifiable to not factor into a common function?

<sub> Question 3 from end of Chapter 3 (pg. 27) </sub>

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Dead Code
---

- Code that never gets run
- Functions that are never called
- Variables that are written but never read
- Parameters passed to an internal method that are never used

<!-- reword and maybe add example -->

***

<!-- Exercises color scheme -->
<!-- background: #063852 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Discussion Question
---

How can you spot and remove dead code?

<sub> Question 4 from end of Chapter 3 (pg. 27) </sub>

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Comments
---

Carefully choose variable, function, and class names

Good structure

Not necesssary to duplicate information conveyed in variable/function/class names with comments.

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Comments
---

Comments should explain **why**

Code itself explains **what** and **how**

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Comments
---

Do not remove code by commenting it out

<!-- Git can track this for you -->

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Example of Commenting Out Code
---

![]()

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Verbosity
---

Reduce effort required to understand code

<!-- sequence handling example -->

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Example of Verbosity
---

Lines 161-166 of [Old version of sequence_handling](https://github.com/MorrellLAB/sequence_handling/blob/old/4_Quality_Trimming.sh)

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# In Practice
---

Remove redundancy and duplication as you find it

Separate tidying up and functional changes

<!-- makes it clear in source control system what happened -->

***

<!-- Exercises color scheme -->
<!-- background: #063852 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Discussion Question
---

Some coding standards mandate that every function is documented with specially formatted code comments. Is this useful? Or is it an unnecessary burden introducing a load of worthless extra comments?

<sub> Question 5 from end of Chapter 3 (pg. 27) </sub>

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Part 2: Wallowing in Filth

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Quicksand Code
---

Code quality benchmarks:

- Well named variable/function/class
- Neat and consistent code layout
- Simple and clear structure of cooperating objects
- Easy to find code that produces a certain effect

***

<!-- Exercises color scheme -->
<!-- background: #063852 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Discussion Question
---

Why does code frequently get so messy?

How can we avoid this from happening in the first place? Can we?

<sub> Question 1 and 2 from the end of Chapter 7 (pg. 61) </sub>

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Tackling Quicksand Code
---

Questions to help identify the appropriate strategy:

- How long will you be working with this section of code?
- How frequently has the code been modified?

Decide if it is appropriate to tidy up the code.

*Always leave the campground cleaner than you found it.*
*- Robert Martin*

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Making Adjustments
---

Make changes slowly and carefully!

- Make separate commits for tidying up layout and functional changes
- Ensure tidying preserves existing behavior

Make sure functionality is not removed!

***

<!-- Exercises color scheme -->
<!-- background: #063852 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Discussion Question
---

What are the advantages of making layout changes separately from code changes?

<sub> Question 3 from the end of Chapter 7 (pg. 61) </sub>

***

<!-- Exercises color scheme -->
<!-- background: #063852 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Discussion Question
---

How many times have you been confronted with distasteful code? 

How often was this code really dire, rather than “not to your taste”?

<sub> Question 4 from the end of Chapter 7 (pg. 61) </sub>
