import subprocess
import os

def convert_to_martini(pdb_path, output_top):
    """
    Uses martinize2 to convert the AF3 output to MARTINI 3.0.
    """
    if not os.path.exists(pdb_path):
        print(f"Error: {pdb_path} not found. Run AF3 first.")
        return

    # command: martinize2 -f input.pdb -itp output.itp -ff martini30 -p backbone
    cmd = [
        "martinize2",
        "-f", pdb_path,
        "-itp", output_top,
        "-ff", "martini30",
        "-p", "backbone",
        "-scfix" # Crucial for keeping sidechain geometry stable
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"Successfully created MARTINI topology: {output_top}")
    except subprocess.CalledProcessError as e:
        print(f"Martinize2 failed: {e}")

if __name__ == "__main__":
    # Placeholder for when you have the AF3 results
    # convert_to_martini("data/processed/all_L_model.pdb", "models/martini_itp/all_L.itp")
    print("Builder ready. Awaiting PDB inputs from AlphaFold.")
