import os
import re


# Read all text files in corpus
def read_text_files_as_strings(file_path):
    text = ""
    for file in os.listdir(file_path):
        if file.endswith('.txt'):
            with open(os.path.join(file_path, file), 'r', encoding='utf-8') as f:
                text += f.read() + "\n"
    return text


def clean_text_as_list(text):
    # Remove non-alphanumeric characters except for spaces
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Remove extra spaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    # Remove html tags
    cleaned_text = re.sub(r'<[^>]+>', '', cleaned_text)
    # Split the text into words and remove empty strings
    words = [word for word in cleaned_text.split() if word]
    return words


def load_and_clean_corpus(file_path):
    text = read_text_files_as_strings(file_path)
    return clean_text_as_list(text)