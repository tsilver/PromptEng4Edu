import streamlit as st
import os
import sys
from utils.navigation import scroll_to_top
from utils.state_management import initialize_session_state, mark_page_completed
from components.breadcrumb_navigator import render_breadcrumb
from components.bottom_navigator import render_bottom_navigator
from components.course_navigation import render_course_navigation
from components.top_navigator import render_top_navigator
from components.teacher_notes import render_teacher_notes

# Configure page
st.set_page_config(
    page_title="Lesson 1 Introduction",
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
    "title": "Quick Start Guide: Introduction to LLMs and Basic Prompting",
    "lesson": "1",
    "section": "introduction",
    "order": 1
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
    st.title(PAGE_INFO["title"])
    
    # Objective
    st.markdown("## Objective")
    st.markdown("""
    To provide adult educators with a foundational understanding of Large Language Models (LLMs) 
    and the essential elements of basic prompting using a simplified version of the PTC-FREI framework.
    """)
    
    # Real-World Hook
    st.markdown("## Real-World Hook")
    st.markdown("""
    Imagine having a tireless assistant who can help you brainstorm lesson ideas, draft emails, 
    or even create simple learning materials. Today, we'll explore how LLMs can be that assistant, 
    and how you can effectively communicate with them.
    """)
    
    # Jargon-Free Explanation
    st.markdown("## Understanding LLMs and Prompting")
    
    st.markdown("""
    **LLMs (Large Language Models)**: Think of these as super-smart computers that have read tons of books 
    and articles. They can understand and generate text, like answering questions, writing stories, 
    or summarizing information.
    
    **Prompting**: This is simply telling the LLM what you want it to do. Like giving instructions to 
    that helpful assistant.
    """)
    
    # Introduction to the Framework
    st.markdown("## Introduction to the PTC-FREI Framework")
    
    st.markdown("""
    Before we dive into basic prompting, let's briefly look at the complete PTC-FREI framework. 
    This framework will be our guide throughout this course. It stands for:
    
    * **P**ersona: Defining the role the LLM should play
    * **T**ask: Specifying what you want the LLM to do
    * **C**ontext: Providing background information
    * **F**ormat: Specifying the desired output format
    * **R**eference: Providing source materials
    * **E**valuation: Assessing the LLM's output
    * **I**teration: Refining the prompt based on evaluation
    
    For our Quick Start Guide, we'll focus on the core elements of **Task, Context, and Format**. 
    These are the most essential for getting started with basic prompting. We'll explore the other 
    elements in more detail as we progress through the curriculum.
    """)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Begin by asking participants about their current experiences with AI tools, if any
    * Reassure educators who may feel intimidated by technology - prompt engineering is about clear communication, not coding
    * Emphasize that this framework will become more intuitive with practice
    * Relate prompting to how teachers give instructions to students or assistants - it's a transferable skill
    
    **Common Challenges:**
    
    * Some educators may feel overwhelmed by the complete framework - reassure them we'll focus on the essentials first
    * Others may want to jump ahead to advanced techniques - acknowledge their enthusiasm while emphasizing the importance of fundamentals
    * Technical terminology can be a barrier - continue using everyday language and analogies
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
        
        # Check for lesson files
        lesson_md_path = os.path.join(current_dir, "Lessons", "Lesson 1.md")
        st.write(f"Lesson 1 MD exists: {os.path.exists(lesson_md_path)}")
        if os.path.exists(lesson_md_path):
            try:
                with open(lesson_md_path, 'r') as f:
                    content = f.read()
                    import re
                    title_match = re.search(r'\*\*Lesson\s+\d+\s*:\s*([^\*]+)\*\*', content)
                    if title_match:
                        st.write(f"Extracted title: {title_match.group(1).strip()}")
            except Exception as e:
                st.write(f"Error reading lesson file: {str(e)}")
