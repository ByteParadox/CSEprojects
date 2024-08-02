'''import docx2txt
job_description=docx2txt.process('pth of your file ')
resume=docx2txt.process('path of your file')
print(resume)
content=[job_description,resume]
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
mat = cv.fit_transform(content)
from sklearn.metrics.pairwise import cosine_similarity
similarity__mat=cosine_similarity(mat)
print(similarity__mat)
print("Resume matches by: "+str(similarity__mat[1][0]*100)+"%")

if(str(similarity__mat[1][0]*100)==0):
  print("No match found.")
#https://colab.research.google.com/drive/1Plky72n_ujzZg68MZs3TCXa9ggwxPcSM#scrollTo=ewDETL-U6Cpc'''
import docx2txt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

# Load documents
try:
    job_description = docx2txt.process('path_of_your_file')
    resume = docx2txt.process('path_of_your_file')
except Exception as e:
    print(f"Error processing files: {e}")
    raise

# Prepare data for analysis
content = [job_description, resume]
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
mat = tfidf_vectorizer.fit_transform(content)

# Calculate cosine similarity
similarity_mat = cosine_similarity(mat)
similarity_score = similarity_mat[1][0] * 100

# Output results
if similarity_score < 50:
    print("No match found.")
else:
    print(f"Resume matches by: {similarity_score:.2f}%")

# Optional visualization
labels = ['Job Description', 'Resume']
scores = [similarity_mat[0][1] * 100, similarity_mat[1][0] * 100]

plt.bar(labels, scores, color=['blue', 'green'])
plt.xlabel('Documents')
plt.ylabel('Similarity (%)')
plt.title('Document Similarity')
plt.show()
