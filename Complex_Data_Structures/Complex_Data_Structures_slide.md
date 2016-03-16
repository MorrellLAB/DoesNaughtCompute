#Complex Data Structures 
###_Does[0]compute?_   
####March 11, 2016    
####Li Lei & Jeffrey Neyhart   

###Data Structures to Cover:  
- **Less complex** 
    - ####Lists 
    - ####Sets 
    - ####Tuples 
    - ####Dicts 
- ###**Somewhat complex** 

* ####Lists of lists 

* ####Lists of dicts 

* ####Lists of tuples 

>###**More complex** 

* ####Dicts of sets 

* ####Dicts of tuples 

* ####Dicts of lists 

* ####Nested lists 

Newline

>###Lists, tuple, set and dict 


| Type | What? |
| ---- | ----- |
| List | An **`unordered`**, **`mutable`** collection of primitive types |
| Tuple | An **`unordered`**, **`unmutable`** collection of primitive types |
| Set | An **`unordered`**, **`mutable`**, **`unique`** collection of primitive types |
| Dict | An **`unordered`**, **`mutable`** collection of primitive types stored in **`key: value`** pairs | 




>###Lists and lists of lists  

>>>#####An empty list
>>>`L = [ ]`    
#####four items : indexes 0..3 
>>>`L = [1, 2, 3, 4, 5]`  
>>> `print (L[0])`  
>>>#####1 
#####lists of lists, matrix 
>>> ` L = [`    
>>>>>`[1, 2, 3, 4],`    
>>>>> `[5, 6, 7, 8],`     
>>>>> `[9, 10, 11, 12]`    

>>>>>`]`    

>>>#####index
>>> `print (L[1])`   
[5, 6, 7, 8]   
>>> `print (L[1][2])`   
7 

>###Operations of lists  
>>>#####concatenate  
>>> `[1,2,3] + [4,5,6]`   
[1, 2, 3, 4, 5, 6] 
>>>#####repeat 
>>> `['Li']*4`  
['Li', 'Li', 'Li', 'Li'] 
>>>#####iteration 
>>> `for x in L:`     
>>>> `print (x)`  
[1, 2, 3, 4]   
[5, 6, 7, 8]   
[9, 10, 11, 12] 

>>>#####Methods  
>>> `L.append(4)`   
>>> `print (L)`   
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], 4]  
>>> `L.extend([13,14,15,16])`   
>>> `print (L)`   
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], 
13, 14, 15, 16]  
>>>`L.pop()`   
[9, 10, 11,12]   
>>> `seq = ['A','G','T','C','G','G','T']`   
>>> `seq.reverse()`   
>>> `print (seq)`   
['T', 'G', 'G', 'C', 'T', 'G', 'A']   
>>> `seq.insert(2,'basepairs')`   
>>> `print (seq)`   
['A', 'G', 'basepairs', 'T', 'C', 'G', 'G', 'T']   
>>> `del L[1:]`  
>>> `print (L)`   
[[1, 2, 3, 4]]   

>###Tuples  
>>>#####An empty tuple 
>>> `T = ()`  
>>>#####A four-item tuple 
>>> `T = (0,'Li','2','apples')`  
>>>#####Nested tuples 
>>> `T = (`  
>>>>>`('Li','Jeff'),`  
>>>>>`('Tom','Chaochih'),`  
>>>>>`('Paul','Shawn')`  
  
>>>>>`)`
    
>>> `print (T[1])`     
('Tom', 'Chaochih')   
>>> `print (T[1][0])`   
#####Tom 
 

>>>#####Iteration 
>>> `for e in T:` 
>>>> `print (e)`   
('Li', 'Jeff')  
('Tom', 'Chaochih')   
('Paul', 'Shawn')
  
>>>#####index 
>>> `T.index(('Tom','Chaochih'))`   
1  
>>> `del T[1:]`   
Traceback (most recent call last):   
  File "`<stdin>`", line 1, in `<module>`   
TypeError: 'tuple' object does not support   
item deletion 
 
>###Tuples' operations  
>>> `T.pop()`  
Traceback (most recent call last):   
  File "`<stdin>`", line 1, in `<module> `  
AttributeError: 'tuple' object has no attribute   
'pop' 
 
>>> `T.sort()`   
Traceback (most recent call last):   
  File "`<stdin>`", line 1, in `<module>` 
AttributeError: 'tuple' object has no attribute   
'sort' 
 
>>> `T.extend((2,3))`   
Traceback (most recent call last):   
  File "`<stdin>`", line 1, in `<module>`  
AttributeError: 'tuple' object has no attribute 
'extend' 
 
 
 >###Similarity vs. difference of lists and tuples   
>>>`Differences`  |   `Similarities` 


>###Sets 
>>>#####A empty set 
>>> `S = {}`    
>>>#####straightforward construct a set 
>>> `S = {1,2,3}`  
 
>>>#####convert to set 
>>> `l = [1,2,3]`   
>>> `S = set(l)`   
>>> `S`   
{1, 2, 3} 
 
>>>#####uniq 
>>> `l = [1,2,3,3]`   
>>> `S = set(l)`   
>>> `S`    
{1, 2, 3}  

>###Set operations 
>>>#####fast membership testing 
>>> `1 in s`   
True   
>>> `4 in s`   
False   
>>> `set1 = set(['Shawn','Paul','Chaochih','Tom','Li','Jeff'])`   
>>> `set2 = set(['Felipe','Skylar','Paul','Chaochih','Peter','Ana'])`   
>>>#####Union 
>>> `set1 |set2`   
{'Chaochih', 'Li', 'Paul', 'Jeff', 'Felipe', 'Peter', 'Skylar', 'Shawn', 'Ana', 
'Tom'} 
>>>#####Intersection 
>>>`set1 & set2`   
{'Chaochih', 'Paul'} 
 
>>>#####difference 
>>> `set1 - set2`   
{'Shawn', 'Tom', 'Li', 'Jeff'} 
 

>>>#####symmetric difference (elements that are in the first set and the second, but not in both) 

>>> `set1 ^ set2`   
{'Tom', 'Felipe', 'Peter', 'Li', 'Skylar', 'Shawn', 'Ana', 'Jeff'} 
 
>###Summary 

>When to use lists:   
* Need to be ordered 
* Need to be changed or extended 
* Do not need  to be unique  

>When to use tuple:  
* Store your data in logical immutable pairs, triples etc. 
* Store data that doesn’t have to change   

>When to use set:  
* A unique set of data 
* Constantly changes: Sets, just like lists, are mutable 
* Mathematically: difference, union, intersection, etc. 
* Do not need to store nested lists, sets: Sets don’t support 
unhashable types 

>###Exercise1 

>####Adapter trimming: 
>>The file seq.txt contains a number of DNA sequences, one per line. 
Each sequence starts with the same 14 base pair fragment – a 
sequencing adapter that should have been removed. Write a program 
that will (1) trim this adapter and write the cleaned sequences to a new 
file and (2) print the length of each sequence to the screen.  
 

>###More Complex Structures 

* Lists of dicts 

* Lists of tuples 

* Dicts of lists 

* Dicts of sets 

* Dicts of tuples 

>###Lists of dicts

>>>#####List of dictionaries
>>>`enzyme =[`  
>>>>>>`{'name' : 'ApeKI', 'organism' : 'Aeropyrum pernix', 'site' : '[G|C]WGC'},`    
>>>`{'name' : 'PstI', 'organism' : 'Providencia stuartii', 'site' : 'CTGC[A|G]'},`   
>>>`{'name' : 'HindIII', 'organism' : 'Haemophilus influenzae', 'site' : '[A|A]GCTT'}`  
>>>`]`  

>>>#####We can iterate over the records and call upon dictionary values with a key 
>>>`for record in enzymes:`   
>>>>>`print("Enzyme: " + record['name'])`  
>>>>>`print("Species: " + record['organism'])`  

>>>Enzyme: ApeKI   
Species: Aeropyrum pernix   
Enzyme: PstI 
Species: Providencia stuartii   
Enzyme: HindIII   
Species: Haemophilus influenzae   



>###List of tuples 

>>>#####However if the order of dictionary items is constant, a list of tuples may be more appropriate 
>>>`enzymes = [`   
>>>>>>>`('ApeKI', 'Aeropyrum pernix', '[G|C]WGC'),`   
>>>>>>>`('PstI', 'Providencia stuartii', 'CTGC[A|G]'),`   
>>>>>>>`('HindIII', 'Haemophilus influenzae', '[A|A]GCTT')`   
>>>>>>>`]`   

 
>>>#####We can similarly iterate over the list, however now we don’t need to call values with a key 
>>> `for record in enzymes:`   
>>>>>`print("Enzyme: " + record[1])`   
 `print("Species: " + record[2])` 

>>>Enzyme: ApeKI   
Species: Aeropyrum pernix   
Enzyme: PstI   
Species: Providencia stuartii   
Enzyme: HindIII   
Species: Haemophilus influenzae   

>###Dicts of sets 

>>>#####Create a dictionary of sets for enzymes used in GBS experiments (most of this is made up) 
>>>`enzyme_sets = {`   
>>>>>>>>`'maize' : {'ApeKI', 'HpaII', 'MseI'},`   
 `'wheat' : {'PstI', 'MspI', 'MseI', 'BamHI'},`   
 `'barley' : {'PstI', 'MspI', 'ApoI',},`   
 `'soybean' : {'ApeKI', 'SbfI', 'NdeI', 'ApoI'}`  
`}` 

 
>>>#####This allows us to quickly ask some questions, for instance: with what species can we use ‘ApeKI’? 
>>>`for species, enzyme in enzyme_sets.items():`   
>>>>>`if 'ApeKI' in enzyme:`    
>>>>>>>>>>`print(species)` 
  
>###Dicts of tuples 

>>>#####If we are confident that elements are unique to records, we can store the information as a dictionary of 
>>>#####tuples for quick look-up 
>>>`enzymes = {`   
>>>>>>>`'ApeKI' :  ('Aeropyrum pernix', '[G|C]WGC'),`   
>>>>>>>`'PstI' : ('Providencia stuartii', 'CTGC[A|G]'),`  
>>>>>>>`'HindIII' : ('Haemophilus influenzae', '[A|A]GCTT')`   
>>>>>>>`}` 
 
>>>#####We can quickly access a record by using the element name 
>>> `my_record = enzymes.get('ApeKI')`   

>###Dicts of lists 

>>>#####A dict of lists allows one to look up multiple values from a single key 
>>> `dna = 'aattggaattggaattg'`   
>>>`k = 4`  
>>>`kmer2list = {}`   
>>>`for start in range(len(dna) - k + 1):`   
 >>>>>`kmer = dna[start:start+k]`   
 >>>>>`list_of_positions = kmer2list.get(kmer, [])` 
 >>>>>`list_of_positions.append(start)`   
 >>>>>`kmer2list[kmer] = list_of_positions`   
 
 >>> `print(kmer2list)`   
 {'ggaa': [4, 10], 'aatt': [0, 6, 12], 'gaat': [5, 11], 'tgga': [3, 9], 'attg': [1, 7, 13], 'ttgg': [2, 8]} 
>>>#####We can then look up the positions of any one kmer 
>>> `print(kmer2list.get('aatt'))`   
 ######[0, 6, 12] 
 
 

>###Exercise 2 

>>>Let’s reuse the `TAIR10_Chr4.gff` file from last session   
For this exercise, find the start positions of all exons for each gene ID (i.e. 
AT4G00570.1) and store them as a `dictionary of lists`. Next, find all exon start 
positions for the gene id: `AT4G00570.1` 

