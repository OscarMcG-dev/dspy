#!/usr/bin/env bash
set -euo pipefail
npx promptfoo eval --config api/tasks/$1/promptfoo/promptfooconfig.yaml
