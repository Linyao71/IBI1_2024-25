'''
1. write a function to determine the restriction enzyme cut	sites within a supplied	DNA	sequence
2. input 2 parameters: (1) the DNA sequence	(2) the	sequence recognised	by the enzyme
3. return positions where the enzyme cuts
'''
AA = {'A','T','C','G'}

while True:
    DNA = input("please input the DNA sequence to be cut: ").strip().upper()
    flag1 = True

    for AADNA in DNA:
        if AADNA not in AA:
            print("Faulty DNA sequence, please re-enter") 
            flag1 = False
            break       

    if flag1:
        break

while True:
    recognised_sequence = input("please input the sequence recognised by the restriction enzyme: ").strip().upper()
    flag2 = True
    if len(recognised_sequence) > len (DNA):
        print("Faulty recognised sequence, please re-enter") 
        flag2 = False
        break   
        

    for AArecognised_sequence in recognised_sequence:
        if AArecognised_sequence not in AA:
            print("Faulty recognised sequence, please re-enter") 
            flag2 = False
            break       

    if flag2:
        break

def find(dna, recognised):
    cut_length = len(recognised)
    cut_site = []
    
    for i in range(len(dna) - cut_length + 1):
        if dna[i:i + cut_length] == recognised:
            cut_site.append(i)  
    
    return cut_site

site = find(DNA, recognised_sequence)
if len(site) == 0:
    print("There is no enzyme cutting position")
elif len(site) == 1:
    print(f"the enzyme cutting position is {site}")
else:
    print(f"the enzyme cutting position are {site}")

'''runing example:
>please input the DNA sequence to be cut: 
>ATCGTACGGATCCGATACCTAGATCCGGAATTCX
>Faulty DNA sequence, please re-enter

>please input the DNA sequence to be cut: 
>ATCGTACGGATCCGATACCTAGATCCGGAATTC

>please input the sequence recognised by the restriction enzyme: 
>GGATCCX
>Faulty recognised sequence, please re-enter

>please input the sequence recognised by the restriction enzyme: 
>GGATCC

>the enzyme cutting position is [7]
'''