# 🤖 Git-to-Blog AI

Automatically generate beautiful blog posts from your GitHub commit activity using **FastAPI**, **Langchain**, and **Next.js**. Perfect for developers who want to showcase their work without writing blogs manually.

> 🔗 Live blog at: [https://rajanbuilds.com/blog](https://rajanbuilds.com/blog)

---

## ✨ Features

- 🔑 GitHub OAuth integration: connect your account and select which repos to track
- 🔁 (Optional) GitHub Webhook listener for real-time updates on repos you control
- 🧠 AI-powered daily commit summarization (Langchain)
- 📝 Generates a single `.mdx` blog post per user per day, summarizing all commit activity
- 🌐 Dynamic frontend rendering with Next.js
- ☁️ MDX storage via GitHub, or SQLite
- 👥 Multi-user, multi-repo support

---

<!-- ## 📷 Demo -->
<!-- ![Demo](https://github.com/rajanshresth/git-to-blog/assets/demo.gif) -->

---

## 🧩 Tech Stack

| Layer      | Tech                                    |
| ---------- | --------------------------------------- |
| Backend    | FastAPI, Langchain, Python              |
| Frontend   | Next.js, TypeScript, MDX                |
| Storage    | SQLite or Github API                    |
| Deployment | Vercel (Frontend), EC2/Lambda (Backend) |

---

## 🚀 How It Works

1. User connects their GitHub account via OAuth and selects repositories to track
2. (Optional) GitHub webhook triggers for real-time updates on selected repos
3. FastAPI backend fetches all commits for each user daily
4. Langchain summarizes daily code changes into a single blog post
5. `.mdx` file is generated with title, tags, and meta
6. File is saved (GitHub/SQLite)
7. Next.js dynamically renders the post

---

## 🏁 Getting Started

### Backend (FastAPI)

```bash
uv venv
source .venv/bin/activate  # or .venv/Scripts/activate on Windows
uv pip install -r pyproject.toml

uvicorn app.main:app --reload
```
