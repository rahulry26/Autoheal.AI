
#!/bin/bash

echo "Starting AutoHeal.AI on Render port $PORT"
uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-10000}

