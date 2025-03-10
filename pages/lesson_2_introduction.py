import streamlit as st
import os
import sys
from utils.navigation import scroll_to_top, get_all_pages
from utils.state_management import initialize_session_state, mark_page_completed
from components.teacher_notes import render_teacher_notes
from components.bottom_navigator import render_bottom_navigator
from components.breadcrumb_navigator import render_breadcrumb
from components.course_navigation import render_course_navigation
from components.top_navigator import render_top_navigator
from components.first_visit_dialog import show_first_visit_dialog
from components.progress_manager import render_teacher_controls_sidebar

# Configure page
st.set_page_config(
    page_title="Lesson 2: The Power of Context (C)",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Get the current directory and add to path if needed
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Page metadata
PAGE_INFO = {
    "title": "The Power of Context (C)",
    "lesson": "2",
    "section": "introduction",
    "order": 1
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_2_introduction"
st.session_state.current_page = current_page

# Get all available pages for navigation
try:
    all_pages = get_all_pages()
except Exception as e:
    st.error(f"Error loading pages: {str(e)}")
    all_pages = []

# Scroll to top when page loads
scroll_to_top()

# Show the first visit dialog if this is the first time visiting this page
show_first_visit_dialog(
    "lesson_2_introduction",
    "introduction",
    "Lesson 2: The Power of Context",
    """
    **Welcome to Lesson 2 on Context in Prompting.**
    
    In this lesson, you'll learn:
    - Why context is crucial for effective prompts
    - How context shapes AI responses
    - Different types of context to include in your prompts
    
    Navigate through the sections using the tabs at the top.
    """
)

# Render the improved teacher controls in the sidebar
render_teacher_controls_sidebar()

# Create main layout with content area on the left and navigation on the right
content_col, nav_col = st.columns([4, 1])

# Render the main content area
with content_col:
    # Render breadcrumb navigation at the top
    render_breadcrumb(current_page)
    
    # Render section navigation at the top
    render_top_navigator(PAGE_INFO["lesson"], PAGE_INFO["section"])
    
    # Main content
    st.markdown(f"# Lesson 2: {PAGE_INFO['title']}")
    
    # Objective
    st.markdown("## Objective")
    st.markdown("""
    To demonstrate the importance of context in prompt engineering and how it influences the LLM's response.
    """)
    
    # Real-world hook
    st.info("""
    ### Real-World Hook
    
    Imagine you're asking a student, "What is water?" How would your response change if you were 
    talking to a kindergarten student versus a college physics student? Providing context is key 
    to getting the right information.
    """)
    
    # Jargon-Free Explanation
    st.markdown("## Understanding Context in Prompting")
    
    st.markdown("""
    Context in prompting is like giving the LLM extra information to help it understand exactly what you want.
    It's like providing background knowledge or setting the scene.
    
    By adding context to your prompts, you:
    
    - Help the LLM understand the purpose of your request
    - Provide necessary background information
    - Set the appropriate level of detail and complexity
    - Guide the LLM toward the specific type of response you need
    """)
    
    # Illustrative diagram
    st.markdown("## How Context Shapes Responses")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("""
        **🔍 Without Context:**
        ```
        "Tell me about clouds."
        ```
        
        ⬇️
        
        **Generic, broad response**
        - General definition
        - Basic types of clouds
        - Common facts
        """)
        
    with col_b:
        st.markdown("""
        **🌟 With Context:**
        ```
        "Tell me about clouds for a 
        2nd-grade science lesson focusing 
        on the water cycle and weather."
        ```
        
        ⬇️
        
        **Tailored, relevant response**
        - Age-appropriate explanation
        - Connection to water cycle
        - Simple types relevant to weather
        - Kid-friendly language
        """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator - ensure it's called correctly
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Before showing examples, ask students to brainstorm what kind of context might be important when asking about different topics
    * Relate context in prompting to how teachers adjust their explanations based on student age, prior knowledge, and learning objectives
    * Emphasize that context doesn't need to be lengthy - even a few words can make a big difference
    * Demonstrate how the same prompt with different contexts produces dramatically different responses
    """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    **Prompt Engineering for Educators** | &copy; 2025 | A comprehensive course for teaching staff  
     ***Presenting an [AIxponential](http://aixponential.org) experience***            
    """)

# Render course navigation in the right column
with nav_col:
    render_course_navigation(all_pages, current_page, current_dir)

# Debug section at the bottom
if st.session_state.get("show_debug", False):
    with st.expander("Debug Information", expanded=True):
        st.write("### Debug Info")
        st.write(f"Current Page: {current_page}")
        st.write(f"Current Directory: {current_dir}")
        st.write(f"Pages Directory: {os.path.join(current_dir, 'pages')}")
        st.write(f"sys.path: {sys.path}")
        st.write(f"All Pages: {all_pages}")
        st.write(f"Session State: {dict(st.session_state)}") 