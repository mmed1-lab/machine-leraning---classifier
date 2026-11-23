import re

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"http\S+|www\.\S+", " ", text)   # URLs
    text = re.sub(r"@\w+|#", " ", text)             # mentions / hashtags
    text = re.sub(r"[^a-z!?']", " ", text)   # garde les lettres, ! et ?
    text = re.sub(r"\s+", " ", text).strip()
    return text