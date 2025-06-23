import re


def clean_text_as_list(text):
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text) 
    # Removed non alphanumeric characters except underscores, hyphens, and spaces
    cleaned_text = re.sub(r'[^a-zA-Z0-9_\-\s]', '', text)
    # Remove extra spaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    # Regex patterns for different term formats
    snake_case_pattern = r'\b[a-z]+(?:_[a-z]+)+\b' # lowercase with underscores with 2 or more words
    hyphen_pattern = r'\b[a-zA-Z]+(?:-[a-zA-Z0-9]+)+\b' # hyphenated terms with 2 or more words
    camel_case_pattern = r'\b(?:[A-Z][a-z0-9]+){2,}\b' # Uppercase words without spaces with 2 or more words
    acronym_pattern = r'\b[A-Z]{2,}\b' # Uppercase acronyms with 2 or more letters
    proper_case_multiword = r'\b(?:[A-Z][a-z0-9]+\s){1,2}[A-Z][a-z]+\b' # Multi-word terms with proper case

    # Find all matches for the patterns but avoid duplicate detection in terms in the same span (position)
    patterns = [snake_case_pattern, hyphen_pattern, camel_case_pattern, acronym_pattern, proper_case_multiword]
    potential_terms = []  # List to hold potential terms
    seen_spans = set()  # Track spans to avoid duplicates
    stopwords_start = {'the', 'a', 'an', 'and', 'of', 'in', 'to', 'for'}  # Set of common stopwords at the start
    for pattern in patterns:
        for match in re.finditer(pattern, cleaned_text):
            span = match.span() # Get the span of the match (start, end)
            if span not in seen_spans: # if the span is not already seen
                if pattern == proper_case_multiword:
                    words = match.group().split() # Split multi-word terms
                    if words[0].lower() in stopwords_start: # if the first word is a stopword
                        continue
                potential_terms.append(match.group()) # add the matched term
                seen_spans.add(span) # track where it was already matched

    return potential_terms