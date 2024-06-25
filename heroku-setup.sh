#!/bin/bash
apt-get update && apt-get install -y --no-install-recommends $(cat Aptfile)
playwright install chromium
