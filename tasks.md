# 📝 tasks.md — Git-to-Blog AI Project

## 🎯 Goal  
Automatically generate and publish blog posts based on GitHub commit activity using Langchain, FastAPI, and Next.js.

---

## ✅ Phase 1: Project Setup

### 📌 Week 1 – Setup Foundations

#### Backend (FastAPI + Langchain)
- [ ] Initialize FastAPI project (`fastapi-git-blog-ai`)
- [ ] Set up GitHub webhook endpoint: `POST /github/webhook`
- [ ] Handle GitHub push event JSON payload
- [ ] Extract the following:
  - [ ] Repo name
  - [ ] Commit SHA(s)
  - [ ] Commit messages
  - [ ] Git diff via GitHub API
- [ ] Authenticate GitHub API via Personal Access Token (PAT)
- [ ] Setup basic logging and error handling

#### Frontend (Next.js - `rajanbuilds.com`)
- [ ] Initialize Next.js project (or reuse your personal site)
- [ ] Add MDX support using `next-mdx-remote` or `contentlayer`
- [ ] Create dynamic route: `/blog/[repo]/[slug].tsx`
- [ ] Add blog card layout with TailwindCSS + shadcn/ui
- [ ] Build blog home page: `/blog`

---

## 🧠 Phase 2: AI Commit Summarizer

### 📌 Week 2 – AI Logic with Langchain

- [ ] Install and configure Langchain
- [ ] Write prompt templates for:
  - [ ] Summarizing commit messages
  - [ ] Explaining what was built/changed
  - [ ] Formatting output into markdown blog post
- [ ] Create Langchain chain or function:
  - [ ] Input: commit messages, diffs
  - [ ] Output: `.mdx` file
- [ ] Parse content into:
  - [ ] Blog Title
  - [ ] Meta description
  - [ ] Tags
  - [ ] MDX body

---

## 💾 Phase 3: Saving Blog Posts

### 📌 Week 3 – Blog Storage Options

- [ ] Choose one of the following:
  - [ ] Push `.mdx` file to GitHub content repo
  - [ ] Upload `.mdx` to AWS S3
  - [ ] Store blog content in Postgres
- [ ] Automate file upload from FastAPI backend
- [ ] Trigger blog rebuild (if using GitHub + Vercel)

---

## 🌐 Phase 4: Displaying Blogs

- [ ] Configure Next.js to fetch or import `.mdx` content
- [ ] Render blog using MDX provider
- [ ] Add share buttons, author bio, and date
- [ ] Display commit metadata (date, repo, link to GitHub)

---

## 🚀 Phase 5: Finishing Touches

- [ ] Deploy FastAPI backend (Render, EC2, or Railway)
- [ ] Set up webhook with GitHub (test on one of your repos)
- [ ] Deploy Next.js frontend to Vercel
- [ ] Polish UI with animations, icons, footer
- [ ] Add `/blog/rss.xml` feed (optional)

---

## 🧪 Testing Plan

- [ ] Test with multiple repos and commit styles
- [ ] Validate blog accuracy against commit content
- [ ] Test edge cases (non-code commits, large diffs)

---

## 🎉 Stretch Goals (Optional)
- [ ] Add support for image upload (screenshots, diagrams)
- [ ] Add search and filter on blog page
- [ ] Schedule weekly AI blog digests
- [ ] Deploy as a SaaS for devs or teams

---

## 📅 Timeline (Example)
| Day  | Task                                     |
|------|------------------------------------------|
| Day 1| Setup FastAPI & Next.js project structure |
| Day 2| GitHub webhook + API integration         |
| Day 3| Langchain summarizer logic               |
| Day 4| Format & save `.mdx` files               |
| Day 5| Blog display in frontend                 |
| Day 6| Deployment + GitHub webhook setup        |
| Day 7| Final polish & testing                   |

---

**Let me know** if you want this broken into GitHub issues or a Notion board!
