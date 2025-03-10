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
    page_title="Lesson 4: Reflection",
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
    "title": "Specifying Format: Reflection and Next Steps",
    "lesson": "4",
    "section": "reflection",
    "order": 4
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_4_reflection"
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
    "lesson_4_reflection",
    "reflection",
    "Lesson 4: Reflection",
    """
    **This is where you reflect on what you've learned about specifying formats in prompts.**
    
    ✨ **Important:** Completing this reflection by saving your responses will:
    - Mark Lesson 4 as complete
    - Unlock Lesson 5
    - Save your progress in the course
    
    Take a moment to consider how you can apply format specification principles to improve 
    the usability of AI outputs for your educational needs.
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
    
    st.info("✏️ **Note:** Completing this reflection marks your completion of Lesson 4. Take a moment to consolidate what you've learned before moving on to the next lesson.")
    
    st.markdown("""
    To conclude this lesson on specifying format in prompts, take a moment to reflect on what you've 
    learned and how you might apply it in your teaching practice.
    """)
    
    # Reflection questions
    reflection1 = st.text_area(
        "What are three formats you commonly use in your teaching materials, and how could you specify these formats in prompts to an AI?",
        height=100,
        key="reflection1"
    )
    
    reflection2 = st.text_area(
        "Think of a recent situation where you created teaching materials. How might adding specific format instructions to an AI prompt have saved you time or improved the output?",
        height=100,
        key="reflection2"
    )
    
    reflection3 = st.text_area(
        "Now that you've learned about Context (C), Task (T), and Format (F), write a complete CTF prompt for a resource you could use in your teaching. How does each component contribute to the effectiveness of the prompt?",
        height=150,
        key="reflection3"
    )
    
    # Check if at least one field has content for validation
    has_content = any([reflection1, reflection2, reflection3])

    # Calculate the next lesson path for direct navigation
    next_lesson_id = get_next_lesson_id(PAGE_INFO["lesson"])  # Should return "5"
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
    * **Format makes content usable**: Specifying format turns raw information into ready-to-use resources
      
    * **Structure supports function**: The right format enhances understanding and application of the content
      
    * **CTF creates powerful prompts**: Combining Context, Task, and Format creates highly targeted, useful AI outputs
      
    * **Format is about organization**: Good format specifications organize information in ways that support specific educational goals
    """)
    
    # Encouraging remark and segue
    st.markdown("---")
    st.markdown("""
    ## Excellent work on mastering format specification!
    
    You now have the skills to ensure AI outputs are structured exactly as you need them, saving you time and effort.
    In the next lesson, we'll explore persona engineering - how to define roles for the AI to enhance response quality.
    """)
    
    # Mark this page as viewed (completion is handled by save_reflection_and_navigate)
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator 
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Discussion Prompts:**
    
    * Ask participants to share their favorite format specifications from their reflections
    * Discuss the relationship between educational purpose and format selection
    * Have participants identify formats that are specific to their subject areas
    
    **Looking Ahead:**
    
    In the next lesson on "Persona Engineering (P)," connect how format and persona work together:
    - Format defines how the output is structured
    - Persona defines the voice, style, and expertise level
    - Together they create outputs that are not just well-organized, but communicate in appropriate ways
    
    **Assessment Opportunity:**
    
    The third reflection question provides an excellent opportunity to assess whether participants can effectively combine Context, Task, and Format in a complete prompt. Look for:
    - Clear context that includes relevant background
    - Specific task with action verbs
    - Detailed format specifications
    - Logical connections between all three components
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