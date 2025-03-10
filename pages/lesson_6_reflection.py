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
    page_title="Lesson 6: Reflection",
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
    "title": "Reference Materials: Reflection and Next Steps",
    "lesson": "6",
    "section": "reflection",
    "order": 4
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_6_reflection"
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
    "lesson_6_reflection",
    "reflection",
    "Lesson 6: Reflection",
    """
    **This is where you reflect on what you've learned about using reference materials in prompts.**
    
    ✨ **Important:** Completing this reflection by saving your responses will:
    - Mark Lesson 6 as complete
    - Unlock Lesson 7
    - Save your progress in the course
    
    Take a moment to consider how you can apply reference material techniques to improve 
    the alignment and accuracy of AI outputs for your educational needs.
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
    st.markdown("## Reflection")
    
    st.info("✏️ **Note:** Completing this reflection marks your completion of Lesson 6. Take a moment to consolidate what you've learned before moving on to the next lesson.")
    
    st.markdown("""
    To conclude this lesson on reference materials in prompts, take a moment to reflect on what you've 
    learned and how you might apply it in your teaching practice.
    """)
    
    # Reflection questions
    reflection1 = st.text_area(
        "List 3-5 specific reference materials you regularly use in your teaching that could be included in prompts. For each, briefly describe how you would use it in a prompt.",
        height=150,
        key="reflection1"
    )
    
    reflection2 = st.text_area(
        "Think of a situation where using reference materials in a prompt would be particularly important for ensuring curriculum alignment or content accuracy. What reference materials would you include, and why?",
        height=100,
        key="reflection2"
    )
    
    reflection3 = st.text_area(
        "Now that you've learned about all five PCTFR elements (Persona, Context, Task, Format, Reference), write a complete PCTFR prompt for an educational resource. Then explain how the reference element specifically enhances the effectiveness of your prompt.",
        height=200,
        key="reflection3"
    )
    
    # Check if at least one field has content for validation
    has_content = any([reflection1, reflection2, reflection3])

    # Calculate the next lesson path for direct navigation
    next_lesson_id = get_next_lesson_id(PAGE_INFO["lesson"])  # Should return "7"
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
    
    # Key takeaways
    st.markdown("## Key Takeaways")
    
    st.markdown("""
    * **References ensure alignment**: Including specific curriculum materials in prompts ensures AI outputs match your teaching standards and requirements
      
    * **Extracts work better than full documents**: Selecting the most relevant portions of longer documents creates more focused and effective prompts
      
    * **Source variety matters**: Different types of reference materials (standards, textbooks, student work, etc.) serve different pedagogical purposes
      
    * **PCTFR creates comprehensive prompts**: Combining Reference Materials with Persona, Context, Task, and Format gives you complete control over AI responses
    """)
    
    # Encouraging remark and segue
    st.markdown("---")
    st.markdown("""
    ## Excellent work on mastering reference materials!
    
    You now have the skills to ensure AI outputs are perfectly aligned with your curriculum and teaching materials.
    In the next lesson, we'll explore evaluation techniques - how to assess and improve AI outputs.
    """)
    
    # Mark this page as viewed (completion is handled by save_reflection_and_navigate)
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator 
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Discussion Prompts:**
    
    * Ask participants to share the reference materials they identified in their reflection responses
    * Discuss challenges in selecting which portions of reference materials to include
    * Explore the relationship between reference materials and academic integrity/plagiarism
    
    **Looking Ahead:**
    
    In the next lesson on "Evaluation (E)," connect how reference materials and evaluation work together:
    - Reference materials provide the source content for alignment
    - Evaluation techniques help assess if the alignment was successful
    - Together they ensure outputs both incorporate proper references and meet quality standards
    
    **Assessment Opportunity:**
    
    The third reflection question provides an excellent opportunity to assess whether participants can effectively combine all five PCTFR elements in a complete prompt. Look for:
    - A well-defined persona with role, communication style, and perspective elements
    - Appropriate context for the educational situation
    - Clear task specification
    - Detailed format requirements
    - Specific, relevant reference materials
    - Thoughtful explanation of how the reference materials enhance the prompt
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