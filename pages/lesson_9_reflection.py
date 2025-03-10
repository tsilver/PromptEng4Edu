import streamlit as st
import os
import sys
from utils.navigation import scroll_to_top, get_all_pages
from utils.state_management import initialize_session_state, mark_page_completed
from components.teacher_notes import render_teacher_notes
from components.bottom_navigator import render_bottom_navigator
from components.breadcrumb_navigator import render_breadcrumb
from components.course_navigation import render_course_navigation
from components.top_navigator import render_top_navigator
from components.first_visit_dialog import show_first_visit_dialog
from components.progress_manager import render_teacher_controls_sidebar, save_reflection_and_navigate, get_next_lesson_id, get_next_lesson_path

# Configure page
st.set_page_config(
    page_title="Lesson 9: Reflection",
    page_icon="images/favicon_io/favicon.ico",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Get the current directory and add to path if needed
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Page metadata
PAGE_INFO = {
    "title": "Zero-Shot Prompting: Reflection",
    "lesson": "9",
    "section": "reflection",
    "order": 4
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_9_reflection"
st.session_state.current_page = current_page

# Get all available pages for navigation
try:
    all_pages = get_all_pages()
except Exception as e:
    st.error(f"Error loading pages: {str(e)}")
    all_pages = []

# Scroll to top when page loads
scroll_to_top()

# Show the first visit dialog if this is the first time visiting this page
show_first_visit_dialog(
    "lesson_9_reflection",
    "reflection",
    "Lesson 9: Reflection",
    """
    **This is where you reflect on what you've learned about zero-shot prompting.**
    
    ✨ **Important:** Completing this reflection by saving your responses will:
    - Mark Lesson 9 as complete
    - Unlock Lesson 10
    - Save your progress in the course
    
    Take a moment to consider how you can apply zero-shot prompting in your teaching practice.
    """
)

# Render the improved teacher controls in the sidebar
render_teacher_controls_sidebar()

# Create main layout with content area on the left and navigation on the right
content_col, nav_col = st.columns([4, 1])

# Render the main content area
with content_col:
    # Render breadcrumb navigation at the top
    render_breadcrumb(current_page)
    
    # Render section navigation at the top
    render_top_navigator(PAGE_INFO["lesson"], PAGE_INFO["section"])
    
    # Main content
    st.markdown("## Reflection: Zero-Shot Prompting")
    
    st.info("✏️ **Note:** Completing this reflection marks your completion of Lesson 9. Take a moment to consolidate what you've learned before moving on to the next lesson.")
    
    st.markdown("""
    To conclude this lesson on zero-shot prompting, reflect on what you've 
    learned and how you might apply it in your teaching practice.
    """)
    
    # Reflection questions
    reflection1 = st.text_area(
        "List 3-5 specific types of educational content you create regularly that would be well-suited for zero-shot prompting. Explain why zero-shot would work well for these particular content types.",
        height=150,
        key="reflection1"
    )
    
    reflection2 = st.text_area(
        "Write one complete zero-shot prompt for a specific educational need in your teaching context. Explain why you structured it the way you did and what parameters you included to ensure quality output.",
        height=200,
        key="reflection2"
    )
    
    reflection3 = st.text_area(
        "Compare and contrast zero-shot prompting with the full PCTFREI framework. In what situations would you use each approach, and why?",
        height=150,
        key="reflection3"
    )
    
    # Check if at least one field has content for validation
    has_content = any([reflection1, reflection2, reflection3])

    # Calculate the next lesson path for direct navigation
    next_lesson_id = get_next_lesson_id(PAGE_INFO["lesson"])  # Should return "10"
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
    
    # Connecting to Advanced Prompting Techniques
    st.markdown("## Advanced Prompting Techniques")
    
    st.markdown("""
    Zero-shot prompting is the first of several advanced techniques we'll explore:
    
    - **Zero-Shot Prompting**: Using the model's existing knowledge without examples (this lesson)
    
    - **Few-Shot Prompting**: Providing a few examples to guide the model's responses (next lesson)
    
    - **Chain-of-Thought Prompting**: Guiding the model through step-by-step reasoning
    
    - **Role Prompting**: Using rich persona descriptions to shape responses
    
    These techniques complement the PTC-FREI framework, giving you a comprehensive toolkit for 
    prompt engineering in educational contexts.
    """)
    
    # Key takeaways
    st.markdown("## Key Takeaways")
    
    st.markdown("""
    * **Zero-shot works with common educational tasks**: The model already has knowledge of standard educational content and formats
      
    * **Specificity matters**: Clear parameters guide the model without requiring examples
      
    * **Educational terminology helps**: Using terms like "formative assessment" or "differentiation" taps into specialized knowledge
      
    * **Structure improves results**: Organizing requirements as numbered lists increases clarity
      
    * **PCTFREI elements enhance zero-shot**: You can incorporate PCTFREI framework elements even in zero-shot prompts
    """)
    
    # Encouraging remark and segue
    st.markdown("---")
    st.markdown("""
    ## Excellent work on mastering zero-shot prompting!
    
    You now have a powerful technique for quickly generating educational content without needing to provide examples.
    In the next lesson, we'll explore Few-Shot Prompting - how to guide the AI with a small number of examples
    when you need more control over the style, format, or approach.
    """)
    
    # Mark this page as viewed (completion is handled by save_reflection_and_navigate)
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator 
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Discussion Prompts:**
    
    * Ask participants to share their most valuable insight about zero-shot prompting
    * Discuss situations where zero-shot might not be sufficient and why
    * Explore how zero-shot could be integrated into their existing lesson planning workflow
    
    **Looking Ahead:**
    
    In the next lesson on Few-Shot Prompting, make connections to this lesson by emphasizing:
    - How few-shot builds on zero-shot when more control is needed
    - The balance between simplicity (zero-shot) and specificity (few-shot)
    - Situations where each approach might be preferred
    
    **Assessment Opportunity:**
    
    The reflection questions provide insight into participants' understanding of zero-shot prompting. Look for:
    - Appropriate identification of content types well-suited to zero-shot
    - Effective prompt construction with clear parameters
    - Thoughtful comparison between zero-shot and the PCTFREI framework
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
        st.write(f"Session State: {dict(st.session_state)}")
        st.write(f"Next Lesson ID: {next_lesson_id}")
        st.write(f"Next Lesson Path: {next_lesson_path}")
        st.write(f"Already Completed: {already_completed}") 