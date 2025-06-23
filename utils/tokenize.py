from tokenizers import Tokenizer
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.models import BPE
from tokenizers.normalizers import Sequence, Lowercase, NFD
from tokenizers.trainers import BpeTrainer
import re
import os


TOKENIZER_PATH = "tokenizer.json"


# Load the tokenizer from a file if it exists
def load_tokenizer_from_file():
    path = "tokenizer.json"  # Path to the tokenizer file
    if os.path.exists(TOKENIZER_PATH):
        tokenizer = Tokenizer.from_file(TOKENIZER_PATH) # Ensure the tokenizer file exists
        return tokenizer
    return None


# Save the trained tokenizer to a file
def save_tokenizer_to_file(tokenizer):
    Tokenizer.save(tokenizer, TOKENIZER_PATH)


# Clean corpus for training of BPE tokenizer
def clean_corpus(text):
    text = text.lower()  # Lowercase
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove non-alphanumeric characters
    text = re.sub(r'\s+', ' ', text)  # Remove excess spaces
    return text.strip()


# Initialize a tokenizer with a BPE model
def initialize_tokenizer():
    tokenizer = Tokenizer(BPE()) # Set up a BPE tokenizer with an unknown token
    tokenizer.normalizer = Sequence([NFD(), Lowercase()]) #  Normalize text to unicode and lowercase
    tokenizer.pre_tokenizer = Whitespace() # Use whitespace as the pre-tokenizer
    return tokenizer


# Train the tokenizer on the cleaned corpus
def train_tokenizer(corpus):
    tokenizer = load_tokenizer_from_file()  # Load existing tokenizer if available
    if tokenizer:
        return tokenizer  # Return the loaded tokenizer if it exists
    
    cleaned_corpus = clean_corpus(corpus)  # Clean the corpus text
    tokenizer = initialize_tokenizer()  # Initialize the tokenizer
    # Set up the trainer with specific parameters
    trainer = BpeTrainer(
        vocab_size=100,  # Set vocabulary size
        min_frequency=1,  # Minimum frequency for tokens to be included
        special_tokens=["[UNK]"]  # Define special tokens
    )
    tokenizer.train_from_iterator([cleaned_corpus], trainer=trainer) # Train the tokenizer
    save_tokenizer_to_file(tokenizer)  # Save the trained tokenizer to a file
    return tokenizer  # Return the trained tokenizer