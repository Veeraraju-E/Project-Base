# Project-Base
A simple python script to build up the base folders for any ML project.

## Usage
- clone the repo
- run the python script:
  
```bash
python create_project.py path/to/your/project
```
- This creates the following tree structure

```tree
ProjectName/
├── configs/
│   └── train.yaml
├── data/
├── datasets/
├── docs/
│   └── overview.md
├── outputs/
│   └── plots/
├── scripts/
│   └── train.py
├── src/
│   ├── models/
│   └── trainers/
├── README.md
└── requirements.txt
```

## Future
- bash scripts and cookiecutter templates coming soon
