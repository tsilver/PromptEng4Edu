import os
import importlib.util
import streamlit as st
from utils.state_management import initialize_session_state, mark_page_completed
import glob
import re

def get_all_pages():
    """Get a list of all available pages in the application"""
    # Get the current directory where this file is located
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Path to the pages directory
    pages_dir = os.path.join(current_dir, 'pages')
    
    # Find all Python files in the pages directory
    page_files = glob.glob(os.path.join(pages_dir, '*.py'))
    
    # Extract just the filename without extension and path
    pages = [os.path.splitext(os.path.basename(file))[0] for file in page_files]
    
    return sorted(pages)

def get_page_by_path(path):
    """Get page info by its path."""
    pages = get_all_pages()
    for page in pages:
        if page == path:
            return page
    return None

def scroll_to_top():
    """Scroll to the top of the page"""
    st.markdown(
        """
        <script>
            window.scrollTo({top: 0, behavior: 'smooth'});
        </script>
        """,
        unsafe_allow_html=True
    )

def navigate_to(page_id):
    """Navigate to the specified page"""
    try:
        # Get the full path
        page_path = f"pages/{page_id}.py"
        
        # Switch to the page
        st.switch_page(page_path)
    except Exception as e:
        st.error(f"Failed to navigate to {page_id}: {str(e)}")
        if st.session_state.get("show_debug", False):
            st.error(f"Error details: {e.__class__.__name__}: {str(e)}")

def get_next_page(current_page):
    """
    Get the next page in the sequence based on the current page.
    Returns the page ID or None if there is no next page.
    """
    # Get all available pages
    all_pages = get_all_pages()
    
    # If the current page is the course introduction, return the first lesson
    if current_page == "course_introduction":
        for page in all_pages:
            if page.startswith("lesson_1_introduction"):
                return page
        return None
    
    # If it's a lesson page, determine the next logical page
    if current_page.startswith("lesson_"):
        parts = current_page.split("_")
        if len(parts) >= 3:
            lesson_num = int(parts[1])
            section = parts[2]
            
            # Determine the next section or lesson
            if section == "introduction":
                next_page = f"lesson_{lesson_num}_examples"
            elif section == "examples":
                next_page = f"lesson_{lesson_num}_activities"
            elif section == "activities":
                next_page = f"lesson_{lesson_num}_reflection"
            elif section == "reflection":
                # After reflection, go to the next lesson's introduction
                next_lesson = lesson_num + 1
                if next_lesson <= 17:  # Assuming there are 17 lessons
                    next_page = f"lesson_{next_lesson}_introduction"
                else:
                    # Last lesson completed, go to completion page
                    return "course_completion"
            else:
                # Unknown section, try to find next page in alphabetical order
                try:
                    idx = all_pages.index(current_page)
                    if idx < len(all_pages) - 1:
                        return all_pages[idx + 1]
                    return None
                except ValueError:
                    return None
            
            # Check if the calculated next page exists
            if next_page in all_pages:
                return next_page
            
            # If not, try to find the next available page
            for page in all_pages:
                if page > next_page:
                    return page
    
    # For any other page type or if no next page is found
    try:
        idx = all_pages.index(current_page)
        if idx < len(all_pages) - 1:
            return all_pages[idx + 1]
    except ValueError:
        pass
    
    return None

def get_prev_page(current_page):
    """
    Get the previous page in the sequence based on the current page.
    Returns the page ID or None if there is no previous page.
    """
    # Get all available pages
    all_pages = get_all_pages()
    
    # If it's the first lesson introduction, previous is course introduction
    if current_page == "lesson_1_introduction":
        return "course_introduction"
    
    # If it's a lesson page, determine the previous logical page
    if current_page.startswith("lesson_"):
        parts = current_page.split("_")
        if len(parts) >= 3:
            lesson_num = int(parts[1])
            section = parts[2]
            
            # Determine the previous section or lesson
            if section == "introduction":
                if lesson_num > 1:
                    prev_page = f"lesson_{lesson_num-1}_reflection"
                else:
                    prev_page = "course_introduction"
            elif section == "examples":
                prev_page = f"lesson_{lesson_num}_introduction"
            elif section == "activities":
                prev_page = f"lesson_{lesson_num}_examples"
            elif section == "reflection":
                prev_page = f"lesson_{lesson_num}_activities"
            else:
                # Unknown section, try to find prev page in alphabetical order
                try:
                    idx = all_pages.index(current_page)
                    if idx > 0:
                        return all_pages[idx - 1]
                    return None
                except ValueError:
                    return None
            
            # Check if the calculated previous page exists
            if prev_page in all_pages:
                return prev_page
            
            # If not, try to find the previous available page
            for page in reversed(all_pages):
                if page < current_page:
                    return page
    
    # For any other page type or if no previous page is found
    try:
        idx = all_pages.index(current_page)
        if idx > 0:
            return all_pages[idx - 1]
    except ValueError:
        pass
    
    return None
