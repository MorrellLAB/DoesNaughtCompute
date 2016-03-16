#!/usr/bin/env python

# Restriction enzyme cut information
# enzymes = [
# 	{'name' : 'ApeKI', 'organism' : 'Aeropyrum pernix', 'site' : '[G|C]WGC'},
# 	{'name' : 'PstI', 'organism' : 'Providencia stuartii', 'site' : 'CTGC[A|G]'},
# 	{'name' : 'HindIII', 'organism' : 'Haemophilus influenzae', 'site' : '[A|A]GCTT'}
# ]

# for record in enzymes:
# 	print("Enzyme: " + record['name'])
# 	print("Species: " + record['organism'])

# Store as list of tuples
# enzymes = [
# 	('ApeKI', 'Aeropyrum pernix', '[G|C]WGC'),
# 	('PstI', 'Providencia stuartii', 'CTGC[A|G]'),
# 	('HindIII', 'Haemophilus influenzae', '[A|A]GCTT')
# ]

# for record in enzymes:
# 	print("Enzyme: " + record[1])
# 	print("Species: " + record[2])

# Create a dict of sets of enzymes in GBS experiments
# enzyme_sets = {
# 	'maize' : {'ApeKI', 'HpaII', 'MseI'},
# 	'wheat' : {'PstI', 'MspI', 'MseI', 'BamHI'},
# 	'barley' : {'PstI', 'MspI', 'ApoI',},
# 	'soybean' : {'ApeKI', 'SbfI', 'NdeI', 'ApoI'}
# }

# # Parse
# for species, enzyme in enzyme_sets.items():
# 	if 'ApeKI' in enzyme:
# 		print(species)


# # Store enzyme information as a dict of tuples
# enzymes = {
# 	'ApeKI' :  ('Aeropyrum pernix', '[G|C]WGC'),
# 	'PstI' : ('Providencia stuartii', 'CTGC[A|G]'),
# 	'HindIII' : ('Haemophilus influenzae', '[A|A]GCTT')
# }

# # Call on records by using the element
# my_record = enzymes.get('ApeKI')

# # Tuple unpacking within dict
# (my_species, my_site) = enzymes.get('ApeKI')

# print(my_species)

# dna = 'aattggaattggaattg'
# k = 4
# kmer2count = {}
# for start in range(len(dna) - k + 1):
# 	kmer = dna[start:start+k]
# 	current_count = kmer2count.get(kmer, 0)
# 	kmer2count[kmer] = current_count + 1

# print(kmer2count)

# dna = 'aattggaattggaattg'
# k = 4
# kmer2list = {}
# for start in range(len(dna) - k + 1):
# 	kmer = dna[start:start+k]
# 	list_of_positions = kmer2list.get(kmer, [])
# 	list_of_positions.append(start)
# 	kmer2list[kmer] = list_of_positions

# print(kmer2list)

# print(kmer2list.get('aatt'))


# Exercise
# The exercise will be to create a dictionary of lists, where the keys
## are the gene names and the values are lists of start positions of exons
import sys
filename = sys.argv[1]

gene_id_list = {}

with open(filename, 'r') as f:
	# Iterate over the lines in the file
	for line in f:
		# Split the line
		tmp = line.strip().split('\t')
		# Find the annotation name
		annotation = tmp[2]

		# If the annotation is an exon, find the gene ID name
		if annotation == 'exon':
			description = tmp[8]
			gene_id = description.split('=')[1]
			gene_parent = gene_id.split('.')[0]

			# Find the exon position
			exon_pos = tmp[3]

			# Look for the gene id in the gene_id_list
			# If absent, return a blank list
			list_of_exon_positions = gene_id_list.get(gene_id, [])
			# Append the exon position
			list_of_exon_positions.append(exon_pos)
			# Add the gene_id as a key
			gene_id_list[gene_id] = list_of_exon_positions

my_favorite_gene_id = gene_id_list.get('AT4G00570.1')
print my_favorite_gene_id






























