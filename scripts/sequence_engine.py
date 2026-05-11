import csv
import itertools
import os

def generate_chiral_library(base_sequence, max_permutations=100):
    """
    Generates permutations of L and D for a given sequence.
    Saves to data/raw/sequence_library.csv
    """
    n = len(base_sequence)
    # For long sequences, we sample randomly; for short ones, we can do all.
    # Here, we'll just demonstrate a systematic alternating or random approach.
    library = []
    
    # Example: Generate All-L, All-D, and Alternating L-D
    library.append({"name": "all_L", "sequence": base_sequence, "chirality": "L" * n})
    library.append({"name": "all_D", "sequence": base_sequence, "chirality": "D" * n})
    
    alt_pattern = "".join(["L" if i % 2 == 0 else "D" for i in range(n)])
    library.append({"name": "alternating_LD", "sequence": base_sequence, "chirality": alt_pattern})

    # Ensure directory exists
    os.makedirs("data/raw", exist_ok=True)
    
    with open("data/raw/sequence_library.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "sequence", "chirality"])
        writer.writeheader()
        writer.writerows(library)
    print(f"Generated {len(library)} sequences in data/raw/sequence_library.csv")

if __name__ == "__main__":
    # Test with a 10-mer of Alanine
    generate_chiral_library("AAAAAAAAAA")
