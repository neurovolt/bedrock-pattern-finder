# Minecraft Bedrock Chunk Finder

A web tool that shows the exact bedrock pattern for any Minecraft chunk using the real Java RNG algorithm.

## 🚀 Features
- Visual 16×16 chunk grid
- Accurate bedrock generation (Java 1.16+)
- Works for both bottom and top bedrock layers
- Flask backend + HTML/JS frontend

## 📌 How to Use
1. Enter **Chunk X** and **Chunk Z** (or use F3 screen in Minecraft to find them).
2. Enter **Y layer** (0–4 for bottom bedrock, 123–127 for top bedrock).
3. Click **Load Chunk**.
4. Black squares = Bedrock, Gray = Non-bedrock.

## 🌐 Online Version
Deployed on Render: (Your public URL will go here)

## 🛠️ Run Locally
```
pip install flask
python app.py
```
Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## 📸 Screenshots
*(Add screenshots of your site here)*

## 📜 License
Free to use and modify.
