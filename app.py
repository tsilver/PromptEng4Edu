import streamlit as st
import os
import sys
import traceback
from utils.navigation import scroll_to_top
from utils.state_management import initialize_session_state
from utils.page_config import set_standard_page_config
from components.breadcrumb_navigator import render_breadcrumb
from components.course_navigation import render_course_navigation
from components.page_header import render_page_header

# Configure Streamlit page settings with the new utility
set_standard_page_config("Prompt Engineering Course")

# Add the parent directory to sys.path to ensure we can find our modules
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Initialize session state variables
initialize_session_state()

# Get all available pages
from utils.navigation import get_all_pages
all_pages = get_all_pages()

# Update session state
st.session_state.current_page = "app"

# Scroll to top of page on each page load
scroll_to_top()

# Render teacher controls in the sidebar
st.sidebar.title("Teacher Controls")
st.sidebar.markdown("---")

# Teacher/Student toggle
st.sidebar.checkbox(
    "Show Teacher Content",
    value=st.session_state.show_teacher_content,
    key="toggle_teacher_content"
)

# Debug toggle in sidebar - Note the unique key for app.py
st.sidebar.checkbox(
    "Show Debug Info",
    value=st.session_state.get("show_debug", False),
    key="toggle_debug_app"  # Unique key for app.py
)

# Create main layout with content on the left and navigation on the right
content_col, nav_col = st.columns([4, 1])

# Render the main content area
with content_col:
    # Render the standard header
    render_page_header()
    
    # Welcome section with reduced spacing
    st.markdown("""
    ## Welcome to the Course!
    
    This comprehensive course is designed to help educators leverage AI through effective prompt engineering. 
    You'll learn how to craft prompts that generate exactly the content you need for your teaching practice.

    Our goal is to avoid 'artificial' intelligence that seeks to supplant human reasoning and leads to a loss of critical thinking skills.  We are seeking to augment and amplify human creativity and critical thinking with Generative AI."
    """)
    
    # Create a visually appealing call to action with a single prominent button
    st.markdown("""
    <div style="padding: 2rem; background-color: #f0f7ff; border-radius: 0.75rem; margin: 1.5rem 0; text-align: center;">
        <h2 style="margin-top: 0; color: #0068C9;">Start Your Learning Journey</h2>
        <p style="font-size: 1.2rem; margin-bottom: 1rem;">Begin exploring the Prompt Engineering course with a comprehensive introduction.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Large, prominent button to navigate to course introduction
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Enter Course Introduction", key="go_to_intro", type="primary", use_container_width=True):
            try:
                # Navigate to course introduction
                st.switch_page("pages/course_introduction.py")
            except Exception as e:
                st.error(f"Error navigating to course introduction: {str(e)}")
                if st.session_state.get("show_debug", False):
                    st.error(traceback.format_exc())
    
    # Course overview section
    st.markdown("""
    ## What You'll Learn
    
    - Master the PTC-FREI framework for crafting effective prompts
    - Learn techniques for different educational tasks
    - Practice with real-world educational examples
    - Create classroom-ready materials using AI
    
    This course includes interactive activities, practical examples, and guided practice to help you 
    develop your prompt engineering skills.
    """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    **Prompt Engineering for Educators** | &copy; 2025 | A comprehensive course for teaching staff
    """)

# Render course navigation in the right column
with nav_col:
    render_course_navigation(all_pages, "app", current_dir)

# Debug section at the bottom
if st.session_state.get("show_debug", False):
    with st.expander("Debug Information", expanded=True):
        st.write("### Debug Info")
        st.write(f"Current Page: app")
        st.write(f"Current Directory: {current_dir}")
        st.write(f"Pages Directory: {os.path.join(current_dir, 'pages')}")
        st.write(f"sys.path: {sys.path}")
        st.write(f"All Pages: {all_pages}")
        st.write(f"Session State: {dict(st.session_state)}")
        
        # Check if specific key files exist
        course_intro_path = os.path.join(current_dir, "pages", "course_introduction.py")
        st.write(f"Course Intro exists: {os.path.exists(course_intro_path)}")
