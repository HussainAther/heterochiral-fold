# Heterochiral Foldability Pipeline

```
heterochiral-fold/
├── .github/                # CI/CD for automated testing of Python scripts
├── data/
│   ├── raw/                # Original sequence lists (simplified alphabets)
│   └── processed/          # AF3 outputs and PDB files
├── models/
│   ├── af3_templates/      # JSON skeletons for AlphaFold 3 "hacks"
│   └── martini_itp/        # Custom MARTINI 3.0 force field parameters
├── notebooks/              # For Dick to see the "results" quickly
│   ├── 01_af3_confidence_analysis.ipynb
│   └── 02_rmsd_stability_plots.ipynb
├── scripts/                # The "Engine"
│   ├── sequence_engine.py  # Generates permutations of D-L sequences
│   ├── fold_wrapper.py     # Automates AF3 JSON generation
│   ├── martini_builder.py  # Converts PDBs to coarse-grained topologies
│   └── thermal_screen.py   # MD analysis script for temperature effects
├── environment.yml         # Conda environment for reproducibility
├── README.md               # The project "Manifesto"
└── LICENSE                 # (e.g., MIT or Apache 2.0)
```

This project investigates the "borderlands of foldability" by mapping the 
structural landscape of mixed D-L peptides. 

## Research Context
Following our work on *Cold-Selective Topological Bias*, we hypothesize that 
thermal environments not only selected the lipid "vessel" but also 
constrained the "contents"—the first folding polymers.

## Pipeline Features
* **AF3-Chiral:** A Python wrapper to extend AlphaFold 3's predictive power 
  to heterochiral sequences.
* **Selection Filter:** Automated screening for $pLDDT$ (confidence) 
  vs. chiral noise.
* **Membrane Integration:** Direct export to MARTINI 3.0 for 
  thermodynamic stability testing in prebiotic bilayers.

## Key Questions
1. Does a "Cold-Selective" membrane stabilize D-L folds that fail in bulk water?
2. Is there a "critical chirality" threshold where foldability collapses?

