#!/bin/bash
# save as: curl_openai.sh
# Make it executable: chmod +x curl_openai.sh
# Usage: ./curl_openai.sh

# OpenAI API endpoint
API_URL="https://api.openai.com/v1/responses"

# Your API key (replace with your actual key if needed)
API_KEY="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"

# Model and prompt
MODEL="gpt-5-nano"  # Note: This model does not exist; use a real one like "gpt-4o-mini" or "gpt-4o"
PROMPT="write a haiku about ai"

# JSON payload
PAYLOAD=$(cat <<EOF
{
  "model": "$MODEL",
  "input": "$PROMPT",
  "store": true
}
EOF
)

echo "Sending request to OpenAI API..."

curl -s \
  -X POST "$API_URL" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d "$PAYLOAD"

echo -e "\n\nRequest complete."
