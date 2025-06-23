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
    corpus = read_text_files_as_strings(CORPUS_PATH)  # Read the corpus text files
    terms = clean_text_as_list(corpus)  # Extract terms from the corpus
    terms_with_variants_dict = get_terms_with_variants(terms)  # Get dictionary of terms with variants
    terms = list(terms_with_variants_dict.keys())  # Extract the unique terms
    tokenizer = train_tokenizer(corpus)  # Train the tokenizer on the corpus
    tokenized_terms = tokenize_terms(tokenizer, terms)  # Tokenize the terms
    definitions, examples = fetch_definitions_and_examples(terms)  # Fetch definitions and examples for the terms

    Glossary = []  # Initialize an empty list to hold GlossaryEntry objects

    i = 0
    for term in terms:
        variants = terms_with_variants_dict[term]["variants"]
        tokens = tokenized_terms.get(term, {}).get("tokens", [])
        entry = GlossaryEntry(
            term=term,
            variants=variants,
            tokens=tokens,
            definition=definitions[i] if i < len(definitions) else "",
            example=examples[i] if i < len(examples) else ""
        )
        Glossary.append(entry)
        i += 1

    glossary_json = convert_glossary_to_json(Glossary)
    save_glossary_to_json(glossary_json, 'glossary.json')


if __name__ == "__main__":
    main()