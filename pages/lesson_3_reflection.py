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
    page_title="Lesson 3: Reflection",
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
    "title": "Defining the Task: Reflection and Next Steps",
    "lesson": "3",
    "section": "reflection",
    "order": 4
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_3_reflection"
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
    "lesson_3_reflection",
    "reflection",
    "Lesson 3: Reflection",
    """
    **This is where you reflect on what you've learned about defining tasks in prompts.**
    
    ✨ **Important:** Completing this reflection by saving your responses will:
    - Mark Lesson 3 as complete
    - Unlock Lesson 4
    - Save your progress in the course
    
    Take a moment to consider how you can apply task definition principles to improve 
    your prompts in real educational scenarios.
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
    
    st.info("✏️ **Note:** Completing this reflection marks your completion of Lesson 3. Take a moment to consolidate what you've learned before moving on to the next lesson.")
    
    st.markdown("""
    To conclude this lesson on defining tasks in prompts, take a moment to reflect on what you've 
    learned and how you might apply it in your teaching practice.
    """)
    
    # Reflection questions
    reflection1 = st.text_area(
        "How has your understanding of task definition in prompts changed after this lesson?",
        height=100,
        key="reflection1"
    )
    
    reflection2 = st.text_area(
        "Think of a prompt you've used or seen that had a vague task. How would you rewrite it now to make the task more effective?",
        height=100,
        key="reflection2"
    )
    
    reflection3 = st.text_area(
        "What are 3-5 common educational tasks where you think AI could be helpful to you? What specific action verbs would you use for each?",
        height=100,
        key="reflection3"
    )
    
    # Check if at least one field has content for validation
    has_content = any([reflection1, reflection2, reflection3])

    # Calculate the next lesson path for direct navigation
    next_lesson_id = get_next_lesson_id(PAGE_INFO["lesson"])  # Should return "4"
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
    * **Action verbs matter**: Starting your task with a clear action verb sets the direction for the AI's response
      
    * **Specificity creates clarity**: The more precise your task definition, the more targeted and useful the AI's output will be
      
    * **Parameters provide boundaries**: Including constraints like quantity, format, and audience helps shape the response to your needs
      
    * **Task and context work together**: The task defines what to do, while context (from Lesson 2) shapes how it's done
    """)
    
    # Encouraging remark and segue
    st.markdown("---")
    st.markdown("""
    ## Great job mastering task definition!
    
    You now have the skills to tell an AI exactly what you want it to do using precise, action-oriented language.
    In the next lesson, we'll explore how to specify the format of the AI's response to get outputs structured exactly how you need them.
    """)
    
    # Mark this page as viewed (completion is handled by save_reflection_and_navigate)
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator 
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Discussion Prompts:**
    
    * Ask participants to share their most valuable insight about task definition
    * Discuss how different subject areas might require different approaches to task definition
    * Have participants brainstorm a collection of effective action verbs specific to educational tasks
    
    **Looking Ahead:**
    
    In the next lesson on "Specifying Format," help participants understand the connection between task and format:
    - Task defines what the AI should do
    - Format defines how the output should be structured
    - Together they create outputs that are both relevant and immediately usable
    
    **Assessment Opportunity:**
    
    The reflection on rewriting a vague task provides a good opportunity to assess whether participants have grasped the core concepts of effective task definition. Look for:
    - Use of specific action verbs
    - Addition of parameters and constraints
    - Clarity of purpose
    - Appropriate specificity
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