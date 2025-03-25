#!/usr/bin/env python

import os
import subprocess
import sys

# usage: python cut_fmri_data_toystory.py <subject> <space>
# use "standard" space by default to stay in MNI space 

subject = sys.argv[1]
native_or_standard_space = sys.argv[2]

if native_or_standard_space=='native':
    space = '_native_space'
elif native_or_standard_space=='standard':
    space=''
else:
    raise Exception

input_folder = '/jukebox/norman/rsiyer/isc/toystory/nuisance_regressed'
output_folder = '/jukebox/norman/rsiyer/isc/toystory/nuisance_regressed_cut'

assert os.path.exists(input_folder)
assert os.path.exists(output_folder)

input_file = subject + space + '.nii.gz'
input_path = os.path.join(input_folder, input_file)
output_file = subject + space + '.nii.gz'
output_path = os.path.join(output_folder, output_file)

print(input_path, output_path)
assert os.path.exists(input_path)

result = subprocess.check_output(['fslinfo', '%s' % input_path], universal_newlines=True)
result = result.split()
fslinfo = {result[i]: result[i + 1] for i in range(0, len(result), 2)}

dim4 = int(fslinfo['dim4'])
print(dim4)

if dim4 == 300:
    start_vol = 12
elif dim4 == 295:
    start_vol = 7

assert dim4 in [300, 295]
fslroi = ['fslroi %s %s %i 288' % (input_path, output_path, start_vol)]
print(fslroi[0])
subprocess.run(fslroi, shell=True)
print("done")


# import subprocess

# pathname = '/Volumes/BCI/Ambivalent_Affect/fMRI_Study/ISC_Data'

# quick and dirty way to view lengths of all files
# dim4_array=(); 
# for file in *.nii.gz 
    # dim4=$(fslinfo input.nii.gz | awk '/^dim4/ {print $2}')
    # dim4_array+=("$dim4")
# done
# echo $dim4_array

# # General form:

# # dim4=$(fslinfo input.nii.gz | awk '/^dim4/ {print $2}')
#     # $ refers to setting a variable
#     # | passes the output of the prev part on, so the fslinfo output goes to awk which wild card finds dim4 and takes
#         # the 2nd column which has the actual data (1st column is the header "dim4")
# # fslroi input.nii.gz output.nii.gz start_vol num_vols
# for i, input_file in enumerate(input_files):
#     output_file = output_files[i]
#     result = subprocess.check_output(['fslinfo', '%s' % input_file], universal_newlines=True)  # result gets the
#     # output of running the fslinfo command, universal_newlines converts it into a string rather than a bytes object
#     result = result.split()  # splits string into list
#     fslinfo = {result[i]: result[i + 1] for i in range(0, len(result), 2)}  # dict comprehension to convert list into
#     # keys and values based on alternating indices

#     dim4 = int(fslinfo['dim4'])  # value of dim4 key in fslinfo dict
#     print(dim4)

# # by default for the 472 ones, take off 12 from the beginning and 6 from the end
# # if 470, cut 14 from beginning and 2 from end (edited)

#     if dim4 == 472:
#         print("its 472")
#         start_vol = 12
#     elif dim4 == 471:
#         print("its 471")
#         start_vol = 13
#     elif dim4 == 470:
#         print("its 470")
#         start_vol = 14
    
#     assert dim4 in [470, 471, 472]
#     fslroi = ['fslroi %s %s %i 454' % (input_file, output_file, start_vol)]
#     print(fslroi[0])
#     subprocess.run(fslroi, shell=True)
#     print("done")
