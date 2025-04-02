import re

option = ['GTAG', 'GCAG', 'ATAC']

print("possible splice donor/acceptor combinations: GTAG, GCAG, ATAC")
while True:
    splice = input("input a splice combination: ").strip().upper()
    if splice in option:
        break
    print("Meaningless input. Please choose from GTAG, GCAG, ATAC.")

input = open ('tata_genes.fa','r')
output1 = f'{splice}_spliced_genes.fa'
output = open (output1,'w')
currentseq = ''
currentname = "unknown_gene"

for line in input:
    if bool(re.match ('>', line)):  
        if currentseq:
            full = ''.join(currentseq)

            if re.search(splice, full):
                 number = len(re.findall(r'TATA[AT]A[AT]', full, re.IGNORECASE))
                 output.write(f'>{currentname} TATA_count={number}\n{full}\n')

        currentseq = []
        getname = re.search(r'>(\S+)', line)
        currentname = getname.group(1) if getname else "unknown_gene"
    
    else:
        currentseq += line.strip()

if currentseq:
        full = ''.join(currentseq)
        if re.search(splice, full):
            number = len(re.findall(r'TATA[AT]A[AT]', full, re.IGNORECASE))
            output.write(f'>{currentname} TATA_count={number}\n{full}\n')

print(f"Results saved to {output1}")
