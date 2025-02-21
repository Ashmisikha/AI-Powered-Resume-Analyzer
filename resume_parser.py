import pdfplumber
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_skills(file):
    text = ""
    if file.filename.endswith('.pdf'):
        with pdfplumber.open(file) as pdf:
            text = " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif file.filename.endswith('.txt'):
        text = file.read().decode("utf-8")

    doc = nlp(text)
    skills = [token.text for token in doc.ents if token.label_ == "ORG" or token.label_ == "PRODUCT"]
    return list(set(skills))
