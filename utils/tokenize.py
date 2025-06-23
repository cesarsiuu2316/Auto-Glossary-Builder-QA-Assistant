from tokenizers import Tokenizer, pre_tokenizers
from tokenizers.models import BPE
from tokenizers.normalizers import Sequence, Lowercase, NFD
from tokenizers.trainers import BpeTrainer
import re


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
    tokenizer.pre_tokenizer = pre_tokenizers.Whitespace() # Use whitespace as the pre-tokenizer
    return Tokenizer


# Train the tokenizer on the cleaned corpus
def train_tokenizer(corpus):
    
    cleaned_corpus = clean_corpus(corpus)  # Clean the corpus text
    tokenizer = initialize_tokenizer()  # Initialize the tokenizer
    # Set up the trainer with specific parameters
    trainer = BpeTrainer(
        vocab_size=300,  # Set vocabulary size
        min_frequency=1,  # Minimum frequency for tokens to be included
        special_tokens=["[UNK]"]  # Define special tokens
    )
    tokenizer.train_from_iterator([cleaned_corpus], trainer=trainer) # Train the tokenizer
    return tokenizer  # Return the trained tokenizer