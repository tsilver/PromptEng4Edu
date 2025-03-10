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
    page_title="Lesson 1 Reflection",
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
    "title": "Quick Start Guide: Reflection and Next Steps",
    "lesson": "1",
    "section": "reflection",
    "order": 4
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = f"lesson_{PAGE_INFO['lesson']}_{PAGE_INFO['section']}"
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
    st.title("Reflection ✨: Quick Start Guide")
    
    st.info("✏️ **Note:** Completing this reflection marks your completion of Lesson 1. Take a moment to consolidate what you've learned before moving on to the next lesson.")
    
    st.markdown("""
    Let's take a moment to reflect on what you've learned about basic prompting 
    and how you might apply these skills in your teaching practice.
    """)
    
    # If this is a reflection page, show special notice about progression
    st.warning("""
    ## 🔑 Unlock Next Lesson
    
    **Important:** Completing this reflection by saving your responses below is the key to 
    unlocking the next lesson. This reflection helps consolidate your learning and prepares 
    you for the next set of concepts.
    """)
    
    # Reflection questions
    st.markdown("## Reflect on Your Learning")
    
    reflection1 = st.text_area(
        "What is one new thing you learned about LLMs or prompting today?",
        height=100,
        key="reflection1"
    )
    
    reflection2 = st.text_area(
        "How might you see yourself using basic prompting in your daily teaching tasks?",
        height=100,
        key="reflection2"
    )
    
    reflection3 = st.text_area(
        "What is one question you still have about prompt engineering?",
        height=100,
        key="reflection3"
    )
    
    # Save reflections button - prominently displayed
    st.markdown("---")
    
    st.markdown("""
    ### 🔑 Complete Your Reflection
    
    Saving your responses below will mark this lesson as complete and unlock the next lesson.
    """)
    
    # Check if at least one field is completed
    has_content = bool(reflection1 or reflection2 or reflection3)
    
    # Calculate the next lesson path for direct navigation
    next_lesson_id = get_next_lesson_id(PAGE_INFO["lesson"])  # Should return "2"
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
    * **Prompt components matter**: Using Task, Context, and Format together creates clear, effective prompts
      
    * **Specificity improves results**: The more precise and detailed your prompt, the better the AI's response will match your needs
      
    * **Teacher skills transfer**: Your experience giving clear instructions to students is directly applicable to prompt engineering
    """)
    
    # Encouraging remark and segue
    st.markdown("---")
    st.markdown("""
    ## Great job completing the Quick Start Guide!
    
    You've taken your first steps into the world of prompt engineering. Now that you understand 
    the basics of Task, Context, and Format, we'll dive deeper into each component, starting with 
    the power of context in the next lesson.
    """)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Discussion Prompts:**
    
    * Ask participants to share their most surprising insight from this lesson
    * Discuss how the Task-Context-Format approach compares to how they currently give instructions to students
    * Invite participants to brainstorm one specific way they could use prompt engineering in their upcoming lessons
    
    **Looking Ahead:**
    
    The next lesson on Context goes deeper into one of the three components introduced here. Emphasize that:
    - Context is often the difference between generic and classroom-ready responses
    - This is a place where teachers have particular expertise (knowing students' needs, background knowledge, etc.)
    - Context can include not just educational level but cultural references, regional specifics, etc.
    
    **Assessment Check:**
    
    By now, participants should be able to:
    1. Identify the basic components of a prompt
    2. Create a simple prompt with Task, Context, and Format elements
    3. Recognize the difference between basic and well-structured prompts
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
        
        # Check if next lesson page exists
        page_path = os.path.join(current_dir, "pages", f"lesson_{next_lesson_id}_introduction.py")
        st.write(f"Lesson {next_lesson_id} Intro Exists: {os.path.exists(page_path)}")
        st.write(f"Absolute Path: {os.path.abspath(page_path)}")
        
        # Check unlocked lessons
        st.write(f"Unlocked Lessons: {st.session_state.get('unlocked_lessons', [])}")
