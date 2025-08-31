import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier

test_data = pd.read_csv("titanic/test.csv")
train_data = pd.read_csv("titanic/train.csv")

for i in range(0,4):
    if i == 0:
        men = train_data.loc[(train_data.Sex == 'male'), "Survived"]
        rate_men=sum(men)/len(men)
        print(f"Men have a probability of surviving of {rate_men}")

    else:
        i_class_men = train_data.loc[(train_data.Pclass == i) & (train_data.Sex == 'male'), "Survived"]
        rate_i_class_men=sum(i_class_men)/len(i_class_men)
        print(f"{i}st class men have a probability of surviving of {rate_i_class_men}")

for i in range(0,4):
    if i == 0:
        women = train_data.loc[(train_data.Sex == 'female'), "Survived"]
        rate_women=sum(women)/len(women)
        print(f"\n Women have a probability of surviving of {rate_women}")

    else:
        i_class_women = train_data.loc[(train_data.Pclass == i) & (train_data.Sex == 'female'), "Survived"]
        rate_i_class_women=sum(i_class_women)/len(i_class_women)
        print(f"{i}st class women have a probability of surviving of {rate_i_class_women}")