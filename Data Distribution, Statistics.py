Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> ######### Write a Python program using Pandas to calculate and display central tendencies and dispersion measures for the data from 1experience.csv
>>> ##Central Tendency - >1. Mean , 2.Median ,3.Mode.
>>> import pandas as pd
>>> file=r'C:\Users\CHIRANTH D\OneDrive\Desktop\BCA Hons\SEM - 02\PYTHON LAB\Github Assingment\1experience.csv'
>>> df=pd.read_csv(file)
>>> column = 'YearsExperience'
>>> #Mean
>>> print(df[column].mean())
2.266666666666667
>>> #median
>>> print(df[column].median())
2.2
>>> #Mode
>>> print(df[column].mode()[0])
3.2
>>> ### dispersion measures -> 1. Standard Deviation ,2.Variance ,3.Range.
>>> ### Standard Deviation
>>> print(df[column].std())
0.8396427811873333
>>> ### Variance
>>> print(df[column].var())
0.7050000000000001
>>> ### Range
>>> print(df[column].max() - df[column].min())
2.1
