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
    page_title="Lesson 11: Reflection",
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
    "title": "Chain-of-Thought Prompting: Reflection",
    "lesson": "11",
    "section": "reflection",
    "order": 4
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_11_reflection"
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
    "lesson_11_reflection",
    "reflection",
    "Lesson 11: Reflection",
    """
    **This is where you reflect on what you've learned about chain-of-thought prompting.**
    
    ✨ **Important:** Completing this reflection by saving your responses will:
    - Mark Lesson 11 as complete
    - Unlock Lesson 12
    - Save your progress in the course
    
    Take a moment to consider how you can apply chain-of-thought prompting in your teaching practice.
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
    st.markdown("## Reflection: Chain-of-Thought Prompting")
    
    st.info("✏️ **Note:** Completing this reflection marks your completion of Lesson 11. Take a moment to consolidate what you've learned before moving on to the next lesson.")
    
    st.markdown("""
    To conclude this lesson on chain-of-thought prompting, reflect on what you've 
    learned and how you might apply it in your teaching practice.
    """)
    
    # Reflection questions
    reflection1 = st.text_area(
        "How does chain-of-thought prompting differ from other prompting techniques we've explored? What unique educational benefits does it offer?",
        height=150,
        key="reflection1"
    )
    
    reflection2 = st.text_area(
        "Identify a specific concept or skill in your teaching area where making the thinking process explicit would particularly benefit students. Explain why this approach would be valuable for this topic.",
        height=200,
        key="reflection2"
    )
    
    reflection3 = st.text_area(
        "How might you use chain-of-thought prompting to create materials that model metacognitive strategies for your students? What specific thinking steps would you want to demonstrate?",
        height=150,
        key="reflection3"
    )
    
    # Check if at least one field has content for validation
    has_content = any([reflection1, reflection2, reflection3])

    # Calculate the next lesson path for direct navigation
    next_lesson_id = get_next_lesson_id(PAGE_INFO["lesson"])  # Should return "12"
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
    We've now explored three important prompting techniques:
    
    - **Zero-Shot Prompting**: Using the model's existing knowledge without examples (Lesson 9)
    
    - **Few-Shot Prompting**: Providing a few examples to guide the model's responses (Lesson 10)
    
    - **Chain-of-Thought Prompting**: Guiding the model through step-by-step reasoning (this lesson)
    
    In the next lesson, we'll explore another advanced technique:
    
    - **Role Prompting**: Using rich persona descriptions to shape responses
    
    Each of these techniques offers unique advantages for different educational needs, and they can be 
    combined with the PTC-FREI framework we explored earlier in the course.
    """)
    
    # Key takeaways
    st.markdown("## Key Takeaways")
    
    st.markdown("""
    * **Explicitness matters**: Always explicitly ask for step-by-step thinking or reasoning
      
    * **Discipline-specific thinking**: Different subjects require different reasoning processes
      
    * **Metacognitive modeling**: Chain-of-thought prompting helps model effective thinking for students
      
    * **Verification tool**: Seeing the reasoning process helps you verify the quality of responses
      
    * **Combinable technique**: Chain-of-thought works well when combined with other techniques
    """)
    
    # Encouraging remark and segue
    st.markdown("---")
    st.markdown("""
    ## Excellent work on mastering chain-of-thought prompting!
    
    You now have a powerful technique for generating educational content that not only provides answers
    but also models effective thinking processes. This approach is particularly valuable for helping students
    understand how to approach complex problems and develop their own metacognitive skills.
    
    In the next lesson, we'll explore Role Prompting - a technique that uses detailed persona instructions
    to shape AI responses in specific ways, which can be particularly valuable for creating engaging,
    voice-appropriate educational content.
    """)
    
    # Mark this page as viewed (completion is handled by save_reflection_and_navigate)
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator 
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Discussion Prompts:**
    
    * Ask participants to share specific concepts in their subject areas where making thinking explicit is particularly challenging
    * Discuss how chain-of-thought prompting might be used directly with students as a learning tool
    * Explore how this technique connects to broader educational goals around metacognitive development
    
    **Looking Ahead:**
    
    In the next lesson on Role Prompting, make connections to this lesson by emphasizing:
    - How role prompting can be combined with chain-of-thought to create voice-appropriate explanations
    - The value of having explanations delivered in specific voices for different educational contexts
    - How combining these techniques creates even more versatile educational resources
    
    **Assessment Opportunity:**
    
    The reflection questions provide insight into participants' understanding of chain-of-thought prompting. Look for:
    - Comparison of chain-of-thought with other techniques (demonstrating understanding of differences)
    - Application to specific teaching contexts (demonstrating transfer of learning)
    - Connection to metacognitive development (demonstrating deeper pedagogical implications)
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