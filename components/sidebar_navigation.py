import streamlit as st
from utils.state_management import initialize_session_state, get_progress_percentage
import os
import traceback

def render_sidebar(all_pages, current_page):
    """
    Render a simplified sidebar navigation showing only lesson entries.
    
    Parameters:
    - all_pages: List of page filenames (strings)
    - current_page: Currently active page filename (string)
    """
    initialize_session_state()
    
    st.sidebar.title("Course Navigation")
    
    # Group pages by lesson
    lessons = {}
    
    # Add course intro
    intro_page = "course_introduction"
    if intro_page in all_pages:
        lessons["intro"] = {
            "title": "Welcome to the Course",
            "default_page": intro_page
        }
    
    # Group lesson pages
    for page in all_pages:
        # Extract lesson info from page filename (e.g., "lesson_1_introduction" → Lesson 1)
        if page.startswith("lesson_"):
            parts = page.split("_")
            if len(parts) >= 3:
                lesson_num = parts[1]
                section = parts[2]
                
                if lesson_num not in lessons:
                    lessons[lesson_num] = {
                        "title": f"Lesson {lesson_num}",
                        "default_page": f"lesson_{lesson_num}_introduction",
                        "pages": []
                    }
                
                lessons[lesson_num]["pages"].append(page)
                
                # Store last visited page for this lesson if it matches current
                if page == current_page:
                    st.session_state[f"last_page_lesson_{lesson_num}"] = page
    
    # Use a custom sort that places "intro" first and handles numeric sort correctly
    def lesson_sort_key(x):
        if x == "intro":
            return (0, 0)  # (sort group, sort value) - "intro" goes first (group 0)
        try:
            return (1, int(x))  # Regular lessons go in group 1, sorted by number
        except ValueError:
            return (2, x)  # Non-numeric lessons go last (group 2)
    
    sorted_lesson_keys = sorted(lessons.keys(), key=lesson_sort_key)
    
    # Determine current lesson
    current_lesson = None
    if current_page == "course_introduction":
        current_lesson = "intro"
    elif current_page.startswith("lesson_"):
        parts = current_page.split("_")
        if len(parts) >= 3:
            current_lesson = parts[1]
    
    # Render simplified sidebar with just lesson entries
    for lesson_key in sorted_lesson_keys:
        lesson = lessons[lesson_key]
        
        is_current = lesson_key == current_lesson
        is_completed = False  # Could be improved to check if all pages in lesson are completed
        
        # Add icon based on status
        if is_completed:
            icon = "✅ "
        elif is_current:
            icon = "🔶 "
        else:
            icon = "📘 "
        
        # Create button for each lesson
        if st.sidebar.button(
            f"{icon} {lesson['title']}",
            key=f"nav_lesson_{lesson_key}",
            use_container_width=True,
            type="primary" if is_current else "secondary"
        ):
            # Determine which page to navigate to
            target_page = None
            
            # If we have a stored last page for this lesson, use it
            last_page_key = f"last_page_lesson_{lesson_key}"
            if last_page_key in st.session_state:
                target_page = st.session_state[last_page_key]
            # Otherwise use the default page (introduction)
            else:
                target_page = lesson.get("default_page")
            
            # Navigate using st.switch_page
            if target_page:
                try:
                    # Get the current working directory
                    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                    # Get the full path to the page file
                    page_path = os.path.join(current_dir, "pages", f"{target_page}.py")
                    
                    # Check if file exists before attempting to switch
                    if os.path.exists(page_path):
                        st.switch_page(page_path)
                    else:
                        error_msg = f"Page file not found: {page_path}"
                        st.sidebar.error(error_msg)
                        
                        # In debug mode, show more information
                        if st.session_state.get("show_debug", False):
                            st.sidebar.write(f"Target page: {target_page}")
                            st.sidebar.write(f"Current directory: {current_dir}")
                            
                            # List files in the pages directory
                            pages_dir = os.path.join(current_dir, "pages")
                            if os.path.exists(pages_dir):
                                st.sidebar.write("Files in pages directory:")
                                st.sidebar.write(os.listdir(pages_dir))
                except Exception as e:
                    st.sidebar.error(f"Failed to navigate to {target_page}: {str(e)}")
                    if st.session_state.get("show_debug", False):
                        st.sidebar.error(traceback.format_exc())
    
    # Progress indicator
    st.sidebar.markdown("---")
    progress = get_progress_percentage()
    st.sidebar.progress(progress / 100)
    st.sidebar.markdown(f"**Course Progress:** {progress}%")
    
    # Teacher/Student toggle
    st.sidebar.markdown("---")
    st.sidebar.checkbox(
        "Show Teacher Content",
        value=st.session_state.show_teacher_content,
        key="toggle_teacher_content"
    )
    
    # Debug toggle
    if "show_debug" in st.session_state:
        st.sidebar.checkbox(
            "Show Debug Info",
            value=st.session_state.show_debug,
            key="toggle_debug_info"
        )
