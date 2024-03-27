#!/bin/bash

if [ ! -d venv ]; then
        python -m venv venv
fi

if [ "$OSTYPE" == "linux-gnu"* ] || [ "$OSTYPE" == "darwin"* ]; then
        source venv/bin/activate
elif [ "$OSTYPE" == "win32" ] || [ "$OSTYPE" == "msys" ]; then
        source venv/Scripts/activate  
else
        echo "get a real operating system, tf is $OSTYPE"
        exit 69
fi

pip -q install -r requirements.txt
chmod 600 ~/.kaggle/kaggle.json
kaggle competitions download -c hms-harmful-brain-activity-classification
unzip -q hms-harmful-brain-activity-classification.zip -d data

if [ $# -eq 1 ] && [ $1 == "-r" ]; then
    rm hms-harmful-brain-activity-classification.zip
fi

echo logs > .gitignore
echo X_train_list.npy >> .gitignore
echo hms-harmful-brain-activity-classification.zip >> .gitignore
echo data >> .gitignore
echo venv >> .gitignore
