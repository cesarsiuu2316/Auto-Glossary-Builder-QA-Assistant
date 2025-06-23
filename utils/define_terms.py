import requests
import json


# fetch definitions and examples for a list of terms
def fetch_definitions_and_examples(terms):
    definitions = [] # List to hold definitions
    examples = [] # List to hold examples
    for term in terms:
        response = requests.post("http://localhost:11434/api/generate", 
            json={
                'model': 'phi3-glossary:latest',
                'prompt': term,
                'stream': False
            }
        )
        if response.status_code == 200: # Check if the request was successful
            data = json.loads(response.json()["response"]) # Parse the JSON response received in type string
            definitions.append(data["definition"])
            examples.append(data["example"])
        else:
            return None, None
        
    return definitions, examples 