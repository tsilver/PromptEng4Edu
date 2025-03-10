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
    page_title="Lesson 4: Examples",
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
    "title": "Specifying Format: Examples",
    "lesson": "4",
    "section": "examples",
    "order": 2
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_4_examples"
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
    "lesson_4_examples",
    "examples",
    "Lesson 4: Examples of Format Specification",
    """
    **This section demonstrates how format specification transforms AI responses.**
    
    You'll see:
    - Side-by-side comparisons of prompts with and without format specifications
    - Examples of various format types useful for education
    - How combining context, task, and format creates powerful prompts
    
    Look through these examples to understand how specifying format 
    helps generate more structured and immediately useful responses.
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
    st.markdown("## Format Specification Examples")
    
    st.markdown("""
    The following examples demonstrate how specifying format in your prompts significantly 
    improves the usability of AI responses. Compare these examples to see the power of format specification.
    """)
    
    # Example 1: List Formats
    st.markdown("### Example 1: List Formats")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Basic Prompt (No Format):**
        ```
        Give me classroom management tips.
        ```
        
        **Potential Issues:**
        - Could be a long paragraph of text
        - May not highlight separate tips clearly
        - Difficult to scan quickly
        - No indication of priority or organization
        """)
    
    with col2:
        st.markdown("""
        **Format-Specific Prompt:**
        ```
        Provide 5 classroom management tips 
        for a middle school science lab. 
        Format as a numbered list with a 
        brief one-sentence explanation for each tip.
        ```
        
        **Format Elements:**
        - Specified number (5 tips)
        - Numbered list structure
        - Defined scope for each item (one sentence)
        - Clear context for relevant content
        """)
    
    st.markdown("""
    **List Format Variations:**
    
    ```
    "Present this as bullet points with headers in bold."
    
    "Organize this as a hierarchical list with main points and 3-4 sub-points under each."
    
    "Create a checklist format with actionable items that can be completed in sequence."
    ```
    """)
    
    # Example 2: Table Formats
    st.markdown("### Example 2: Table Formats")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Basic Prompt (No Format):**
        ```
        Explain the differences between 
        formative and summative assessment.
        ```
        
        **Potential Issues:**
        - Likely a prose explanation
        - Differences not clearly juxtaposed
        - Difficult to see parallel comparisons
        - Requires reading through full text
        """)
    
    with col2:
        st.markdown("""
        **Format-Specific Prompt:**
        ```
        Create a comparison table of formative 
        vs. summative assessment with these 
        rows: Purpose, Timing, Examples, 
        Feedback type, and Grading approach. 
        Include a brief title for the table.
        ```
        
        **Format Elements:**
        - Table structure specified
        - Exact row categories listed
        - Column structure implied (comparison)
        - Title requested
        """)
    
    st.markdown("""
    **Actual AI Response with Table Format:**
    
    # Comparison of Formative and Summative Assessment
    
    | Aspect | Formative Assessment | Summative Assessment |
    |--------|---------------------|----------------------|
    | **Purpose** | To monitor student learning and provide ongoing feedback | To evaluate student learning at the end of an instructional period |
    | **Timing** | During the learning process | After completion of a unit, course, or program |
    | **Examples** | Exit tickets, quick quizzes, classroom polls, discussion | Final exams, standardized tests, end-of-unit projects, term papers |
    | **Feedback type** | Immediate, specific, and focused on improvement | Evaluative, comprehensive, and focused on achievement |
    | **Grading approach** | Low-stakes or ungraded, emphasis on growth | High-stakes, contributes significantly to final grades |
    """)
    
    # Example 3: Educational Template Formats
    st.markdown("### Example 3: Educational Template Formats")
    
    st.markdown("""
    **Lesson Plan Template Format:**
    
    ```
    Create a 45-minute lesson plan on photosynthesis for 6th-grade science 
    using this exact template:
    
    Title:
    Learning Objectives (3 measurable objectives):
    Materials and Resources:
    Activation (5 minutes):
    Instruction (15 minutes):
    Guided Practice (15 minutes):
    Independent Practice (5 minutes):
    Assessment (5 minutes):
    Extensions/Differentiation:
    ```
    
    **Format Elements:**
    - Template structure with specific sections
    - Time allocation for each section
    - Number specifications (3 measurable objectives)
    - Section titles and organization
    """)
    
    # Example 4: Combining Context, Task, and Format
    st.markdown("### Example 4: Complete CT-F Prompts for Education")
    
    st.markdown("""
    Here are examples that combine Context, Task, and Format specifications for powerful educational prompts:
    
    **Example A: Student Feedback**
    ```
    Context: For a 10th-grade student who struggles with organizing ideas in persuasive essays 
             but shows strong critical thinking skills.
    
    Task: Generate constructive feedback on their introductory paragraph that acknowledges 
          strengths while providing guidance for improvement.
    
    Format: Structure the feedback in three parts:
            1. A positive opening that highlights specific strengths (2-3 sentences)
            2. Growth areas with specific suggestions (3-4 bullet points)
            3. A motivational closing statement (1-2 sentences)
    ```
    
    **Example B: Concept Explanation**
    ```
    Context: For 7th-grade math students who understand basic fractions but are struggling 
             with the concept of negative fractions.
    
    Task: Explain how to add and subtract negative fractions with different denominators.
    
    Format: Create a visual guide with:
            - A brief explanation at the top (max 3 sentences)
            - 3 worked examples showing step-by-step solutions with color-coding
            - A numbered procedure list that students can follow
            - A "common mistakes" box at the bottom with 2-3 errors to avoid
    ```
    """)
    
    # Educational Format Library
    st.markdown("## Educational Format Library")
    
    st.markdown("""
    Here's a collection of format specifications tailored to common educational needs:
    
    ### For Assessment
    
    **Quiz Format:**
    ```
    Format as a 10-question multiple-choice quiz with 4 options per question, 
    labeled A-D. Include an answer key at the end.
    ```
    
    **Rubric Format:**
    ```
    Create a 4-level rubric (Beginning, Developing, Proficient, Exemplary) 
    with 3 criteria. For each cell, include 2-3 descriptors of performance.
    ```
    
    ### For Instruction
    
    **Concept Map Format:**
    ```
    Format as a concept map with the main concept in the center, 5-7 related 
    concepts branching out, and brief descriptions of each connection.
    ```
    
    **Guided Notes Format:**
    ```
    Create a guided notes template with section headers, key terms bolded, 
    and blank lines for students to fill in essential information.
    ```
    
    ### For Planning
    
    **Unit Plan Format:**
    ```
    Format as a unit overview table with columns for: Day, Topic, 
    Learning Objectives, Activities, and Assessment. Include 10 days of instruction.
    ```
    
    **Differentiation Matrix:**
    ```
    Create a differentiation matrix with rows for different student needs 
    (struggling, on-level, advanced) and columns for Content, Process, and Product.
    ```
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific guidance
    render_teacher_notes("""
    **Key Points to Emphasize:**
    
    * The format makes the difference between usable and frustrating AI outputs
    * Format specifications can be used with any AI tool - not just educational-specific ones
    * Teachers already use formats in their daily work - this is extending that practice to AI
    * Experimenting with different formats for the same content can significantly enhance usability
    
    **Discussion Questions:**
    
    * What formats do you regularly use in your teaching materials?
    * How might standard formats save you time when working with AI?
    * For your subject area, what specialized formats would be most valuable?
    
    **Extension Activity:**
    
    Ask participants to identify one teaching document they regularly create and define its format specification in a way that an AI could reproduce it.
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