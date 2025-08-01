# 📉 Insta Unfollowers Tracker (Streamlit App)

Track who unfollowed or followed you on Instagram by uploading your `followers.json` file — fully offline, private, and powered by Python & Streamlit.

---

## 🚀 Features

- ✅ Upload `followers.json` exported from Instagram
- 🔄 Compare current vs previous followers
- 👎 Detect unfollowers
- 👍 Identify new followers
- 💾 Snapshot saved locally for future comparison
- 🔐 100% offline, no Instagram login or third-party tools

---

## 🛠 Tech Stack

| Tech         | Purpose                         |
|--------------|----------------------------------|
| Python 3     | Core logic & processing          |
| Streamlit    | Web-based GUI                    |
| JSON         | Instagram data input             |
| Local Files  | Snapshot persistence             |

---

## 📁 Folder Structure

```
insta_unfollowers_tracker_streamlit/
├── app.py                         # Main Streamlit app
├── data/
│   └── followers_snapshot.json    # Auto-created for comparison
├── README.md
├── LICENSE
├── .gitignore
```

---

## 📂 How to Use

### 1. 🔽 Download Your Instagram Data
- Go to **Instagram → Settings → Your Activity → Download Your Information**
- Choose **JSON** format and download the ZIP file
- Extract it and locate:

```
followers_and_following/followers.json
```

---

### 2. 🚀 Run the App

#### Step-by-step:

```bash
# Clone the repository
git clone https://github.com/ganesh76/Insta-Followers-Tracker.git
cd Insta-Followers-Tracker

# Install required dependencies using:

```bash
pip install -r requirements.txt
```

# Run the app
streamlit run app.py
```

- This will open a browser window at: [http://localhost:8501](http://localhost:8501)
- Upload your `followers.json` file
- The app will compare against any previous snapshot and show:
  - 👎 Unfollowers
  - 👍 New followers

---

## 🔐 Privacy & Security

- No Instagram login required
- No external API calls
- No data leaves your machine
- Personal snapshot is stored locally in `data/followers_snapshot.json` (and excluded via `.gitignore`)

---

## ✅ .gitignore Highlights

```gitignore
__pycache__/
data/followers_snapshot.json
```

---

## 📌 Planned Improvements

- Compare `following.json` (for mutuals and non-mutuals)
- Export unfollower lists as CSV/TXT
- Deployable version on Streamlit Cloud
- Compare engagement (ghost followers, top likers, etc.)

---

## 🙌 Contributing

Pull requests and feature ideas are welcome!  
If you found this useful, consider starring ⭐ the repository.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE)
© 2025 [Ganesh Gundu](https://github.com/ganesh76)

---

## 🏷️ Badges

[![Python](https://img.shields.io/badge/python-3.7%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red?logo=streamlit)](https://streamlit.io/)
[![MIT License](https://img.shields.io/github/license/ganesh76/Insta-Followers-Tracker)](LICENSE)
[![GitHub Repo stars](https://img.shields.io/github/stars/ganesh76/Insta-Followers-Tracker?style=social)](https://github.com/ganesh76/Insta-Followers-Tracker/stargazers)

---