#!/usr/bin/env python3
import pandas as pd
from subprocess import call
import os

# ToyStoryNuisanceRegressed folder (output folder) needs to exist

subjects = [
    "Pilot3",
    # "VR1",
    # "VR10",
    # "VR11",
    # "VR12",
    # "VR13",
    # "VR14",
    # "VR16",
    # "VR17",
    # "VR18",
    # "VR19",
    # "VR2",
    # "VR20",
    # "VR21",
    # "VR22",
    # "VR23",
    # "VR3",
    # "VR4",
    # "VR5",
    # "VR7",
    # "VR8",
    # "VR9",
    # "pilot01",
    # "pilot2"
]

print(f'{len(subjects)} subjects entered')

fmriprep_folder = "/jukebox/norman/rsiyer/isc/toystory/fmriprep/"
task = 'toystory'
study = 'ses-KaplanVRCyberball'
output_folder = "/jukebox/norman/rsiyer/isc/toystory/nuisance_regressed"

assert os.path.exists(output_folder)

bad_subj = []
for s, subject in enumerate(subjects): 
	fmripreproot= fmriprep_folder + 'sub-' + subject + f'/{study}/func'
	tsv = f"{fmripreproot}/sub-{subject}_{study}_task-{task}_run-01_desc-confounds_timeseries.tsv"
	if not os.path.isfile(tsv):
		print(tsv)
		print(f'del {subjects[s]}')
		# breakpoint()
		del subjects[s]	
		s -= 1

print(f'there are {len(subjects)} subjects being nuisance regressed')

for subject in subjects:
	print(subject)
	fmripreproot= fmriprep_folder + 'sub-' + subject + f'/{study}/func'
	input_file= f"{fmripreproot}/sub-{subject}_{study}_task-{task}_run-01_desc-confounds_timeseries.tsv" 
	df = pd.read_csv(input_file, sep="\t", encoding='latin-1')
	columns_to_extract = []
	for col in df.columns[4:13]:
		columns_to_extract.append(col)
	for col in df.columns:
		if "aroma" in col.lower():
			columns_to_extract.append(col)
	df_extracted = df[columns_to_extract]
	if subject == "pilot01":
		sub = "P1"
	elif subject == "pilot2":
		sub = "P2"
	elif subject == "Pilot3":
		sub = "P3"
	else:
		sub = subject
	nuisance_regressor = fmripreproot + '/' + sub + 'nuisance.tsv'
	df_extracted.to_csv(nuisance_regressor, sep="\t", index=False)
	# time.sleep(1)  # for I/O
	uncut_data = f"{fmripreproot}/sub-{subject}_{study}_task-{task}_run-01_space-MNI152NLin6Asym_desc-smoothAROMAnonaggr_bold.nii.gz"
	# os.system(f"")

	uncut_regressed = f"{output_folder}/%s.nii.gz" % sub
	beta = f"{output_folder}/%s_beta.nii.gz" % sub
	command = 'fsl_glm -i %s -d %s -o %s --out_res=%s' % (uncut_data,nuisance_regressor,beta,uncut_regressed)
	# print(uncut_data)
	# print(command)
	# os.system(f"fslinfo {uncut_data} | grep 'data_type'")
	call(command,shell=True)
