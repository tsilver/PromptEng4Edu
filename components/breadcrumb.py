import streamlit as st
from utils.navigation import get_all_pages

def render_breadcrumb(current_page_info):
    """Render breadcrumb navigation for the current page."""
    lesson_num = current_page_info["lesson"]
    section = current_page_info["section"].title()
    
    # Get all pages from this lesson
    all_pages = get_all_pages()
    lesson_pages = [p for p in all_pages if p["lesson"] == lesson_num]
    
    # Create breadcrumb HTML
    breadcrumb_html = f"""
    <div style="padding: 0.5rem 0; margin-bottom: 1rem; font-size: 0.9rem;">
        <a href="?page=lesson_{lesson_num}_introduction" style="color: #4A90E2; text-decoration: none;">Lesson {lesson_num}</a>
        &gt;
        <span style="font-weight: bold;">{section}</span>
    </div>
    """
    
    st.markdown(breadcrumb_html, unsafe_allow_html=True)
    
    # Display page title
    st.title(current_page_info["title"])
