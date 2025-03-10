import streamlit as st
import os
import sys
from utils.navigation import scroll_to_top
from utils.state_management import initialize_session_state, mark_page_completed
from components.breadcrumb_navigator import render_breadcrumb
from components.bottom_navigator import render_bottom_navigator
from components.course_navigation import render_course_navigation
from components.top_navigator import render_top_navigator
from components.teacher_notes import render_teacher_notes
from components.progress_manager import save_reflection_and_navigate, get_next_lesson_id, get_next_lesson_path

# Configure page
st.set_page_config(
    page_title="Course Reflection",
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
    "title": "Course Reflection",
    "lesson": "intro",
    "section": "reflection",
    "order": 3
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "course_reflection"
st.session_state.current_page = current_page

# Get all available pages for navigation
try:
    from utils.navigation import get_all_pages
    all_pages = get_all_pages()
except Exception as e:
    st.error(f"Error loading pages: {str(e)}")
    all_pages = []

# Scroll to top when page loads
scroll_to_top()

# Render teacher controls in the sidebar
st.sidebar.title("Teacher Controls")
st.sidebar.markdown("---")

# Teacher/Student toggle
st.sidebar.checkbox(
    "Show Teacher Content",
    value=st.session_state.show_teacher_content,
    key="toggle_teacher_content"
)

# Debug toggle in sidebar - Note the unique key
debug_key = f"toggle_debug_{PAGE_INFO['lesson']}_{PAGE_INFO['section']}"
st.sidebar.checkbox(
    "Show Debug Info",
    value=st.session_state.get("show_debug", False),
    key=debug_key
)

# Create main layout with content on the left and navigation on the right
content_col, nav_col = st.columns([4, 1])

# Render the main content area
with content_col:
    # Render breadcrumb navigation at the top
    render_breadcrumb(current_page)
    
    # Render section navigation at the top
    render_top_navigator(PAGE_INFO["lesson"], PAGE_INFO["section"])
    
    # Main content
    st.title("Course Reflection ✨")
    
    st.markdown("""
    Before beginning the lessons, take a moment to reflect on your expectations and goals
    for this course. This reflection will help you get the most out of your learning journey.
    """)
    
    # Course progression highlight
    st.warning("""
    ## 🔑 Unlock Lesson 1
    
    **Important:** Completing this reflection by saving your responses below is the key to 
    unlocking Lesson 1. This process will be the same for all lessons - completing each 
    lesson's reflection section will unlock the next lesson.
    """)
    
    # Current experience section - simplified
    st.markdown("## Your Current Experience")
    
    experience = st.radio(
        "How would you describe your current experience with AI tools?",
        [
            "Novice - Just starting to explore AI tools",
            "Beginner - Have used AI tools a few times",
            "Intermediate - Use AI tools regularly",
            "Advanced - Experienced with AI tools"
        ],
        key="experience_level"
    )
    
    current_usage = st.text_area(
        "How do you currently use AI in your work?",
        height=80,
        placeholder="e.g., Generating ideas, creating materials, research assistance...",
        key="current_usage"
    )
    
    # Course goals section - simplified
    st.markdown("## Your Learning Goals")
    
    primary_goal = st.text_area(
        "What is your primary goal for taking this course?",
        height=80,
        key="primary_goal"
    )
    
    success_measure = st.text_area(
        "How will you know if this course has been successful for you?",
        height=80,
        key="success_measure"
    )
    
    # Save reflections button - prominently displayed
    st.markdown("---")
    
    st.markdown("""
    ### 🔑 Complete Your Reflection
    
    Saving your responses below will mark the introduction as complete and unlock Lesson 1.
    """)
    
    # Check if at least one field is completed
    has_content = bool(current_usage or primary_goal)
    
    # Calculate the next lesson path for direct navigation
    next_lesson_id = get_next_lesson_id(PAGE_INFO["lesson"])  # Should return "1"
    next_lesson_path = get_next_lesson_path(next_lesson_id)

    # If already completed, show the next lesson button
    already_completed = current_page in st.session_state.get("completed_pages", [])
    if already_completed:
        st.success("🎉 You've already completed this reflection. Lesson 1 is unlocked!")
        if st.button("Begin Lesson 1 →", key="begin_lesson1_done", type="primary", use_container_width=True):
            try:
                st.switch_page(next_lesson_path)
            except Exception as e:
                st.error(f"Error navigating to Lesson 1: {str(e)}")
                st.error(f"Path tried: {next_lesson_path}")
    else:
        # Save and navigate button with validation
        if st.button("Save Reflections & Unlock Lesson 1", key="save_reflections", 
                    type="primary", use_container_width=True, disabled=not has_content):
            if has_content:
                # Prepare reflection data
                reflection_data = {
                    "experience_level": experience,
                    "current_usage": current_usage,
                    "primary_goal": primary_goal,
                    "success_measure": success_measure
                }
                
                # Save reflection and navigate directly to next lesson
                save_reflection_and_navigate(PAGE_INFO["lesson"], reflection_data)
            else:
                st.warning("Please fill in at least one of the reflection fields.")
    
    # Add bottom navigator - mirrors the top navigator
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Facilitation Notes:**
    
    * This simplified reflection focuses on establishing a baseline of participant experience
      and setting clear learning goals
    * The reflection is intentionally brief as it comes early in the course
    * Emphasize that this pattern of completing reflections to unlock new content will continue
      throughout the course
    
    **Key Points to Emphasize:**
    
    * Reflections are an important part of the learning process, not just a procedural step
    * Setting clear goals at the beginning helps learners measure their progress
    * The reflection data can be valuable for course facilitators to understand learner needs
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
        st.write(f"Next Lesson Path: {next_lesson_path}")
        st.write(f"Already Completed: {already_completed}")
        st.write(f"Has Content: {has_content}")
        st.write(f"Session State: {dict(st.session_state)}")
        st.write(f"Completed Pages: {st.session_state.get('completed_pages', [])}")
        st.write(f"Path Check: {'pages/lesson_1_introduction.py' in all_pages}")
        
        # Check if specific page exists
        page_path = os.path.join(current_dir, "pages", "lesson_1_introduction.py")
        st.write(f"Lesson 1 Intro Exists: {os.path.exists(page_path)}")
        st.write(f"Absolute Path: {os.path.abspath(page_path)}")
        
        # Check unlocked lessons
        st.write(f"Unlocked Lessons: {st.session_state.get('unlocked_lessons', [])}") 