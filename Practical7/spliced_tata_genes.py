import re

option = ['GTAG', 'GCAG', 'ATAC']

print("possible splice donor/acceptor combinations: GTAG, GCAG, ATAC")
while True:
    splice = input("input a splice combination: ").strip().upper()
    if splice in option:
        break
    print("Meaningless input. Please choose from GTAG, GCAG, ATAC.")

start = splice[:2]
finish = splice[-2:]

input = open ('tata_genes.fa','r')
output1 = f'{splice}_spliced_genes.fa'
output = open (output1,'w')

tata = re.compile(r'TATA[AT]A[AT]')
pattern = re.compile(rf"{start}[ACGT]+") 

currentseq = ''
currentname = 'unknown_gene'

for line in input:
    if re.search ('>', line):  
        if currentseq:
            full = ''.join(currentseq)

            while re.search(start, full):
                 cut1 = re.search(start, full)
                 place1 = cut1.start() 
                 cut = full[place1:]
                 cut2 = re.search(finish, cut)

                 if cut2:
                      place2 = cut2.start() + 2
                      gene = cut[:place2]
                      if re.search(tata, gene):
                           number = len(re.findall(tata, gene))
                           output.write(f'>{currentname} TATA_count={number}\n{gene}\n')
                           full = cut[place2:]

        currentseq = ''
        getname = re.search(r'>(\S+)', line)
        currentname = getname.group(1) if getname else "unknown_gene"
    
    else:
        currentseq += line.strip()

if currentseq:
     full = ''.join(currentseq)
     while re.search(start, full):
             cut = pattern.findall(full)
             cut2 = re.search(finish, cut)

             if cut2:
                  place2 = cut2.start() + 2
                  gene = cut[:place2]
                  if re.search(tata, gene):
                       number = len(re.findall(tata, gene))
                       output.write(f'>{currentname} TATA_count={number}\n{gene}\n')
                       full = cut[place2:]

print(f"Results saved to {output1}")
