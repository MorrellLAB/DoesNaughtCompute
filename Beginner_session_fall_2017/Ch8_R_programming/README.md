<!-- background: #ffffff-->
<!-- color: #181816 -->
<!-- font: metronova -->

# What's a Pirate's Favorite Programming Language?

### Follow along with the presentation at: z.umn.edu/rprogramming

![](http://www.lindinglab.org/external-files/images/Rlogo1.png/image)

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# R as a programming language: Everything you need to know

Chaochih Liu

December 13<sup>th</sup>, 2017

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# R for statistics

![](http://www.sthda.com/sthda/RDoc/figure/statistics/correlation-matrix-correlogram-1.png)

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# R as a programming language

- Data exploration
- Data transformation
- Data analyses
- Data visualization

For more on visualization, see Vince Buffalo's *Bioinformatics Data Skills* Chapter 8.

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Overview

Part I: Review basic R commands and R fundamentals

Part II: Use R as a data programming language

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Part I: Review basic R commands and R fundamentals

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Quick R Review

```R
#   To install packages
install.packages("ape")
```

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Quick R Review

![](https://www.dropbox.com/s/v1w6ts547fbkh45/BDS_Table8-1.png?dl=1)

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Quick R Review

Assigning variables

```R
x <- 3

#   Combine values with the function c()
df <- data.frame(sample = c("one", "two", "three"), values = c(1, 2, 3))

#   View data stored in variable df
df
  sample values
1    one      1
2    two      2
3  three      3
```

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Quick R Review

Help for any generic function and their methods can be accessed with a `?`

```R
?data.frame
```

![](https://www.dropbox.com/s/fjjcx5ftuqcijfz/R_data_frame_help.png?dl=1)

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Quick R Review

For loops

```R
for (year in 2010:2015){
    print(paste("The year is", year))
}
[1] "The year is 2010"
[1] "The year is 2011"
[1] "The year is 2012"
[1] "The year is 2013"
[1] "The year is 2014"
[1] "The year is 2015"
```

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Vectors

Definition: A container of contiguous data.

R's base collection is a vector

```R
#   Vector of length 1
length(3.1)
[1] 1

#   Longer vectors
x <- c(1, 10, 20)
x
[1]  1 10 20

length(x)
[1] 3
```

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Vectorization

Vectorization is the act of applying a function across vector elements

```R
x <- c(5, 6, 7, 8, 25)
y <- c(1, 2, 3, 4, 5)

x + y
[1]  6  8 10 12 30

x/y
[1] 5.000000 3.000000 2.333333 2.000000 5.000000
```

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Quickly creating vectors

```R
seq(1, 10, by = 2)
[1] 1 3 5 7 9

1:10
[1]  1  2  3  4  5  6  7  8  9 10
```

Caution with vectorized operations!

If vectors are unequal in length, R recycles values in shorter vector!

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Vector types

Vectors must contain elements of the same type!

Many errors in R are from type-related issues.

![](https://www.dropbox.com/s/mpl2cxv74y3hyg1/BDS_Table8-3.png?dl=1)

![](https://www.dropbox.com/s/m95f5g0fcu1kaxq/BDS_Table8-3_part2.png?dl=1)

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Troubleshooting type-related issues

Always check help documentation!
- Each command will say what type each option accepts under the "Arguments" section

Use `class()` to check what type your data is

```R
df <- c(1, 2, 3)
class(df)
[1] "numeric"

df <- c("Monday", "Tuesday", "Wednesday")
class(df)
[1] "character"

df <- c(TRUE, FALSE)
class(df)
[1] "logical"
```

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# R's special values

R has four special values

| Type | Test Function | What? |
|----- | ------------- | ----- |
| `NA` | `is.na()` | built-in value to represent missing data |
| `NULL` | `is.null()` | represents not having a value, different than missing value |
| `-Inf`, `Inf` | `is.finite()`, `is.infinite()` | negative infinite and positive infinite values |
| `NaN` | `is.nan()` | stands for "not a number" (i.e. 0/0 or Inf + -Inf) |

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Indexing

R vectors are 1-indexed

Example:

![](http://s2.postimg.org/40doixek9/single_nucleotide_or_variant.jpg)

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Indexing

```R
x <- c(5, 6, 7, 8, 25)

#   Retrieve 2nd element
x[2]
[1] 6
```

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Slicing and dicing

![](http://al2na.github.io/compgenr/nonR_figures/slicingDataFrames.png)

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Slicing and dicing

```R
#   Create data frame
df <- data.frame(
    person = c("Chaochih", "Peter", "Li", "Erica", "Corey"),
    type = c("PC", "Mac", "Mac", "PC", "PC"),
    computer = c("Asus Zenbook Pro", "Apple Macbook Pro", "Apple Macbook Pro", "Microsoft Surface Book Pro", "Microsoft Surface Book Pro"))

#   View data frame
df
    person type                   computer
1 Chaochih   PC           Asus Zenbook Pro
2    Peter  Mac          Apple Macbook Pro
3       Li  Mac          Apple Macbook Pro
4    Erica   PC Microsoft Surface Book Pro
5    Corey   PC Microsoft Surface Book Pro

#   Retrieve column 2 rows 1-2
df[1:2, 1:2]
    person type
1 Chaochih   PC
2    Peter  Mac
```

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Slicing and dicing

```R
#   View data frame
df
    person type                   computer
1 Chaochih   PC           Asus Zenbook Pro
2    Peter  Mac          Apple Macbook Pro
3       Li  Mac          Apple Macbook Pro
4    Erica   PC Microsoft Surface Book Pro
5    Corey   PC Microsoft Surface Book Pro

#   Retrieve all who own a Mac
df[df$type == "Mac", ]
  person type          computer
2  Peter  Mac Apple Macbook Pro
3     Li  Mac Apple Macbook Pro
```

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Operators

![](https://www.dropbox.com/s/ttv5vd1fe2zcqtu/BDS_Table8-2.png?dl=1)

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Part II: Use R as a data programming language

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# How R thinks

Interpreted:
- Do not need to compile source code before running program
- Can enter an 'interactive' mode for R

![](https://qph.ec.quoracdn.net/main-qimg-ba6211548280b83387b5ca93fba19714)

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# How R thinks

Object-oriented:
- Can tell the computer what kind of data we're working with
- Can create class-specific functions, or methods, that are specialized for the data we have

Functional:
- R works best when everything is a function
- Functions can be mapped, or applied, over large quantities of data
   - This enables vectorization of functions to increase speed
   - For-loops are horrendously slow in R

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Functional vs imperative

*Functional*

```r
> numbers <- c(1,2,3,4,5) # Create an array of numbers
> doubled <- sapply(X = numbers, FUN = function(x) {return(x*2)}) # Tell the computer to double all numbers
> doubled
[1]  2  4  6  8 10
```

*Imperative*

```python
>>> numbers = [1, 2, 3, 4, 5] # Create a list of numbers
>>> doubled = [] # Create an empty list for doubled numbers
>>> for i in numbers: # For each number
...     newNumber = i * 2 # Create a new number equal to the current number times two
...     doubled.append(newNumber) # Add this to the list of doubled numbers
...
>>> doubled # Print our list to the screen
[2, 4, 6, 8, 10]
```

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Objects in R

- Computers don't inherently know what data is or how to use it
- **Classes** tell the computer what kind of data we have and what we're allowed to use it for
- We use these data by calling functions for each specific class to manipulate data and perform analyses

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Objects in R

- R is very good at handling complex data structures
- R has no object for single-values, everything is a collection
- R's base collection is a vector, a single number is a vector of length 1

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->


# (Some of) R's common classes

The following are classes that vectors can take

| Type | What? |
| ---- | ----- |
| `character` | Characters or strings, literally whatever you put in: "Hello world"|
| `logical` | Boolean values: `TRUE`, `FALSE`, and `NA`|
| `numeric` | Numbers, both whole integers and floating point values: 3, 12.9 |
| `factor` | A variable that can take on a limited set of values |

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# (Some of) R's common classes

| Type | What? |
| ---- | ----- |
| `vector` | Simplest collection of other types|
| `list` | A collection of vectors that can be called by name|
| `matrix` | A collection of vectors in multiple dimensions|
| `data.frame` | A collection of vectors in multiple dimensions that can be called by name |
| `null` | Empty value, `NULL` |
| `generic` | A function that is not designed to operate on a specific class. Functions have methods attached for specific classes: `is()`, `is.vector()`, `is.matrix()` |

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# (Some of) R's common classes

```r
> "Hello world" # Character
[1] "Hello world"
> TRUE # Logical
[1] TRUE
> 5 # Numeric
[1] 5
> factor(c(1, 4, 6, 1))
[1] 1 4 6 1
Levels: 1 4 6
```

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# (some of) R's common classes

```r
> c(1, 4, 5) # Vector
[1] 1 4 5
> list(nums= c(1, 4, 6), logs = c(TRUE, FALSE)) # List
$nums
[1] 1 4 6

$logs
[1]  TRUE FALSE
> matrix(data = c(1, 5, 2, 6, 3, 6 , 2, 5 ,2), ncol = 3, byrow = TRUE) # Matrix
     [,1] [,2] [,3]
[1,]    1    5    2
[2,]    6    3    6
[3,]    2    5    2
> data.frame(nums = c(1, 4, 5), logs = c(TRUE, TRUE, FALSE)) # Data Frame
  nums  logs
1    1  TRUE
2    4  TRUE
3    5 FALSE
```

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Functions in R

Functions are their own class in R
 - Base functions are called `generics`
 - `generics` have methods associated with them for other classes
  - `as()`
  - `as.character()`
  - `as.logical()`
 - Functions can be passed to other functions

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# User-defined functions

```r
myFunction <- function(x, y = 2) { # Create a function and assign it to myFunction
    # x does not have a default set
    # y defaults to 2, but can be set otherwise
    z <- x * y # Create a variable called z that's the product of x and y
    return(z) # Return z
}
```

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# The `apply` family

The `apply()` functions are designed to vectorize pre-built or user-defined functions

For-loops in R are slow and cumbersome, the `apply()` functions are quick and vectorized

| Function | Use |
| -------- | --- |
| `apply()` | Transform a complex data structure, ie. matrix or data frame; works in multiple dimensions |
| `lapply()` | Works with list-structured data |
| `sapply()` | Works with vectors and matrices |
| `vapply()` | Same as `sapply()` but has a pre-structured return value, ie. give it a vector to put values in to |
| `mapply()` | Multivariate version of `sapply()`, allows you to feed it multiple lists to iterate over |

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Why not to use for loops?

Slow for the same reason interpreted languages are slow.

Example

```R
#   Create temporary matrix
m <- matrix(as.numeric(1:100000))

#   Sum values in matrix using for loop
system.time({
    Sum = 0
    for (i in seq_along(m)) {
        Sum = Sum + m[[i]]
    }
    Sum
})
user  system elapsed
   0.08    0.00    0.08

system.time(sum(m))
   user  system elapsed
      0       0       0
```

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# The `apply` family

```r
# Double all numbers in a vector
sapply(X = c(1, 2, 3, 4, 5), FUN = function(x) {return(x*2)})
[1] 2 4 6 8 10

# Sum the two columns in a data frame on a row-by-row basis
# MARGIN of 1 indicates rows, 2 indicates columns
apply(X = data.frame(V1 = c(1, 4, 5, 8), V2 = c(19, 43, 12, 16)), MARGIN = 1, FUN = sum)
[1] 20 47 17 24
```

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Writing scripts

A script is a series of commands to perform some kind of analysis, exploration, or transformation

Uses for scripts:
- Take notes of what was done
- Quickly replicate analysis
- Write a program that accepts command-line arguments and performs analysis or transformation on various datasets

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Tips for scripting R

- Write functions
- Design functions to work on subsets of data
- Pay attention to classes
- _Don't_ use R for text processing
- **Do** use R for data transformation, exploration, and analyses
- Avoid for-loops, vectorize instead

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Example scripts

Very simple example of script that does one simple task: [`transpose_data.R`](https://github.com/liux1299/Utilities/blob/master/transpose_data.R)

More complex example of script that does multiple tasks and is computationally intensive: [`LDheatmap.R`](https://github.com/liux1299/Utilities/blob/master/LDheatmap.R)

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Graphing (aka exercise)!

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

# Graphing cheat sheets!

[Cheat Sheet for Plotting Symbols and Color Palettes](http://vis.supstat.com/2013/04/plotting-symbols-and-color-palettes/)

[R color cheatsheet](https://www.nceas.ucsb.edu/~frazier/RSpatialGuides/colorPaletteCheatsheet.pdf)

***

<!-- background: #ffffff -->
<!-- color: #181816 -->
<!-- font: metronova -->

Thetas File Layout

| Column | Contents |
| ------ | -------- |
| Chr | Name of contig |
| WinCenter | Center of window for Thetas Analysis |
| tW | Raw Watterson's Theta value |
| tP | Raw Pairwise Theta value |
| tF | Raw Fu and Li's Theta value |
| tH | Raw Fay's Theta value |
| tL | Raw Maximum Likelihood Theta value |
| Tajima | Tajima's D |
| fuf | Fu and Li's F |
| fud | Fu and Li's D |
| fayh | Fay's H |
| zeng | Zeng's E |
| nSites | Effective number of sites |

To plot a Theta's value, you need to divide the Theta's column by nSites

Data and coding challenges are located in: [MorrellLAB/DoesNaughtCompute/Beginner_session_fall_2017/Ch8_R_programming/Coding_Challenges](https://github.com/MorrellLAB/DoesNaughtCompute/tree/master/Beginner_session_fall_2017/Ch8_R_programming/Coding_Challenges)

More example scripts are located in: [MorrellLAB/DoesNaughtCompute/Beginner_session_fall_2017/Ch8_R_programming/Example_Scripts](https://github.com/MorrellLAB/DoesNaughtCompute/tree/master/Beginner_session_fall_2017/Ch8_R_programming/Example_Scripts)