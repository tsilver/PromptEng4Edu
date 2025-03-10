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
from components.progress_manager import render_teacher_controls_sidebar, save_reflection_and_navigate, get_next_lesson_id, get_next_lesson_path

# Configure page
st.set_page_config(
    page_title="Lesson 7: Reflection",
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
    "title": "Evaluation: Reflection",
    "lesson": "7",
    "section": "reflection",
    "order": 4
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_7_reflection"
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
    "lesson_7_reflection",
    "reflection",
    "Lesson 7: Reflection",
    """
    **This is where you reflect on what you've learned about evaluating AI outputs.**
    
    ✨ **Important:** Completing this reflection by saving your responses will:
    - Mark Lesson 7 as complete
    - Unlock Lesson 8
    - Save your progress in the course
    
    Take a moment to consider how you can apply evaluation techniques to improve
    your prompt engineering practice.
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
    st.markdown("## Reflection: Evaluation")
    
    st.info("✏️ **Note:** Completing this reflection marks your completion of Lesson 7. Take a moment to consolidate what you've learned before moving on to the next lesson.")
    
    st.markdown("""
    To conclude this lesson on evaluation in prompt engineering, reflect on what you've 
    learned and how you might apply it in your teaching practice.
    """)
    
    # Reflection questions
    reflection1 = st.text_area(
        "Based on what you've learned, what are 3-5 key criteria you would include in an evaluation rubric for AI-generated content in your specific teaching context? Explain why each criterion is important.",
        height=150,
        key="reflection1"
    )
    
    reflection2 = st.text_area(
        "Describe a specific AI output (lesson plan, assessment, activity, etc.) that you recently created or would like to create. How would you evaluate its effectiveness using the approaches from this lesson?",
        height=150,
        key="reflection2"
    )
    
    reflection3 = st.text_area(
        "How might you involve students in evaluating AI-generated content? What benefits could this provide for developing their critical thinking and digital literacy skills?",
        height=120,
        key="reflection3"
    )
    
    # Check if at least one field has content for validation
    has_content = any([reflection1, reflection2, reflection3])

    # Calculate the next lesson path for direct navigation
    next_lesson_id = get_next_lesson_id(PAGE_INFO["lesson"])  # Should return "8"
    next_lesson_path = get_next_lesson_path(next_lesson_id)

    # If already completed, show the next lesson button
    already_completed = current_page in st.session_state.get("completed_pages", [])
    if already_completed:
        st.success(f"🎉 You've already completed this reflection. Lesson {next_lesson_id} is unlocked!")
        if st.button(f"Begin Lesson {next_lesson_id} →", key="begin_next_lesson_done", type="primary", use_container_width=True):
            try:
                st.switch_page(next_lesson_path)
            except Exception as e:
                st.error(f"Error navigating to Lesson {next_lesson_id}: {str(e)}")
                st.error(f"Path tried: {next_lesson_path}")
    else:
        # Save and navigate button with validation
        if st.button("Save Reflections & Unlock Next Lesson", key="save_reflections", 
                    type="primary", use_container_width=True, disabled=not has_content):
            if has_content:
                # Prepare reflection data
                reflection_data = {
                    "reflection1": reflection1,
                    "reflection2": reflection2,
                    "reflection3": reflection3
                }
                
                # Save reflection and navigate directly to next lesson
                save_reflection_and_navigate(PAGE_INFO["lesson"], reflection_data)
            else:
                st.warning("Please fill in at least one of the reflection fields.")
    
    # Connection to the PTC-FREI Framework
    st.markdown("## Evaluation in the PTC-FREI Framework")
    
    st.markdown("""
    Let's review what we've learned about the PTC-FREI framework so far:
    
    - **P**ersona - The voice and perspective the AI should adopt
    - **T**ask - The specific action you want the AI to perform
    - **C**ontext - The background information that shapes understanding
    - **F**ormat - How you want the response structured
    - **R**eference Materials - The specific content to draw from
    - **E**valuation - How to assess and improve AI outputs
    
    Evaluation is crucial because it helps you:
    1. Determine if the AI output meets your educational standards
    2. Identify specific areas for improvement
    3. Develop better prompts through iterative refinement
    4. Establish quality control for AI-generated educational content
    
    In the next lesson, we'll explore Iteration (I) - how to systematically improve 
    your prompts based on evaluation results.
    """)
    
    # Key takeaways
    st.markdown("## Key Takeaways")
    
    st.markdown("""
    * **Structured evaluation matters**: Using consistent criteria helps assess AI outputs objectively
      
    * **Evaluation drives improvement**: Specific feedback leads to better prompts and outputs
      
    * **Context-specific criteria**: Different educational contexts require different evaluation approaches
      
    * **The ACRE framework provides a starting point**: Accuracy, Curriculum Alignment, Readability, and Engagement
      
    * **Evaluation is iterative**: As your prompting skills improve, your evaluation criteria may evolve
    """)
    
    # Encouraging remark and segue
    st.markdown("---")
    st.markdown("""
    ## Well done on mastering evaluation techniques!
    
    You now have the skills to systematically assess AI-generated content for educational use.
    In the next lesson, we'll explore iteration techniques - how to use evaluation results to 
    systematically improve your prompts over time.
    """)
    
    # Mark this page as viewed (completion is handled by save_reflection_and_navigate)
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator 
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Discussion Prompts:**
    
    * Ask participants to share their most important evaluation criteria from their reflections
    * Discuss how different subject areas might require different evaluation approaches
    * Explore how evaluation practices might evolve as AI capabilities advance
    
    **Looking Ahead:**
    
    In the next lesson on "Iteration (I)," connect how evaluation and iteration work together:
    - Evaluation identifies areas for improvement
    - Iteration applies those insights to create better prompts
    - Together they create a continuous improvement cycle
    
    **Assessment Opportunity:**
    
    The reflection questions provide insight into how participants are applying evaluation concepts to their specific teaching contexts. Look for:
    - Thoughtful selection of evaluation criteria relevant to their teaching area
    - Specific applications to their own AI content creation needs
    - Creative approaches to involving students in evaluation
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
        st.write(f"Next Lesson ID: {next_lesson_id}")
        st.write(f"Next Lesson Path: {next_lesson_path}")
        st.write(f"Already Completed: {already_completed}") 