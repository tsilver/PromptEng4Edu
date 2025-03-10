import streamlit as st
from utils.state_management import initialize_session_state

def render_teacher_notes(content):
    """
    Render teacher-specific notes that are only visible when the teacher mode is enabled.
    
    Parameters:
    - content: The markdown content to display in the teacher notes section
    """
    # Make sure session state is initialized
    initialize_session_state()
    
    # Only show teacher notes if the toggle is enabled
    if st.session_state.show_teacher_content:
        with st.expander("👩‍🏫 Teacher Notes", expanded=False):
            st.markdown(content)
