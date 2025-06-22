from GlossaryEntry import GlossaryEntry
import json
import os


TXT_FILE_PATHS = "corpus"


def read_text_files_as_strings():
    text = ""
    for file in os.listdir(TXT_FILE_PATHS):
        if file.endswith('.txt'):
            with open(os.path.join(TXT_FILE_PATHS, file), 'r', encoding='utf-8') as f:
                text += f.read() + "\n"
    return text


def save_glossary_to_json(glossary, filename):
    with open(filename, 'w') as f:
        json.dump(glossary, f, indent=4)


def convert_glossary_to_json(entry_list):
    return {
        "Glossary": {
            entry.term: entry.to_dict() for entry in entry_list
        }
    }


def main():
    entry_list = []
    entry = GlossaryEntry(
        term="Python",
        variants=["py", "python3"],
        tokens=["programming", "language"],
        definition="A high-level programming language known for its readability and versatility.",
        example="Python is widely used in web development, data analysis, artificial intelligence, and more."
    )
    entry_list.append(entry)

    glossary_json = convert_glossary_to_json(entry_list)
    save_glossary_to_json(glossary_json, 'glossary.json')
    

if __name__ == "__main__":
    main()