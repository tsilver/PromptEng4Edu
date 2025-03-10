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
    page_title="Lesson 6: Reference Materials (R)",
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
    "title": "Reference Materials (R)",
    "lesson": "6",
    "section": "introduction",
    "order": 1
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_6_introduction"
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
    "lesson_6_introduction",
    "introduction",
    "Lesson 6: Reference Materials",
    """
    **Welcome to Lesson 6 on Reference Materials in Prompting.**
    
    In this lesson, you'll learn:
    - How to incorporate external content and resources into your prompts
    - Techniques for guiding AI to use specific information sources
    - Strategic approaches for creating content aligned with existing materials
    
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
    st.markdown(f"# Lesson 6: {PAGE_INFO['title']}")
    
    # Objective
    st.markdown("## Objective")
    st.markdown("""
    To teach educators how to effectively incorporate reference materials into their prompts to create 
    AI-generated content that accurately reflects specific sources, standards, or curriculum materials.
    """)
    
    # Real-world hook
    st.info("""
    ### Real-World Hook
    
    As an educator, you often need to create materials that align with specific standards, textbooks, or 
    curriculum guides. Rather than having the AI generate content based solely on its training data, you 
    can provide excerpts from your actual standards documents, textbook passages, or other materials to 
    ensure the AI's output is directly relevant to your specific curriculum and teaching context.
    """)
    
    # Jargon-Free Explanation
    st.markdown("## Understanding Reference Materials in Prompting")
    
    st.markdown("""
    When we talk about reference materials in prompt engineering, we mean providing the AI with specific 
    content to draw from when generating its response. This can be as simple as a quote to analyze or as 
    complex as curriculum standards to align with.
    
    Using reference materials helps you:
    
    - Ensure accuracy and alignment with specific sources
    - Create content based on your curriculum or standards
    - Generate responses that reference particular texts or materials
    - Produce outputs that use the same terminology and approach as your existing resources
    """)
    
    # Illustrative diagram
    st.markdown("## The Impact of Including Reference Materials")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("""
        **🔍 Without References:**
        ```
        "Create a lesson plan about fractions for 
        4th-grade students."
        ```
        
        ⬇️
        
        **Generic, potentially misaligned content**
        - Based on the AI's general knowledge
        - May not match your curriculum
        - Could use different terminology
        - Might cover standards you haven't taught
        """)
        
    with col_b:
        st.markdown("""
        **🌟 With References:**
        ```
        "Create a lesson plan about fractions for 
        4th-grade students based on these standards:
        
        MATH.4.NF.1: Explain equivalence of fractions 
        using visual models and attention to numerator 
        and denominator.
        
        MATH.4.NF.2: Compare two fractions with 
        different numerators and denominators by 
        creating common denominators or numerators."
        ```
        
        ⬇️
        
        **Precisely aligned content**
        - Focuses on the exact standards provided
        - Uses the same terminology
        - Covers appropriate scope and sequence
        - Connects to your specific curriculum
        """)
    
    # Types of Reference Materials
    st.markdown("## Types of Reference Materials for Educational Prompts")
    
    st.markdown("""
    You can incorporate many types of reference materials into your prompts:
    
    ### 1. Curriculum Standards
    - State or national standards
    - School or district curriculum guides
    - Scope and sequence documents
    
    ### 2. Content Sources
    - Textbook excerpts
    - Reading passages
    - Primary source documents
    - Data sets or research findings
    
    ### 3. Pedagogical Materials
    - Existing lesson plans or unit outlines
    - Assessment rubrics
    - Teaching methodologies or frameworks
    
    ### 4. Student Work
    - Writing samples for feedback
    - Project descriptions for evaluation
    - Assessment responses for analysis
    """)
    
    # How to Incorporate References
    st.markdown("## How to Incorporate References in Your Prompts")
    
    st.markdown("""
    There are several effective techniques for including reference materials:
    
    ### 1. Direct Quotation
    
    ```
    "Based on this excerpt from our textbook: '[paste text here]', 
    create comprehension questions that assess..."
    ```
    
    ### 2. Standards References
    
    ```
    "Using these learning standards: [paste standards], 
    develop a lesson that addresses..."
    ```
    
    ### 3. Resource Synthesis
    
    ```
    "Given these three resources:
    1. [Resource 1]
    2. [Resource 2]
    3. [Resource 3]
    
    Create a study guide that synthesizes the key information..."
    ```
    
    ### 4. Analysis Direction
    
    ```
    "Analyze this student essay: '[paste essay]' using 
    the following rubric criteria: [paste rubric]..."
    ```
    """)
    
    # Relationship to previous lessons
    st.markdown("## Progress in the PTC-FREI Framework")
    
    st.markdown("""
    So far, we've covered:
    
    - **Context (C)** - Lesson 2: The background information that shapes understanding
    - **Task (T)** - Lesson 3: The specific action you want the AI to perform
    - **Format (F)** - Lesson 4: How you want the response structured
    - **Persona (P)** - Lesson 5: The voice and perspective for the response
    - **Reference Materials (R)** - Lesson 6 (Today): The specific content to draw from
    
    Let's see how reference materials work with the other components:
    
    ```
    Persona: "As a science curriculum specialist familiar with NGSS standards"
    
    Context: "For a 5th-grade class studying ecosystems"
    
    Task: "Create a formative assessment"
    
    Format: "With 5 multiple-choice questions and 2 short answer questions"
    
    Reference: "Based on these NGSS standards:
    5-LS2-1: Develop a model to describe the movement of matter among plants, 
    animals, decomposers, and the environment.
    5-PS3-1: Use models to describe that energy in animals' food was once 
    energy from the sun."
    ```
    
    The reference materials ensure that the content created matches specific curriculum requirements, while the other components guide how that content is delivered.
    """)
    
    # Best Practices for Reference Materials
    st.markdown("## Best Practices for Using Reference Materials")
    
    st.markdown("""
    To get the most out of reference materials in your prompts:
    
    ### 1. Be Selective
    Don't overwhelm the AI with too much reference material. Choose the most relevant sections.
    
    ### 2. Provide Context for References
    Tell the AI why you're including these references and how they should be used.
    
    ### 3. Check for Alignment
    Verify that the AI's output accurately reflects and aligns with the provided references.
    
    ### 4. Use Clear Formatting
    Clearly distinguish reference materials from your instructions using formatting like quotation marks, bullet points, or paragraph breaks.
    
    ### 5. Consider Copyright and Fair Use
    When using published materials, ensure your use complies with copyright laws and fair use guidelines.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Have participants identify reference materials they regularly use in their teaching that could be incorporated into prompts
    * Discuss how reference materials can help ensure AI-generated content complies with curriculum requirements
    * Emphasize that reference materials are especially important when accuracy and alignment are critical
    * Point out how including standards can save time in creating standards-aligned materials
    
    **Common Challenges:**
    
    * Including too much reference material, which can overwhelm the AI or make it lose focus
    * Not being clear about how the references should be used in generating the response
    * Using references without proper attribution or consideration of copyright
    * Expecting the AI to perfectly understand complex curriculum documents without additional guidance
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