import numpy as np
from sentence_transformers import SentenceTransformer

MODEL = 'sentence-transformers/all-MiniLM-L6-v2'


def get_embeddings(text_chunks):
    model = SentenceTransformer(MODEL)

    print(f"Creating embeddings for {len(text_chunks)} chunks")
    embeddings = model.encode(text_chunks, show_progress_bar=True)

    print(f"Embeddings shape: {embeddings.shape}")
    return np.array(embeddings)
