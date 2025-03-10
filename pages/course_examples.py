import streamlit as st
import os
import sys
from utils.navigation import scroll_to_top
from utils.state_management import initialize_session_state, mark_page_completed
from components.breadcrumb_navigator import render_breadcrumb
from components.bottom_navigator import render_bottom_navigator
from components.course_navigation import render_course_navigation
from components.top_navigator import render_top_navigator

# Configure page
st.set_page_config(
    page_title="Course Examples",
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
    "title": "Course Examples",
    "lesson": "intro",
    "section": "examples",
    "order": 1
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "course_examples"
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
    st.title("Course Examples")
    
    st.markdown("""
    This section showcases examples of how educators are using AI and prompt engineering 
    in their teaching practice. These real-world examples illustrate the potential of 
    prompt engineering to transform educational tasks.
    """)
    
    # Course progression note
    st.info("""
    **📚 Course Progression:** 
    
    Viewing these examples is an important part of the course introduction. After exploring these examples:
    
    1. Try the hands-on activities in the Activities section
    2. Complete the Reflection section (marked with ✨) to unlock Lesson 1
    """)
    
    # Example 1: Lesson Planning
    st.markdown("## Example 1: Enhancing Lesson Planning")
    
    st.markdown("""
    Effective prompt engineering can dramatically improve the quality and relevance 
    of AI-generated lesson plans.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Basic Prompt")
        st.code("Create a lesson plan on photosynthesis.")
        
        st.markdown("""
        **Result:**
        
        - Generic lesson plan
        - One-size-fits-all approach
        - May require significant modification
        - Lacks specific teaching strategies
        """)
    
    with col2:
        st.markdown("### Engineered Prompt")
        st.code("""Create a 5th-grade science lesson plan on photosynthesis 
that incorporates hands-on experiments.

Include:
- 3 clear learning objectives aligned with NGSS standards
- A 10-minute engagement activity using household items
- A 20-minute guided investigation
- A 15-minute explanation section with age-appropriate vocabulary
- A 10-minute formative assessment
- Modifications for students with different learning needs""")
        
        st.markdown("""
        **Result:**
        
        - Grade-specific content and vocabulary
        - Standards-aligned objectives
        - Structured timing for different activities
        - Includes differentiation strategies
        - Ready-to-use experiential learning components
        """)
    
    # Example 2: Assessment Creation
    st.markdown("## Example 2: Differentiated Assessment Creation")
    
    st.markdown("""
    By carefully crafting prompts, educators can generate varied assessment items 
    that target different levels of understanding.
    """)
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("### Basic Prompt")
        st.code("Create quiz questions about World War II.")
        
        st.markdown("""
        **Result:**
        
        - Random assortment of questions
        - Inconsistent difficulty level
        - May focus on memorization only
        - Lack of structure or grading guidance
        """)
    
    with col4:
        st.markdown("### Engineered Prompt")
        st.code("""Create a balanced assessment on World War II for 10th grade 
history students who have studied the European theater.

Include:
- 5 multiple-choice questions (2 recall, 2 analysis, 1 evaluation)
- 3 short-answer questions focused on cause-effect relationships
- 1 document analysis question using the attached primary source
- 1 comparison question examining different perspectives

For each question, include:
- Point value
- Answer key
- Cognitive level (according to Bloom's taxonomy)""")
        
        st.markdown("""
        **Result:**
        
        - Balanced assessment with varied question types
        - Mix of cognitive levels
        - Specific focus on taught content
        - Includes grading guidance
        - Pedagogically sound design
        """)
    
    # Example 3: Feedback Generation
    st.markdown("## Example 3: Personalized Student Feedback")
    
    st.markdown("""
    Prompt engineering allows educators to generate more helpful, specific 
    feedback for student work.
    """)
    
    col5, col6 = st.columns(2)
    
    with col5:
        st.markdown("### Basic Prompt")
        st.code("Provide feedback on this student essay.")
        
        st.markdown("""
        **Result:**
        
        - General comments about writing quality
        - May be overly positive or vague
        - Inconsistent focus on different aspects
        - Lacks specific improvement strategies
        """)
    
    with col6:
        st.markdown("### Engineered Prompt")
        st.code("""As a supportive 8th grade English teacher, provide 
constructive feedback on this student's persuasive essay.

Focus on:
- Thesis clarity and development (high priority)
- Evidence quality and integration (high priority)
- Organization and transitions (medium priority)
- Voice and style (low priority)

For each area of feedback:
1. Highlight 1-2 specific strengths with examples
2. Identify 1-2 areas for improvement with examples
3. Provide a concrete, actionable strategy the student can apply
4. Use encouraging, growth-mindset language

The feedback should be specific enough to guide revision but not 
rewrite the essay for the student.""")
        
        st.markdown("""
        **Result:**
        
        - Prioritized feedback on key areas
        - Balance of strengths and growth areas
        - Specific examples from student work
        - Actionable improvement strategies
        - Developmentally appropriate tone
        """)
    
    # Key Takeaways
    st.markdown("## Key Takeaways from These Examples")
    
    st.markdown("""
    These examples demonstrate how well-crafted prompts can dramatically improve AI outputs for educational purposes:
    
    1. **Specificity matters**: The more specific your prompt, the more tailored the result
    2. **Structure guides output**: Formatting your prompt helps structure the AI's response
    3. **Educational context improves relevance**: Including grade level, standards, and pedagogical approach creates more useful outputs
    4. **Prioritization focuses responses**: Indicating what matters most results in better emphasis
    
    In the following lessons, you'll learn the systematic framework for crafting these types of effective prompts.
    """)
    
    # Next steps
    st.success("""
    **Next Steps:**
    
    Now that you've seen what well-crafted prompts can do, try the interactive activities to start
    developing your own prompting skills, then complete the reflection to set your learning goals.
    """)
    
    # Add bottom navigator - mirrors the top navigator
    render_bottom_navigator(PAGE_INFO)
    
    # Mark this page as completed when viewed
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