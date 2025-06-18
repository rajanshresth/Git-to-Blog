# 📝 git-to-blog — Project Roadmap

## 🎯 Goal

Aggregate all GitHub commit pushes for a 24-hour period, summarize them into a blog post using Langchain/Langraph, FastAPI, and OpenAI, and publish the result to your blog website. Support both webhook and OAuth-based GitHub integration for scalable, multi-repo, multi-user tracking.

---

## ✅ Phase 1: Foundations & Integration

- [x] Initialize FastAPI project
- [x] Set up GitHub webhook endpoint: `POST /github/webhook` (optional, for repos where you control settings)
- [x] Implement GitHub OAuth flow for user authentication and repo access
- [ ] Store user OAuth tokens securely
- [x] Allow users to select which repositories to track

---

## 🕒 Phase 2: Daily Commit Aggregation

- [ ] Implement a scheduled job (e.g., cron, APScheduler) to run every 24 hours
- [ ] For each connected user, fetch all commits from selected repos in the last 24 hours using GitHub API
- [ ] Aggregate commits by repo (and optionally by author)
- [ ] Fetch additional commit data/diffs from GitHub API as needed

---

## 🤖 Phase 3: AI Summarization

- [ ] Integrate Langchain/Langraph and OpenAI
- [ ] Design prompt templates for summarizing daily commit activity into a blog post
- [ ] Generate blog post content (title, summary, tags, MDX body) from aggregated commits

---

## 💾 Phase 4: Blog Post Storage & Publishing

- [ ] Choose storage method:
  - [ ] Push `.mdx` file to a content repo (GitHub)
  - [ ] Upload to S3 or database
- [ ] Automate publishing/upload from FastAPI backend
- [ ] Trigger blog rebuild or notify frontend (if needed)

---

## 🌐 Phase 5: Blog Website Integration

- [ ] Configure Next.js (or your blog platform) to fetch/import new blog posts
- [ ] Render blog post with commit metadata, author, date, and links
- [ ] Add blog home page and individual post pages

---

## 👤 Phase 6: User Dashboard & Management

- [ ] Build a dashboard for users to:
  - [ ] Connect/disconnect GitHub account
  - [ ] Select repositories to track
  - [ ] View and manage generated blog posts

---

## 🚀 Phase 7: Automation, Testing & Polish

- [ ] End-to-end test: GitHub OAuth → aggregation → AI summary → blog post → website
- [ ] Handle edge cases (no commits, non-code commits, large diffs)
- [ ] Add logging, error handling, and notifications
- [ ] Polish UI/UX, add RSS, share buttons, etc.

---

## 🧠 Stretch Goals

- [ ] Support multiple repos/authors
- [ ] Weekly/monthly digests
- [ ] Image/media support in blog posts
- [ ] SaaS/multi-user support

---

## 🗓️ Example Timeline

| Day   | Task                                          |
| ----- | --------------------------------------------- |
| Day 1 | FastAPI setup, OAuth, webhook, commit storage |
| Day 2 | Aggregation logic, GitHub API integration     |
| Day 3 | Langchain/OpenAI summarizer                   |
| Day 4 | Blog post generation & storage                |
| Day 5 | Frontend integration                          |
| Day 6 | Automation, polish, deployment                |
| Day 7 | Final testing & stretch goals                 |

---

**Let me know if you want this broken into GitHub issues, a Notion board, or want help with any specific phase!**
