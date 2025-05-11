
#!/bin/bash

# Ensure PORT is picked up from Render's environment
echo "Starting app on port ${PORT:-10000}"
uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-10000}

