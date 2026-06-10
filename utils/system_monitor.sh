#!/bin/bash
set -euo pipefail
echo "=== RECOVERY ROBOT HOST STATUS ==="
if [ -d /sys/class/thermal/thermal_zone0 ]; then
    TEMP_RAW=$(cat /sys/class/thermal/thermal_zone0/temp)
    echo "CPU Temperature: $((TEMP_RAW / 1000))°C"
fi
if [ -d /sys/class/power_supply/BAT0 ]; then
    CAPACITY=$(cat /sys/class/power_supply/BAT0/capacity)
    STATUS=$(cat /sys/class/power_supply/BAT0/status)
    echo "Host Battery: ${CAPACITY}% (${STATUS})"
fi
free -m | awk 'NR==2{printf "Container RAM Usage: %s/%sMB (%.2f%%)\n", $3,$2,$3*100/$2 }'
