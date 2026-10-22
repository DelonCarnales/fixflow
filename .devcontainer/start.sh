#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

if ! curl --silent --fail http://127.0.0.1:8000/health >/dev/null 2>&1; then
  nohup bash -c "cd '$ROOT_DIR/backend' && exec python -m uvicorn main:app --host 0.0.0.0 --port 8000" >/tmp/fixflow-backend.log 2>&1 &
fi

if ! curl --silent --fail http://127.0.0.1:5173/ >/dev/null 2>&1; then
  nohup bash -c "cd '$ROOT_DIR/frontend' && exec python3 -m http.server 5173 --bind 0.0.0.0" >/tmp/fixflow-frontend.log 2>&1 &
fi

for attempt in $(seq 1 30); do
  if curl --silent --fail http://127.0.0.1:8000/health >/dev/null 2>&1 && curl --silent --fail http://127.0.0.1:5173/ >/dev/null 2>&1; then
    echo "FixFlow is running."
    echo "Frontend: port 5173"
    echo "Backend:  port 8000"
    exit 0
  fi
  sleep 1
done

echo "FixFlow did not start correctly. Check /tmp/fixflow-backend.log and /tmp/fixflow-frontend.log."
exit 1
