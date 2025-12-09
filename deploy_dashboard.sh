#!/bin/bash
set -e  # stop on error

echo "🚀 Starting Streamlit dashboard deployment..."

# Move into dashboard folder
cd "$(dirname "$0")/.."

# Optional: Install dependencies (if not already)
pip install -r ../requirements.txt || true

# Launch Streamlit dashboard
nohup streamlit run app.py --server.port 8501 --server.headless true &

echo "✅ Streamlit dashboard launched successfully on port 8501"

