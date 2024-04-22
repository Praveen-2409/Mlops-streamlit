import os
import streamlit as st
import pickle
import numpy as np

# Get the absolute path to the pickle file
pickle_file_path = os.path.join(os.getcwd(), '219.pkl')

# Check if the file exists
if os.path.exists(pickle_file_path):
    with open(pickle_file_path, 'rb') as f:
        model = pickle.load(f)
else:
    st.error("Error: pickle file '219.pkl' not found.")
    st.stop()

def predict_vol(Date, Open, High, Low, Close, AdjClose):
    input_data = np.array([[Date, Open, High, Low, Close, AdjClose]]).astype(np.float32)  # Adjust data type if needed
    print("Input data:", input_data)  # Debugging: Print input data
    print("Input data shape:", input_data.shape)  # Debugging: Print input data shape
    prediction = model.predict(input_data.reshape(1,-1))
    # pred = '{0:.{1}f}'.format(prediction, 2)
    return prediction


def main():
    st.title("Streamlit")
    html_temp = """
    <div style="background-color:black ;padding:10px">
    <h2 style="color:white;text-align:center;"> Volume Prediction</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    Date = st.number_input("Date")
    Open = st.number_input("Open")
    High = st.number_input("High")
    Low = st.number_input("Low")
    Close = st.number_input("Close")
    AdjClose = st.number_input("AdjClose")
    
    safe_html = """
       <div style="background-color:grey ;padding:10px">
       <h2 style="color:white;text-align:center;">The volume is high</h2>
       </div>
    """

    danger_html = """
       <div style="background-color:grey ;padding:10px">
       <h2 style="color:white;text-align:center;">The volume is low</h2>
       </div>
    """

    if st.button("Predict"):
        output = predict_vol(Date,Open,High,Low,Close,AdjClose)
        st.success("The predicted volume is {}".format(output))

        if output > 0.5:
            st.markdown(danger_html, unsafe_allow_html=True)
        else:
            st.markdown(safe_html, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
