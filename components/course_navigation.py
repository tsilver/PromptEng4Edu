import streamlit as st
import os
import re
from utils.state_management import get_progress_percentage

def render_course_navigation(all_pages, current_page, current_dir):
    """
    Render the course navigation in the right column.
    
    Parameters:
    - all_pages: List of available page filenames
    - current_page: Currently active page
    - current_dir: Root directory of the application
    """
    # Progress indicator at the top for better visibility
    render_progress_indicator()
    
    # Lessons section - now includes Course Introduction as "Lesson 0"
    st.markdown("### Course Content")
    
    # Course Introduction with consistent styling
    render_course_as_lesson(current_page)
    
    # Regular lessons
    lessons_dict = extract_lesson_info(all_pages, current_dir)
    render_lesson_buttons(lessons_dict, current_page)
    
    # Debug info for lesson detection
    if st.session_state.get("show_debug", False):
        st.markdown("---")
        st.markdown("#### Detected Lessons")
        for num, lesson in sorted(lessons_dict.items()):
            st.markdown(f"- **{lesson['title']}**")

def render_course_as_lesson(current_page):
    """Render course introduction as Lesson 0 with the same styling as regular lessons."""
    # Check if any course page is current
    is_course_current = current_page == "app" or current_page.startswith("course_")
    
    # Check if course is completed (simple check if course_reflection is completed)
    is_completed = "course_reflection" in st.session_state.get("completed_pages", set())
    
    # Choose icon based on status
    if is_completed:
        icon = "✅ "
    elif is_course_current:
        icon = "🔶 "
    else:
        icon = "📝 "
    
    button_type = "primary" if is_course_current else "secondary"
    
    # Render course introduction as a lesson
    if st.button(f"{icon} Course Introduction", 
                key="nav_course_intro", 
                use_container_width=True,
                type=button_type):
        try:
            st.switch_page("pages/course_introduction.py")
        except Exception as e:
            st.error(f"Navigation error: {str(e)}")

def render_course_intro_buttons(current_page):
    """Render buttons for the course introduction section."""
    # Define course pages
    course_pages = [
        ("course_introduction", "📘 Introduction"),
        ("course_examples", "🔍 Examples"),
        ("course_activities", "🎯 Activities"),
        ("course_reflection", "💭 Reflection")
    ]
    
    # Render buttons for each section
    for page_id, label in course_pages:
        # Check if this is the current page
        is_current = current_page == page_id or (current_page == "app" and page_id == "course_introduction")
        button_type = "primary" if is_current else "secondary"
        
        if st.button(label, key=f"nav_{page_id}", use_container_width=True, type=button_type):
            try:
                st.switch_page(f"pages/{page_id}.py")
            except Exception as e:
                st.error(f"Navigation error: {str(e)}")

def extract_lesson_info(all_pages, current_dir):
    """
    Extract lesson information including titles from markdown files.
    
    Returns a dictionary where keys are lesson numbers and values are 
    dictionaries with 'title' and 'page' keys.
    """
    lessons = {}
    
    # First pass: collect all lesson numbers from page filenames
    for page in all_pages:
        if page.startswith("lesson_"):
            parts = page.split("_")
            if len(parts) >= 3:
                lesson_num = parts[1]
                section = parts[2]
                
                # Initialize lesson entry if it doesn't exist
                if lesson_num not in lessons:
                    lessons[lesson_num] = {
                        "title": f"Lesson {lesson_num}",
                        "page": f"lesson_{lesson_num}_introduction",
                        "sections": []
                    }
                
                # Track available sections
                if section not in lessons[lesson_num]["sections"]:
                    lessons[lesson_num]["sections"].append(section)
    
    # Second pass: try to get descriptive titles from markdown files
    for lesson_num in lessons:
        # Get a more descriptive title from the Lessons directory if available
        lesson_md_path = os.path.join(current_dir, "Lessons", f"Lesson {lesson_num}.md")
        if os.path.exists(lesson_md_path):
            try:
                with open(lesson_md_path, 'r') as f:
                    content = f.read()
                    # Extract lesson title from the first line that looks like "**Lesson X: Title**"
                    title_match = re.search(r'\*\*Lesson\s+\d+\s*:\s*([^\*]+)\*\*', content)
                    if title_match:
                        lessons[lesson_num]["title"] = f"Lesson {lesson_num}: {title_match.group(1).strip()}"
            except Exception:
                pass  # If can't read file, just use the default title
    
    return lessons

def render_lesson_buttons(lessons_dict, current_page):
    """Render buttons for each lesson."""
    # Sort lessons by number
    try:
        sorted_lessons = sorted(lessons_dict.keys(), key=lambda x: int(x))
    except ValueError:
        sorted_lessons = sorted(lessons_dict.keys())
    
    # Render lesson buttons
    for lesson_num in sorted_lessons:
        lesson = lessons_dict[lesson_num]
        lesson_page = lesson["page"]
        is_lesson_current = current_page.startswith(f"lesson_{lesson_num}_")
        
        # Check if lesson is completed
        is_completed = False
        reflection_page = f"lesson_{lesson_num}_reflection"
        if reflection_page in st.session_state.get("completed_pages", set()):
            is_completed = True
        
        # Choose icon based on status
        if is_completed:
            icon = "✅ "
        elif is_lesson_current:
            icon = "🔶 "
        else:
            icon = "📝 "
        
        button_type = "primary" if is_lesson_current else "secondary"
        
        # Use the descriptive title
        if st.button(f"{icon} {lesson['title']}", 
                    key=f"nav_lesson_{lesson_num}", 
                    use_container_width=True,
                    type=button_type):
            try:
                # Navigate to the lesson introduction page
                st.switch_page(f"pages/{lesson_page}.py")
            except Exception as e:
                st.error(f"Navigation error: {str(e)}")

def render_progress_indicator():
    """Render the progress indicator."""
    st.markdown("### Course Progress")
    progress = get_progress_percentage()
    st.progress(progress / 100)
    st.markdown(f"**{progress}% Complete**")
