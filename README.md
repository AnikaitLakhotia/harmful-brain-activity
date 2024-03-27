# Harmful Brain Activity

## How to run the Main ipynb file?

### 1. Setting Up Kaggle folder to download the dataset

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


### 2. Running the Virtual Enviornment 

You can skip steps 2 and 3 by running:
```bash
make [-r] 
```
> `-r` will remove the zip file after downloaded

- Create and run the virtual enviornment 
  
```bash
python -m venv venv
source venv/bin/activate
```

You may have to run 

- Uninstalls and then install ipykernel, lib necessary to run jupyter files.
```bash
pip uninstall ipykernel
pip install ipykernel
```



### 3. Running the Jupyter files

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

## Ease of Reusability

- Once you run the main ipynb file, you do not need to extract all the data from data folder at all. 
- Once created X_train_list.npy consists of all the possible data you need for a single instance of x_train.
