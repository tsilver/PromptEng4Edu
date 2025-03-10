import streamlit as st
import os
import sys
import json
import datetime
import pandas as pd
from utils.navigation import scroll_to_top, get_all_pages
from utils.state_management import initialize_session_state, mark_page_completed
from utils.teacher_client import TeacherClient
from components.breadcrumb_navigator import render_breadcrumb
from components.bottom_navigator import render_bottom_navigator
from components.course_navigation import render_course_navigation
from components.top_navigator import render_top_navigator
from components.teacher_notes import render_teacher_notes
from components.progress_manager import save_progress_to_indexed_db
from components.first_visit_dialog import show_first_visit_dialog

# Initialize the TeacherClient
client = TeacherClient()

# Configure page
st.set_page_config(
    page_title="Lesson 1: Activities",
    page_icon="images/favicon_io/favicon.ico",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Get the current directory and add to path if needed
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Page metadata
PAGE_INFO = {
    "title": "Quick Start Guide: Activities",
    "lesson": "1",
    "section": "activities",
    "order": 3
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_1_activities"
st.session_state.current_page = current_page

# Helper function for tooltips
def render_tooltip(tooltip_id, tooltip_text, icon="ℹ️"):
    """Render a tooltip with the given ID and text"""
    return f"""<span 
        data-tooltip-id="{tooltip_id}"
        data-tooltip-content="{tooltip_text}"
        style="cursor: help;"
    >{icon}</span>
    <style>
    [data-tooltip-id="{tooltip_id}"] {{
        color: #0068C9; 
        margin-left: 5px;
    }}
    </style>
    """

# Mock mode detection
MOCK_MODE = not hasattr(client, "is_connected") or not client.is_connected()

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
    "lesson_1_activities",
    "activities",
    "Lesson 1 Activities",
    """
    **This section provides hands-on practice with basic prompting.**
    
    You'll:
    - Create basic prompts using the Task, Context, Format framework
    - Analyze prompt effectiveness
    - Apply what you've learned to real educational scenarios
    
    Complete these activities to strengthen your understanding before 
    moving to the reflection.
    """
)

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

# Create main layout with content area on the left and navigation on the right
content_col, nav_col = st.columns([4, 1])

# Render the main content area
with content_col:
    # Render breadcrumb navigation at the top
    render_breadcrumb(current_page)
    
    # Render section navigation at the top
    render_top_navigator(PAGE_INFO["lesson"], PAGE_INFO["section"])
    
    # Main content
    st.markdown(f"# Activities: {PAGE_INFO['title']}")
    
    # Add a progress note 
    st.info("""
    **📝 Course Progression Note:** 
    
    Complete the activities below to practice basic prompting using the Task, Context, Format framework. 
    After finishing these activities, proceed to the Reflection section to solidify your learning 
    and unlock the next lesson.
    """)
    
    # Activity 1
    st.markdown("## Activity 1: Identify Task, Context, and Format")
    
    st.markdown("""
    Look at the prompt below and identify which parts correspond to Task, Context, and Format.
    
    ```
    Write a short story about a student overcoming math anxiety before a big test. 
    Focus on growth mindset principles and make it appropriate for 7th graders.
    Structure it with a clear beginning, middle, and end, and keep it under 300 words.
    ```
    """)
    
    # Expandable answer section
    with st.expander("Check Your Answer"):
        st.markdown("""
        **Task:** "Write a short story about a student overcoming math anxiety before a big test."
        
        **Context:** "Focus on growth mindset principles and make it appropriate for 7th graders."
        
        **Format:** "Structure it with a clear beginning, middle, and end, and keep it under 300 words."
        """)
    
    # Activity 2
    st.markdown("## Activity 2: Improve a Basic Prompt")
    
    st.markdown("""
    Improve the following basic prompt by adding context and format specifications:
    
    **Basic Prompt:** "Write about photosynthesis."
    
    Use the text areas below to add context and format to make this prompt more effective:
    """)
    
    # Input fields for the improved prompt
    context = st.text_area("Add Context:", placeholder="Example: Appropriate for 5th graders who are learning about plant biology for the first time.", key="context_input")
    format_spec = st.text_area("Add Format:", placeholder="Example: Include a simple diagram, list the main steps, and use 3-4 everyday analogies.", key="format_input")
    
    # Show the improved prompt
    if context or format_spec:
        st.markdown("### Your Improved Prompt:")
        
        improved_prompt = "Write about photosynthesis."
        if context:
            improved_prompt += f" {context}"
        if format_spec:
            improved_prompt += f" {format_spec}"
        
        st.code(improved_prompt)
        
        st.markdown("""
        **Notice how your additions:**
        - Give the LLM more specific guidance on who the content is for
        - Clarify what kind of information to include and how to structure it
        - Result in a prompt more likely to produce exactly what you need
        """)
    
    # Activity 3
    st.markdown("## Activity 3: Create an Educational Prompt")
    
    st.markdown("""
    Create a prompt for an educational task using the Task, Context, Format framework. 
    Choose one of the scenarios below:
    
    **Scenario 1:** Generating discussion questions for a high school literature class
    
    **Scenario 2:** Creating a simple science experiment for elementary students
    
    **Scenario 3:** Drafting a parent communication about an upcoming school event
    """)
    
    # Input fields for the educational prompt
    scenario = st.radio("Select a scenario:", ["Scenario 1", "Scenario 2", "Scenario 3"], key="scenario_select")
    
    task = st.text_area("Task:", placeholder="What specific output do you want the LLM to create?", key="task_input")
    prompt_context = st.text_area("Context:", placeholder="What background information, audience details, or constraints should the LLM know?", key="prompt_context_input")
    prompt_format = st.text_area("Format:", placeholder="How should the response be structured or presented?", key="prompt_format_input")
    
    # Show the complete prompt
    if task or prompt_context or prompt_format:
        st.markdown("### Your Complete Educational Prompt:")
        
        complete_prompt = ""
        if task:
            complete_prompt += f"{task}"
        if prompt_context:
            complete_prompt += f" {prompt_context}"
        if prompt_format:
            complete_prompt += f" {prompt_format}"
        
        if complete_prompt:
            st.code(complete_prompt)
            
            st.markdown("""
            **Reflection Questions:**
            - How does your prompt provide clear guidance to the LLM?
            - What elements make your prompt specifically relevant to education?
            - How might you improve this prompt further?
            """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * For Activity 1, consider having students share their answers and discuss why certain parts fit into each component.
    * For Activity 2, highlight particularly effective context and format additions from students' submissions.
    * For Activity 3, encourage students to trade prompts and evaluate each other's work based on clarity and effectiveness.
    
    **Facilitation Questions:**
    - Ask: "How does providing context change what the LLM will produce?"
    - Ask: "Why is format important when working with educational content?"
    - Ask: "What educational tasks would benefit most from carefully crafted prompts?"
    
    **Common Challenges:**
    - Students may still create vague tasks - encourage specificity
    - Some may include too many instructions - discuss the balance between guidance and overcomplication
    - Context may be missing educational relevance - remind them to think about learner needs
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
        st.write(f"Mock Mode: {MOCK_MODE}")
        st.write(f"Saved Activities: {st.session_state.get('activities', {})}")
