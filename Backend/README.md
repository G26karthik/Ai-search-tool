# AI Search Tool - Backend (FastAPI)

## 🚀 Setup Instructions

### 1️⃣ Install Python Dependencies
Run this command inside the `backend/` folder:
```sh
pip install -r requirements.txt
```

### 2️⃣ Set Up Environment Variables
Create a .env file in backend/ and add:
```sh
SERPAPI_KEY=your_serpapi_key
YOUTUBE_API_KEY=your_youtube_api_key
```
### 3️⃣ Run the Backend Server
```
uvicorn main:app --reload
```
###4️⃣ Test the API
Open your browser and go to:
```
http://127.0.0.1:8000/docs
```
