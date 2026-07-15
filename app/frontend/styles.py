import streamlit as st

def load_css():

    st.markdown("""
<style>

.main{
    background:#F4F9FF;
}

.block-container{
    padding-top:1rem;
    padding-bottom:1rem;
    padding-left:2rem;
    padding-right:2rem;
}

section[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#0B3D91,#1565C0);
}

section[data-testid="stSidebar"] *{
    color:white;
}

.dashboard-title{
    color:#0B3D91;
    font-size:40px;
    font-weight:700;
}

.dashboard-subtitle{
    color:#64748B;
    font-size:18px;
}

.metric-card{
    background:white;
    border-radius:20px;
    padding:22px;
    box-shadow:0px 5px 20px rgba(0,0,0,0.08);
    border-left:8px solid #00C853;
    transition:0.3s;
    margin-bottom:12px;
}

.metric-card:hover{
    transform:translateY(-6px);
    box-shadow:0px 12px 30px rgba(0,0,0,0.18);
}

.metric-title{
    color:#64748B;
    font-size:18px;
}

.metric-value{
    font-size:38px;
    color:#1565C0;
    font-weight:bold;
}

.metric-change{
    color:#00C853;
    font-size:15px;
}

.section-card{
    background:white;
    border-radius:20px;
    padding:25px;
    margin-top:20px;
    box-shadow:0px 5px 20px rgba(0,0,0,.08);
}

.stButton>button{
    background:#00C853;
    color:white;
    border:none;
    border-radius:10px;
    font-size:16px;
    font-weight:bold;
    padding:10px 24px;
}

.stButton>button:hover{
    background:#009624;
    color:white;
}

.success-card{
    background:#E8F5E9;
    padding:18px;
    border-radius:12px;
    border-left:8px solid #00C853;
}

.warning-card{
    background:#FFF8E1;
    padding:18px;
    border-radius:12px;
    border-left:8px solid orange;
}

.danger-card{
    background:#FFEBEE;
    padding:18px;
    border-radius:12px;
    border-left:8px solid #E53935;
}

.ai-card{
    background:linear-gradient(90deg,#0B3D91,#1565C0);
    color:white;
    border-radius:18px;
    padding:20px;
}

.block-card{
    background:linear-gradient(90deg,#00C853,#4CAF50);
    color:white;
    border-radius:18px;
    padding:20px;
}

.status-online{
    color:#00C853;
    font-weight:bold;
}

.status-warning{
    color:#FB8C00;
    font-weight:bold;
}

.status-offline{
    color:#E53935;
    font-weight:bold;
}

thead tr th{
    background:#1565C0 !important;
    color:white !important;
}

.stTextInput input,
.stNumberInput input,
.stSelectbox div{
    border-radius:10px;
}

.footer{
    text-align:center;
    color:#64748B;
    margin-top:40px;
    font-size:15px;
}

::-webkit-scrollbar{
    width:10px;
}

::-webkit-scrollbar-thumb{
    background:#1565C0;
    border-radius:20px;
}

::-webkit-scrollbar-track{
    background:#F4F9FF;
}

</style>
""", unsafe_allow_html=True)