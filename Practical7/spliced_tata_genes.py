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
            part = ''.join(currentseq)

            while re.search(start, part):
                cut1 = re.search(start, part)
                place1 = cut1.start() 
                cut = part[place1:]
                cut2 = re.search(finish, cut)

                if cut2:
                    place2 = cut2.start() + 2
                    gene = cut[:place2]
                    if re.search(tata, gene):
                        number = len(re.findall(tata, gene))
                        output.write(f'>{currentname} TATA_count={number}\n{gene}\n')
                    part = cut[place2:]

                else:
                    break

        currentseq = ''
        getname = re.search(r'>(\S+)', line)
        currentname = getname.group(1) if getname else "unknown_gene"
    
    else:
        currentseq += line.strip()

if currentseq:
    part = ''.join(currentseq)

    while re.search(start, part):
        cut1 = re.search(start, part)
        place1 = cut1.start() 
        cut = part[place1:]
        cut2 = re.search(finish, cut)

        if cut2:
            place2 = cut2.start() + 2
            gene = cut[:place2]
        
            if re.search(tata, gene):
                number = len(re.findall(tata, gene))
                output.write(f'>{currentname} TATA_count={number}\n{gene}\n')
            part = cut[place2:]

        else:
            break

print(f"Results saved to {output1}")
input.close()
output.close()