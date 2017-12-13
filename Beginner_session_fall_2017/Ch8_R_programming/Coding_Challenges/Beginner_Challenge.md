---
output: html_document
---
# Beginner Challenge

***

## Task

1. Read in Thetas file
2. Plot Watterson's Theta
3. Plot Pairwise Theta
4. Plot Tajima's D

All commands needed have been provided below. Open up RStudio and start typing commands into Source. For help on any command, type `?` followed by command name. For example, to find help on `read.delim()` type `?read.delim`.

***

### Commands to set working directory:

Command: `setwd()`

Arguments: 

`setwd(dir = "path to directory")`

***

### Commands and arguments to read in data:

Command: `read.delim()`

Arguments: 
- `file = "path to file"`
- `header = TRUE` to include file headers, `header = FALSE` to ignore file headers
- `sep = ""` for separator as white space, `sep = "\t"` for separator as tabs, sep = "\n"

***

### Commands and arguments to plot thetas with lowess lines

**First, calculate Watterson's Thetas and Pairwise Thetas.**

- Watterson's Thetas can be calculated by dividing tW by nSites
- Pairwise Thetas can be calculated by dividing tP by nSites

To **plot Watterson's Thetas**, use `WinCenter` column for x-axis and `Watterson` column for y-axis.

To **plot Pairwise Theta**, use `WinCenter` column for x-axis and `Pairwise` column for y-axis.

To **plot Tajima's D**, use `WinCenter` column for x-axis and `Tajima` column for y-axis.

Command: `plot()`

Arguments:
- `x = x_values`
- `y = y_values`
- `type = 'p'` to plot points, `type = l` to plot lines, `type = b` to plot both points and lines
- `main = "Title of graph"`
- `xlab = "Title of x-axis"`
- `ylab = "Title of y-axis"`
- `pch = 19` for filled in points. For more options see [Cheat Sheet for Plotting Symbols and Color Palettes](http://vis.supstat.com/2013/04/plotting-symbols-and-color-palettes/)
- `col = "cornflowerblue"`. For more color options see [R color cheatsheet](https://www.nceas.ucsb.edu/~frazier/RSpatialGuides/colorPaletteCheatsheet.pdf)

To plot lines on your graphs, the `lines()` command will need to immediately follow your plotting command. The commands we will use to plot lines is:

`lines(x = lowess(x, y, f), col = "color")`

Command: `lines()`

Arguments:
- `x = x_values`
- `y = y_values`

Command: `lowess()`

Arguments:
- `x = x_values`
- `y = y_values`
- `f = 0.1` uses smoother span. Larger values give more smoothness.
- `col = "pick your favorite"`
