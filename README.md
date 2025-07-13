# <div align="center"><img src="static/images/logo.png" alt="Miso Logo" width="200"/></div>

# 📚 Miso

A community-driven platform for writers and readers to connect through articles. ✍️📖

Whether you're passionate about sharing your thoughts or discovering new perspectives, Miso provides a welcoming space for meaningful expression. 

## ❓ Why Miso?

Many writers struggle to find platforms that:

- 🔍 Focus on long-form content (not just social media snippets)
- 💬 Offer genuine engagement (not just algorithms)
- 🎨 Allow authentic self-expression without restrictions

## ✨ Features

### 🖋️ For Writers

- **Easy Publishing**: Write and format articles effortlessly 🚀
- **Categories**: Tag your work by topic 🏷️
- **Reader Feedback**: Get meaningful engagement 💌

### 👀 For Readers

- **Free Signup** – Join in seconds ⚡
- **Smart Search** – Find articles easily 🔎
- **Read Unlimited** – No paywalls 🆓

## 🛠️ Technologies Used
| Category       | Technologies |  
|---------------|-------------|  
| Frontend      | HTML, CSS, JavaScript, Jinja2 Templates |  
| Backend       | Python, Flask |  
| Database      | SQLite |  
| Authentication| Flask-Login, Password Hashing |  



## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- pip package manager
- SQLite3

### Local Development
```bash
# 1. Clone the repository
git clone https://github.com/CodexEsto/Team-1-project.git
cd Team-1-project

# 2. Set up virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env file with your settings

# 5. Initialize database
flask db upgrade

# 6. Run the application
flask run