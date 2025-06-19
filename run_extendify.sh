#!/bin/zsh

cd ~/Desktop/extendify
source venv/bin/activate

output=$(python3 extendify.py 2>&1)
exit_code=$?

show_notification() {
  local title="$1"
  local message="$2"
  osascript <<EOF
display notification "${message}" with title "${title}"
EOF
}

if [ $exit_code -eq 0 ]; then
  show_notification "Spotify Quick Action ✅" "$output"
else
  show_notification "Spotify Quick Action ❌" "Something went wrong: $output"
fi