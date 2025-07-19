#edututor ai: personalized learning with generative ai and lms
📁 Project Structure
EduTutorAI/
├── backend/
│   ├── app.py                   # Flask backend
│   ├── quiz_generator.py        # Quiz creation logic (mocked Granite)
│   ├── watsonx_adapter.py       # IBM Watsonx model adapter (stub)
│   ├── google_classroom_api.py  # Mock sync function
│   └── requirements.txt         # Python dependencies
│
├── models/
│   ├── adaptive_model.py        # Adaptive difficulty logic
│   └── diagnostics_model.py     # Initial diagnostic test generation
│
├── database/
│   └── pinecone_integration.py  # Vector DB setup (stub)
│
├── frontend/
│   ├── index.html               # Student view
│   ├── dashboard.html           # Educator dashboard
│   ├── styles.css               # UI styling
│   └── script.js                # JS for API interactions
│
├── config/
│   └── config.json              # API keys & settings
│
├── run.sh                       # Shell script to launch app
└── README.md                    # Documentation

📌 Key Features
🔄 Google Classroom Sync – Sync courses from Google Classroom (mocked)

✏️ Dynamic Quiz Generation – Quizzes based on course topic using Granite LLM (mocked)

🎯 Diagnostic & Adaptive Testing – Personalized quizzes based on performance

📊 Educator Dashboard – Track quiz history and scores

🧠 Vector Search Ready – Integration scaffolded for Pinecone

🌐 Modular Flask Backend + HTML Frontend

🔧 Technologies Used
| Component                | Technology                                                |
| ------------------------ | --------------------------------------------------------- |
| 💻 Backend API           | Python, Flask, IBM Watsonx (Granite), Flask-CORS          |
| 🧠 AI/ML Models          | IBM Watsonx foundation models (mocked in current version) |
| 🗄️ Vector DB            | Pinecone (stubbed integration)                            |
| 📚 LMS Integration       | Google Classroom API (placeholder logic)                  |
| 🌐 Frontend              | HTML, CSS, JavaScript                                     |
| ☁️ Deployment (optional) | IBM Cloud, Streamlit, or Heroku                           |
| 🔑 Config Management     | JSON config file (`config/config.json`)                   |
| 📦 Package Manager       | `pip`, `venv`                                             |
| 📁 Version Control       | Git + GitHub                                              |

🛠️ Installation & Setup
📥 1. Clone the Repository
bash
git clone https://github.com/your-username/EduTutorAI.git
cd EduTutorAI
🧪 2. Create Virtual Environment
bash
python -m venv venv
venv\Scripts\activate    # For Windows
# or
source venv/bin/activate  # For Mac/Linux
📦 3. Install Python Dependencies
bash
pip install -r backend/requirements.txt
🚀 4. Run the Backend
bash
python backend/app.py
The server will start at: http://127.0.0.1:5000

🌐 5. Launch Frontend
In another terminal:
bash
cd frontend
python -m http.server 8080
Visit: http://localhost:8080

🧠 Notes
The current version uses mocked data for IBM Watsonx, Google Classroom, and Pinecone to simulate a real environment.

You can replace these with real API calls once API credentials and tokens are available.

Basic CORS support is enabled via Flask-CORS for cross-origin requests from the frontend.

📄License
MIT License

Copyright (c) 2025 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


# EduTutor AI

EduTutor AI is a personalized learning platform integrating IBM Watsonx and Google Classroom.

## Features
- Personalized Quiz Generation
- Google Classroom Sync
- Educator Dashboard
- Diagnostic & Adaptive Testing

## Setup
```bash
bash run.sh
``
# EduTutor-AI-Personalized-Learning-with-Generative-AI-and-LMS-Integration
 725396d62391934bdc966e40f0ecbc9ed62ad75c



#zipfile: [EduTutorAI.zip](https://github.com/user-attachments/files/21325237/EduTutorAI.zip)

#demolink: https://drive.google.com/file/d/1h-05vJwqoGZS_YLV-ydrKsQglwP3ZKhC/view?usp=sharing
