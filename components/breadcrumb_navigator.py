import streamlit as st
import os

def render_breadcrumb(current_page):
    """
    Render a breadcrumb navigation at the top of the main content area.
    
    Parameters:
    - current_page: Currently active page filename (string)
    """
    # Check if we should show the AIxponential logo (not on course_introduction.py)
    show_logo = current_page != "course_introduction"
    
    if show_logo:
        # Create a two-column layout for logo + breadcrumb
        logo_col, breadcrumb_col = st.columns([1, 5])
        
        # Display the AIxponential logo in the first column
        with logo_col:
            st.image("images/aix_logo.png", width=70)
        
        # Use breadcrumb_col for the breadcrumb content
        breadcrumb_column = breadcrumb_col
    else:
        # On course_introduction.py, render directly (without any 'with' context)
        breadcrumb_column = None
    
    # Extract page info from filename
    if current_page == "app":
        # Special case for app.py (root)
        parts = [("Home", "app")]
    elif current_page == "course_introduction":
        # Special case for course introduction
        parts = [("Home", "app"), ("Course Introduction", "course_introduction")]
    elif current_page.startswith("course_"):
        # Other course pages
        section = current_page.replace("course_", "")
        section_name = section.capitalize()
        parts = [
            ("Home", "app"),
            ("Course Introduction", "course_introduction"),
            (section_name, current_page)
        ]
    else:
        # Handle lesson pages (format: lesson_X_section.py)
        page_parts = current_page.split("_")
        
        if len(page_parts) >= 3 and page_parts[0] == "lesson":
            # Get lesson number and section
            lesson_num = page_parts[1]
            section = page_parts[2]
            
            # Format the section name
            if section == "introduction":
                section_name = "Introduction"
            elif section == "examples":
                section_name = "Examples"
            elif section == "activities":
                section_name = "Activities"
            elif section == "reflection":
                section_name = "Reflection"
            else:
                section_name = section.capitalize()
            
            # Create breadcrumb parts
            parts = [
                ("Home", "app"),
                ("Course", "course_introduction"),
                (f"Lesson {lesson_num}", f"lesson_{lesson_num}_introduction"),
                (section_name, current_page)
            ]
        else:
            # For any other page pattern
            parts = [("Home", "app"), (current_page, current_page)]
    
    # Create HTML for the breadcrumb with larger font and more prominent appearance
    breadcrumb_html = ['<div style="font-size: 1.2rem; margin-bottom: 1.5rem; font-weight: 500; display: flex; align-items: center;">']
    
    for i, (label, page) in enumerate(parts):
        # Don't make the current page a link
        if i == len(parts) - 1:
            breadcrumb_html.append(f'<span style="color: #0068C9; font-weight: 600;">{label}</span>')
        else:
            # Direct navigation using st.switch_page
            if page == "app":
                # For the home (app) page
                breadcrumb_html.append(
                    f'<a href="#" onclick="window.parent.location.href=\'/\'; return false;" '
                    f'style="color: #555; text-decoration: none; font-weight: 500;">{label}</a>'
                )
            else:
                # For any other page
                breadcrumb_html.append(
                    f'<a href="#" onclick="streamlitNavigateTo(\'{page}\'); return false;" '
                    f'style="color: #555; text-decoration: none; font-weight: 500;">{label}</a>'
                )
            
        # Add separator except after last item
        if i < len(parts) - 1:
            breadcrumb_html.append('<span style="margin: 0 0.5rem; color: #555;"> &gt; </span>')
    
    breadcrumb_html.append('</div>')
    
    # Add JavaScript for page switching
    breadcrumb_html.append('''
    <script>
        function streamlitNavigateTo(pageName) {
            // This works because Streamlit pages have the structure 'pages/pageName.py'
            const url = 'pages/' + pageName + '.py';
            try {
                // Use Streamlit's navigation mechanism
                window.parent.postMessage({
                    type: 'streamlit:setComponentValue',
                    value: url
                }, '*');
            } catch (e) {
                console.error('Failed to navigate:', e);
                // Fallback
                window.parent.location.href = '/?' + pageName;
            }
        }
    </script>
    ''')
    
    # Render the breadcrumb in the appropriate column or directly
    breadcrumb_content = ''.join(breadcrumb_html)
    
    if breadcrumb_column is not None:
        # For pages with logo, render in the breadcrumb column
        with breadcrumb_column:
            st.markdown(breadcrumb_content, unsafe_allow_html=True)
    else:
        # For course_introduction.py, render directly
        st.markdown(breadcrumb_content, unsafe_allow_html=True) 