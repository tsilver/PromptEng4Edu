import streamlit as st
import os
import sys
from utils.navigation import scroll_to_top
from utils.state_management import initialize_session_state, mark_page_completed
from utils.page_config import set_standard_page_config
from components.breadcrumb_navigator import render_breadcrumb
from components.bottom_navigator import render_bottom_navigator
from components.course_navigation import render_course_navigation
from components.top_navigator import render_top_navigator
from components.page_header import render_page_header

# Configure page
set_standard_page_config("Prompt Engineering Course Introduction")

# Get the current directory and add to path if needed
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Page metadata
PAGE_INFO = {
    "title": "Welcome to the Prompt Engineering Course",
    "lesson": "intro",
    "section": "introduction",
    "order": 0
}

# Initialize session state variables
initialize_session_state()

# Set current page in session state
current_page = "course_introduction"
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
st.sidebar.checkbox(
    "Show Debug Info",
    value=st.session_state.get("show_debug", False),
    key="toggle_debug_intro"
)

# Create main layout with content on the left and navigation on the right
content_col, nav_col = st.columns([4, 1])

# Render the main content area
with content_col:
    # Render the standard header
    render_page_header()
    
    # Render breadcrumb navigation at the top
    render_breadcrumb(current_page)
    
    # Render navigation links for Course Intro and its sections
    render_top_navigator("intro", "introduction")
    
    # Course content starts immediately
    st.markdown("""
    This course will teach you how to effectively use Large Language Models (LLMs) in your 
    teaching practice. You'll learn to craft effective prompts using the PTC-FREI framework
    and discover strategies to leverage AI as a powerful tool in education.
    """)
    
    # Course Progress Indicator
    st.info("""
    **📚 Course Progression:** 
    
    The course is designed to be completed in sequence. To progress through the course:
    
    1. Explore all four sections of the Course Introduction (Introduction, Examples, Activities, Reflection)
    2. Complete the Reflection section by saving your responses
    3. Once the Reflection is complete, you'll unlock Lesson 1
    
    Look for the ✨ symbol next to Reflection sections throughout the course - completing these
    is your key to unlocking the next lesson!
    """)
    
    # Course Overview
    st.markdown("## Course Overview")
    st.markdown("""
    In this course, you'll learn:
    
    - **Fundamentals of LLMs**: Understand how large language models work and their capabilities
    - **Effective Prompting Techniques**: Master the PTC-FREI framework for creating effective prompts
    - **Educational Applications**: Apply prompting techniques to teaching, lesson planning, and assessment
    - **Best Practices**: Learn strategies for getting the most out of AI in educational settings
    """)
    
    # Course Structure in an expander
    with st.expander("Complete Course Structure", expanded=False):
        st.markdown("""
        The course is organized into 17 lessons, each covering a different aspect of prompt engineering:
        
        1. **Quick Start Guide**: Introduction to LLMs and Basic Prompting
        2. **The Power of Context**: Understanding how context influences LLM outputs
        3. **Defining the Task**: Creating clear task instructions in prompts
        4. **Specifying the Format**: Controlling the output structure
        5. **Defining the Persona**: Creating character and role-based prompts
        6. **Incorporating References**: Using external materials
        7. **Evaluation**: Assessing and improving LLM outputs
        8. **Iteration**: Refining prompts for better results
        9. **Zero-Shot Prompting**: Leveraging LLM knowledge without examples
        10. **Few-Shot Prompting**: Guiding LLMs with examples
        11. **Chain-of-Thought Prompting**: Breaking down complex reasoning
        12. **Role Prompting**: Using personas effectively
        13. **Prompting for Lesson Planning and Assessment Creation**
        14. **Prompting for Student Feedback and Writing Prompts**
        15. **Prompting for Discussion Questions and Content Creation**
        16. **Prompting for Email Composition and Presentation Outlines**
        17. **Comprehensive Review and Integration**
        """)
    
    # How to Use This Course
    st.markdown("## How to Use This Course")
    st.markdown("""
    Each lesson in this course has four main sections:
    
    1. **Introduction**: Learn the core concepts and principles
    2. **Examples**: See the techniques in action with relevant educational examples
    3. **Activities**: Practice the techniques with hands-on exercises
    4. **Reflection** ✨: Consolidate your learning and plan for implementation
    
    The navigation bar at the top of each page allows you to move between these sections,
    while the course navigation on the right lets you jump between different lessons.
    
    **Important:** Completing the Reflection section by saving your responses is what marks
    a lesson as complete and unlocks the next lesson in the sequence.
    """)
    
    # Navigation explanation
    st.markdown("## Course Navigation")
    st.markdown("""
    This course features an intuitive navigation system:
    
    - **Top and Bottom Navigation**: Quick access to the four sections of each lesson
    - **Right-Side Navigation**: Jump to any unlocked lesson or course section
    - **Breadcrumb Trail**: Always see where you are in the course and navigate back to previous sections
    
    Sections you've already visited will appear with a checkmark (✓) in the navigation.
    """)
    
    # Call to Action section with improved visual styling
    st.markdown("""
    <div style="padding: 1.5rem 2rem; background-color: #f0f7ff; border-radius: 0.5rem; margin: 2rem 0; border-left: 5px solid #0068C9;">
    <h3 style="margin-top: 0; color: #0068C9;">Explore the Course</h3>
    <p>Start by exploring all sections of the Course Introduction:</p>
    <ol>
        <li>Browse the <strong>Examples</strong> to see prompt engineering in action</li>
        <li>Try the <strong>Activities</strong> to start practicing basic skills</li>
        <li>Complete the <strong>Reflection</strong> to set your learning goals and unlock Lesson 1</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # Add bottom navigator - mirrors the top navigator
    render_bottom_navigator(PAGE_INFO)
    
    # Mark this page as viewed
    mark_page_completed(current_page)
    
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
        
        # Check if specific key files exist
        lesson_files = {
            "Course Intro": os.path.exists(os.path.join(current_dir, "pages", "course_introduction.py")),
            "Course Examples": os.path.exists(os.path.join(current_dir, "pages", "course_examples.py")),
            "Course Activities": os.path.exists(os.path.join(current_dir, "pages", "course_activities.py")),
            "Course Reflection": os.path.exists(os.path.join(current_dir, "pages", "course_reflection.py")),
            "Lesson 1 Intro": os.path.exists(os.path.join(current_dir, "pages", "lesson_1_introduction.py")),
        }
        st.write("File check:", lesson_files)