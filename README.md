# Harmful Brain Activity

# How to run the Main ipynb file?

- If running for the first time
  - Run the enviornment_setup.ipynb.
  - Then run harmful_brain_activity.ipynb
- Else
  - Directly run harmful_brain_activity.ipynb

#### Updates from Sargun
- Added EEG_Research folder
- Contains image files that explains the outputs.
- Contains sample_eeg.parquet and sample_spectrogram.parquet, which are the input files.
- Contains EEG_Research.ipynb, which is the jupyter notebook going over everything.
- Contains convert-jupyter.sh that convert EEG_Research.ipynb to EEG_Research.pdf
- Created a virtual enviornment for python, so you have no problems with dependencies.

To run ./convert-jupyter.sh after updating EEG_Research.ipynb, do, in your command line

```bash
cd EEG_Research
chmod a+x convert-jupyter.sh
./convert-jupyter.sh
```

## Running the Virtual Enviornment 

```bash
source venv/bin/activate
```

## gitignore inputs

- If you run and want to commit to GitHub, have in your .gitignore

```
logs
test_spectrograms
train_spectrograms
test_eegs
train_eegs
X_train_list.npy
hms-harmful-brain-activity-classification.zip
```

## Setting Up Kaggle folder to download the dataset

- Go the Kaggle Settings
- Go to Settings
- Scroll down to API
- Create New Token and then save the file kaggle.json on your computer.
- Open terminal and browse to the place where you stored kaggle.json
- Then run the following code in the terminal

```bash
mkdir ~/.kaggle
scp kaggle.json ~/.kaggle/kaggle.json 
```