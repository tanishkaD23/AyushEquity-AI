import streamlit as st
import sqlite3
import pandas as pd
from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph
)

import streamlit as st



st.title("📄 Reports")

    # rest of code

conn = sqlite3.connect("app/database/database.db")

beneficiaries = pd.read_sql(
    "SELECT * FROM Beneficiaries",
    conn
)

claims = pd.read_sql(
    "SELECT * FROM Claims",
    conn
)

hospitals = pd.read_sql(
    "SELECT * FROM Hospitals",
    conn
)

conn.close()

report = st.selectbox(

    "Select Report",

    [

        "Beneficiaries",

        "Claims",

        "Hospitals"

    ]

)

if report == "Beneficiaries":

    df = beneficiaries

elif report == "Claims":

    df = claims

else:

    df = hospitals

st.subheader("Preview")

st.dataframe(

    df,

    use_container_width=True

)

st.divider()

col1,col2,col3 = st.columns(3)

# ==========================
# CSV
# ==========================

with col1:

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(

        "⬇ Download CSV",

        csv,

        f"{report}.csv",

        "text/csv"

    )

# ==========================
# Excel
# ==========================

with col2:

    excel_buffer = BytesIO()

    with pd.ExcelWriter(
        excel_buffer,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name=report
        )

    st.download_button(

        "⬇ Download Excel",

        excel_buffer.getvalue(),

        f"{report}.xlsx",

        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    )

# ==========================
# PDF
# ==========================

with col3:

    pdf_buffer = BytesIO()

    doc = SimpleDocTemplate(pdf_buffer)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(

        Paragraph(
            f"{report} Report",
            styles["Title"]
        )

    )

    table_data = [df.columns.tolist()] + df.head(20).values.tolist()

    table = Table(table_data)

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.darkblue),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),1,colors.black),

            ("BACKGROUND",(0,1),(-1,-1),colors.beige),

            ("ALIGN",(0,0),(-1,-1),"CENTER"),

            ("BOTTOMPADDING",(0,0),(-1,0),10)

        ])

    )

    elements.append(table)

    doc.build(elements)

    st.download_button(

        "⬇ Download PDF",

        pdf_buffer.getvalue(),

        f"{report}.pdf",

        "application/pdf"

    )

st.divider()

st.success("✅ Reports generated successfully.")