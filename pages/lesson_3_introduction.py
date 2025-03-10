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
    page_title="Lesson 3: Defining the Task (T)",
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
    "title": "Defining the Task (T)",
    "lesson": "3",
    "section": "introduction",
    "order": 1
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_3_introduction"
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
    "lesson_3_introduction",
    "introduction",
    "Lesson 3: Defining the Task",
    """
    **Welcome to Lesson 3 on Task Definition in Prompting.**
    
    In this lesson, you'll learn:
    - How to clearly specify what you want the AI to do
    - Techniques for defining tasks with precision
    - The importance of action verbs and specificity
    
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
    st.markdown(f"# Lesson 3: {PAGE_INFO['title']}")
    
    # Objective
    st.markdown("## Objective")
    st.markdown("""
    To teach learners how to clearly define the task in a prompt to achieve specific and desired outcomes from the LLM.
    """)
    
    # Real-world hook
    st.info("""
    ### Real-World Hook
    
    Think of giving instructions to a new assistant. If you say, "Do something with these papers," they'll be lost. 
    But if you say, "Please file these papers alphabetically in the green folder," they know exactly what to do. 
    Defining the task in a prompt works the same way.
    """)
    
    # Jargon-Free Explanation
    st.markdown("## Understanding Tasks in Prompting")
    
    st.markdown("""
    Task in prompting is simply telling the LLM precisely what you want it to do. It's about being specific 
    and clear in your instructions.
    
    A well-defined task:
    - Specifies the exact action you want the LLM to perform
    - Uses clear, directive language
    - Avoids ambiguity and vagueness
    - Sets boundaries and parameters
    """)
    
    # Illustrative diagram
    st.markdown("## The Anatomy of a Task Definition")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("""
        **🔍 Vague Task:**
        ```
        "Write about education."
        ```
        
        ⬇️
        
        **Unpredictable, broad response**
        - Could be about any aspect of education
        - Unknown length and format
        - May not address your specific needs
        """)
        
    with col_b:
        st.markdown("""
        **🌟 Clear Task:**
        ```
        "Write a 300-word summary of the 
        benefits of project-based learning 
        in middle school science classes."
        ```
        
        ⬇️
        
        **Focused, useful response**
        - Specific topic
        - Defined length
        - Clear educational context
        - Particular learning approach
        """)
    
    st.markdown("""
    ## Key Components of an Effective Task
    
    1. **Action Verb**: Start with a clear action (create, generate, list, summarize, explain)
    2. **Specificity**: Indicate exactly what you want (5 activities, a 2-paragraph summary)
    3. **Parameters**: Include any constraints or requirements (suitable for 3rd graders, excluding examples with violence)
    4. **Purpose**: When helpful, explain why you need this (to help students visualize the concept)
    
    ### Creating a Task Library
    
    Consider developing a personal library of effective task instructions:
    
    | For This Purpose | Use These Action Verbs |
    |------------------|------------------------|
    | Lesson content   | Explain, summarize, outline, describe |
    | Assessment       | Generate, create, develop, design |
    | Differentiation  | Adapt, modify, simplify, enhance |
    | Feedback         | Evaluate, analyze, suggest, review |
    """)
    
    # Relationship to other prompt components
    st.markdown("## How Task Relates to Context and Format")
    
    st.markdown("""
    Remember that a complete prompt often includes:
    
    - **Context (C)**: The background information (previously covered in Lesson 2)
    - **Task (T)**: What you want the LLM to do (our focus today)
    - **Format (F)**: How you want the output structured (coming in a future lesson)
    
    These components work together. The task defines what action to take, the context shapes 
    how that action is applied, and the format determines how the result is presented.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator - ensure it's called correctly
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Have participants practice transforming vague tasks into specific ones
    * Connect task definition to learning objectives - just as clear objectives lead to better lessons, clear tasks lead to better LLM outputs
    * Discuss how the same task can yield different results when paired with different contexts
    * Encourage teachers to identify the most common tasks they might need for their subject area
    
    **Common Challenges:**
    
    * Participants may struggle with being too vague ("discuss" or "talk about" instead of specific actions)
    * Some may be too wordy in task definitions, diluting the core instruction
    * Finding the right balance between specificity and flexibility can be difficult
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