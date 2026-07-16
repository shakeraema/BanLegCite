#!/bin/bash
# produced_by: setup_label_studio.sh
# date: 2026-07-15
# stage: Phase 1 — Infrastructure Setup
# Description: Instructions and script to setup Label Studio for citation annotation

echo "=== Label Studio Setup for BanLegit-Cite ==="

# Create a virtual environment if not already present
if [ ! -d "venv" ]; then
    echo "Creating python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install Label Studio
echo "Installing Label Studio and dependencies..."
pip install --upgrade pip
pip install label-studio

# Start Label Studio instruction
echo ""
echo "===================================================================="
echo "Label Studio setup ready. Run the following command to start Label Studio:"
echo "  source venv/bin/activate"
echo "  label-studio start"
echo ""
echo "Once Label Studio starts, create a new project and import annotation/config.xml"
echo "as the custom labeling interface template."
echo "===================================================================="
