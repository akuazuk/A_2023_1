import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.write("""
# Decision Tree Classifier
This app is a simple example of using a decision tree classifier for a 
binary classification task.
""")

def load_data():
    data = pd.read_csv("data.csv")
    return data

@st.cache
def split_data(data):
    X = data.drop("target", axis=1)
    y = data["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
test_size=0.2, random_state=0)
    return X_train, X_test, y_train, y_test

def run_classifier(X_train, X_test, y_train, y_test):
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    return acc

data = None
if st.button("Load Data"):
    data = load_data()
    X_train, X_test, y_train, y_test = split_data(data)
    acc = run_classifier(X_train, X_test, y_train, y_test)
    st.write("Accuracy: ", acc)

if data is not None:
    st.dataframe(data)

