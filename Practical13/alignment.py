import requests
from Bio import SeqIO
from io import StringIO
from Bio.Align import substitution_matrices
import random

# Get 2 protein sequences from UniProt
def get_uniprot_sequence(uniprot_id):
    url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    fasta_data = response.text
    record = SeqIO.read(StringIO(fasta_data), "fasta")
    return str(record.seq)

# Get the BLOSUM62 matrix
blosum62 = substitution_matrices.load("BLOSUM62")

def calculate_alignment(seq1, seq2, blosum):
    total_score = 0
    identical = 0
    for aa1, aa2 in zip(seq1, seq2):
        try:
            score = blosum[aa1, aa2]
        except KeyError:  # Handle non-standard amino acids
            score = -4  # Default gap penalty
        total_score += score
        if aa1 == aa2:
            identical += 1
    
    percent_identity = (identical / len(seq1)) * 100
    return total_score, percent_identity

human_seq = get_uniprot_sequence("P04179")
mouse_seq = get_uniprot_sequence("P09671")

amino_acids = 'ACDEFGHIKLMNPQRSTVWY'  # standard amino acids
random_seq = ''.join(random.choice(amino_acids) for AA in range(len(human_seq)))

# Calculate scores
human_mouse_score, human_mouse_identity = calculate_alignment(human_seq, mouse_seq, blosum62)
human_random_score, human_random_identity = calculate_alignment(human_seq, random_seq, blosum62)
mouse_random_score, mouse_random_identity = calculate_alignment(mouse_seq, random_seq, blosum62)
        
# Print results
print("Human sequence:", human_seq)
print("Mouse sequence:", mouse_seq)
print("Random sequence:", random_seq)
print(f"sequence length: {len(human_seq)}")
print("\nAlignment results:")
print(f"Human vs Mouse - alignment score: {human_mouse_score}, Percent Identity: {human_mouse_identity:.2f}%")
print(f"Human vs Random - alignment score: {human_random_score}, Percent Identity: {human_random_identity:.2f}%")
print(f"Mouse vs Random - alignment score: {mouse_random_score}, Percent Identity: {mouse_random_identity:.2f}%")