

import sys
import re

input = open ('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
tata = re.compile(r'TATA[AT][AT]', re.IGNORECASE)
output = open('tata_genes.fa','w')
currentseq = []
currentname = "unknown_gene"

for line in input:
    if bool(re.match ('>', line)):  
        if currentseq:
            full = ''.join(currentseq)
            if tata.search(full):
                at_sequences = re.findall(r'(AT[ACGT]+)', full)
                output.write(f">{currentname}\n{full}\n")
        currentseq = []
        match = re.search(r'gene:(\S+)', line)
        currentname = match.group(1) if match else "unknown_gene"
    
    else:
        currentseq.append(line.strip())

if currentseq:
        full = ''.join(currentseq)
        if tata.search(full):
            t_sequences = re.findall(r'(AT[ACGT]+)', full)
            output.write(f">{currentname}\n{full}\n")
