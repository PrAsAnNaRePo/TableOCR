import tabula
import pandas as pd
import streamlit as st
import os

os.system('apt install openjdk-8-jdk')

st.title("TableOCR")

st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.form(key='my_form'):
    file = st.file_uploader("Upload a file", type="pdf", accept_multiple_files=False)
    page_no = st.number_input("Enter page number", min_value=1, value=1)
    submit_button = st.form_submit_button(label='Submit')

    if submit_button and file is not None and page_no is not None:
        with st.spinner("Converting PDF page to image..."):
            tables = tabula.read_pdf(file, pages=page_no, multiple_tables=True)
            table_df = tables[0] if tables else pd.DataFrame()
            st.write("Scroll down to download the output file.")
            st.table(table_df)
            table_df.to_excel("output.xlsx", index=False)
            st.markdown(
                f'<a href="output.xlsx" download="output.xlsx">Click here to download the output file</a>',
                unsafe_allow_html=True
            )