import streamlit as st
import os
import sys
from utils.navigation import scroll_to_top
from utils.state_management import initialize_session_state, mark_page_completed
from utils.teacher_client import TeacherClient
from components.breadcrumb_navigator import render_breadcrumb
from components.bottom_navigator import render_bottom_navigator
from components.course_navigation import render_course_navigation
from components.top_navigator import render_top_navigator
from components.teacher_notes import render_teacher_notes

# Initialize the TeacherClient
client = TeacherClient()

# Configure page
st.set_page_config(
    page_title="Lesson 1 Examples",
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
    "title": "Quick Start Guide: Examples",
    "lesson": "1",
    "section": "examples",
    "order": 2
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = f"lesson_{PAGE_INFO['lesson']}_{PAGE_INFO['section']}"
st.session_state.current_page = current_page

# Get all available pages for navigation
try:
    from utils.navigation import get_all_pages
    all_pages = get_all_pages()
except Exception as e:
    st.error(f"Error loading pages: {str(e)}")
    all_pages = []

# Scroll to top when page loads
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

# Debug toggle in sidebar - Note the unique key
debug_key = f"toggle_debug_{PAGE_INFO['lesson']}_{PAGE_INFO['section']}"
st.sidebar.checkbox(
    "Show Debug Info",
    value=st.session_state.get("show_debug", False),
    key=debug_key
)

# Create main layout with content on the left and navigation on the right
content_col, nav_col = st.columns([4, 1])

# Render the main content area
with content_col:
    # Render breadcrumb navigation at the top
    render_breadcrumb(current_page)
    
    # Render section navigation at the top
    render_top_navigator(PAGE_INFO["lesson"], PAGE_INFO["section"])
    
    # Main content
    st.title("Examples: Effective Prompting")
    
    st.markdown("""
    In this section, we'll explore relevant and accessible examples that demonstrate 
    the power of combining Task, Context, and Format in your prompts.
    """)
    
    # General Examples
    st.markdown("## General Examples")
    
    st.markdown("""
    Let's start with some general examples to see how these components work together
    in everyday scenarios.
    """)
    
    # Example 1
    st.markdown("### Example 1: Finding a Restaurant")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Basic Prompt")
        st.code("Find a restaurant.", language="text")
        
        st.markdown("""
        **Result:**
        
        - Generic list of restaurants
        - No constraints or focus
        - Missing key information for decision-making
        - Requires follow-up questions
        """)
    
    with col2:
        st.markdown("#### Enhanced Prompt with TCF")
        st.code("""Find a highly rated Italian restaurant near Times Square.
        
Context: I'm looking for a place that is family friendly and open late.
        
Format: Provide a list with the restaurant's name, address, and a short review.""", language="text")
        
        st.markdown("""
        **Result:**
        
        - Focused on specific cuisine and location
        - Includes important contextual constraints
        - Clear format for easy comparison
        - Complete information in a single response
        """)
    
    # Example 2
    st.markdown("### Example 2: Summarizing Information")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("#### Basic Prompt")
        st.code("Summarize the plot of Inception.", language="text")
        
        st.markdown("""
        **Result:**
        
        - Generic summary
        - May miss key elements
        - No focus on specific aspects
        - One-size-fits-all approach
        """)
    
    with col4:
        st.markdown("#### Enhanced Prompt with TCF")
        st.code("""Summarize the plot of the movie 'Inception'.
        
Context: Focus on the main characters and the central concept of dream layering.
        
Format: Write a short paragraph that would help someone understand the basic premise without spoilers.""", language="text")
        
        st.markdown("""
        **Result:**
        
        - Focused on key elements
        - Respects the constraint of avoiding spoilers
        - Clear length and format guidance
        - More useful for the intended purpose
        """)
    
    # Teacher-Specific Examples
    st.markdown("## Teacher-Specific Examples")
    
    st.markdown("""
    Now let's look at examples specifically relevant to educational settings.
    These show how the TCF framework can help create classroom-ready materials.
    """)
    
    # Example 3
    st.markdown("### Example 3: Creating Educational Content")
    
    col5, col6 = st.columns(2)
    
    with col5:
        st.markdown("#### Basic Prompt")
        st.code("Write about the water cycle.", language="text")
        
        st.markdown("""
        **Result:**
        
        - Generic explanation at unknown level
        - May be too simple or too complex
        - No focus on specific processes
        - Generic language not tailored to students
        """)
    
    with col6:
        st.markdown("#### Enhanced Prompt with TCF")
        st.code("""Write a short paragraph summarizing the water cycle.
        
Context: Focus on the processes of evaporation, condensation, and precipitation, and tailor the language to a 4th-grade level.
        
Format: Include one analogy that would help students understand the cyclical nature of the process.""", language="text")
        
        st.markdown("""
        **Result:**
        
        - Age-appropriate explanation
        - Focused on key processes
        - Includes analogy for conceptual understanding
        - Classroom-ready without major edits
        """)
    
    # Example 4
    st.markdown("### Example 4: Creating Discussion Questions")
    
    col7, col8 = st.columns(2)
    
    with col7:
        st.markdown("#### Basic Prompt")
        st.code("Generate questions about Romeo and Juliet.", language="text")
        
        st.markdown("""
        **Result:**
        
        - Mix of simple recall and complex questions
        - No focus on specific themes
        - Questions of varying quality and relevance
        - No organization or structure
        """)
    
    with col8:
        st.markdown("#### Enhanced Prompt with TCF")
        st.code("""Generate 5 discussion questions about the themes in 'Romeo and Juliet'.
        
Context: Focus on themes of love, fate, and family conflict. The questions should be appropriate for high school freshmen who have just finished reading the play.
        
Format: Provide a numbered list with questions that encourage critical thinking rather than simple recall.""", language="text")
        
        st.markdown("""
        **Result:**
        
        - Focused on specific themes
        - Age-appropriate complexity
        - Promotes higher-order thinking
        - Organized in a ready-to-use format
        """)
    
    # Component Analysis
    st.markdown("## Key Components Analysis")
    
    st.markdown("""
    In the examples above, notice how the three core components make the prompts more effective:
    
    **Task**:
    - Clarifies exactly what you want (find, summarize, write, generate)
    - Sets boundaries (short paragraph, 5 questions)
    
    **Context**:
    - Provides critical background (4th-grade level, high school freshmen)
    - Includes constraints (family-friendly, avoid spoilers)
    
    **Format**:
    - Shapes the output structure (numbered list, paragraph with analogy)
    - Ensures the response meets your needs (critical thinking questions, restaurant details)
    """)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Teacher-specific guidance
    render_teacher_notes("""
    **Key Teaching Points:**
    
    * Point out how the educational examples mirror how teachers would give instructions to a colleague or student teacher
    * Emphasize that specificity saves time - the more clear your prompt, the less likely you'll need to refine it
    * Highlight the difference between generic responses and tailored, classroom-ready materials
    * Note that educators have an advantage in prompt engineering - they're already expert instruction-givers!
    
    **Application Ideas:**
    
    * Have participants identify which component (Task, Context, or Format) makes the biggest difference in each example
    * Ask them to share what aspects of the education examples would be most useful in their specific teaching areas
    * Discuss how prompt components align with instructional design principles (objectives, prerequisites, assessment)
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
