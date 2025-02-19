# AXA Insurance data scientist interview technical assessment
This repo is for completing technical assessment for AXA insurance data scientist interview. This task is using a dataset from Kaggle competition, i.e. https://www.kaggle.com/datasets/anthonytherrien/depression-dataset/data . It contains 3 questions:

1. Use methods of your choice (e.g. exploratory data analysis, statistical methods, visualisations etc.)  to extract useful insights from the data. 
2. Use suitable models to predict if an individual will suffer mental illness (variable titled “History of Mental Illness”) using all or some of the other variables present in the data. 
3. What are the limitations of your chosen approach? How can you improve the performance of your model?

 
## Coding environment
`Python 3.12.7` is used for this task, and the virtual environment of Jupyter notebook and Python scripts are managed using `conda`. 

To **build the conda environment**:

```conda create --name axa-depression-classifier python=3.12.7 --file requirements.txt ```

To **activate the environment**:

```conda activate axa-depression-classifier```

## Files contained within this repo
The `data` contains the dataset from Kaggle website, and `src` contains main coding for EDA and model codes.
