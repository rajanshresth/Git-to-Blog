# 🤖 Git-to-Blog AI

Automatically generate beautiful blog posts from your GitHub commit activity using **FastAPI**, **Langchain**, and **Next.js**. Perfect for developers who want to showcase their work without writing blogs manually.

> 🔗 Live blog at: [https://rajanbuilds.com/blog](https://rajanbuilds.com/blog)

---

## ✨ Features

- 🔁 GitHub Webhook listener (FastAPI)
- 🧠 AI-powered commit summarization (Langchain)
- 📝 Generates `.mdx` blog posts automatically
- 🌐 Dynamic frontend rendering with Next.js
- ☁️ MDX storage via GitHub, or SQLite

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

1. GitHub push triggers webhook
2. FastAPI receives payload and fetches diffs
3. Langchain summarizes code changes
4. `.mdx` file is generated with title, tags, and meta
5. File is saved (GitHub/SQLite)
6. Next.js dynamically renders the post

---

## 🏁 Getting Started

### Backend (FastAPI)

```bash
uv venv
source .venv/bin/activate  # or .venv/Scripts/activate on Windows
uv pip install -r pyproject.toml

uvicorn app.main:app --reload
```
