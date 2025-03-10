import streamlit as st

def render_top_navigator(lesson_num, current_section):
    """
    Render a horizontal navigation bar at the top of the page for section navigation.
    
    Parameters:
    - lesson_num: Lesson number (as string)
    - current_section: Current section (introduction, examples, activities, reflection)
    """
    # Define sections and their icons
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
    
    # Simple navigation function to avoid issues
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
    
    # Render buttons for each section
    for i, (section_id, label) in enumerate(sections):
        with cols[i]:
            # Determine if this is the current section
            is_current = section_id == current_section
            
            # Add special styling for reflection button
            button_type = "primary" if section_id == "reflection" and not is_current else "secondary"
            
            # Add special indicator for reflection button
            if section_id == "reflection" and not is_current:
                label = "💭✨ Reflection"
            
            if is_current:
                # For current section, show a disabled-looking button
                st.markdown(f"""
                <div style="
                    padding: 0.5rem; 
                    border-radius: 0.25rem; 
                    background-color: #f0f2f6; 
                    color: #262730; 
                    text-align: center;
                    font-weight: bold;
                    margin-bottom: 1rem;
                ">
                    {label}
                </div>
                """, unsafe_allow_html=True)
            else:
                # For non-current sections, show a clickable button
                if st.button(
                    label, 
                    key=f"top_nav_{section_id}_{lesson_num}", 
                    type=button_type,
                    use_container_width=True
                ):
                    nav_to_section(section_id)
    
    # Add a small gap after the navigation
    st.markdown("<div style='margin-bottom: 1.5rem;'></div>", unsafe_allow_html=True) 