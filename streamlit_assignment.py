import streamlit as st
import pandas as pd
data = {'Product': ['Natural herbs','Syrona','Nix'],
'Category': ['Shampoo','Menstrual Cup','Wooden comb'],
'Sales':[3000,2900,2950] 
}
df = pd.DataFrame(data)
st.title("Annual sales summary - Fiscal year(2025-2026)")
st.subheader("Virugambakkam branch revenue data")
filter_options = st.sidebar.selectbox("Select by category:",options = df['Category'].unique().tolist())
filtered_df = df[df['Category'] == filter_options]
st.dataframe(filtered_df, use_container_width=True)
st.line_chart(df.set_index('Product')['Sales'])