import altair as alt
import pandas as pd
import streamlit as st

# Example test data
test_name = "GLUCOSE (FASTING)"
value = 8.0
ref_range = "4.1-5.6"

# Parse the reference range
ref_low, ref_high = map(float, ref_range.split('-'))

# Data for the reference range bar
ref_df = pd.DataFrame({
    "Test": [test_name],
    "Start": [ref_low],
    "End": [ref_high]
})

# Data for the user value
val_df = pd.DataFrame({
    "Test": [test_name],
    "Value": [value]
})

# Build reference range bar
ref_chart = alt.Chart(ref_df).mark_bar(color='lightgreen').encode(
    x="Start",
    x2="End",
    y=alt.Y("Test", axis=None)
)

# Build value marker
val_chart = alt.Chart(val_df).mark_rule(color='red', strokeWidth=2).encode(
    x="Value",
    y="Test"
)

# Combine both charts
chart = ref_chart + val_chart

st.altair_chart(chart, use_container_width=True)
