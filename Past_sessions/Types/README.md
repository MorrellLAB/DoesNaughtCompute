# Types
## Paul Hoffman
## June 10, 2016

## What are types?
### Parnas, Shore, and Weiss (1976)

 - ~~A type is a purely syntactic label associated with a variable when it is declared.~~
 ```R
 > var = 5
> class(var)
[1] "numeric"
> class(var) <- 'duck'
> class(var)
[1] "duck"
```

 - A type is a set of values which a variable can possess and a set of functions that one can apply to these values.
 - Types provide additional information about the intended use of the data
 - Types allow for abstraction of data, enabling the solution to one problem to be applied to multiple problems
 - Types create specialized methods for interacting with data, resulting in shorter, cleaner code

## Why *Cython*?
### Thinking about types rather than data
 - C/C++ are statically typed
  - Each variable must have a type associated with it
  - The compiler will not figure out what type you have automatically
 - Python is dynamically typed
  - Python figures out what you have and what you can do with it

 - Dynamic typing is easy, but encourages iffy practices with programming
 - Statically typed languages
  - More efficient that dynamically typed languages
  - Ensure variables have known limits on content and function
  - Enable easy debugging by ensuring the answer to what type is that is not “I don’t know”

 - Dynamically typed languages
  - Allow for variables of many types
  - Do not restrict code to certain data values
  - **Error-prone when variables of the wrong type are passed**

# Goals
 - Program as if you were working with a statically typed language
 - Understand and ask the question *what __type__ is that?*

## Debugging Programs
### GetMajorMinor

```python
#   Adapted from Peter Morrell's genotype_conversion.py

#   Note that the type of 'snp' is unknown, and this function
#   is logic error prone when giving an unexpected type

def GetMajorMinor(snp):
    missing = 'NA'
    valid_bases = {'A', 'C', 'T', 'G'}
    snp = [x for x in snp if x != missing]
    all_calls = ''.join(snp)
    alleles = set(all_calls)
    if len(alleles) < 2:
        return('N', list(alleles)[0])
    alleles = alleles.intersection(valid_bases)
    counts = {}
    for a in alleles:
        counts[a] = all_calls.count(a)
    minor_allele = min(counts, key=counts.get)
    major_allele = max(counts, key=counts.get)
    if minor_allele == major_allele:
        minor_allele = list(alleles)[0]
        major_allele = list(alleles)[0]
    return(minor_allele, major_allele)

#   The error checking for this program is contained outside of the function
#   in the original source code.
```

```cpp
// Class definition for MajorMinor 
class MajorMinor {
    protected:
        char major;
        char minor;
    public:
        MajorMinor() {
            major = 'N';
            minor = 'N';
        }
        MajorMinor(char min, char maj) {
            major = maj;
            minor = min;
        }
        char getMajor() {
            return major;
        }
        char getMinor() {
            return minor;
        }
        friend ostream& operator<<(ostream& out, MajorMinor mm) {
            out << "Major:\t" << mm.major << endl;
            out << "Minor:\t" << mm.minor << endl;
            return out;
        }
};

// Version of code that works
// Note that you know the exact inputs for this program, including type
MajorMinor GetMajorMinor(string snp[], int num_snps) {
    string all_calls, alleles, valid;
    char major_allele, minor_allele;
    int major_freq = num_snps * -1000, minor_freq = num_snps*1000;
    for(int i = 0; i < num_snps; i++) {
        if(snp[i] != "NA") {
            all_calls += snp[i];
        }
    }
    alleles = uniqueCharacters(all_calls);
    if(alleles.length() < 2) {
        return MajorMinor('N', alleles[0]);
    }
    valid = intersection(alleles, "ACGT");
    for(int i = 0; i < valid.length(); i++) {
        int count = 0, position = -1;
        while(true) {
            position = all_calls.find(valid[i], position + 1);
            if(position == string::npos) {
                break;
            }
            else {
                count++;
            }
        }
        if(count+1 < minor_freq) {
            minor_allele = valid[i];
            minor_freq = count;
        }
        if(count + 1 > major_freq) {
            major_allele = valid[i];
            major_freq = count;
        }
    }
    return MajorMinor(minor_allele, major_allele);
}
```

## Creating Modular Programs
### Selective Coefficients

```python
#   Adapted from Colin Pierce

#   How do we go about modularizing this code to create
#   a variable amount of simuPOP.MaSelector objects with
#   variable fitness values and generations?

preOps = [
    simuPOP.SNPMutator(u=Mutation, v=Mutation),
    simuPOP.MaSelector(loci=0, fitness=Fitness1, begin=Gen0, end=Gen1), 
    simuPOP.MaSelector(loci=0, fitness=Fitness2, begin=Gen1, end=Gen2),
    simuPOP.MaSelector(loci=0, fitness=Fitness1, begin=Gen2, end=Gen3),
    simuPOP.MaSelector(loci=0, fitness=Fitness2, begin=Gen3, end=Gen4),
    simuPOP.MaSelector(loci=0, fitness=Fitness1, begin=Gen4, end=Gen5),
    simuPOP.MaSelector(loci=0, fitness=Fitness2, begin=Gen5, end=Gen6),
    simuPOP.MaSelector(loci=0, fitness=Fitness1, begin=Gen6, end=Gen7),
    simuPOP.MaSelector(loci=0, fitness=Fitness2, begin=Gen7, end=Gen8),
    simuPOP.MaSelector(loci=0, fitness=Fitness1, begin=Gen8, end=Gen9),
    simuPOP.MaSelector(loci=0, fitness=Fitness2, begin=Gen9, end=Gen10)
]

#   preOps is a **list**, we can use the list concatenation property of Python
#   to split this up into separate lists
preOps = [ simuPOP.SNPMutator(u=Mutation, v=Mutation) ] + [
    simuPOP.MaSelector(loci=0, fitness=Fitness1, begin=Gen0, end=Gen1), 
    simuPOP.MaSelector(loci=0, fitness=Fitness2, begin=Gen1, end=Gen2),
    simuPOP.MaSelector(loci=0, fitness=Fitness1, begin=Gen2, end=Gen3),
    simuPOP.MaSelector(loci=0, fitness=Fitness2, begin=Gen3, end=Gen4),
    simuPOP.MaSelector(loci=0, fitness=Fitness1, begin=Gen4, end=Gen5),
    simuPOP.MaSelector(loci=0, fitness=Fitness2, begin=Gen5, end=Gen6),
    simuPOP.MaSelector(loci=0, fitness=Fitness1, begin=Gen6, end=Gen7),
    simuPOP.MaSelector(loci=0, fitness=Fitness2, begin=Gen7, end=Gen8),
    simuPOP.MaSelector(loci=0, fitness=Fitness1, begin=Gen8, end=Gen9),
    simuPOP.MaSelector(loci=0, fitness=Fitness2, begin=Gen9, end=Gen10)
]
```

```python
#   Adapted from Colin Pierce

#   This function creates a variable number of simuPOP.MaSelector objects
#   and returns a list

def GenerateSelectiveEnv(selcoeff, switches, gens, SelectionType, UpperSelValue):
    if selcoeff == 'random':
        selcoeff = [random.uniform(1, UpperSelValue) for i in range(0, switches)]
    stable_period = gens/switches
    coeffs = []
    while len(coeffs) < switches:
        for s in selcoeff: 
            coeffs.append(s) 
    breakpoints = [i for i in range(0, gens+1) if i%stable_period == 0]
    listselcoeff = [random.uniform(1, UpperSelValue) for i in range(0, 100000)]
    sel = []
    if SelectionType == 'Symmetrical':
        for i in range(1, len(breakpoints)):
            j = i-1
            if i % 2 == 1:
                c = [coeffs[j], 1]
            else:
                c = [1, coeffs[j]]
            s = simuPOP.MaSelector(
                loci=0,
                fitness=c,
                begin=breakpoints[j],
                end=breakpoints[i]
            )
            sel.append(s)   
    else:
        for i in range(1, len(breakpoints)):
            j = i-1
            c = random.sample(listselcoeff, 2)
            s = simuPOP.MaSelector(
                loci=0,
                fitness=c,
                begin=breakpoints[j],
                end=breakpoints[i]
            )
            sel.append(s)
    return(sel)

```

```python
preOps = [simuPOP.SNPMutator(u=Mutation, v=Mutation)] + GenerateSelectiveEnv(
    selcoeff='random',
    switches=10,
    gens=10,
    SelectionType='Symmetrical',
    UpperSelValue=1.005
)

#   is equivalent to
preOps = [ simuPOP.SNPMutator(u=Mutation, v=Mutation) ] + [
    simuPOP.MaSelector(loci=0, fitness=[1.0018076453778229, 1], begin=0, end=1), 
    simuPOP.MaSelector(loci=0, fitness=[1, 1.0033219854101134], begin=1, end=2),
    simuPOP.MaSelector(loci=0, fitness=[1.0018076453778229, 1], begin=2, end=3),
    simuPOP.MaSelector(loci=0, fitness=[1, 1.0033219854101134], begin=3, end=4),
    simuPOP.MaSelector(loci=0, fitness=[1.0018076453778229, 1], begin=4, end=5),
    simuPOP.MaSelector(loci=0, fitness=[1, 1.0033219854101134], begin=5, end=6),
    simuPOP.MaSelector(loci=0, fitness=[1.0018076453778229, 1], begin=6, end=7),
    simuPOP.MaSelector(loci=0, fitness=[1, 1.0033219854101134], begin=7, end=8),
    simuPOP.MaSelector(loci=0, fitness=[1.0018076453778229, 1], begin=8, end=9),
    simuPOP.MaSelector(loci=0, fitness=[1, 1.0033219854101134], begin=9, end=10)
]

#   is equivalent to
preOps = [ 
    simuPOP.SNPMutator(u=Mutation, v=Mutation),
    simuPOP.MaSelector(loci=0, fitness=[1.0018076453778229, 1], begin=0, end=1), 
    simuPOP.MaSelector(loci=0, fitness=[1, 1.0033219854101134], begin=1, end=2),
    simuPOP.MaSelector(loci=0, fitness=[1.0018076453778229, 1], begin=2, end=3),
    simuPOP.MaSelector(loci=0, fitness=[1, 1.0033219854101134], begin=3, end=4),
    simuPOP.MaSelector(loci=0, fitness=[1.0018076453778229, 1], begin=4, end=5),
    simuPOP.MaSelector(loci=0, fitness=[1, 1.0033219854101134], begin=5, end=6),
    simuPOP.MaSelector(loci=0, fitness=[1.0018076453778229, 1], begin=6, end=7),
    simuPOP.MaSelector(loci=0, fitness=[1, 1.0033219854101134], begin=7, end=8),
    simuPOP.MaSelector(loci=0, fitness=[1.0018076453778229, 1], begin=8, end=9),
    simuPOP.MaSelector(loci=0, fitness=[1, 1.0033219854101134], begin=9, end=10)
]
```

## Typing Challenge
### Admixture Analysis

Write a function that plots admixutre results for any number of populations generated

Requirements
 - Declare all types for all variables
 - No for-loops

```R
#   admixture: matrix with samples in columns and populations in rows
#       The names for samples and populations are in the colnames()
#       and rownames() properties of the matrix
#       The values for each cell of admixture are all
#       floating point values (numeric type in R)
plotAdmix <- function(admixture) {
    par(mar = c(8, 4, 4, 5) + 0.1) # Change the graphing parameters
    barplot(
        height = admixture, # R sums all the numeric types per column
        #   Sample from the list of colors, given the number of populations in the data
        col = sample(x = colors(), size = nrow(x = admixture), replace = FALSE),
        space = 0,
        border = NA,
        ylab = 'Admixture Proportion', # Character string for Y-label
        main = 'Admixture Analysis', # Character string for main label
        #   Use the column names (sample names) as the labels along the X-axis
        names.arg = colnames(x = admixture), 
        las = 2
    )
}
```