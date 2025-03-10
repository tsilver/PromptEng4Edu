import streamlit as st
import os
from utils.navigation import get_next_page, get_prev_page

def render_lesson_navigator(page_info):
    """
    Render a compact lesson navigation component for the sidebar.
    
    Parameters:
    - page_info: Dictionary with page metadata including:
        - title: Page title
        - lesson: Lesson number (as string)
        - section: Section type (introduction, examples, activities, reflection)
        - order: Order within the section (usually 1-4)
    """
    # Get lesson number and section
    lesson_num = page_info.get("lesson", "")
    section = page_info.get("section", "")
    
    # Skip rendering for intro page
    if lesson_num == "intro":
        return
    
    st.sidebar.markdown("### Explore This Lesson")
    
    # Generate page IDs for each section
    if lesson_num:
        intro_page = f"lesson_{lesson_num}_introduction" 
        examples_page = f"lesson_{lesson_num}_examples"
        activities_page = f"lesson_{lesson_num}_activities"
        reflection_page = f"lesson_{lesson_num}_reflection"
        
        # Get current page
        current_page = f"lesson_{lesson_num}_{section}"
        
        # Create a button for each section
        if st.sidebar.button(
            "🌟 Introduction", 
            key=f"nav_intro_{lesson_num}",
            use_container_width=True,
            type="primary" if section == "introduction" else "secondary"
        ):
            # Store the current page as the last visited page for this lesson
            st.session_state[f"last_page_lesson_{lesson_num}"] = current_page
            
            # Navigate using st.switch_page
            try:
                page_path = os.path.join("pages", f"{intro_page}.py")
                st.switch_page(page_path)
            except Exception as e:
                st.error(f"Failed to navigate to Introduction: {str(e)}")
            
        if st.sidebar.button(
            "🔍 Examples", 
            key=f"nav_examples_{lesson_num}",
            use_container_width=True,
            type="primary" if section == "examples" else "secondary"
        ):
            # Store the current page as the last visited page for this lesson
            st.session_state[f"last_page_lesson_{lesson_num}"] = current_page
            
            # Navigate using st.switch_page
            try:
                page_path = os.path.join("pages", f"{examples_page}.py")
                st.switch_page(page_path)
            except Exception as e:
                st.error(f"Failed to navigate to Examples: {str(e)}")
            
        if st.sidebar.button(
            "🎯 Activities", 
            key=f"nav_activities_{lesson_num}",
            use_container_width=True,
            type="primary" if section == "activities" else "secondary"
        ):
            # Store the current page as the last visited page for this lesson
            st.session_state[f"last_page_lesson_{lesson_num}"] = current_page
            
            # Navigate using st.switch_page
            try:
                page_path = os.path.join("pages", f"{activities_page}.py")
                st.switch_page(page_path)
            except Exception as e:
                st.error(f"Failed to navigate to Activities: {str(e)}")
            
        if st.sidebar.button(
            "💭 Reflection", 
            key=f"nav_reflection_{lesson_num}",
            use_container_width=True,
            type="primary" if section == "reflection" else "secondary"
        ):
            # Store the current page as the last visited page for this lesson
            st.session_state[f"last_page_lesson_{lesson_num}"] = current_page
            
            # Navigate using st.switch_page
            try:
                page_path = os.path.join("pages", f"{reflection_page}.py")
                st.switch_page(page_path)
            except Exception as e:
                st.error(f"Failed to navigate to Reflection: {str(e)}")
        
        # Lesson navigation
        st.sidebar.markdown("---")
        
        # Calculate next and previous pages
        prev_page = get_prev_page(current_page)
        next_page = get_next_page(current_page)
        
        # Previous lesson button (if available)
        if prev_page and prev_page.startswith("lesson_"):
            prev_parts = prev_page.split("_")
            if len(prev_parts) >= 3:
                prev_lesson = prev_parts[1]
                if prev_parts[2] == "reflection":
                    # If previous page is a reflection, it's the end of the previous lesson
                    button_text = f"← Lesson {prev_lesson}"
                else:
                    button_text = f"← Previous Page"
                
                if st.sidebar.button(
                    button_text,
                    key=f"nav_prev_{lesson_num}",
                    use_container_width=True
                ):
                    # Store the current page as the last visited page for this lesson
                    st.session_state[f"last_page_lesson_{lesson_num}"] = current_page
                    
                    # Navigate using st.switch_page
                    try:
                        page_path = os.path.join("pages", f"{prev_page}.py")
                        st.switch_page(page_path)
                    except Exception as e:
                        st.error(f"Failed to navigate to previous page: {str(e)}")
        
        # Next lesson button (if available)
        if next_page and next_page.startswith("lesson_"):
            next_parts = next_page.split("_")
            if len(next_parts) >= 3:
                next_lesson = next_parts[1]
                if next_parts[2] == "introduction" and next_lesson != lesson_num:
                    # If next page is an introduction of a different lesson, it's the start of the next lesson
                    button_text = f"Lesson {next_lesson} →"
                else:
                    button_text = f"Next Page →"
                
                if st.sidebar.button(
                    button_text,
                    key=f"nav_next_{lesson_num}",
                    use_container_width=True
                ):
                    # Store the current page as the last visited page for this lesson
                    st.session_state[f"last_page_lesson_{lesson_num}"] = current_page
                    
                    # Navigate using st.switch_page
                    try:
                        page_path = os.path.join("pages", f"{next_page}.py")
                        st.switch_page(page_path)
                    except Exception as e:
                        st.error(f"Failed to navigate to next page: {str(e)}")

def get_all_pages():
    """Helper function to get all pages for progress tracking"""
    import glob
    import os
    
    pages = []
    pattern = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'pages', '*.py')
    for file in glob.glob(pattern):
        # Extract the filename without extension
        filename = os.path.basename(file)[:-3]
        # Skip __init__.py and other special files
        if not filename.startswith('__'):
            pages.append(filename)
    return sorted(pages) 