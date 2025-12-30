# 📺 YouTube Playlist Duration Calculator

A Python CLI tool that helps you analyze YouTube playlists and courses **without using the YouTube Data API**. It calculates total duration, compares courses, and even creates a **day-wise study plan** based on the time you have available.

This project uses **yt-dlp** to extract playlist metadata directly from YouTube.

---

## 🚀 Features

- 📌 **Playlist Analysis**
  - Playlist name
  - Total number of videos
  - Total duration
  - Average video duration
  - Longest & shortest video

- ⚖ **Course Comparison Mode**
  - Compare two playlists/courses
  - Find which course is shorter and by how much

- 📅 **Study Plan Generator**
  - Enter how many days you have
  - Get a clear day-wise breakdown:
    - Day 1 → Video X to Y
    - Day 2 → Video A to B

- ❌ **No YouTube API required**

---

## 🛠 Requirements

- Python **3.8+**
- Internet connection

### Python Libraries

```bash
pip install yt-dlp
```

---

## 📂 Project Structure

```text
YouTube_Playlist_Duration_Calculator.py   # Main Python script
README.md  # Project documentation
```

---

## ▶ How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Install dependencies:

```bash
pip install yt-dlp
```

3. Run the program:

```bash
python YouTube_Playlist_Duration_Calculator.py
```

---

## 📋 Usage Modes

After running the script, you will see:

```text
📺 YouTube Playlist Duration Calculator
1. Length Calculation
2. Course Comparison Mode
3. Study Plan (Day-wise videos)
```

### 1️⃣ Length Calculation
- Paste a YouTube playlist link
- Get complete duration statistics

### 2️⃣ Course Comparison Mode
- Paste **two** playlist links
- Instantly know which course is shorter

### 3️⃣ Study Plan Mode
- Paste playlist link
- Enter number of days
- Get a structured learning plan

---

## 🔗 Supported Links

- YouTube Playlists
- Most course-style playlists

> ⚠ Note: Some private or restricted videos may not be counted.

---

## 🧠 Example Output

```text
📌 Playlist Name: Python Full Course
🎥 Total Videos: 120
⏱ Total Duration: 42h 18m 10s
📊 Avg Video Duration: 21m 9s
⬆ Longest Video: 1h 45m 2s
⬇ Shortest Video: 2m 10s
```

---

## ❗ Known Limitations

- Does not work with private playlists
- Accuracy depends on metadata provided by YouTube

---

## 🤝 Contributing

Contributions are welcome!

- Fork the repo
- Create a new branch
- Submit a pull request

---

## 📜 License

This project is open-source and free to use for learning purposes.

---

## 🙌 Author

**Asaman Pal**  
Built with ❤️ using Python

---

⭐ If you like this project, consider giving it a star on GitHub!
