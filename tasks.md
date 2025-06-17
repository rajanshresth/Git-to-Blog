# 📝 git-to-blog — Project Roadmap

## 🎯 Goal

Aggregate all GitHub commit pushes for a 24-hour period, summarize them into a blog post using Langchain/Langraph, FastAPI, and OpenAI, and publish the result to your blog website.

---

## ✅ Phase 1: Foundations & Webhook

- [x] Initialize FastAPI project
- [x] Set up GitHub webhook endpoint: `POST /github/webhook`
- [x] Parse and store incoming push event payloads (repo, commit SHAs, messages, diffs)
- [ ] Store received commits in a database or temporary storage for aggregation

---

## 🕒 Phase 2: Daily Commit Aggregation

- [ ] Implement a scheduled job (e.g., cron, APScheduler) to run every 24 hours
- [ ] Aggregate all commits received in the last 24 hours, grouped by repo (and optionally by author)
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

## 🚀 Phase 6: Automation, Testing & Polish

- [ ] End-to-end test: GitHub push → webhook → aggregation → AI summary → blog post → website
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

| Day   | Task                                      |
| ----- | ----------------------------------------- |
| Day 1 | FastAPI setup, webhook, commit storage    |
| Day 2 | Aggregation logic, GitHub API integration |
| Day 3 | Langchain/OpenAI summarizer               |
| Day 4 | Blog post generation & storage            |
| Day 5 | Frontend integration                      |
| Day 6 | Automation, polish, deployment            |
| Day 7 | Final testing & stretch goals             |

---

**Let me know if you want this broken into GitHub issues, a Notion board, or want help with any specific phase!**
