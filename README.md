# Harmful Brain Activity

## How to run the Main ipynb file?

### 1. Running the Virtual Enviornment 

```bash
source venv/bin/activate
```

You may have to run 

```bash
pip uninstall ipykernel
pip install ipykernel
```


### 3. Setting Up Kaggle folder to download the dataset

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

### 2. Running the Jupyter files

- If running for the first time
  - Run the enviornment_setup.ipynb.
  - Then run harmful_brain_activity.ipynb
- Else
  - Directly run harmful_brain_activity.ipynb


## Working with EEG_Research.ipynb

To run ./convert-jupyter.sh after updating EEG_Research.ipynb, do, in your command line

```bash
cd EEG_Research
chmod a+x convert-jupyter.sh
./convert-jupyter.sh
```
