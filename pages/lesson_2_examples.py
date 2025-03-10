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
    page_title="Lesson 2: Examples",
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
    "title": "The Power of Context: Examples",
    "lesson": "2",
    "section": "examples",
    "order": 2
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_2_examples"
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
    "lesson_2_examples",
    "examples",
    "Lesson 2: Examples of Context",
    """
    **This section demonstrates how context transforms AI responses.**
    
    You'll see:
    - Side-by-side comparisons of prompts with and without context
    - Analysis of how context changes the output
    - Educational examples relevant to teaching
    
    Look through these examples to understand how context helps 
    generate more relevant and useful responses.
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
    st.markdown("## Relevant and Accessible Examples")
    
    st.markdown("""
    The following examples demonstrate how adding context to your prompts significantly 
    changes the AI's response. Click on each example to view a comparison between prompts 
    with and without context.
    """)
    
    st.markdown("### General Examples")
    
    # Example 1 - Using popover
    col_a, col_b = st.columns(2)
    
    with col_a:
        with st.popover("📝 Example 1: Writing a Story", use_container_width=True):
            st.markdown("### Compare Prompts With and Without Context")
            
            st.markdown("""
            **Prompt 1 (No Context):** "Write a story about a dog."
            """)
            
            if st.button("Try without context", key="example1_no_context"):
                try:
                    with st.spinner("Getting response from AI..."):
                        prompt = "Write a story about a dog."
                        response = client.send_prompt(prompt)
                        st.session_state.example1_response_no_context = response['response']
                except Exception as e:
                    st.error(f"Error: {str(e)}")
            
            if "example1_response_no_context" in st.session_state and st.session_state.example1_response_no_context:
                st.markdown("### AI Response (No Context):")
                st.markdown(st.session_state.example1_response_no_context)
            
            st.markdown("---")
            
            st.markdown("""
            **Prompt 2 (With Context):** "Write a short story about a mischievous golden retriever puppy named Sunny who loves to chase squirrels in the park."
            """)
            
            if st.button("Try with context", key="example1_with_context"):
                try:
                    with st.spinner("Getting response from AI..."):
                        prompt = "Write a short story about a mischievous golden retriever puppy named Sunny who loves to chase squirrels in the park."
                        response = client.send_prompt(prompt)
                        st.session_state.example1_response_with_context = response['response']
                except Exception as e:
                    st.error(f"Error: {str(e)}")
            
            if "example1_response_with_context" in st.session_state and st.session_state.example1_response_with_context:
                st.markdown("### AI Response (With Context):")
                st.markdown(st.session_state.example1_response_with_context)
    
    with col_b:
        with st.popover("🧠 Example 2: Educational Explanation", use_container_width=True):
            st.markdown("### Compare Prompts With and Without Context")
            
            st.markdown("""
            **Prompt 1 (No Context):** "Explain photosynthesis."
            """)
            
            if st.button("Try without context", key="example2_no_context"):
                try:
                    with st.spinner("Getting response from AI..."):
                        prompt = "Explain photosynthesis."
                        response = client.send_prompt(prompt)
                        st.session_state.example2_response_no_context = response['response']
                except Exception as e:
                    st.error(f"Error: {str(e)}")
            
            if "example2_response_no_context" in st.session_state and st.session_state.example2_response_no_context:
                st.markdown("### AI Response (No Context):")
                st.markdown(st.session_state.example2_response_no_context)
            
            st.markdown("---")
            
            st.markdown("""
            **Prompt 2 (With Context):** "Explain photosynthesis in a way that is easy for 5th-grade students to understand. Use simple language and analogies."
            """)
            
            if st.button("Try with context", key="example2_with_context"):
                try:
                    with st.spinner("Getting response from AI..."):
                        prompt = "Explain photosynthesis in a way that is easy for 5th-grade students to understand. Use simple language and analogies."
                        response = client.send_prompt(prompt)
                        st.session_state.example2_response_with_context = response['response']
                except Exception as e:
                    st.error(f"Error: {str(e)}")
            
            if "example2_response_with_context" in st.session_state and st.session_state.example2_response_with_context:
                st.markdown("### AI Response (With Context):")
                st.markdown(st.session_state.example2_response_with_context)
    
    # Side-by-side comparison
    st.markdown("## Context Impact Analysis")
    
    st.markdown("""
    Notice how adding context transforms the AI's responses:
    
    | Without Context | With Context |
    |-----------------|--------------|
    | Generic information | Targeted information |
    | Standard level of detail | Appropriate level of detail for audience |
    | May include unnecessary information | Focuses on what's most relevant |
    | Default tone and style | Adjusted tone and style for purpose |
    | One-size-fits-all approach | Customized to specific needs |
    """)
    
    # Education-specific examples
    st.markdown("## Educational Examples")
    
    st.markdown("""
    Here are examples specifically relevant to educators:
    """)
    
    # Example 3
    st.markdown("### Example 3: Lesson Planning")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Basic Prompt:**
        ```
        Create a lesson plan on multiplication.
        ```
        
        **Response:**
        A generic lesson plan covering multiplication concepts, likely at a middle level of complexity, with standard activities.
        """)
    
    with col2:
        st.markdown("""
        **Context-Rich Prompt:**
        ```
        Create a 30-minute introductory lesson plan on 
        multiplication for 3rd graders who understand 
        addition but haven't been formally introduced 
        to multiplication. Include a hands-on activity 
        using manipulatives and a simple assessment.
        ```
        
        **Response:**
        An age-appropriate lesson with specific time allocation, activities tailored to beginners using concrete materials, and assessment matched to introductory skills.
        """)
    
    # Example 4
    st.markdown("### Example 4: Student Feedback")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Basic Prompt:**
        ```
        Write feedback for a student essay.
        ```
        
        **Response:**
        Generic feedback that might not match the essay's actual strengths and weaknesses or the student's needs.
        """)
    
    with col2:
        st.markdown("""
        **Context-Rich Prompt:**
        ```
        Write constructive feedback for a 9th-grade student's 
        persuasive essay that shows strong ideas but has 
        issues with paragraph organization and supporting 
        evidence. The student is preparing for a state 
        writing assessment and needs specific guidance 
        on improving structure while maintaining confidence.
        ```
        
        **Response:**
        Targeted feedback addressing specific weaknesses (organization, evidence) while acknowledging strengths (ideas), with appropriate language for a 9th grader and focused on an upcoming assessment.
        """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific guidance
    render_teacher_notes("""
    **Key Points to Emphasize:**
    
    * The specificity in the context-rich prompts gives the AI clear guidelines for generating content
    * Notice how the tone and complexity adapt based on the context provided
    * Point out how the audience information (5th-grade students, 9th-grade student) completely changes the language level
    * Highlight how adding details makes the output more engaging and relevant
    
    **Classroom Application:**
    
    These examples can be used to start a discussion about how teachers already use context in their explanations:
    - How do they adjust explanations for different grade levels?
    - What contextual information do they include when giving assignments?
    - How does providing context help students understand expectations?
    
    **Technical Note:**
    
    When using these examples in a workshop setting, consider having pre-generated responses ready to show, as live API calls may vary in their exact outputs.
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