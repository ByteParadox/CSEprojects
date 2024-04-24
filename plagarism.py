# Install required packages
#!pip install docx2txt PyPDF2
#https://colab.research.google.com/drive/1Plky72n_ujzZg68MZs3TCXa9ggwxPcSM#scrollTo=ewDETL-U6Cpc
import docx2txt
import PyPDF2
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to preprocess text
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    return text

# Load documents from database
job_description = docx2txt.process('path of your file')
resume = docx2txt.process('path of your file')

# Preprocess documents
job_description = preprocess_text(job_description)
resume = preprocess_text(resume)

# Create a list of documents in the database
documents = [job_description, resume]

# Create CountVectorizer object
cv = CountVectorizer()

# Fit and transform documents
mat = cv.fit_transform(documents)

# Calculate cosine similarity
similarity_mat = cosine_similarity(mat)

# Function to check plagiarism
def check_plagiarism(submitted_text, threshold=0.8):
    # Preprocess submitted text
    submitted_text = preprocess_text(submitted_text)
    
    # Transform submitted text
    submitted_mat = cv.transform([submitted_text])
    
    # Calculate similarity with each document in the database
    similarities = [cosine_similarity(submitted_mat, doc) for doc in mat]
    
    # Check for plagiarism
    if max(similarities) >= threshold:
        return True
    else:
        return False

# Example usage
submitted_text = docx2txt.process('path of your file')
if check_plagiarism(submitted_text):
    print("Plagiarism detected!")
else:
    print("No plagiarism detected.")
