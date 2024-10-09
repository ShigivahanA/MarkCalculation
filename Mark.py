import streamlit as st

# Title of the app
st.title("Marks Converter (Out of 80 to 20)")

# User input for marks out of 80
marks_out_of_80 = st.number_input("Enter your marks (out of 80):", min_value=0.0, max_value=80.0, step=1.0)

# Convert the marks to a scale of 20
converted_marks = (marks_out_of_80 / 80) * 20

# Display the converted marks
st.write(f"Converted Marks (out of 20): {converted_marks:.2f}")
