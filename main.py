import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Cryptocurrency')
st.header('Top 10 Cryptocurrency and Weight')

### --- LOAD DATAFRAME
excel_file = 'Cryptocurrency.xlsx'
sheet_name = 'DATA'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='B:C',
                   header=3)

# --- STREAMLIT SELECTION
name = df['Name'].unique().tolist()
weight = df['Weight'].unique().tolist()

weight_selection = st.slider('Weight:',
                        min_value= min(weight),
                        max_value= max(weight),
                        value=(min(weight),max(weight)))

name_selection = st.multiselect('Name:',
                                    name,
                                    default=name)

# --- FILTER DATAFRAME BASED ON SELECTION
mask = (df['Weight'].between(*weight_selection)) & (df['Name'].isin(name_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')

# --- DISPLAY DATAFRAME
col1, col2 = st.columns(2)
col1.dataframe(df[mask])
with col2:st.write("""
**Bitcon:**
Bitcoin is trading at $21, 974 (£18,000). It's fallen 25% in the past five days alone, to its What's happening to Bitcoin?lowest value in 18 months. Its peak of almost $70,000, in November, feels a lifetime ago.
Experts say this is because of the wider global climate. It's not just in the crypto world things are not looking good.
Recession looms, inflation is soaring, interest rates are rising and living costs are biting. Stock markets are wobbling too, with the US S&P 500 now in a bear market (down 20% from its recent high).
As a result, even the big investors are less free with their money. And many ordinary investors - not rich hedge-fund owners or corporations but people like you and me - have less to invest in anything, full stop.
For many, an investment in something as volatile and unpredictable as cryptocurrency feels like a risk too great in these times.It's unregulated and unprotected by the financial authorities, so if you're using your savings to invest in it and it loses value, or you lose access to your crypto wallet, your money has gone.
[More](https://www.businessghana.com/site/news/technology/265112/Bitcoin:-Why-is-the-largest-cryptocurrency-crashing)""")


# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df.sort_values(['Name', 'Weight'])

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped,
                   x='Name',
                   y='Weight',
                   color_discrete_sequence = ['#F63366']*len(df_grouped),
                   template= 'plotly_white')
st.plotly_chart(bar_chart,use_column_width=True)