#!/bin/bash

# Define the list of subjects
subjects=(
    # "P3"
    "VR1"
    "VR10"
    "VR11"
    "VR12"
    "VR13"
    "VR14"
    "VR16"
    "VR17"
    "VR18"
    "VR19"
    "VR2"
    "VR20"
    "VR21"
    "VR22"
    "VR23"
    "VR3"
    "VR4"
    "VR5"
    "VR7"
    "VR8"
    "VR9"
    "P1"
    "P2"
)

# Default space
SPACE="standard"

# Allow space to be set as an argument
if [ ! -z "$1" ]; then
    SPACE="$1"
fi

# Path to the Python script
PYTHON_SCRIPT="cut_fmri_data_toystory.py"

# Loop through each subject and run the Python script
for subj in "${subjects[@]}"; do
    echo "Processing subject: $subj in space: $SPACE"
    python "$PYTHON_SCRIPT" "$subj" "$SPACE"
    echo "Finished processing $subj"
done
