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
    page_title="Lesson 11: Chain-of-Thought Prompting",
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
    "title": "Chain-of-Thought Prompting",
    "lesson": "11",
    "section": "introduction",
    "order": 1
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_11_introduction"
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
    "lesson_11_introduction",
    "introduction",
    "Lesson 11: Chain-of-Thought Prompting",
    """
    **Welcome to Lesson 11 on Chain-of-Thought Prompting!**
    
    In this lesson, you'll learn:
    - What chain-of-thought prompting is and why it's powerful
    - How to guide AI to show its reasoning process step-by-step
    - Techniques for breaking down complex problems
    - Applications of chain-of-thought prompting in education
    
    This approach is particularly valuable for teaching critical thinking and reasoning skills!
    """
)

# Render the teacher controls in the sidebar
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
    st.markdown(f"# Lesson 11: {PAGE_INFO['title']}")
    
    # Objective
    st.markdown("## Objective")
    st.markdown("""
    To understand and apply chain-of-thought prompting techniques that guide AI to show its reasoning process
    and generate better results for complex educational tasks requiring step-by-step thinking.
    """)
    
    # Real-world hook
    st.info("""
    ### Real-World Hook
    
    Have you ever asked a student to "show their work" when solving a math problem? Or asked them to 
    explain their reasoning when analyzing a text? Chain-of-thought prompting does exactly that with AI - 
    it asks the AI to explain its thinking process step-by-step, leading to more accurate, transparent, 
    and educational responses.
    """)
    
    # Jargon-Free Explanation
    st.markdown("## Understanding Chain-of-Thought Prompting")
    
    st.markdown("""
    **Chain-of-Thought (CoT) Prompting** is a technique where you instruct the AI to break down its thinking 
    into a sequence of logical steps before providing the final answer.
    
    Instead of simply asking for an answer, you're asking the AI to:
    1. Think through the problem step-by-step
    2. Show its reasoning process
    3. Arrive at a conclusion based on that reasoning
    
    This approach is especially valuable when dealing with:
    - Complex reasoning tasks
    - Multi-step problems
    - Critical thinking exercises
    - Tasks requiring analysis and evaluation
    """)
    
    # Why it matters in education
    st.markdown("## Benefits for Education")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### For Teachers
        
        - Creates more accurate AI-generated content
        - Models effective reasoning for students
        - Produces transparent explanations you can verify
        - Helps identify misconceptions in step-by-step solutions
        - Creates excellent examples of "showing work"
        """)
        
    with col2:
        st.markdown("""
        ### For Students
        
        - Provides clear step-by-step explanations
        - Teaches reasoning processes alongside content
        - Shows how to break down complex problems
        - Supports development of critical thinking skills
        - Makes learning processes explicit rather than implicit
        """)
    
    # Key concepts
    st.markdown("## Key Concepts in Chain-of-Thought Prompting")
    
    st.markdown("""
    ### 1. Explicit Instructions
    
    Tell the AI explicitly to "think step-by-step" or "show your reasoning" rather than assuming it will do so.
    
    ### 2. Breaking Down Complex Problems
    
    Complex tasks become more manageable when broken into smaller, sequential steps.
    
    ### 3. Transparency in Reasoning
    
    The reasoning process becomes visible, making it easier to evaluate the quality of the answer.
    
    ### 4. Integration with Few-Shot Prompting
    
    Chain-of-thought can be combined with few-shot examples to demonstrate the specific reasoning pattern you want.
    
    ### 5. Building on Previous Techniques
    
    Chain-of-thought prompting builds on our previous lessons (Task, Context, Format, Few-Shot examples) 
    but adds the critical element of explicit reasoning.
    """)
    
    # Simple comparison
    st.markdown("## Basic vs. Chain-of-Thought Approach")
    
    basic_prompt = """
    Find the volume of a cylinder with radius 5cm and height 12cm.
    """
    
    cot_prompt = """
    Find the volume of a cylinder with radius 5cm and height 12cm. 
    Think step-by-step about the formula needed and each calculation.
    """
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Basic Prompt:")
        st.code(basic_prompt, language="text")
        st.markdown("""
        **Typical response:**
        
        The volume of the cylinder is 942.5 cubic centimeters.
        """)
        
    with col2:
        st.markdown("### Chain-of-Thought Prompt:")
        st.code(cot_prompt, language="text")
        st.markdown("""
        **Improved response:**
        
        To find the volume of a cylinder, I'll use the formula:
        V = π × r² × h
        
        Given information:
        - Radius (r) = 5 cm
        - Height (h) = 12 cm
        
        Step 1: Calculate r²
        r² = 5² = 25 cm²
        
        Step 2: Multiply by π
        π × r² = 3.14159 × 25 = 78.54 cm²
        
        Step 3: Multiply by height
        V = 78.54 × 12 = 942.48 cm³
        
        Therefore, the volume of the cylinder is 942.5 cubic centimeters (rounded to one decimal place).
        """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Relate this technique to "think aloud" protocols used in education
    * Emphasize that chain-of-thought is particularly valuable for math, science, and logical reasoning tasks
    * Discuss how this approach aligns with teaching students to show their work and explain their thinking
    * Point out how chain-of-thought prompting can be used to demonstrate problem-solving approaches for students
    
    **Implementation Ideas:**
    
    * Create worked examples that model problem-solving processes
    * Generate step-by-step explanations of complex concepts
    * Create "deconstruction" of literary analysis or historical reasoning
    * Develop mathematics solutions that explicitly show each step with explanations
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