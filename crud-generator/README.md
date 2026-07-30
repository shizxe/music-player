# CRUD Generator Setup

This folder contains a Python-based CRUD generator that works with Laravel project files.

## Requirements

The generator uses these Python packages:
- Jinja2
- openpyxl
- pandas

## Step-by-step installation

### 1. Go to the project root

```bash
cd ~/laravel-project/backend-api
```

### 2. Check Python

Make sure Python 3 is installed:

```bash
python3 --version

sudo apt update
sudo apt install python3 python3-pip
```

### 3. Install Python packaging tools

On Ubuntu or Debian systems:

```bash
sudo apt update
sudo apt install -y python3-venv python3-pip
```

### 4. Create a virtual environment (recommended)

```bash
cd crud-generator
python3 -m venv .venv
source .venv/bin/activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

If you prefer to install them manually:

```bash
pip install Jinja2 openpyxl pandas
```

## Run the generator

From the project root:

```bash
bash crud-generator/generate.sh crud-generator/module.xlsx
```

Or directly with Python:

```bash
cd crud-generator
source .venv/bin/activate
python generator.py ../crud-generator/module.xlsx
```

## Troubleshooting

If you see an error like:

```bash
ModuleNotFoundError: No module named 'openpyxl'
```

it means the dependencies are not installed in the current Python environment. Re-run:

```bash
pip install -r requirements.txt
```
