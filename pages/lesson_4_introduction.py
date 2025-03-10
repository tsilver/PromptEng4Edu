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
    page_title="Lesson 4: Specifying Format (F)",
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
    "title": "Specifying Format (F)",
    "lesson": "4",
    "section": "introduction",
    "order": 1
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_4_introduction"
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
    "lesson_4_introduction",
    "introduction",
    "Lesson 4: Specifying Format",
    """
    **Welcome to Lesson 4 on Format Specification in Prompting.**
    
    In this lesson, you'll learn:
    - How to specify the structure and format of AI outputs
    - Techniques for getting consistently organized responses
    - Common output formats useful for educational purposes
    
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
    st.markdown(f"# Lesson 4: {PAGE_INFO['title']}")
    
    # Objective
    st.markdown("## Objective")
    st.markdown("""
    To teach educators how to specify the format of AI outputs, ensuring responses are structured 
    in a way that is immediately useful and relevant for educational purposes.
    """)
    
    # Real-world hook
    st.info("""
    ### Real-World Hook
    
    Imagine asking a colleague to write a student summary report. Without specifying the format, 
    you might receive anything from a paragraph of text to a detailed spreadsheet. The same is true 
    with AI - if you don't specify the format, the AI will choose one for you, which may not match 
    what you need.
    """)
    
    # Jargon-Free Explanation
    st.markdown("## Understanding Format in Prompting")
    
    st.markdown("""
    Format in prompting refers to the structure, organization, or presentation of the AI's response. 
    It's like giving the AI a template or blueprint for how you want the information delivered.
    
    Specifying format helps you:
    
    - Receive information in a consistent, predictable structure
    - Get responses that are ready to use without reformatting
    - Control the level of detail and organization
    - Focus the AI on delivering exactly what you need
    """)
    
    # Illustrative diagram
    st.markdown("## The Impact of Format Specification")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("""
        **🔍 Without Format:**
        ```
        "List the planets in our solar system."
        ```
        
        ⬇️
        
        **Unpredictable format**
        - Might be a paragraph of text
        - Could be a simple list
        - May include extensive details
        - Organization unknown
        """)
        
    with col_b:
        st.markdown("""
        **🌟 With Format:**
        ```
        "List the planets in our solar system in 
        a table with columns for: 
        1) Planet name
        2) Distance from sun
        3) One interesting fact for elementary students"
        ```
        
        ⬇️
        
        **Precise, usable format**
        - Tabular structure specified
        - Exact columns defined
        - Level of detail controlled
        - Ready for educational use
        """)
    
    # Common Format Types
    st.markdown("## Common Format Types for Educators")
    
    st.markdown("""
    Here are some useful formats you can specify in your prompts:
    
    ### 1. Lists
    - Bullet points for quick scanning
    - Numbered lists for sequential steps
    - Nested lists for hierarchical information
    
    ### 2. Tables
    - Excellent for comparing multiple items across common criteria
    - Organized way to present structured data
    - Easy to convert into handouts or slides
    
    ### 3. Templates
    - Lesson plans with consistent sections
    - Rubrics with standard criteria
    - Feedback forms with regular components
    
    ### 4. Educational Formats
    - Cornell notes format
    - KWL (Know, Want to know, Learned) charts
    - Concept maps and mind maps
    - Timeline presentations
    """)
    
    # Relationship to previous lessons
    st.markdown("## Bringing It All Together: Context, Task, and Format")
    
    st.markdown("""
    Remember our progress through the PTC-FREI framework:
    
    - **Context (C)** - Lesson 2: The background information that shapes understanding
    - **Task (T)** - Lesson 3: The specific action you want the AI to perform
    - **Format (F)** - Lesson 4 (Today): How you want the response structured
    
    Let's see how these work together:
    
    ```
    Context: "For a 5th-grade science class studying plant biology for the first time"
    Task: "Create a quiz with 8 questions"
    Format: "Each question should have 4 multiple-choice options labeled A-D, 
             and the questions should progress from easy to challenging.
             Include an answer key at the end in a table."
    ```
    
    By mastering all three components, you create prompts that generate precisely what you need.
    """)
    
    # How to Specify Format
    st.markdown("## How to Specify Format in Your Prompts")
    
    st.markdown("""
    There are several effective ways to indicate your desired format:
    
    ### 1. Direct Format Request
    
    ```
    "Present this information in a table with three columns..."
    ```
    
    ### 2. Use the Word "Format"
    
    ```
    "Format your response as a list of bullet points."
    ```
    
    ### 3. Provide a Template or Example
    
    ```
    "Structure your response following this template:
    Title:
    Objective:
    Materials:
    Procedure:
    Assessment:"
    ```
    
    ### 4. Specify Multiple Format Elements
    
    ```
    "Present this as a concept map with the main idea in the center, 
    5-7 related concepts branching out, and brief descriptions of each connection."
    ```
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Connect format specification to how teachers format their own instructional materials
    * Discuss how different educational purposes require different formats (e.g., assessment vs. instruction)
    * Have participants share formats they commonly use in their teaching practice
    * Emphasize that format specification saves time by delivering content in a ready-to-use structure
    
    **Common Challenges:**
    
    * Forgetting to specify format entirely, leading to inconsistent outputs
    * Being too vague in format requests ("make it organized" vs. specific structure)
    * Requesting formats that are too complex or that the AI struggles to maintain
    * Confusing format specification with task definition
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