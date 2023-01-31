import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier

@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def main():
    st.title("Machine Learning Model - Kyphosis Detection")
    st.sidebar.title("Kyphosis Detection")

    file_path = st.sidebar.file_uploader("Upload Kyphosis Data (CSV file)", type=["csv"])
    if file_path is not None:
        data = load_data(file_path)
        st.dataframe(data.head())
        st.write("Number of rows and columns:", data.shape)

        X = data.drop("Kyphosis", axis=1)
        y = data["Kyphosis"]

        st.sidebar.subheader("Model Selection")
        algorithm = st.sidebar.selectbox("Select Algorithm", ["Decision Tree"])

        if algorithm == "Decision Tree":
            clf = DecisionTreeClassifier()
            clf.fit(X, y)
            accuracy = clf.score(X, y)
            st.write("Accuracy: ", accuracy)

        st.subheader("Visualizing Data")
        if st.checkbox("Show Scatter Plot with Class labels"):
            plt.scatter(X["Age"], X["Number"], color='red, cmap="viridis")
            plt.xlabel("Age")
            plt.ylabel("Number")
            st.pyplot()

if __name__ == '__main__':
    main()

