import re


def clean_text(text: str) -> str:
    temp = re.sub(r'\s+', ' ', text)
    temp = re.sub(r'[^\x00-\x7F]+', ' ', temp)
    return temp.strip()
