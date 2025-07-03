# Webhook Receiver & UI

This repository contains a basic webhook receiver built in Python using Flask.

## Features
- Webhook receiver endpoint (`/webhook`)
- Handles timestamp freshness
- Ignores duplicate or stale data
- Clean, commented code

## Setup

```bash
pip install -r requirements.txt
python app/main.py
