
#!/bin/bash

# Default to port 10000 if not set
PORT=${PORT:-10000}

echo "Starting AutoHeal.AI on port $PORT"

# Start Uvicorn using dynamic port
uvicorn app.main:app --host 0.0.0.0 --port $PORT

