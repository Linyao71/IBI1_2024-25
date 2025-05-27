import re

option = ['GTAG', 'GCAG', 'ATAC']

# Prompt user for splice donor/acceptor combination
print("possible splice donor/acceptor combinations: GTAG, GCAG, ATAC")
while True:
    splice = input("input a splice combination: ").strip().upper()
    if splice in option:
        break
    print("Meaningless input. Please choose from GTAG, GCAG, ATAC.")

# Compile the regular expression for splice donor/acceptor
splice_tata = re.compile(splice[:2]+ r'.*'+ splice[-2:])

# Open the input file and output file
input = open ('tata_genes.fa','r')
output1 = f'{splice}_spliced_genes.fa'
output = open (output1,'w')

# Compile the regular expression for TATA box
tata = re.compile(r'TATA[AT]A[AT]')
currentseq = ''
currentname = "unknown_gene"

# Process the input file line by line
for line in input:

    if re.search ('>', line):  
        if currentseq:
            if re.search(splice_tata, currentseq):
                number = len(re.findall(tata, currentseq))
                if number > 0:
                    output.write(f'>{currentname} TATA count={number}\n{currentseq}\n')

        currentseq = ''
        getname = re.search(r'>(\S+)', line)

    else:
        currentseq += line.strip()

# process the last sequence
if currentseq:
    if re.search(splice_tata, currentseq):
        number = len(re.findall(tata, currentseq))
        if number > 0:
            output.write(f'>{currentname} TATA count={number}\n{currentseq}\n')

# tell the user the results are saved
print(f"Results saved to {output1}")