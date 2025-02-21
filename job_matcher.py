from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_job(resume_skills, job_description):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_skills, job_description])
    similarity_score = cosine_similarity(vectors)[0][1]
    return round(similarity_score * 100, 2)
