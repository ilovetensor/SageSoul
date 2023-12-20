import numpy as np
import math
from bs4 import BeautifulSoup
import gensim
from urllib.request import urlopen
import re
import pandas as pd
from .models import Books
from sentence_transformers import SentenceTransformer
sentence_model = SentenceTransformer('all-MiniLM-L12-v2')
import pinecone
def get_para_from_index(query_encoding, index):

    query_data = index.query(vector=[float(i) for i in query_encoding], top_k=5, include_value=True)

    idx = [a['id'] for a in  query_data['matches']]


    # most_similar_para = [BookModel.get(id) for id in idx]
    # name = [obj.book_name for obj in most_similar_para]
    # print("posting++++====================")
    # para = [obj.book_content for obj in most_similar_para]
    # pinecone.deinit()
    return {"name": idx, "para": idx}

def get_encoding(user_input):
    query_encoding = np.array(sentence_model.encode(user_input))
    return query_encoding
