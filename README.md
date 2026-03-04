# Chattrix 📊

### NLP Powered WhatsApp Chat Analyzer

Chattrix is a Python-based analytics dashboard that processes exported WhatsApp chats and provides insights such as message statistics, most active users, word frequency, emoji analysis, and more.

This project demonstrates concepts from **Natural Language Processing (NLP), Data Analysis, and Web App Development using Streamlit**.

---

## 🚀 Features

- 📊 Chat statistics (messages, words, media, links)
- 👥 Most active users analysis
- 📝 Most common words in chat
- 😂 Emoji usage analysis
- 📄 Structured chat data viewer
- 📥 Download processed chat data as CSV
- 🌐 Interactive dashboard built with Streamlit

---

## 🧠 Project Architecture

Chat File (.txt)
↓
preprocessor.py → Text parsing & structuring
↓
DataFrame
↓
helper.py → Data analysis functions
↓
app.py → Streamlit web dashboard
