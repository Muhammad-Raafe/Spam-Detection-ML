import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import(accuracy_score,confusion_matrix,classification_report)
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv("spam.csv",encoding="latin-1")

# print(df.info())

df=df.drop(columns=["Unnamed: 2","Unnamed: 3","Unnamed: 4"])
print(df.info())

df.columns=["label","message"]
print(df.info())

le=LabelEncoder()
df["label"]=le.fit_transform(df["label"])

x=df["message"]
y=df["label"]

cv=CountVectorizer()
x=cv.fit_transform(x)

x_train,x_test,y_train,y_test=train_test_split(
    x,
    y,
    random_state=42,
    test_size=0.2
)




model=MultinomialNB()
model.fit(x_train,y_train)
prediction=model.predict(x_test)

print("Accuracy Score Is: ",accuracy_score(y_test,prediction))
print("Confusion Matrix : ",confusion_matrix(y_test,prediction))
print("Classification Report: ",classification_report(y_test,prediction))