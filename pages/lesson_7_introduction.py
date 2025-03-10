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
    page_title="Lesson 7: Evaluation (E)",
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
    "title": "Evaluation (E)",
    "lesson": "7",
    "section": "introduction",
    "order": 1
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_7_introduction"
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
    "lesson_7_introduction",
    "introduction",
    "Lesson 7: Evaluation",
    """
    **Welcome to Lesson 7 on Evaluation in Prompting.**
    
    In this lesson, you'll learn:
    - Why evaluation is crucial in prompt engineering
    - Different methods to assess AI responses
    - How to create evaluation criteria for educational contexts
    - Techniques for providing effective feedback to improve prompts
    
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
    st.markdown(f"# Lesson 7: {PAGE_INFO['title']}")
    
    # Objective
    st.markdown("## Objective")
    st.markdown("""
    To understand the importance of evaluation in prompt engineering and learn structured approaches 
    for assessing AI outputs in educational contexts.
    """)
    
    # Real-world hook
    st.info("""
    ### Real-World Hook
    
    Imagine you've received essays from both your students and AI. How do you determine which is which? 
    And more importantly, how do you assess if AI-generated content meets your educational standards? 
    Evaluation helps you systematically analyze AI outputs to ensure they're appropriate, accurate, 
    and aligned with your teaching goals.
    """)
    
    # Jargon-Free Explanation
    st.markdown("## Understanding Evaluation in Prompting")
    
    st.markdown("""
    Evaluation in prompt engineering is like using a rubric to grade student work. It provides a structured 
    way to assess if AI outputs meet your needs and expectations. Just as you might evaluate student work 
    based on content, organization, and clarity, you can apply similar criteria to AI-generated content.

    By incorporating evaluation into your prompt engineering practice, you:

    - Ensure the AI content meets educational standards
    - Identify strengths and weaknesses in your prompts
    - Provide specific feedback for improvement
    - Create a cycle of continuous refinement
    """)
    
    # Core Evaluation Approaches
    st.markdown("## Core Evaluation Approaches")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Quantitative Evaluation
        
        **Numerical assessment using specific metrics:**
        - Accuracy: How factually correct is the content?
        - Relevance: How closely does it address the prompt?
        - Depth: How comprehensive is the coverage?
        - Clarity: How understandable is the explanation?
        """)
        
    with col2:
        st.markdown("""
        ### Qualitative Evaluation
        
        **Subjective assessment of quality and value:**
        - Educational appropriateness
        - Tone and voice consistency
        - Pedagogical effectiveness
        - Student engagement potential
        - Alignment with curriculum goals
        """)
    
    # Evaluation Framework for Education
    st.markdown("## The ACRE Framework for Educational Evaluation")
    
    st.markdown("""
    When evaluating AI outputs for educational use, consider the ACRE approach:
    
    **A**ccuracy: Is the information factually correct and current?
    
    **C**urriculum Alignment: Does it match your learning objectives and standards?
    
    **R**eadability: Is it appropriate for your students' level?
    
    **E**ngagement: Will it capture and maintain student interest?
    """)
    
    # Visual example
    st.markdown("## Example of Evaluation in Action")
    
    st.markdown("""
    **Original Prompt:**
    ```
    Explain photosynthesis.
    ```
    
    **AI Response:**
    ```
    Photosynthesis is how plants make food. They use sunlight, water, and carbon dioxide to create glucose and oxygen.
    ```
    
    **Evaluation:**
    - Accuracy: ⭐⭐⭐☆☆ (Correct but oversimplified)
    - Curriculum Alignment: ⭐☆☆☆☆ (No grade level targeting)
    - Readability: ⭐⭐⭐⭐☆ (Simple and clear)
    - Engagement: ⭐☆☆☆☆ (Basic, no engaging elements)
    
    **Overall Assessment:** The response needs improvement in curriculum alignment and engagement.
    """)
    
    # Best Practices
    st.markdown("## Best Practices for Evaluation")
    
    st.markdown("""
    1. **Create evaluation rubrics** before generating content
    2. **Use consistent criteria** across similar prompts
    3. **Consider multiple perspectives** (teacher, student, parent)
    4. **Document your evaluations** to inform prompt improvements
    5. **Balance standards** with practical usability
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator - ensure it's called correctly
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Connect evaluation criteria to familiar assessment practices teachers already use
    * Encourage teachers to develop customized rubrics for their specific subject areas
    * Remind participants that evaluation directly informs the iteration process (the final step in PTC-FREI)
    * Point out that evaluation skills also help teachers guide students in critically assessing AI-generated content
    
    **Common Challenges:**
    
    * Some educators may find formalized evaluation time-consuming - emphasize that practice makes it more efficient
    * The subjective nature of some criteria can make standardization difficult - suggest collaboration with colleagues
    * Balancing high standards with practical requirements - discuss the concept of "good enough" for different contexts
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