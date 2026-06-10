#!/bin/bash
set -euo pipefail
WORKSPACE_ROOT="/home/kessiathecreator/recovery_robot"
HOME_DIR="/home/kessiathecreator"
echo "Syncing system images and clearing temporary logs..."
if [ -f "$HOME_DIR/vendor_boot.img" ]; then
    echo "Detecting raw system image in home directory. Creating reference point..."
    sha256sum "$HOME_DIR/vendor_boot.img" > "$WORKSPACE_ROOT/configs/current_target_hash.txt"
fi
find "$WORKSPACE_ROOT" -type d -name "__pycache__" -exec rm -rf {} +
echo "Done."
