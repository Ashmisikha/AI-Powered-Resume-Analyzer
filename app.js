import React, { useState } from "react";
import axios from "axios";

const App = () => {
    const [resume, setResume] = useState(null);
    const [skills, setSkills] = useState([]);
    const [jobDesc, setJobDesc] = useState("");
    const [matchScore, setMatchScore] = useState(null);

    const handleFileUpload = (e) => {
        setResume(e.target.files[0]);
    };

    const extractSkills = () => {
        const formData = new FormData();
        formData.append("resume", resume);

        axios.post("http://localhost:5000/upload", formData)
            .then(res => setSkills(res.data.skills))
            .catch(err => console.log(err));
    };

    const matchJob = () => {
        axios.post("http://localhost:5000/match", { resume_skills: skills.join(", "), job_description: jobDesc })
            .then(res => setMatchScore(res.data.match_score))
            .catch(err => console.log(err));
    };

    return (
        <div>
            <h1>📄 AI Resume Analyzer</h1>
            <input type="file" onChange={handleFileUpload} />
            <button onClick={extractSkills}>Extract Skills</button>

            <h2>🔍 Skills Extracted</h2>
            <ul>{skills.map(skill => <li key={skill}>{skill}</li>)}</ul>

            <h2>💼 Job Description</h2>
            <textarea onChange={e => setJobDesc(e.target.value)} />

            <button onClick={matchJob}>Match Resume</button>

            {matchScore && <h2>✅ Match Score: {matchScore}%</h2>}
        </div>
    );
}

export default App;
