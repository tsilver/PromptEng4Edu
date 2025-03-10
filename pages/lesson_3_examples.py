import streamlit as st
import os
import sys
from utils.navigation import scroll_to_top, get_all_pages
from utils.state_management import initialize_session_state, mark_page_completed
from utils.teacher_client import TeacherClient
from components.teacher_notes import render_teacher_notes
from components.bottom_navigator import render_bottom_navigator
from components.breadcrumb_navigator import render_breadcrumb
from components.course_navigation import render_course_navigation
from components.top_navigator import render_top_navigator
from components.first_visit_dialog import show_first_visit_dialog
from components.progress_manager import render_teacher_controls_sidebar

# Initialize the TeacherClient
client = TeacherClient()

# Configure page
st.set_page_config(
    page_title="Lesson 3: Examples",
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
    "title": "Defining the Task: Examples",
    "lesson": "3",
    "section": "examples",
    "order": 2
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_3_examples"
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
    "lesson_3_examples",
    "examples",
    "Lesson 3: Examples of Task Definition",
    """
    **This section demonstrates how task definition transforms AI responses.**
    
    You'll see:
    - Side-by-side comparisons of vague versus specific tasks
    - Examples of effective action verbs for different purposes
    - Educational examples relevant to teaching tasks
    
    Look through these examples to understand how precise task definition 
    helps generate more focused and useful responses.
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
    st.markdown("## Task Definition Examples")
    
    st.markdown("""
    The following examples demonstrate how defining tasks clearly in your prompts significantly 
    improves the AI's response. Compare the vague tasks with their well-defined counterparts.
    """)
    
    # Example 1: General Example
    st.markdown("### General Examples of Task Definition")
    
    st.markdown("#### Example 1: Creating Educational Content")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Vague Task:**
        ```
        Tell me about the water cycle.
        ```
        
        **Issues:**
        - Unclear what content format is needed
        - No specified audience or complexity level
        - Unknown purpose for the information
        """)
    
    with col2:
        st.markdown("""
        **Well-Defined Task:**
        ```
        Create a step-by-step explanation of the water cycle 
        with 5 key stages that would be suitable for 
        4th-grade students learning about the topic 
        for the first time.
        ```
        
        **Improvements:**
        - Clear action verb ("Create")
        - Specific content type ("step-by-step explanation")
        - Quantification ("5 key stages")
        - Appropriate audience context
        """)
    
    # Example 2: Assessment Creation
    st.markdown("#### Example 2: Assessment Creation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Vague Task:**
        ```
        Make a quiz about fractions.
        ```
        
        **Issues:**
        - "Make" is ambiguous
        - No indication of difficulty level
        - Unclear what aspects of fractions to cover
        - No specifications for question types or number
        """)
    
    with col2:
        st.markdown("""
        **Well-Defined Task:**
        ```
        Generate 8 multiple-choice questions assessing 
        students' ability to add and subtract fractions 
        with different denominators. Include 4 basic-level 
        and 4 challenge-level questions, and provide an 
        answer key.
        ```
        
        **Improvements:**
        - Specific action ("Generate")
        - Exact number of items specified
        - Precise content focus
        - Differentiation by difficulty
        - Additional output requirement (answer key)
        """)
    
    # Education-specific examples
    st.markdown("### Education-Specific Task Examples")
    
    # Example 3: Differentiation
    st.markdown("#### Example 3: Differentiation Tasks")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Vague Task:**
        ```
        Help me differentiate this lesson.
        ```
        
        **What's Missing:**
        - No clear action 
        - No information about the original lesson
        - No indication of student needs
        - No specific differentiation approach
        """)
    
    with col2:
        st.markdown("""
        **Well-Defined Task:**
        ```
        Modify this middle school geometry lesson on 
        calculating area of triangles to create three 
        versions: one for visual learners using diagrams, 
        one for students who need additional scaffolding, 
        and one with extension activities for advanced 
        students.
        ```
        
        **Task Elements:**
        - Clear action ("Modify")
        - Specific content identified
        - Exact requirements (three versions)
        - Detailed differentiation approaches
        """)
    
    # Example 4: Providing Feedback
    st.markdown("#### Example 4: Feedback Tasks")
    
    st.markdown("""
    **Context:** *You need to give feedback on student writing*
    
    **Poor Task Definition:** "Give feedback."
    
    **Better Task Definition:** "Analyze this 10th-grade argumentative essay draft and provide three specific strengths to reinforce and three actionable suggestions for improving the use of evidence and logical reasoning. Format the feedback in a way that acknowledges the student's effort while encouraging growth."
    
    **Task Components:**
    - Primary action verb: "Analyze" and "provide"
    - Quantification: "three strengths" and "three suggestions"
    - Focus areas: "evidence and logical reasoning"
    - Tone guidance: "acknowledges effort while encouraging growth"
    """)
    
    # Action Verb Library
    st.markdown("## Action Verb Library for Educators")
    
    st.markdown("""
    The first word in your task often determines how effective it will be. Here's a library of action verbs categorized by educational purpose:
    
    ### For Content Creation
    - **Explain:** Give information in a way that makes a concept understandable
    - **Summarize:** Provide a condensed version of key points
    - **Describe:** Give details that help create a mental image
    - **Compare:** Show similarities and differences between concepts
    
    ### For Assessment
    - **Generate:** Create new assessment items
    - **Design:** Create with specific features and purposes
    - **Formulate:** Develop systematically with attention to components
    - **Create:** Produce something original
    
    ### For Lesson Planning
    - **Outline:** Provide a structured framework
    - **Develop:** Create a complete plan with details
    - **Adapt:** Modify existing material for new purposes
    - **Sequence:** Arrange in a logical progression
    
    ### For Student Support
    - **Identify:** Find specific elements or patterns
    - **Suggest:** Recommend possible approaches or solutions
    - **Scaffold:** Build supporting structures for learning
    - **Differentiate:** Adjust for varying student needs
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific guidance
    render_teacher_notes("""
    **Key Points to Emphasize:**
    
    * Task definition is often the weakest part of teachers' initial prompts
    * The action verb choice dramatically affects what the AI produces
    * Specificity doesn't mean wordiness - concise, clear tasks are ideal
    * Consider creating a personal "task template library" for common instructional needs
    
    **Discussion Questions:**
    
    * What tasks do you frequently need AI help with in your teaching?
    * What action verbs would be most relevant for your subject area?
    * How might you adapt these examples for your specific educational context?
    
    **Extension Activity:**
    
    Have participants identify one vague prompt they've used in the past and rewrite it with a well-defined task. Share and discuss the improvements.
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