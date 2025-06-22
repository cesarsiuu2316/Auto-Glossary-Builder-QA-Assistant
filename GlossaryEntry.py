import json

class GlossaryEntry:
    def __init__(self, term, variants=None, tokens=None, definition="", example=""):
        self.term = term
        self.variants = variants if variants else []
        self.tokens = tokens if tokens else []
        self.definition = definition
        self.example = example

    def set_variants(self, variants):
        self.variants = variants

    def set_tokens(self, tokens):
        self.tokens = tokens

    def set_definition_and_example(self, definition, example):
        self.definition = definition
        self.example = example

    def to_dict(self):
        return {
            "variants": self.variants,
            "tokens": self.tokens,
            "definition": self.definition,
            "example": self.example
        }
    
    def __str__(self):
        return (
            f"GlossaryEntry(\n"
            f"  term={self.term},\n"
            f"  variants={self.variants},\n"
            f"  tokens={self.tokens},\n"
            f"  definition={self.definition},\n"
            f"  example={self.example}\n"
            f")"
        )