#!/usr/bin/env python3
import pandas as pd
from subprocess import call

subjects= ["VR15","VR17","VR18","VR19","VR21","VR22","VR23"]

fmriprep_folder = "/Volumes/BCI/Ambivalent_Affect/fMRI_Study/fMRIPrep_Output/"

for subject in subjects:
	fmripreproot= fmriprep_folder + 'sub-' + subject + '/ses-KaplanVRCyberball/func'
	input_file= fmripreproot+ "/sub-%s_ses-KaplanVRCyberball_task-onesmallstep_run-01_desc-confounds_timeseries.tsv" % subject
	df = pd.read_csv(input_file, sep="\t")
	columns_to_extract = []
	for col in df.columns[4:13]:
		columns_to_extract.append(col)
	for col in df.columns:
		if "aroma" in col.lower():
			columns_to_extract.append(col)
	df_extracted = df[columns_to_extract]
	if subject== "pilot01":
		sub = "P1"
	elif subject== "pilot2":
		sub= "P2"
	elif subject=="Pilot3":
		sub="P3"
	else:
		sub= subject
	nuisance_regressor= fmripreproot + '/' + sub + 'nuisance.tsv'
	df_extracted.to_csv(nuisance_regressor, sep="\t", index=False)
	uncut_data= fmripreproot + '/sub-'+ subject + "_ses-KaplanVRCyberball_task-onesmallstep_run-01_space-MNI152NLin6Asym_desc-smoothAROMAnonaggr_bold.nii.gz"
	uncut_regressed = "/Volumes/BCI/Ambivalent_Affect/fMRI_Study/ISC_Data/NuisanceRegressed/%s.nii.gz" % sub
	beta = "/Volumes/BCI/Ambivalent_Affect/fMRI_Study/ISC_Data/NuisanceRegressed/%s_beta.nii.gz" % sub
	command = 'fsl_glm -i %s -d %s -o %s --out_res=%s' % (uncut_data,nuisance_regressor,beta,uncut_regressed)
	call(command,shell=True)

