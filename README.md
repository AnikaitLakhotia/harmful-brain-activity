# Harmful Brain Activity

#### Updates from Sargun
- Added EEG_Research folder
- Contains image files that explains the outputs.
- Contains sample_eeg.parquet and sample_spectrogram.parquet, which are the input files.
- Contains EEG_Research.ipynb, which is the jupyter notebook going over everything.
- Contains convert-jupyter.sh that convert EEG_Research.ipynb to EEG_Research.pdf
- Created a virtual enviornment for python, so you have no problems with dependencies.

To run ./convert-jupyter.sh after updating EEG_Research.ipynb, do, in your command line

```bash
> cd EEG_Research
> chmod a+x convert-jupyter.sh
> ./convert-jupyter.sh
```

## Running the Virtual Enviornment 

```bash
> source venv/bin/activate
```

## Make Sure

- If you run and want to commit to GitHub, have in your .gitignore

```
logs
test_spectrograms
train_spectrograms
test_eegs
train_eegs
X_train_list.npy
```

