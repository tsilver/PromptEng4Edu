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
    page_title="Lesson 10: Reflection",
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
    "title": "Few-Shot Prompting: Reflection",
    "lesson": "10",
    "section": "reflection",
    "order": 4
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_10_reflection"
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
    "lesson_10_reflection",
    "reflection",
    "Lesson 10: Reflection",
    """
    **This is where you reflect on what you've learned about few-shot prompting.**
    
    ✨ **Important:** Completing this reflection by saving your responses will:
    - Mark Lesson 10 as complete
    - Unlock Lesson 11
    - Save your progress in the course
    
    Take a moment to consider how you can apply few-shot prompting in your teaching practice.
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
    st.markdown("## Reflection: Few-Shot Prompting")
    
    st.info("✏️ **Note:** Completing this reflection marks your completion of Lesson 10. Take a moment to consolidate what you've learned before moving on to the next lesson.")
    
    st.markdown("""
    To conclude this lesson on few-shot prompting, reflect on what you've 
    learned and how you might apply it in your teaching practice.
    """)
    
    # Reflection questions
    reflection1 = st.text_area(
        "Compare and contrast zero-shot and few-shot prompting. In what educational scenarios would you choose one approach over the other?",
        height=150,
        key="reflection1"
    )
    
    reflection2 = st.text_area(
        "Describe a specific type of educational content you create where few-shot prompting would be particularly valuable. What examples would you include in your few-shot prompt and why?",
        height=200,
        key="reflection2"
    )
    
    reflection3 = st.text_area(
        "What criteria should you consider when creating examples for a few-shot prompt? How might these criteria differ based on your educational goals or subject area?",
        height=150,
        key="reflection3"
    )
    
    # Check if at least one field has content for validation
    has_content = any([reflection1, reflection2, reflection3])

    # Calculate the next lesson path for direct navigation
    next_lesson_id = get_next_lesson_id(PAGE_INFO["lesson"])  # Should return "11"
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
    We've now explored two important prompting techniques:
    
    - **Zero-Shot Prompting**: Using the model's existing knowledge without examples (Lesson 9)
    
    - **Few-Shot Prompting**: Providing a few examples to guide the model's responses (this lesson)
    
    In the next lessons, we'll continue exploring advanced techniques:
    
    - **Chain-of-Thought Prompting**: Guiding the model through step-by-step reasoning
    
    - **Role Prompting**: Using rich persona descriptions to shape responses
    
    Each of these techniques offers unique advantages for different educational needs, and they can be 
    combined with the PTC-FREI framework we explored earlier in the course.
    """)
    
    # Key takeaways
    st.markdown("## Key Takeaways")
    
    st.markdown("""
    * **Examples demonstrate patterns**: Few-shot prompting uses examples to show the AI exactly what you want
      
    * **Quality matters**: The quality of your examples directly impacts the quality of AI responses
      
    * **Format consistency**: Consistent formatting across examples makes the pattern clearer
      
    * **2-3 examples is usually sufficient**: More examples aren't always better
      
    * **Example selection is strategic**: Choose examples that highlight the specific aspects you care about
    """)
    
    # Encouraging remark and segue
    st.markdown("---")
    st.markdown("""
    ## Excellent work on mastering few-shot prompting!
    
    You now have a powerful technique for creating consistent, high-quality educational content using examples.
    In the next lesson, we'll explore Chain-of-Thought Prompting - a technique that helps AI produce better
    reasoning and step-by-step explanations, which is particularly valuable for educational content.
    """)
    
    # Mark this page as viewed (completion is handled by save_reflection_and_navigate)
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator 
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Discussion Prompts:**
    
    * Ask participants to share examples of content they create that would benefit from consistent formatting
    * Discuss the balance between providing enough examples and keeping prompts concise
    * Explore how few-shot prompting might be used with students directly
    
    **Looking Ahead:**
    
    In the next lesson on Chain-of-Thought Prompting, make connections to this lesson by emphasizing:
    - How few-shot examples can demonstrate reasoning processes
    - The value of showing step-by-step thinking in educational contexts
    - How combining these techniques can create powerful educational tools
    
    **Assessment Opportunity:**
    
    The reflection questions provide insight into participants' understanding of few-shot prompting. Look for:
    - Thoughtful comparison between zero-shot and few-shot approaches
    - Specific applications to their teaching context
    - Understanding of the importance of example quality and consistency
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