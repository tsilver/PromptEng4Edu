import streamlit as st

def set_standard_page_config(title="Prompt Engineering Course", icon_path="images/favicon_io/favicon.ico"):
    """
    Set standard page configuration with consistent favicon and layout.
    
    Parameters:
    - title: The page title to display in the browser tab
    - icon_path: Path to the favicon icon
    
    Returns:
    None
    """
    st.set_page_config(
        page_title=title,
        page_icon=icon_path,
        layout="wide",
        initial_sidebar_state="collapsed"
    ) 