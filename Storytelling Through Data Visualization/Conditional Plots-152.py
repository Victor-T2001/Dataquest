## 2. Introduction to the Data Set ##

import pandas as pd
titanic = pd.read_csv("train.csv")
cols = ["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
titanic = titanic[cols].dropna()

## 3. Creating Histograms In Seaborn ##

import seaborn as sns    # seaborn is commonly imported as `sns`
import matplotlib.pyplot as plt
sns.distplot(titanic["Age"])
plt.show()

## 4. Generating A Kernel Density Plot ##






import seaborn as sns   
import matplotlib.pyplot as plt
sns.kdeplot(titanic["Age"], shade = True)
plt.xlabel("Age")
plt.show()

## 5. Modifying The Appearance Of The Plots ##

import seaborn as sns   
import matplotlib.pyplot as plt
sns.set_style("white")

sns.kdeplot(titanic["Age"], shade = True)
plt.xlabel("Age")
sns.despine(left = True, bottom = True)
plt.show()

## 6. Conditional Distributions Using A Single Condition ##

# Condition on unique values of the "Survived" column.
g = sns.FacetGrid(titanic, col="Pclass", size=6)
# For each subset of values, generate a kernel density plot of the "Age" columns.
sns.despine(left = True, bottom = True)
g.map(sns.kdeplot, "Age", shade=True)

#g = sns.FacetGrid(titanic, col="Survived", size=6)
#g.map(plt.hist, "Age")

## 7. Creating Conditional Plots Using Two Conditions ##

g = sns.FacetGrid(titanic, col="Survived", row="Pclass")
g.map(sns.kdeplot, "Fare", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

## 8. Creating Conditional Plots Using Three Conditions ##

g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue = 'Sex', size = 3)
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

## 9. Adding A Legend ##

g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue = 'Sex', size = 3)

g.map(sns.kdeplot, "Age", shade=True)
g.add_legend()
sns.despine(left=True, bottom=True)
plt.show()
