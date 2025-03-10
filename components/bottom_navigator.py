import streamlit as st

def render_bottom_navigator(page_info):
    """
    Render a horizontal navigation bar at the bottom of the page that mirrors the top navigator.
    
    Parameters:
    - page_info: Dictionary with page metadata including:
        - title: Page title
        - lesson: Lesson number (as string)
        - section: Section type (introduction, examples, activities, reflection)
        - order: Order within the section (usually 1-4)
    """
    # Add a divider before navigation
    st.markdown("<hr style='margin: 2rem 0 1rem 0;'>", unsafe_allow_html=True)
    
    # Get lesson number and current section
    lesson_num = page_info.get("lesson", "")
    current_section = page_info.get("section", "")
    
    # Define sections and their icons (same as top_navigator)
    sections = [
        ("introduction", "🌟 Introduction"),
        ("examples", "🔍 Examples"),
        ("activities", "🎯 Activities"),
        ("reflection", "💭 Reflection")
    ]
    
    # Create columns for each section
    cols = st.columns(len(sections))
    
    # Check if we're in the course introduction pages
    is_course_intro = lesson_num == "intro"
    
    # Simple navigation function to maintain consistency with top_navigator
    def nav_to_section(section_id):
        # For course intro, use different page name pattern
        if is_course_intro:
            if section_id == "introduction":
                page_name = "course_introduction"
            else:
                page_name = f"course_{section_id}"
        else:
            page_name = f"lesson_{lesson_num}_{section_id}"
        
        # Navigate to the target page
        try:
            st.switch_page(f"pages/{page_name}.py")
        except Exception as e:
            st.error(f"Navigation error: {str(e)}")
    
    # Define styles for buttons
    button_styles = {
        "current": {
            "bg_color": "#f0f2f6",
            "text_color": "#262730",
            "border": "none",
            "font_weight": "bold"
        },
        "reflection": {
            "bg_color": "#f0f7ff", 
            "text_color": "#0068C9",
            "border": "1px solid #0068C9",
            "font_weight": "bold"
        },
        "normal": {
            "bg_color": "#ffffff",
            "text_color": "#0068C9",
            "border": "1px solid #e6e6e6",
            "font_weight": "normal"
        }
    }
    
    # Render buttons for each section
    for i, (section_id, label) in enumerate(sections):
        with cols[i]:
            # Determine if this is the current section
            is_current = section_id == current_section
            
            # Add special indicator for reflection button
            if section_id == "reflection" and not is_current:
                label = "💭✨ Reflection"
            
            # Select appropriate styling
            if is_current:
                style = button_styles["current"]
                button_type = "secondary"
            elif section_id == "reflection" and not is_current:
                style = button_styles["reflection"]
                button_type = "primary"
            else:
                style = button_styles["normal"]
                button_type = "secondary"
            
            # For all sections, show a clickable button with appropriate styling
            if st.button(
                label, 
                key=f"bottom_nav_{section_id}_{lesson_num}", 
                type=button_type,
                use_container_width=True,
                disabled=is_current  # Disabled but visible if it's the current section
            ):
                if not is_current:  # Only navigate if it's not the current section
                    nav_to_section(section_id)
    
    # Add some space after the navigation
    st.markdown("<div style='margin-bottom: 1rem;'></div>", unsafe_allow_html=True) 