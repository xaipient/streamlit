import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px

st.header("PREDICTION EXPLANATION")
st.subheader("CASE 129")
st.button("submit")
st.markdown(
    "Our analysis indicates this case has been unfairly predicted to have [high arrest probability]. We demonstrate this by contrasting Case 129 with a closely matching synthetic case (referred to as Synthetic Match), which maintains similar feature values in all respects except for GENDER, the protected attribute."
)


@st.cache
def get_data():
    return pd.read_csv(
        "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-09-12/visualisations/listings.csv"
    )


df1 = get_data()
st.dataframe(df1.head())

cols = ["name", "host_name", "neighbourhood", "room_type", "price"]
st_ms = st.multiselect("Columns", df1.columns.tolist(), default=cols)

image = Image.open("/Users/yz/Documents/GitHub/streamlit/examples/img/logo.png")
# st.sidebar.image(image)
st.sidebar.text("test background gif")

st.subheader("SCORE AND FEATURE VALUE ")
st.markdown(
    "We show below the characteristics of Case 129 and the Synthetic Match. Notice that most attributes are similar except that the GENDER is different. For Case 129, the model produced a highly unfavorable score, i.e. [high arrest probability], whereas for the Synthetic Match, the score is much more favorable."
)
df2 = px.data.tips()
fig = px.density_heatmap(
    df2,
    x="total_bill",
    y="tip",
    nbinsx=20,
    nbinsy=20,
    color_continuous_scale=["#B8C8F9", "#273346", "#E78CAE"],
)
fig.update_xaxes(title_font=dict(color="white"), tickfont=dict(color="white"))
fig.update_yaxes(
    linecolor="#273346", title_font=dict(color="white"), tickfont=dict(color="white")
)
fig.update_layout(
    {"plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)"},
    coloraxis_colorbar=dict(
        title_font=dict(color="white"), tickfont=dict(color="white")
    ),
)
st.plotly_chart(fig, use_container_width=True)
