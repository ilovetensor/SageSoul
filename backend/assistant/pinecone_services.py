# pinecone_service.py

import pinecone
import faiss
import numpy as np
from .models import Books


class PineconeService:
    def __init__(self, index_name, dimension):
        pinecone.init(api_key="e66692b7-057f-47db-b61f-79e085cf8b54")
        self.index = pinecone.Index(index_name=index_name, dimension=dimension)
        self.faiss_index = faiss.IndexFlatL2(dimension)

    def insert_vectors(self, ids, vectors):
        self.index.upsert(ids=ids, vectors=vectors)

        vectors_np = np.array(vectors, dtype=np.float32)
        self.faiss_index.add(vectors_np)


    def query_vector(self, query_vector, top_k=5):
        # Query Pinecone index
        results_pinecone = self.index.query(queries=[query_vector], top_k=top_k)

        # Convert Pinecone results to a list of IDs
        ids_pinecone = [result.id for result in results_pinecone]

        # Query FAISS index
        query_np = np.array([query_vector], dtype=np.float32)
        _, faiss_ids = self.faiss_index.search(query_np, top_k)

        # Convert FAISS results to a list of IDs
        ids_faiss = [str(faiss_id) for faiss_id in faiss_ids[0]]

        # Merge results from Pinecone and FAISS
        merged_ids = list(set(ids_pinecone) | set(ids_faiss))

        return merged_ids



# create_pinecone_dataset.py
import pandas as pd
import pinecone
from sentence_transformers import SentenceTransformer

import pandas as pd
import pinecone
from sentence_transformers import SentenceTransformer


def create_pinecone_dataset(csv_path, api_key, index_name, dimension=384):
    # Load CSV data
    df = pd.read_csv(csv_path)
    df.charaka = df.charaka.to_string()
    # Initialize Pinecone
    pinecone.init(api_key=api_key, environment='gcp-starter')

    # Create a Pinecone index
    pinecone_index = pinecone.Index(index_name)

    # Load a pre-trained sentence embeddings model
    sentence_model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
    embedding_list=[]
    # Create embeddings and upsert into Pinecone index
    for index, row in df.iterrows():
        paragraph = row.charaka

        embedding_list.append(sentence_model.encode(paragraph).tolist())
        print(index)

    # Convert NumPy array to list
    print(embedding_list[0])
    idx = [str(i) for i in df.index]

    pinecone_index.upsert(vectors=zip(idx,embedding_list))

    # Deinitialize Pinecone


# Usage
api_key = "e66692b7-057f-47db-b61f-79e085cf8b54"

def add_data_in_model(path):
    df = pd.read_csv(path)
    for idx, row in df.iterrows():
        obj = BookModel()
        obj.book_index = idx
        obj.book_name = row.book_name
        obj.book_content = row.charaka
        print(row)
        obj.save()




