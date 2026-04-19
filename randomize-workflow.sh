#!/bin/bash

workflow_file=".github/workflows/reschedule.yml"
minute=$(shuf -i 0-58 -n 1)
cron_string="$minute * * * *"

# Use sed to find and replace the cron line in the workflow file
sed -i "s/^    - cron:.*/    - cron: $cron_string/" "$workflow_file"