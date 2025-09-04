#!/usr/bin/env python

import os
import subprocess
import sys

subject = sys.argv[1]
native_or_standard_space = sys.argv[2]

if native_or_standard_space=='native':
    space = '_native_space'
if native_or_standard_space=='standard':
    space=''

input_folder = '/usr/people/ri4541/juke/isc/outputs/onesmallstep/data'
output_folder = '/usr/people/ri4541/juke/isc/outputs/onesmallstep/data/nuisance_regressed_cut'

input_file = subject + space + '.nii.gz'
input_path = os.path.join(input_folder, input_file)
output_file = subject + space + '.nii.gz'
output_path = os.path.join(output_folder, output_file)

result = subprocess.check_output(['fslinfo', '%s' % input_path], universal_newlines=True)
result = result.split()
fslinfo = {result[i]: result[i + 1] for i in range(0, len(result), 2)}

dim4 = int(fslinfo['dim4'])
print(dim4)

if dim4 == 472:
    start_vol = 12
elif dim4 == 471:
    start_vol = 13
elif dim4 == 470:
    start_vol = 14
else:
    raise ValueError

fslroi = ['fslroi %s %s %i 454' % (input_path, output_path, start_vol)]
print(fslroi[0])
subprocess.run(fslroi, shell=True)
print("done")
