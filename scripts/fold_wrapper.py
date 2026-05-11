import json
import csv
import os

def create_af3_json(name, sequence, chirality_string):
    """
    Constructs the AF3 JSON schema. 
    Note: In AF3, D-amino acids are often handled as custom ligands 
    or specific SMILES-defined residues to ensure stereochemistry.
    """
    residues = []
    for i, (aa, chiral) in enumerate(zip(sequence, chirality_string)):
        # If 'D', we use a custom definition (this is the 'extension' part)
        res_entry = {
            "count": 1,
            "id": aa,
            "modifications": [] 
        }
        if chiral == "D":
            # You can specify the D-isomer here using AF3's custom_residue logic
            # For now, we tag it for the pipeline to recognize
            res_entry["modifications"].append("D_ISOMER") 
        
        residues.append(res_entry)

    job_data = {
        "name": name,
        "modelContents": [
            {
                "polymer": {
                    "residues": residues
                }
            }
        ],
        "dialect": "alphafold3",
        "version": 1
    }

    os.makedirs("models/af3_templates", exist_ok=True)
    with open(f"models/af3_templates/{name}_input.json", "w") as f:
        json.dump(job_data, f, indent=4)

def run_conversion():
    with open("data/raw/sequence_library.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            create_af3_json(row['name'], row['sequence'], row['chirality'])
    print("AF3 JSON templates created in models/af3_templates/")

if __name__ == "__main__":
    run_conversion()
