import streamlit as st
import os
import json

def get_all_pages():
    """Get all available pages from the pages directory."""
    # Import locally to avoid circular imports
    import os
    import glob
    
    pages = []
    pattern = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'pages', '*.py')
    for file in glob.glob(pattern):
        # Extract the filename without extension
        filename = os.path.basename(file)[:-3]
        # Skip __init__.py and other special files
        if not filename.startswith('__'):
            pages.append(filename)
    return sorted(pages)

def initialize_session_state():
    """Initialize all required session state variables if they don't exist"""
    
    # Initialize navigation state
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "course_introduction"
    
    # Initialize completed pages tracking
    if 'completed_pages' not in st.session_state:
        st.session_state.completed_pages = set()
    
    # Initialize teacher mode toggle
    if 'show_teacher_content' not in st.session_state:
        st.session_state.show_teacher_content = False
    
    # Initialize debug mode toggle
    if 'show_debug' not in st.session_state:
        st.session_state.show_debug = False
    
    # Initialize content state for various activities
    if 'activity_responses' not in st.session_state:
        st.session_state.activity_responses = {}
    
    # Initialize reflection responses
    if 'reflections' not in st.session_state:
        st.session_state.reflections = {}
    
    # Initialize prompt test results
    if 'prompt_tests' not in st.session_state:
        st.session_state.prompt_tests = {}

def mark_page_completed(page_id):
    """Mark a page as completed for progress tracking"""
    if 'completed_pages' not in st.session_state:
        st.session_state.completed_pages = set()
    
    st.session_state.completed_pages.add(page_id)
    
    # Save to persistent storage if available
    save_progress()

def mark_all_previous_completed(current_page):
    """
    Mark all pages before the current one as completed.
    Used when a user jumps ahead in the course.
    """
    if current_page.startswith("lesson_"):
        parts = current_page.split("_")
        if len(parts) >= 3:
            current_lesson = int(parts[1])
            current_section = parts[2]
            
            # Get section order
            section_order = {"introduction": 1, "examples": 2, "activities": 3, "reflection": 4}
            current_section_order = section_order.get(current_section, 0)
            
            # Mark all previous lessons as completed
            for lesson in range(1, current_lesson):
                for section in ["introduction", "examples", "activities", "reflection"]:
                    page_id = f"lesson_{lesson}_{section}"
                    mark_page_completed(page_id)
            
            # Mark all previous sections in current lesson
            for section, order in section_order.items():
                if order < current_section_order:
                    page_id = f"lesson_{current_lesson}_{section}"
                    mark_page_completed(page_id)

def get_progress_percentage():
    """Calculate the course completion percentage"""
    if 'completed_pages' not in st.session_state:
        return 0
    
    # Total number of pages in the course (17 lessons * 4 sections)
    total_pages = 17 * 4
    
    # Count relevant completed pages (lesson_*_*)
    completed_count = sum(1 for page in st.session_state.completed_pages 
                         if page.startswith("lesson_") and len(page.split("_")) >= 3)
    
    # Calculate percentage
    if total_pages > 0:
        return int((completed_count / total_pages) * 100)
    return 0

def save_progress():
    """Save progress to a file for persistence"""
    # This is a placeholder - in a real app, you would save to a database
    # or a file on the server. For this example, we'll just print.
    
    # Convert set to list for JSON serialization
    progress_data = {
        "completed_pages": list(st.session_state.completed_pages),
        "reflections": st.session_state.reflections,
        "activity_responses": st.session_state.activity_responses
    }
    
    # Print for demonstration
    if st.session_state.get("show_debug", False):
        st.sidebar.write("Progress data saved:")
        st.sidebar.json(progress_data)

def load_progress():
    """Load progress from persistent storage"""
    # This is a placeholder - in a real app, you would load from a database
    # or a file on the server.
    pass
