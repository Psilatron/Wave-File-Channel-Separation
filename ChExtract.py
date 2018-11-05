#!/usr/bin/env python2
# -*- coding: utf-8 -*- 
"""
Created on Wed Aug  8 11:01:34 2018

"""
# This program will seperate a 2Ch .wav file into seperate audio files.

import numpy as np
import soundfile as sf
import time
import os

#--------------------------------

def SelectDir(): #Directory selection GUI function.
    '''function to enable selection of directory by user input'''
    import Tkinter, tkFileDialog, sys
    root = Tkinter.Tk()
    root.wm_attributes("-topmost", 1)##Will display window on top of others
    root.withdraw()
    initialPath = os.getcwd()
    dirname = tkFileDialog.askdirectory(parent=root, initialdir=initialPath, title='Pick a directory')
#    dirname = tkFileDialog.askdirectory(title="Select A Folder", mustexist=1)
#    print("dirname: ", dirname)
    if dirname is '':
        print "Selection Cancelled"
        sys.exit(1)
    root.destroy()
    return dirname
 
def ChSeperate(): #Channel seperation function.
       
    [ChLeft,ChRight]=Audio2Ch[:,0],Audio2Ch[:,1];

    return ChLeft,ChRight

#--------------------------------

current_directory = str(SelectDir()) 
os.chdir(current_directory) #change directory to user selected directory
current_directory = os.getcwd()

file_list = []

start_time = time.time()
for file in os.listdir(current_directory):
    if file.endswith(".wav"):
        if file.startswith("._"): #to exclude ghost files starting with "._"         
            continue
        else:
            file_list.append(file) 

print('')
print('Program Start...')
print('Now separating channels...\n')

ListSz=float(np.size(file_list)) #Shows number of filenames contained in 'file_list' list.

if not os.path.exists("OUTPUT"): #Checks for 'OUTPUT' directory. Will make one if none there.
    os.makedirs("OUTPUT")

f= open("OUTPUT\Log.2chSeperation.txt","w+") #this will create a new text file, and open it.
f.write("=======[Proccessing Info]=======\n"+"\n")

f_counter=0;

for x in range(0,np.size(file_list)): #Step through file names. Read Stereo .wav files using soundfile read() function.
    
    [Audio2Ch,fs]=sf.read(file_list[x])
    
    ChCount=np.ndim(Audio2Ch)
    
    if ChCount == 2:
        f_counter=f_counter+1;

        [Left,Right]=ChSeperate()   
        
        sf.write('OUTPUT\ '+str(f_counter).zfill(3)+'.Lch_'+file_list[x],Left,fs)
        sf.write('OUTPUT\ '+str(f_counter).zfill(3)+'.Rch_'+file_list[x],Right,fs) 
        f.write("File OK: "+file_list[x]+"\n"+"\n")
        
    else:
        print("Warning: File "+ file_list[x]+" is not Stereo\n")
        f.write("Warning: File "+ file_list[x]+" is not Stereo\n"+"\n")

out_file_count=f_counter*2

elapsed_time = time.time() - start_time
elapsed_time = round(elapsed_time, 2) 

file_str="File"

if f_counter>1:
    file_str="Files"
    
f.write("------------[Summary]----------\n"+"\n")
f.write("Processing Time: " + str(elapsed_time) + " Sec."+"["+str((elapsed_time)/60)+" Mins"+"]\n")
f.write(str(out_file_count/2)+" "+file_str+" Processed, ")
f.write(str(out_file_count)+" Files Created.")
f.close()

print(  '------------[Summary]----------\n')
print('Total Processing Time: ' + str(elapsed_time) + ' Sec.' +'['+str((elapsed_time)/60)+' Mins.]') 
print(str(out_file_count/2)+" "+file_str+" Processed, " + str(out_file_count)+" Files Created.")
print('See Log.2chSeperation.txt in OUTPUT directory for summary.')