import streamlit as st


# --- CUSTOM CSS STYLING ---
# This code from ai to help me adjust dashboard style in streamlit

def css_load():
    css = """
    <style>
        /* --- GENERAL STYLING --- */
        /* Main app background */
        .stApp {
            background-color: #ffffff; 
        }

        /* --- SIDEBAR STYLING --- */
        /* Sidebar background */
        [data-testid="stSidebar"] {
            background-color: #fdd8d8;
        }

        /* Sidebar font */
        [data-testid="stSidebar"] .st-emotion-cache-16txtl3 {
            color: #ffffff; /* Dark grey text for readability on white */
            font-family: 'Verdana', sans-serif; /* A clean, professional font */
            font-size: 30px;
        }

        /* Sidebar header font */
        [data-testid="stSidebar"] .st-emotion-cache-1lcbmx1 {
            color: #ffffff;
            font-family: 'Verdana', sans-serif;
        }


        /* --- KPI CARD STYLING --- */
        /* KPI Metric card style */
        [data-testid="stMetric"] {
            background-color: #FFFFFF;
            border: 2px solid #FFFFFF;
            border-radius: 15px; /* More rounded corners */
            padding: 20px;
            /* Adding the shadow you wanted */
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        /* KPI value text */
        [data-testid="stMetricValue"] {
            color: #333333;
            font-weight: bold;
        }

        /* KPI label text */
        [data-testid="stMetricLabel"] {
            color: #333333;
        }

        /* --- PLOT STYLING --- */
        /* This targets the container that holds your Matplotlib/Seaborn plots */
        [data-testid="stImage"] {
            border-radius: 20px; /* Rounded corners for the plot container */
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* Shadow for the plot container */
            border: 2px solid #FFFFFF; /* A white border to make it pop */
        }

    </style>
    """
    return st.markdown(css, unsafe_allow_html=True)
