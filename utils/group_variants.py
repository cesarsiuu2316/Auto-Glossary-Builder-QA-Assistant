from Levenshtein import distance
from collections import Counter
import re


# Get the term and its variants from the corpus
def get_terms_with_variants(terms, max_distance=3):
    word_counts = Counter(terms)  # Count the occurrences of each word in the corpus
    words = list(word_counts.keys())  # Extract the unique words from the corpus
    visited = set()  # Keep track of words already grouped to avoid duplicates
    terms_dictionary = {}  # Initialize an empty dictionary to hold terms and their variants

    for word1 in words:  # Loop through each word
        if word1 in visited:
            continue  # Skip words we've already grouped
        
        # Check if the word is an Acronym, if so store it directly
        if re.fullmatch(r'[A-Z]{2,}', word1):
            terms_dictionary[word1] = {
                "variants": []
            }
            visited.add(word1)
            continue

        variants = []  # Initialize a list to store similar variants
        for word2 in words:  # Compare with every other word
            if word2 in visited:
                continue  # Skip already grouped words

            if distance(word1, word2) <= max_distance:  # Check if words are similar enough

                variants.append(word2)  # Add as a variant
                visited.add(word2) # Mark word as grouped

        # Extract the most frequent variant as the representative term
        term = max(variants, key=lambda w: word_counts[w])

        terms_dictionary[term] = {
            "variants": [v for v in variants if v != term]  # Store the other variants
        }

    return terms_dictionary # Return the final dictionary with terms and their variants