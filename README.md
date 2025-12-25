# Formbricks Seeder

A project to programmatically seed a self-hosted Formbricks instance with realistic survey, user, and response data using APIs.

---

## Aim

To identify a candidate's ability to quickly understand, run, and interact with a new application's API system to programmatically fill it with realistic data.

---

## Brief

You are provided with Formbricks, a self-hosted open-source experience management platform. This project allows you to:

1. Run Formbricks locally using Docker/Docker Compose.
2. Generate realistic survey and user data using an LLM.
3. Seed the Formbricks instance using APIs only.

---

## Project Setup

### 1. Run Formbricks

```bash
python main.py formbricks up
```

### Commands

```bash
python main.py formbricks up
python main.py formbricks generate
python main.py formbricks seed
python main.py formbricks down
```
