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
    page_title="Lesson 9: Zero-Shot Prompting",
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
    "title": "Zero-Shot Prompting",
    "lesson": "9",
    "section": "introduction",
    "order": 1
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_9_introduction"
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
    "lesson_9_introduction",
    "introduction",
    "Lesson 9: Zero-Shot Prompting",
    """
    **Welcome to Lesson 9 on Zero-Shot Prompting.**
    
    In this lesson, you'll learn:
    - What zero-shot prompting is and why it's useful
    - How LLMs can perform tasks without specific examples
    - When to use zero-shot prompting in educational contexts
    - How to craft effective zero-shot prompts
    
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
    st.markdown(f"# Lesson 9: {PAGE_INFO['title']}")
    
    # Objective
    st.markdown("## Objective")
    st.markdown("""
    To understand zero-shot prompting and learn how to leverage LLMs' pre-existing knowledge 
    to perform tasks without providing specific examples.
    """)
    
    # Real-world hook
    st.info("""
    ### Real-World Hook
    
    Imagine having a new teaching assistant who, despite never having seen your specific classroom materials, 
    can immediately help you create lesson plans, assessments, and learning activities because they've been 
    trained on educational best practices. That's the power of zero-shot prompting — the ability to get 
    valuable results from an AI without first showing it examples specific to your needs.
    """)
    
    # Jargon-Free Explanation
    st.markdown("## Understanding Zero-Shot Prompting")
    
    st.markdown("""
    **Zero-shot prompting** means asking an AI to perform a task without giving it specific examples of that task.
    
    Think of it like this: If you ask a well-educated colleague to "write a summary of Romeo and Juliet," 
    they can do this because they already know:
    1. What Romeo and Juliet is
    2. What a summary is and how to write one
    3. What key elements to include in a literary summary
    
    Similarly, LLMs like Claude have been trained on vast amounts of data that include literature, educational 
    content, and writing techniques. This pre-existing knowledge allows them to perform many tasks "from scratch"
    based solely on your instructions, without needing examples.
    """)
    
    # Key Concepts
    st.markdown("## Key Concepts in Zero-Shot Prompting")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### When Zero-Shot Works Well
        
        Zero-shot prompting is most effective when:
        
        - The task is common and well-understood (e.g., summarizing text, generating questions)
        
        - The prompt uses clear, precise instructions
        
        - The task aligns with what the LLM has likely encountered during training
        
        - You need a quick result without spending time creating examples
        
        - You want to leverage the LLM's existing knowledge
        """)
        
    with col2:
        st.markdown("""
        ### When to Consider Alternatives
        
        Consider other approaches when:
        
        - The task is highly specialized or domain-specific
        
        - You need the output to follow a very specific format or style
        
        - The task requires understanding of niche concepts
        
        - Initial zero-shot attempts produce unsatisfactory results
        
        - You need consistent results that precisely match a specific example
        """)
    
    # Zero-Shot in Educational Contexts
    st.markdown("## Zero-Shot Prompting in Education")
    
    st.markdown("""
    Zero-shot prompting is particularly useful for educators because:
    
    1. **Time Efficiency**: Create materials without building elaborate prompt templates
    
    2. **Versatility**: Generate content across different subjects and grade levels
    
    3. **Adaptability**: Quickly switch between different types of educational content
    
    4. **Knowledge Leverage**: Tap into the LLM's broad understanding of educational concepts
    
    5. **Exploration**: Experiment with different approaches without extensive preparation
    """)
    
    # Components of Effective Zero-Shot Prompts
    st.markdown("## Crafting Effective Zero-Shot Prompts")
    
    st.markdown("""
    While zero-shot prompting doesn't require examples, it still benefits from structure. Effective zero-shot prompts typically include:
    
    ### 1. Clear Task Definition
    Explicitly state what you want the AI to do:
    ```
    Create a formative assessment for 7th-grade science students on the water cycle.
    ```
    
    ### 2. Specific Parameters
    Provide details that constrain the output:
    ```
    The assessment should include 5 multiple-choice questions and 2 short-answer questions.
    ```
    
    ### 3. Context and Purpose
    Explain the educational context:
    ```
    This will be used mid-unit to check understanding before a hands-on lab activity.
    ```
    
    ### 4. Output Format Guidance
    Specify how you want the information structured:
    ```
    Format each question with a clear stem, 4 answer choices for multiple-choice, 
    and include an answer key at the end.
    ```
    
    ### 5. Quality Criteria
    State what makes for a good response:
    ```
    Ensure questions assess different cognitive levels, from recall to application.
    ```
    """)
    
    # Benefits over other prompting techniques
    st.markdown("## Advantages of Zero-Shot Prompting")
    
    st.markdown("""
    Zero-shot prompting offers several benefits:
    
    - **Immediacy**: Get results without spending time crafting examples
    
    - **Flexibility**: Easily adapt to different subjects and content types
    
    - **Discovery**: See the AI's "natural" approach to a task before constraining it
    
    - **Simplicity**: Minimal prompt engineering required for many common tasks
    
    - **Accessibility**: Easier for beginners to get started with effective prompting
    """)
    
    # Real and Non-Real Zero-Shot
    st.markdown("## Understanding 'True' Zero-Shot")
    
    st.markdown("""
    It's worth noting the distinction between:
    
    **True Zero-Shot Prompting**: The LLM has never been explicitly trained on the specific task.
    
    **Effective Zero-Shot Prompting**: The LLM has seen similar tasks during training but you don't need to provide examples.
    
    As educators, we're typically using the second type. LLMs have extensive exposure to educational content and tasks during their training, so when you ask them to create a lesson plan or quiz, they're drawing on that training.
    
    This is good news! It means LLMs can generate high-quality educational content without requiring you to provide detailed examples of specific formats or approaches.
    """)
    
    # Zero-Shot vs. PTC-FREI Framework
    st.markdown("## Zero-Shot and the PTC-FREI Framework")
    
    st.markdown("""
    Zero-shot prompting works well with the PTC-FREI framework:
    
    1. **Persona**: Still valuable for establishing voice and perspective
    
    2. **Task**: Critical for clear zero-shot instructions
    
    3. **Context**: Helps focus the zero-shot response
    
    4. **Format**: Guides structure without requiring examples
    
    5. **Reference**: Can incorporate standards even in zero-shot prompts
    
    6. **Evaluation and Iteration**: Still essential for improving results
    
    The difference is that with zero-shot, you're relying more on the LLM's training rather than providing explicit examples of what you want.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Emphasize that zero-shot doesn't mean zero guidance - clear instructions are still essential
    * Relate zero-shot prompting to how we might give instructions to a knowledgeable colleague
    * Point out that zero-shot is often a good starting point, which can be refined with more structured approaches if needed
    * Encourage experimentation with zero-shot across different subject areas
    
    **Common Challenges:**
    
    * Some participants may get inconsistent results with zero-shot prompting - emphasize the importance of clear task definition
    * Others may expect too much domain-specific knowledge - remind them of the limitations when dealing with highly specialized content
    * Participants might struggle to understand when to use zero-shot versus other techniques - the examples section will help clarify this
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