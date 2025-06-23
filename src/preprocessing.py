import re

def clean_text(text: str) -> str:
    """Keep only Amharic letters, common punctuation, and spaces."""
    return re.sub(r"[^\u1200-\u137F።፣\s]", "", text or "").strip()
