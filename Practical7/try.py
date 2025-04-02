import re

#define the function to cut introns from the sequence
def cut_introns(seq, donor, acceptor):
    introns = []
    donor_sites = [m.start() for m in re.finditer(donor, seq)]
    for i in donor_sites:
        A = re.search(acceptor, seq[i+2:])
        if A:
            new_introns = seq[i:A.start()+2+i+2]
            introns.append(new_introns)

    return introns

seq = ''
gene_name = ''
total_introns = []
#read the input file and write the output file
combination = str(input("Enter the splice donor/acceptor combination (GTAG, GCAG, ATAC): "))

if combination == 'GTAG':
    with open ('tata_genes.fa', "r") as file, open('GTAG_spliced_genes.fa', "w") as out:

        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if seq:
                    #to check the squence of ATAT box in the introns
                    total_introns = cut_introns(seq, 'GT', 'AG')  #cut the introns from the sequence
                
                    for one_intron in total_introns:
                        if gene_name and re.search(r'TATA[AT]A[AT]', one_intron):
                            out.write('>' + gene_name[0] + '\n' + one_intron + '\n')

                    seq = '' #reset the sequence for the next gene
                    total_introns = []
                
                gene_name = re.findall(r'>(\S+)', line)
        
            else:
                seq += line.strip()
    print(f"Results saved to GTAG_spliced_genes.fa")
                