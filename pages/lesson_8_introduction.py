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
    page_title="Lesson 8: Iteration (I)",
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
    "title": "Iteration (I)",
    "lesson": "8",
    "section": "introduction",
    "order": 1
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_8_introduction"
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
    "lesson_8_introduction",
    "introduction",
    "Lesson 8: Iteration",
    """
    **Welcome to Lesson 8 on Iteration in Prompting.**
    
    In this lesson, you'll learn:
    - Why iteration is essential for effective prompt engineering
    - Strategies for systematically improving prompts
    - How to implement feedback cycles for prompt refinement
    - Techniques for tracking prompt versions and improvements
    
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
    st.markdown(f"# Lesson 8: {PAGE_INFO['title']}")
    
    # Objective
    st.markdown("## Objective")
    st.markdown("""
    To understand the iterative nature of prompt engineering and learn systematic approaches 
    for refining prompts based on evaluation results.
    """)
    
    # Real-world hook
    st.info("""
    ### Real-World Hook
    
    Think about writing an important email. Do you send the first draft, or do you revise 
    it several times? Prompt engineering works the same way. Your first attempt may be good, 
    but through thoughtful iteration — making small, deliberate improvements — you can transform 
    a basic prompt into an exceptional one that produces exactly what you need.
    """)
    
    # Jargon-Free Explanation
    st.markdown("## Understanding Iteration in Prompt Engineering")
    
    st.markdown("""
    Iteration in prompt engineering is the process of systematically refining your prompts based on 
    evaluation of the AI's responses. It's like a cycle of continuous improvement:

    1. Write a prompt
    2. Evaluate the response
    3. Make targeted improvements
    4. Try again
    
    With each cycle, your prompts become more effective at generating the specific educational 
    content you need. Iteration is the bridge between evaluation and mastery.
    """)
    
    # Illustration of the iteration cycle
    st.markdown("## The Prompt Iteration Cycle")
    
    st.markdown("""
    ```
    ┌─────────────────┐
    │    Create or    │
    │ Modify Prompt   │◄─────┐
    └────────┬────────┘      │
             │               │
             ▼               │
    ┌─────────────────┐      │
    │    Generate     │      │
    │     Output      │      │
    └────────┬────────┘      │
             │               │
             ▼               │
    ┌─────────────────┐      │
    │    Evaluate     │      │
    │     Results     │      │
    └────────┬────────┘      │
             │               │
             ▼               │
    ┌─────────────────┐      │
    │   Identify      │      │
    │ Improvements    ├──────┘
    └─────────────────┘
    ```
    """)
    
    # Key Iteration Strategies
    st.markdown("## Key Iteration Strategies")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Additive Iteration
        
        **Adding elements to address gaps**
        
        Starting point:
        ```
        Create a lesson plan on photosynthesis.
        ```
        
        First iteration:
        ```
        Create a 5th-grade lesson plan on photosynthesis
        that aligns with NGSS standards.
        ```
        
        Second iteration:
        ```
        Create a 5th-grade lesson plan on photosynthesis
        that aligns with NGSS standards LS1-1, includes
        a hands-on activity, and formative assessment.
        ```
        """)
        
    with col2:
        st.markdown("""
        ### Subtractive Iteration
        
        **Removing elements that cause problems**
        
        Starting point:
        ```
        Create a comprehensive high school calculus unit on derivatives
        with 15 advanced problems, extension activities, historical
        context, real-world applications, and connections to physics.
        ```
        
        First iteration:
        ```
        Create a focused high school calculus lesson on derivatives
        with 5 scaffolded problems and one real-world application.
        ```
        
        Second iteration:
        ```
        Create a focused high school calculus lesson on power rule
        derivatives with 3 scaffolded practice problems.
        ```
        """)
    
    # More iteration techniques
    st.markdown("## Additional Iteration Techniques")
    
    st.markdown("""
    ### 1. Parameter Tuning
    
    Adjust specific elements of your prompt while keeping others constant:
    
    - Change the complexity level: "...for beginner students" → "...for advanced students"
    - Modify the output length: "Brief summary" → "Detailed explanation"
    - Alter the tone: "Formal academic style" → "Conversational style for teenagers"
    
    ### 2. Structural Reframing
    
    Reorganize how you present the prompt:
    
    - Single request → Step-by-step instructions
    - General description → Template with placeholders
    - Open-ended question → Multiple-choice options
    
    ### 3. Example-Driven Refinement
    
    Include examples of what you want:
    
    ```
    Create 5 math word problems about fractions.
    For example: "Sarah ate 1/4 of a pizza and Michael ate 2/8 of the same pizza. 
    Who ate more and by how much?"
    
    Each problem should include: (1) a real-world context, (2) at least two fractions, 
    (3) a clear question, and (4) require fraction comparison or operations.
    ```
    """)
    
    # Best Practices
    st.markdown("## Best Practices for Effective Iteration")
    
    st.markdown("""
    1. **Make one change at a time** to clearly identify what improves the output
    
    2. **Document your iterations** to track what works and avoid repeating unsuccessful approaches
    
    3. **Focus on specific issues** identified during evaluation rather than making random changes
    
    4. **Test across different contexts** to ensure your refined prompt works in various scenarios
    
    5. **Set clear success criteria** to know when you've achieved your goal
    
    6. **Save your best prompts** as templates for future use
    """)
    
    # Connection to the PTC-FREI Framework
    st.markdown("## Iteration and the PTC-FREI Framework")
    
    st.markdown("""
    Iteration is the final piece of the PTC-FREI framework, creating a continuous improvement cycle:
    
    - **P**ersona, **T**ask, **C**ontext, **F**ormat, and **R**eference Materials form your initial prompt
    - **E**valuation assesses the output's effectiveness
    - **I**teration refines the prompt based on evaluation
    
    When you complete this lesson, you'll have learned all components of the PTC-FREI framework
    and will be ready to apply the complete process to create highly effective educational prompts.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Emphasize that iteration is not about "fixing failures" but about continuous improvement - even good prompts can be made better
    * Connect iteration in prompt engineering to the revision process in writing, which educators already understand
    * Encourage teachers to save their iterations as they go, creating a library of prompts at different stages of refinement
    * Remind participants that the evaluation techniques from Lesson 7 provide the foundation for effective iteration
    
    **Common Challenges:**
    
    * Some participants may feel that iteration is too time-consuming; emphasize that the investment pays off through reusable templates
    * Others may make too many changes at once, making it hard to identify what helped; stress the value of methodical, incremental changes
    * Teachers may struggle to know when to stop iterating; discuss the concept of "good enough" versus diminishing returns
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