import streamlit as st
from utils.teacher_client import TeacherClient

def render_interactive_activity(title, description, exercise_function, key_prefix=""):
    """
    Render an interactive activity with consistent styling.
    
    Args:
        title (str): Title of the activity
        description (str): Markdown description of the activity
        exercise_function (callable): Function that implements the exercise
        key_prefix (str): Prefix for Streamlit widget keys to avoid duplicates
    """
    st.markdown(f"## {title}")
    st.markdown(description)
    
    with st.container():
        exercise_function(key_prefix)
