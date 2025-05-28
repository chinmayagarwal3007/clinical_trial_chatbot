import pandas as pd
import faiss
import pickle
from sentence_transformers import SentenceTransformer


# Load your data
df = pd.read_csv("clinical_trials.csv")

# Convert each row to a search-friendly document string
def row_to_doc(row):
    return f"""Title: {row['Study Title']}
Condition: {row['Conditions']}
Summary: {row['Brief Summary']}
Eligibility: {row['Eligibility Criteria']}
Intervention: {row['Interventions']}
Sex: {row['Sex']}
Age: {row['Age']}
Phase: {row['Phases']}
Status: {row['Study Status']}"""

documents = df.apply(row_to_doc, axis=1).tolist()
# print(documents)
metadata = df.to_dict(orient="records")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(documents, convert_to_numpy=True)

#print(embeddings)

#Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Save index and metadata
faiss.write_index(index, "faiss_index.index")
with open("faiss_metadata.pkl", "wb") as f:
    pickle.dump(metadata, f)

print("✅ FAISS index created and saved.")
