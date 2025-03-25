# do not use this script; this tried to save corrupted fmriprep or nuisance regressed files by editing binaries, but i re-ran fmriprep instead

# import os
# import glob

# # List of subject IDs
# subjects = ['VR1','VR9','VR20','pilot01','pilot2','Pilot3','VR10','VR11','VR12','VR13','VR14','VR16','VR17','VR18','VR19','VR2','VR21','VR22','VR23','VR3','VR4','VR5','VR7','VR8']

# # Path template for the NIfTI files
# base_path = "/Volumes/BCI/Ambivalent_Affect/fMRI_Study/ToyStoryOutput"

# # Function to check and fix byte 348 in a NIfTI file
# def check_and_fix_nifti(file_path):
#     try:
#         with open(file_path, "r+b") as f:  # Open in read+write binary mode
#             f.seek(348)  # Move to byte index 348
#             byte_value = f.read(1)  # Read 1 byte
            
#             print(f"Byte 348: {byte_value.hex()}")

#             if byte_value != b'\x00':  # If it's nonzero, fix it
#                 f.seek(348)
#                 f.write(b'\x00')
#                 print(f"Fixed byte 348 in {file_path}")

#     except Exception as e:
#         print(f"Error processing {file_path}: {e}")

# # Iterate over subjects and process their files
# for subject in subjects:
#     search_pattern = os.path.join(
#         base_path,
#         f"sub-{subject}/ses-KaplanVRCyberball/func",
#         f"sub-{subject}_ses-KaplanVRCyberball_task-toystory_run-01_space-MNI152NLin6Asym_desc-smoothAROMAnonaggr_bold.nii.gz"
#     )
    
#     files = glob.glob(search_pattern)  # Search for matching files

#     if not files:
#         print(f"No files found for subject {subject}")
#     else:
#         for file_path in files:
#             check_and_fix_nifti(file_path)

