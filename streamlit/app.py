

import pandas as pd

import streamlit as st
import streamlit.components.v1 as components

recomendaciones = pd.read_csv('./para_streamlit.csv')


books = (recomendaciones[['url','cover_image','title']].values)

st.set_page_config(page_title="brisx, a book journey", layout="wide")

#título

st.title("brisx ~ book recommender ~")

#
st.header('')



st.header("Find the next steps in your book journey")
st.subheader("Brisx is a book recomendation engine to help people follow their reading path 👣")

for i in range(0,int(len(books)/4)):
    i = i *4
    cols = st.columns(4)
    cols[0].image(books[i][1], caption=None,width=200, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    cols[1].image(books[i+1][1], caption=None, width=200, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    cols[2].image(books[i+2][1], caption=None, width=200, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    cols[3].image(books[i+3][1], caption=None, width=200, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

    cols[0].write("["+books[i+0][2]+"]("+books[i+0][0]+")")
    cols[1].write("["+books[i+1][2]+"]("+books[i+1][0]+")")
    cols[2].write("["+books[i+2][2]+"]("+books[i+2][0]+")")
    cols[3].write("["+books[i+3][2]+"]("+books[i+3][0]+")")

# for book in books:
    
#     # st.markdown("[![Foo](http://www.google.com.au/images/nav_logo7.png)](http://google.com.au/)")
#     st.write("["+book[2]+"]("+book[0]+")")
#     st.image(book[1], caption=book[0], width=200, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    