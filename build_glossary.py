from utils.extract_terms import clean_text_as_list
from utils.group_variants import get_terms_with_variants
from utils.tokenize import train_tokenizer, tokenize_terms
from utils.define_terms import fetch_definitions_and_examples
from GlossaryEntry import GlossaryEntry
import json
import os


CORPUS_PATH = "corpus"  # Path to the corpus directory
GLOSSARY_PATH = "glossary.json"  # Path to save the glossary JSON file


# Read all text files in corpus
def read_text_files_as_strings(file_path):
    text = ""
    for file in os.listdir(file_path):
        if file.endswith('.txt'):
            with open(os.path.join(file_path, file), 'r', encoding='utf-8') as f:
                text += f.read() + "\n"
    return text


# Save the glossary entries to a JSON file
def save_glossary_to_json(glossary, filename):
    with open(filename, 'w') as f:
        json.dump(glossary, f, indent=4)


# Convert the list of GlossaryEntry objects to a JSON-compatible dictionary
def convert_glossary_to_json(entry_list):
    return {
        "Glossary": {
            entry.term: entry.to_dict() for entry in entry_list
        }
    }


def main():
    corpus = read_text_files_as_strings(CORPUS_PATH)  # Read the corpus text

    terms = clean_text_as_list(corpus)  # Extract terms from the corpus
    print(f"Extracted {len(terms)} potential terms from the corpus.")
    print(f"Sample terms: {terms}")  # Print a sample of the extracted terms
    #entry_list.append(entry)
    #glossary_json = convert_glossary_to_json(entry_list)
    #save_glossary_to_json(glossary_json, 'glossary.json')


if __name__ == "__main__":
    main()