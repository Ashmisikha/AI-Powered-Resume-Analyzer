from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from resume_parser import extract_skills
from job_matcher import match_job

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resumes.db'
db = SQLAlchemy(app)

# Resume Model
class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    skills = db.Column(db.Text, nullable=False)
    score = db.Column(db.Float, default=0)

@app.route('/upload', methods=['POST'])
def upload_resume():
    file = request.files['resume']
    skills = extract_skills(file)
    return jsonify({"skills": skills})

@app.route('/match', methods=['POST'])
def match_resume():
    data = request.json
    score = match_job(data['resume_skills'], data['job_description'])
    return jsonify({"match_score": score})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
