import sys, subprocess, os

# This Python script is used to run a medical image segmentation task using the TotalSegmentator software. 
# The script operates on a list of tasks, where each task corresponds to a different type of medical image data.

# List of tasks to run, where each task corresponds to a different type of medical image data.
# Input data is from Medical Segmentation Decathlon (MSD) http://medicaldecathlon.com/
task_list = ['Task03_Liver', 'Task10_Colon', 'Task05_Prostate', 'Task07_Pancreas'] 

# TotalSegmentator version used v1.5.7 https://github.com/wasserth/TotalSegmentator/tree/v1.5.7
input_path_pattern = '/home/azureuser/cloudfiles/code/Users/data/msd/###/imagesTr'
sys.path.append('/home/azureuser/cloudfiles/code/Users/models/TotalSegmentator')

for task_name in task_list:
    input_path = input_path_pattern.replace('###', task_name)
    output_path = input_path.replace('msd', 'msd_segmentation')
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # List files which end with .nii.gz in input_path
    files = [f for f in os.listdir(input_path) if f.endswith('.nii.gz')]
    for f in files:
        # Run totalsegmentator
        output_path = input_path.replace('msd', 'msd_segmentation')
        output_file = os.path.join(output_path, f)
        if os.path.exists(output_file):
            print('Skipping {} because it already exists'.format(output_file))
            continue

        command = ['TotalSegmentator', \
                    '-i', os.path.join(input_path, f), \
                    '-o', output_file,  '-ml'] #, '--statistics']

        print(command)
        subprocess.run(command)

