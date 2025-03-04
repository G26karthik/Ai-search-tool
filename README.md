# **AI-Powered Search & Aggregation Tool**

## **🌟 Overview**
This is a **full-stack AI-powered search and aggregation tool** that takes user queries, retrieves results from **Google and YouTube**, and presents them in a structured **React UI**. The backend is built with **FastAPI (Python)**, and the frontend is developed using **React.js**.

✅ **Features:**
- **AI-Powered Search Expansion**: Enhances user queries using NLP models.
- **Google & YouTube Integration**: Fetches search results from multiple sources.
- **Multithreading Optimization**: Improves speed using parallel processing.
- **Sorting & Filtering**: Allows users to customize search results.
- **Dark Mode UI**: Aesthetic, user-friendly design similar to Google Search.
- **Toggle AI Search**: Allows users to switch between **AI-enhanced search** and **direct search**.

---

## **🛠️ Tech Stack**
| Technology  | Description  |
|-------------|-------------|
| **Frontend**  | React.js, CSS |
| **Backend**  | FastAPI (Python) |
| **Database** | Not required (API-based search) |
| **APIs Used** | Google Search (SerpAPI), YouTube Data API |
| **AI Model** | Hugging Face Transformers (T5, BART) |
| **Deployment** | Vercel (Frontend), Render (Backend) |

---

## **🚀 Setup & Installation**

### **Clone the Repository**
```sh
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### **🖥️ Backend Setup (FastAPI)**

📌 Navigate to the backend folder:
```
cd backend
```
📌 Install dependencies: 
```
pip install -r requirements.txt
```
📌 Set up environment variables:
Create a .env file inside backend/ and add:
```
SERPAPI_KEY=your_serpapi_key
YOUTUBE_API_KEY=your_youtube_api_key
```
Run the FastAPI server:
```
uvicorn main:app --reload
```
📌 Test the API in browser:
```
http://127.0.0.1:8000/docs
```
### **🌐 Frontend Setup (React.js)**

📌 Navigate to the frontend folder:
```
cd search-tool
```
📌 Install dependencies:
```
npm install
```
📌 Set up environment variables:
Create a .env file inside search-tool/ and add:
```
REACT_APP_BACKEND_URL=http://127.0.0.1:8000
```
📌 Start the frontend:
```
npm start
```
📌 Open in browser:
```
http://localhost:3000
```






