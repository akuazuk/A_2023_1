import streamlit as st
import pandas as pd
from sklearn import tree

st.write("""
# Decision Tree Classifier App
This app predicts the class of iris flowers!
""")

st.set_page_config(page_title="Decision Tree Classifier", 
page_icon=":guardsman:", layout="wide")

def load_data():
    data = pd.read_csv("data.csv")
    return data

def run_classifier(data):
    clf = tree.DecisionTreeClassifier()
    X = data.drop(["class"], axis=1)
    Y = data["class"]
    clf = clf.fit(X, Y)
    return clf

@st.cache
def classify(clf, input_data):
    prediction = clf.predict(input_data)
    return prediction

data = st.file_uploader("Upload your iris data (csv format)", 
type=["csv"])
if data:
    data = pd.read_csv(data)
    st.write("Data Loaded!")
    clf = run_classifier(data)
    input_data = st.text_input("Enter sepal length, sepal width, petal 
length, petal width separated by commas:")
    if input_data:
        input_data = [float(x) for x in input_data.split(",")]
        prediction = classify(clf, [input_data])
        st.write("Class: ", prediction)
else:
    st.write("Please upload the data file")

