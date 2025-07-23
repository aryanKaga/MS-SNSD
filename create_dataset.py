import os
import numpy as np
import threading
import time
import psutil
from stft import convert_to_magnitude,get_duration_difference_ms
import re


dataset={"input":[],"output":[]}




terminal_direc=os.getcwd()

clean_speech_dir=os.path.join(terminal_direc,'CleanSpeech_training') # directory for clean files
noisy_speech_dir=os.path.join(terminal_direc,'data10','NoisySpeech_training') #directory for noisy files

clean_speech=os.listdir(clean_speech_dir)
noisy_speech=os.listdir(noisy_speech_dir)

total_length_list=len(os.listdir(clean_speech_dir)) # the total length depends on unique clean speech available as data

dataset_list = [{"input": [], "output": []} for _ in range(total_length_list+1)]

for filename in clean_speech:
    file_digit = int(re.search(r'clnsp(\d+)\.wav',filename).group(1))
   
    dataset_list[file_digit]['output'].append(filename)


maxindex=0
for filename in noisy_speech:
    file_digit = int(re.search(r'clnsp(\d+)\.wav',filename).group(1))
    
    dataset_list[file_digit]['input'].append(filename)



def create_mag_spectra_dataset():
    
    mag_data={"input":[],"output":[]}


    for data in range(len(dataset_list)):

        input_file=data['input'] #its the clean file to be extracted

        input_mag=convert_to_magnitude(os.path.join(clean_speech_dir,input_file))

        output_file=data['output'] # its list of noisy file corresponding to the above clean file


        for filename in output_file:

            output_mag=convert_to_magnitude(os.path.join(noisy_speech_dir,filename))

            min_width=min(input_mag.shape[1],output_mag.shape[1])

            input_mag=input_mag[:,:min_width]

            output_mag=output_mag[:,:min_width]

            mag_data['input'].append(input_mag)
            mag_data['output'].append(output_mag)

        
    return mag_data
            
            
            
            







