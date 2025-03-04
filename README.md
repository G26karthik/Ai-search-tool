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
git clone https://github.com/G26karthik/Ai-search-tool.git
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
## **📊 Features & Functionality**

### **1️⃣ AI Query Expansion**
- Uses **NLP models** (`T5` or `BART`) from Hugging Face to expand user queries.
- Helps generate more **relevant search terms** to improve results.
- Can be toggled **ON/OFF** using a **toggle button**:
  - **AI Mode ON**: Query is **expanded** before searching.
  - **AI Mode OFF**: Uses the **exact user query** without modification.
- **Alert message appears** when AI search is enabled, informing users that **accuracy may vary**.

---

### **2️⃣ Google & YouTube Search**
- **Google Search**:
  - Uses **SerpAPI** to fetch **organic search results**.
  - Returns **title, snippet, and link** for each result.
- **YouTube Search**:
  - Uses **YouTube Data API v3** to fetch **relevant videos**.
  - Displays **video title, description, and link** to watch.

---

### **3️⃣ Sorting & Filtering**
- Users can **sort results** based on:
  - 🔍 **Relevance** (Default)
  - 📅 **Date** (Latest results first)
  - 🌐 **Source** (Group Google & YouTube separately)
- Filters help **refine search results** for **better accuracy**.

---

### **4️⃣ UI/UX Similar to Google**
- **Search Bar in the Center**:  
  - **Neatly styled**, like **Google Search**.
  - **Toggle button** below it to switch **AI search ON/OFF**.
- **Results Displayed in Two Columns**:
  - **Left Side** → 🌍 **Google Search Results**.
  - **Right Side** → 🎥 **YouTube Search Results**.
- **Clean & Responsive Design**:
  - Fully **mobile-friendly**.
  - **Dark mode UI** for better readability.

---

### **5️⃣ Multithreaded Backend for Faster Searches**
- Uses **Python’s FastAPI + Multithreading** to **speed up** search requests.
- **Google & YouTube searches run in parallel**, reducing load time.

---

## 🌍 Live Demo
**Frontend (Vercel):** [Click Here](https://ai-search-tool.vercel.app/)  
**Backend (Render):** [Click Here](https://your-render-backend-url.com)


## 📌 Deployment Instructions

### Frontend Deployment (Vercel)

# 1️⃣ Install Vercel CLI and log in
```
npm install -g vercel
vercel login
```

# 2️⃣ Deploy the Frontend
```
cd search-tool
vercel --prod
```
## Backend (Render)
📌 Create requirements.txt in backend (already provided).

📌 Push to GitHub & Deploy via Render.com.


## 📑 Challenges & Future Improvements

### ✅ Challenges Faced:

Query expansion sometimes changes the intent of the search.
API rate limits for SerpAPI & YouTube Data API.
Initial slow response time (fixed with multithreading).

### 🚀 Future Improvements:

Add LinkedIn search integration.
Use a database to cache & speed up repeated searches.
Implement user authentication for personalized search history.

## 🚀 Future Improvements

- **Expand Search Sources:**  
  - Integrate additional platforms such as LinkedIn, Reddit, and Twitter for a more comprehensive search experience.

- **Enhanced Ranking & Filtering:**  
  - Develop AI-based ranking algorithms to better prioritize the most relevant results.  
  - Implement customizable filtering options based on user preferences.

- **Database Integration:**  
  - Cache frequently searched queries and results to improve response times.  
  - Store user search history and preferences for personalized recommendations.

- **User Authentication:**  
  - Implement user accounts and secure login systems to provide personalized search experiences and save search histories.

- **Performance Optimization:**  
  - Further optimize API calls and explore serverless architectures to scale with demand.

- **UI/UX Enhancements:**  
  - Improve responsiveness and design for mobile devices.  
  - Add interactive elements and animations for a smoother user experience.

## 🤝 Contributing
To contribute to this project, please follow these steps:

# 1️⃣ Fork the repository on GitHub.
```git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```
# 2️⃣ Create a new branch for your feature or bugfix.
```
git checkout -b feature-branch
```
# 3️⃣ Make your changes and commit them.
```
git add .
git commit -m "Description of your changes"
```

# 4️⃣ Push your branch to GitHub.
```
git push origin feature-branch
```
# 5️⃣ Open a Pull Request (PR) for review.


 ## 📜 License
This project is licensed under the MIT License. You are free to use, modify, and distribute this project with proper attribution.


