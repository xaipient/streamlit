import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import my_component as bt
import SelectableDataTable as tb

st.title("COMPONENT TEST")

# Test HTML component
prediction_score = 45
prediction_result = "Negative"

components.html(f"""
                <div style="font-family: 'Open Sans'; display: flex; flex-direction: row;">
                <script>
                     document.head.innerHTML += '<link href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap" rel="stylesheet">'
                </script>
                <div style="margin:0 2rem 0 0;">
                    <div style="color: #D4D6DA;">
                    Score
                    </div>
                    <div style="color: #FFFFFF; font-size: 2rem;">
                    {prediction_score}
                    </div>
                </div>
                <div style="margin-bottom: 0;">
                    <div style="color: #D4D6DA;">
                    Prediction
                    </div>
                    <div style="color: #FFFFFF; font-size: 2rem;">
                    {prediction_result}
                    </div>
                </div>
                </div>
                """, height=80)

# Test react table component
# Test imported component
raw_data = {
        "First Name": ["Jason", "Molly", "Tina", "Jake", "Amy"],
        "Last Name": ["Miller", "Jacobson", "Ali", "Milner", "Smith"],
        "Age": [42, 52, 36, 24, 73],
    }
df = pd.DataFrame(raw_data, columns=["First Name", "Last Name", "Age"])

rows = tb.selectable_data_table(df)
if rows:
    st.write("You have selected", rows)
    bt_click = bt.my_component(rows)
    if bt_click:
        st.markdown(
            f"""Selected data points {', '.join([str(row) for row in rows])} classified as 'bad' (45%)""")
