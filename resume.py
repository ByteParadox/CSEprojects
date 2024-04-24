import docx2txt
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
#https://colab.research.google.com/drive/1Plky72n_ujzZg68MZs3TCXa9ggwxPcSM#scrollTo=ewDETL-U6Cpc