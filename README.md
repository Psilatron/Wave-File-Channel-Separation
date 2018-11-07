# Wave-File-Channel-Separation

A simple script to seperate the left and right channels of a stereo .wav file, and ouptut these as individual .wav files. After running the script, a window will appear which will allow you to select a folder which has the .wav files you wish to process. The output will be written to the 'OUTPUT' directory of the folder you have selected, along with a log file. 

## Requirements and info

- Stereo only (for now).
- Audio files of different sample rates ok.
- Only .wav format supported (for now).
- The directory containing .wav files to be processed can contain mono or multi-channel .wavs with > 2 channels (however, these will be ignored).
- This program will batch process the .wav files in the selected directory.
