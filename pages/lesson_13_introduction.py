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
    page_title="Lesson 13: Lesson Planning and Assessment Creation",
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
    "title": "Lesson Planning and Assessment Creation",
    "lesson": "13",
    "section": "introduction",
    "order": 1
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_13_introduction"
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
    "lesson_13_introduction",
    "introduction",
    "Lesson 13: Lesson Planning and Assessment Creation",
    """
    **Welcome to Lesson 13 on Lesson Planning and Assessment Creation!**
    
    In this lesson, you'll learn:
    - How to apply prompt engineering techniques to create effective lesson plans
    - Strategies for generating high-quality assessments aligned with learning objectives
    - Techniques for creating differentiated materials for diverse learners
    - How to use the PTC-FREI framework for curriculum development
    
    This begins our application-focused lessons where you'll put your prompt engineering skills to work!
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
    st.markdown(f"# Lesson 13: {PAGE_INFO['title']}")
    
    # Objective
    st.markdown("## Objective")
    st.markdown("""
    To apply the prompt engineering techniques you've learned to create effective lesson plans
    and high-quality assessments that meet educational standards, engage students, and support
    diverse learning needs.
    """)
    
    # Real-world hook
    st.info("""
    ### Real-World Hook
    
    Lesson planning and assessment creation are two of the most time-consuming tasks for educators. 
    A 2023 survey found that teachers spend an average of 7-12 hours per week on these activities alone.
    With effective prompt engineering, you can significantly reduce this time while maintaining or even
    improving quality, freeing up more time to focus on what matters most: working directly with students.
    """)
    
    # Application Focus
    st.markdown("## Applying Your Prompt Engineering Skills")
    
    st.markdown("""
    In previous lessons, you learned several powerful prompt engineering techniques:
    
    - **The PTC-FREI Framework**: Persona, Task, Context, Format, Reference, Evaluation, Iteration
    - **Zero-Shot Prompting**: Using the AI's built-in knowledge
    - **Few-Shot Prompting**: Providing examples to guide responses
    - **Chain-of-Thought Prompting**: Guiding step-by-step reasoning
    - **Role Prompting**: Using specific personas to shape voice and content
    
    Now, you'll apply these techniques to create two essential educational resources:
    
    1. **Lesson Plans**: Structured guides for teaching specific content and skills
    2. **Assessments**: Tools to measure student understanding and mastery
    
    This lesson focuses on practical applications that you can immediately use in your teaching practice.
    """)
    
    # Lesson Planning Strategies
    st.markdown("## Prompt Engineering for Lesson Planning")
    
    st.markdown("""
    Effective lesson plans typically include several key components:
    
    - **Learning objectives**: What students will learn
    - **Standards alignment**: Connections to curriculum standards
    - **Instructional activities**: What students and teachers will do
    - **Materials and resources**: What's needed to implement the lesson
    - **Assessment methods**: How learning will be evaluated
    - **Differentiation strategies**: How to support diverse learners
    
    By using prompt engineering techniques, you can create comprehensive lesson plans that include
    all these components while tailoring them to your specific teaching context.
    """)
    
    # Lesson planning prompting tips
    st.markdown("### Key Strategies for Lesson Plan Prompting")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Effective Techniques
        
        **🔹 Use the Format Component**
        - Specify the exact lesson plan template you want followed
        - Include section headers and required elements
        
        **🔹 Apply Role Prompting**
        - Use content specialist personas for subject-specific lessons
        - Consider pedagogical expert roles for innovative approaches
        
        **🔹 Provide Context**
        - Include student demographics and prior knowledge
        - Specify available resources and time constraints
        """)
    
    with col2:
        st.markdown("""
        #### Common Pitfalls to Avoid
        
        **🔸 Too Vague**
        - "Create a science lesson plan" → Too general
        - "Create a 5E model lesson plan on photosynthesis for 7th graders with hands-on activities" → More specific
        
        **🔸 Ignoring Standards**
        - Include specific curriculum standards to ensure alignment
        
        **🔸 One-Size-Fits-All Approach**
        - Specify differentiation needs for diverse learners
        - Request modifications for different learning profiles
        """)
    
    # Assessment Creation Strategies
    st.markdown("## Prompt Engineering for Assessment Creation")
    
    st.markdown("""
    Quality assessments should:
    
    - Align with learning objectives
    - Assess appropriate cognitive levels (from recall to application to evaluation)
    - Include clear instructions and scoring criteria
    - Provide valid and reliable measures of learning
    - Offer insights for instructional improvement
    
    Prompt engineering can help you create various types of assessments:
    - Formative and summative assessments
    - Multiple-choice, short answer, and extended response questions
    - Performance tasks and project-based assessments
    - Rubrics and scoring guides
    """)
    
    # Assessment prompting tips
    st.markdown("### Key Strategies for Assessment Prompting")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Effective Techniques
        
        **🔹 Use Few-Shot Prompting**
        - Provide examples of high-quality questions
        - Include examples at different cognitive levels
        
        **🔹 Specify Assessment Purpose**
        - Clarify if it's formative or summative
        - Explain how results will be used
        
        **🔹 Request Cognitive Level Variety**
        - Ask for questions at specific Bloom's levels
        - Request a distribution of difficulty levels
        """)
    
    with col2:
        st.markdown("""
        #### Common Pitfalls to Avoid
        
        **🔸 Focus on Recall Only**
        - Request higher-order thinking questions explicitly
        
        **🔸 Unclear Success Criteria**
        - Ask for rubrics and scoring guidelines to accompany assessments
        
        **🔸 Misalignment with Objectives**
        - Include learning objectives in your prompt
        - Ask for explicit connections between objectives and assessment items
        """)
    
    # Combining Framework Components
    st.markdown("## The PTC-FREI Approach to Curriculum Development")
    
    st.markdown("""
    When creating lesson plans and assessments, using the full PTC-FREI framework can be 
    particularly powerful:
    
    | Component | Application in Curriculum Development |
    |-----------|--------------------------------------|
    | **Persona** | Content expert, experienced teacher, instructional coach |
    | **Task** | Create lesson plan, generate assessment, develop rubric |
    | **Context** | Grade level, subject area, student characteristics, standards |
    | **Format** | Specific template or structure for the materials |
    | **Reference** | Curriculum standards, textbooks, existing materials |
    | **Evaluation** | Review for alignment, engagement, differentiation |
    | **Iteration** | Refine based on identified improvements |
    
    This systematic approach ensures comprehensive, high-quality curricular materials
    that are ready to use in your classroom.
    """)
    
    # Practical Application
    st.markdown("## Real-World Applications")
    
    st.markdown("""
    Effective prompting for curriculum development can help you:
    
    - **Save time** on routine planning and assessment creation
    - **Ensure alignment** with standards and objectives
    - **Generate fresh ideas** for engaging activities
    - **Create differentiated materials** for diverse learners
    - **Develop comprehensive assessments** at various cognitive levels
    - **Produce supplementary materials** like handouts and slides
    
    In the examples and activities sections, you'll see specific prompts and techniques
    that bring these benefits to life in practical, immediately useful ways.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Emphasize that AI-generated lesson plans and assessments should be starting points that educators review, modify, and enhance based on their professional judgment
    * Point out that prompt engineering for curriculum development allows educators to focus more on the creative aspects of teaching rather than routine production
    * Encourage participants to collect and organize effective prompts they develop in a personal "prompt library" for future use
    * Discuss how these techniques can support collaboration among teaching teams by generating shared resources
    
    **Implementation Ideas:**
    
    * Suggest developing a collection of "template prompts" for different subject areas and grade levels that can be customized as needed
    * Recommend creating prompts for units rather than individual lessons to ensure coherence across a learning sequence
    * Propose using these techniques to create multilingual materials or resources for specific learning profiles
    * Discuss how AI-generated assessments can be enhanced through human review to ensure they fairly represent diverse perspectives and experiences
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