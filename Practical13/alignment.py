import requests
from Bio import SeqIO
from io import StringIO
from Bio.Align import substitution_matrices
import random

#1. Get 2 protein sequences from UniProt
def get_uniprot_sequence(uniprot_id):
    url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    fasta_data = response.text
    record = SeqIO.read(StringIO(fasta_data), "fasta")
    return str(record.seq)


#2. Generate a random sequence of same length
def generate_random_protein_sequence(length):
    amino_acids = 'ACDEFGHIKLMNPQRSTVWY'  # standard amino acids
    return ''.join(random.choice(amino_acids) for AA in range(length))

#3. Get the BLOSUM62 matrix
blosum62 = substitution_matrices.load("BLOSUM62")

#4. Get the alignment score abd percentage of identical amino acids with BLOSUM62
def calculate_alignment_score(seq1, seq2, matrix):
    edit_distance = 0
    
    for	i in range(len(seq1)):
        if seq1[i]!=seq2[i]:
            edit_distance += 1

    percent_identity = ((len(seq1)-edit_distance) / len(seq1)) * 100
    return edit_distance, percent_identity

human_seq = get_uniprot_sequence("P69905")
mouse_seq = get_uniprot_sequence("P01942")
random_seq = generate_random_protein_sequence(len(human_seq))

# Calculate scores
human_mouse_score, human_mouse_identity = calculate_alignment_score(human_seq, mouse_seq, blosum62)
human_random_score, human_random_identity = calculate_alignment_score(human_seq, random_seq, blosum62)
mouse_random_score, mouse_random_identity = calculate_alignment_score(mouse_seq, random_seq, blosum62)
        

# Print results
print("Human sequence:", human_seq)
print("Mouse sequence:", mouse_seq)
print("Random sequence:", random_seq)
print(f"sequence length: {len(human_seq)}")
print("\nAlignment results:")
print(f"Human vs Mouse - alignment score: {human_mouse_score}, Percent Identity: {human_mouse_identity:.2f}%")
print(f"Human vs Random - alignment score: {human_random_score}, Percent Identity: {human_random_identity:.2f}%")
print(f"Mouse vs Random - alignment score: {mouse_random_score}, Percent Identity: {mouse_random_identity:.2f}%")