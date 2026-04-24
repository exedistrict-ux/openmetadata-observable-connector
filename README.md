# 🔗 OpenMetadata Observable Connector

A Streamlit-based connector that integrates Observable HQ notebooks with OpenMetadata for data discovery and governance.

## 🚀 Features
- Fetch Observable HQ notebooks metadata
- Display collections and dashboards
- OpenMetadata integration ready
- REST API based connector

## 🛠️ Tech Stack
- Python 3.x
- Streamlit
- Observable HQ API
- OpenMetadata API
- Pandas

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/exedistrict-ux/openmetadata-observable-connector.git
cd openmetadata-observable-connector
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Key
Create a `.env` file:
OBSERVABLE_API_KEY=your_key_here

### 4. Run the app
```bash
python -m streamlit run app.py
```

Open browser: `http://localhost:8501`

## 🧪 Testing
```bash
# Test API connection
python -c "import requests; r = requests.get('https://api.observablehq.com/documents/@your-workspace', headers={'Authorization': 'ApiKey YOUR_KEY'}); print(r.status_code)"

# Expected output: 200
```

## 📸 Screenshots
- Notebooks tab: Shows all Observable notebooks
- <img width="1909" height="1071" alt="image" src="https://github.com/user-attachments/assets/13299caa-fa2b-427c-867a-20d90e2a901e" />

- Collections tab: Shows workspace collections
- <img width="1896" height="1073" alt="image" src="https://github.com/user-attachments/assets/b3ec1e40-55d3-465a-a887-ecb7f7b8429c" />


## 🎯 How it works
1. Connects to Observable HQ API
2. Fetches notebook/collection metadata
3. Displays in Streamlit dashboard
4. Ready for OpenMetadata ingestion

## 🏆 Hackathon
Built for **Back to the Metadata Hackathon by @exedistrict-ux
