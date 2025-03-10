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
    page_title="Lesson 8: Reflection",
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
    "title": "Iteration: Reflection",
    "lesson": "8",
    "section": "reflection",
    "order": 4
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_8_reflection"
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
    "lesson_8_reflection",
    "reflection",
    "Lesson 8: Reflection",
    """
    **This is where you reflect on what you've learned about iteration in prompt engineering.**
    
    ✨ **Important:** Completing this reflection by saving your responses will:
    - Mark Lesson 8 as complete
    - Unlock Lesson 9
    - Save your progress in the course
    
    Take a moment to consider how you can apply iteration techniques in your prompt engineering practice.
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
    st.markdown("## Reflection: Iteration")
    
    st.info("✏️ **Note:** Completing this reflection marks your completion of Lesson 8. Take a moment to consolidate what you've learned before moving on to the next lesson.")
    
    st.markdown("""
    To conclude this lesson on iteration in prompt engineering, reflect on what you've 
    learned and how you might apply it in your teaching practice.
    """)
    
    # Reflection questions
    reflection1 = st.text_area(
        "Describe a specific prompt you've created (or would like to create) for your teaching. What iteration strategies from this lesson would you apply to improve it, and why?",
        height=150,
        key="reflection1"
    )
    
    reflection2 = st.text_area(
        "Based on what you've learned, how do you plan to track and manage your prompt iterations in your daily practice? What system or approach would work best for you?",
        height=150,
        key="reflection2"
    )
    
    reflection3 = st.text_area(
        "Now that you've learned all components of the PTC-FREI framework, which elements do you find most valuable, and which are most challenging to implement? How might you overcome these challenges?",
        height=150,
        key="reflection3"
    )
    
    # Check if at least one field has content for validation
    has_content = any([reflection1, reflection2, reflection3])

    # Calculate the next lesson path for direct navigation
    next_lesson_id = get_next_lesson_id(PAGE_INFO["lesson"])  # Should return "9"
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
    
    # PTC-FREI Framework Summary
    st.markdown("## The Complete PTC-FREI Framework")
    
    st.markdown("""
    Congratulations! You've now learned all components of the PTC-FREI framework:
    
    - **P**ersona - The voice, role, or character the AI should adopt
    - **T**ask - The specific action or output you want from the AI
    - **C**ontext - The background information that shapes the response
    - **F**ormat - How you want the response structured or presented
    - **R**eference Materials - The specific content, standards, or sources to draw from
    - **E**valuation - How to assess the AI output against your needs
    - **I**teration - The process of systematically refining prompts
    
    Together, these elements form a comprehensive approach to prompt engineering that can:
    
    1. Generate high-quality educational content
    2. Ensure alignment with curriculum and standards
    3. Produce consistently useful outputs
    4. Save time by reducing the need for extensive editing
    5. Create reusable prompt templates for ongoing use
    
    In the next set of lessons, we'll explore advanced prompting techniques that build on this foundation.
    """)
    
    # Key takeaways
    st.markdown("## Key Takeaways")
    
    st.markdown("""
    * **Iteration is integral to the process**: Effective prompt engineering involves cycles of refinement
      
    * **Systematic changes work best**: Making targeted, purposeful changes helps identify what works
      
    * **Documentation matters**: Tracking iterations creates valuable reference for future prompting
      
    * **Both addition and subtraction are valuable**: Sometimes removing elements improves results
      
    * **The complete framework produces optimal results**: Incorporating all PTC-FREI elements 
      leads to the most effective prompts
    """)
    
    # Encouraging remark and segue
    st.markdown("---")
    st.markdown("""
    ## Congratulations on completing the PTC-FREI framework!
    
    You now have a complete toolkit for creating effective educational prompts. In the next lesson,
    we'll begin exploring advanced prompting techniques, starting with Zero-Shot Prompting.
    These techniques will build on the fundamental framework you've mastered.
    """)
    
    # Mark this page as viewed (completion is handled by save_reflection_and_navigate)
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator 
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Discussion Prompts:**
    
    * Ask participants to share their most valuable insight about the iteration process
    * Discuss how the PCTFREI framework might be adapted for different educational contexts
    * Explore how iteration practices might be taught to students for their own AI interactions
    
    **Looking Ahead:**
    
    In the next set of lessons, we'll shift focus from the PCTFREI framework to specific prompting techniques:
    - Lesson 9: Zero-Shot Prompting
    - Lesson 10: Few-Shot Prompting
    - Lesson 11: Chain-of-Thought Prompting
    - Lesson 12: Role Prompting
    
    These techniques complement the PCTFREI framework and provide additional strategies for specific situations.
    
    **Assessment Opportunity:**
    
    The reflection questions provide insight into how participants are integrating the framework into their practice. Look for:
    - Specific applications to their teaching context
    - Thoughtful approaches to managing iterations
    - Metacognitive awareness of their strengths and challenges with the framework
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