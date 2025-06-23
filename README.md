# **Auto-Glossary-Builder-QA-Assistant**

This project uses **regex, levenshtein, bpe and ollama local models** to generate a glossary for a given group of txt files.This glossary includes: terms, variations, tokens, and a definition and example. Then, it provides a cli for users to get specific information about it.

---

## **Prerequisites**

- **Python version 3.8 - 3.11** must be installed on your system.

---

## **Project Structure**

```
Auto-Glossary-Builder-QA-Assistant/
├── GlossaryEntry.py           # Class to manage glossary entries 
├── build_glossary.py          # Builds the glossary
├── cli.py                     # CLI for users using click library
├── requirements.txt           # Project dependencies
├── corpus/                    # txt files to build the glossary
├── utils/                     # Utility functions used by build_glossary
│   ├── extract_terms.py       # Uses regex to extract list of potential terms.
│   ├── group_variants.py      # Uses levenshtein to extract final terms and variants.
│   ├── tokenize.py            # Uses BPE to tokenize terms
│   └── define_terms.py        # Makes request to local Ollama model to define and exemplify terms.
```

---

## **Steps to Run the Project**

### 1. Clone the repository

```bash
git clone https://github.com/cesarsiuu2316/Auto-Glossary-Builder-QA-Assistant.git
```

---

### 2. Create and Activate a Virtual Environment

It’s recommended to use a virtual environment:

```bash
# Create the virtual environment using pip
python -m venv venv
```

Or specify Python version:

```bash
py -3.11 -m venv venv
```

Activate it 

```bash
# Activate environment
venv\Scripts\activate
```

---

### 3. Install Dependencies

With the virtual environment active:

```bash
pip install -r requirements.txt
```

---

### 4. Run the Project

```bash
python cli.py <command> # Commands: list, define, search, use --help to get more information
```