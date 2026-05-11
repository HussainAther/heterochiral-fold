
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
