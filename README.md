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

## **Implementation Overview**

This section briefly explains the logic behind each component of the project, especially the utility modules used to build the glossary.

### **GlossaryEntry Class**
To streamline the management of glossary entries, a `GlossaryEntry` class was created. This class simplifies how terms, variants, tokens, definitions, and examples are stored and accessed, making the overall process modular and maintainable.

---

### **1. `extract_terms.py`**
This module identifies potential glossary terms using regex.
- **Preprocessing:** Removes HTML tags, non-alphanumeric characters, and extra whitespace to clean the corpus.
- **Pattern Matching:** Custom regex patterns are applied to capture:
  - **snake_case terms**
  - **camelCase terms**
  - **ACRONYMS**
- The output is a list of filtered, cleaned technical terms likely to be relevant to the domain.

---

### **2. `group_variants.py`**
This module clusters term variants using Levenshtein distance.
- **Frequency Analysis:** Word frequencies are computed to prioritize more common terms.
- **Clustering Logic:**
  - Iterates through each term.
  - If a term has already been grouped (tracked in a `visited` set), it is skipped.
  - Otherwise, it checks the Levenshtein distance between the current term and all others.
  - If the distance is within a defined threshold, the term is considered a variant.
- **Canonical Selection:** The most frequent term in the group is chosen as the canonical term using `max(variants, key=lambda x: freq[x])`.
- **Output:** A dictionary where each canonical term maps to a list of its variants.

---

### **3. `tokenize.py`**
This module tokenizes the final list of canonical terms using a custom BPE tokenizer from HuggingFace.
- **Tokenizer Initialization:**
  - A BPE tokenizer is defined and configured.
  - Text is normalized (lowercased, cleaned using regex).
- **Pre-tokenization:** Defines how to split input (e.g., by whitespace).
- **Training:**
  - Trained on the cleaned corpus.
  - Vocabulary size is tuned, with minimum frequency set to 1.
  - Special tokens are added.
- **Persistence:** The tokenizer can be saved and reloaded for reuse.
- **Final Output:** A dictionary mapping each term to its list of tokens.

---

### **4. `define_terms.py`**
This module sends each canonical term to a locally running Ollama model (Phi3) for definition and example generation.
- **POST Requests:** Sends a custom prompt for each term via a POST request.
- **Prompt Tuning:** Prompts are designed to elicit a valid JSON response containing both the **definition** and an **example**.
- **Response Handling:** Parses and stores the response, ensuring JSON consistency by modifying the model's response format.

### **Examples**

python cli.py search Convolutional Neural Netw
Closest match: Convolutional Neural Networks

python cli.py define CNN                 
Canonical: CNN
Definition: Convolutional Neural Networks (CNN) are deep learning algorithms that can take in an input image, assign importance to various aspects of the image and differentiate one from another.
Example: In facial recognition systems, CNN is often used for identifying unique features on a person'in face.

python cli.py listw --count=20
Term                                          # of Variants
------------------------------------------------------------
A2Aform                                       0
AI                                            0
AI-assisted                                   0
AI-based                                      0
AUC                                           0
AWS                                           0
Agent-to-Agent                                1
Agents Model Context                          0
Architectures Deep                            0
Artificial Neural Networks                    0
Auto-ML                                       0
BERT                                          0
CICD                                          0
CNN                                           0
Collaborative Protocols The                   0
Common Algorithms Machine                     0
Communication Autonomous                      0
ConvNets                                      0
Convolutional Neural Networks                 0
Cutting-edge                                  0

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