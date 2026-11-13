from clean_data import clean_text
from load_data import load_documents


def prepare_docs(folder_path='data/'):
    raw_documents = load_documents(folder_path)
    cleaned_documents = [clean_text(document) for document in raw_documents]
    print(f'Prepared {len(cleaned_documents)} documents.')
    return cleaned_documents
