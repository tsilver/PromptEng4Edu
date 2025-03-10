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
    page_title="Lesson 12: Reflection",
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
    "title": "Role Prompting: Reflection",
    "lesson": "12",
    "section": "reflection",
    "order": 4
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_12_reflection"
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
    "lesson_12_reflection",
    "reflection",
    "Lesson 12: Reflection",
    """
    **This is where you reflect on what you've learned about role prompting.**
    
    ✨ **Important:** Completing this reflection by saving your responses will:
    - Mark Lesson 12 as complete
    - Unlock Lesson 13
    - Save your progress in the course
    
    Take a moment to consider how you can apply role prompting in your teaching practice.
    """
)

# Render the teacher controls in the sidebar
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
    st.markdown("## Reflection: Role Prompting")
    
    st.info("✏️ **Note:** Completing this reflection marks your completion of Lesson 12. Take a moment to consolidate what you've learned before moving on to the next lesson.")
    
    st.markdown("""
    To conclude this lesson on role prompting, reflect on what you've 
    learned and how you might apply it in your teaching practice.
    """)
    
    # Reflection questions
    reflection1 = st.text_area(
        "What specific teaching challenges or content creation needs do you have that role prompting could help address? Why would role prompting be particularly valuable for these needs?",
        height=150,
        key="reflection1"
    )
    
    reflection2 = st.text_area(
        "Identify 2-3 specific personas that would be most useful for your educational context. For each, describe what characteristics you would include in the persona and what types of content they would help you create.",
        height=200,
        key="reflection2"
    )
    
    reflection3 = st.text_area(
        "How might you combine role prompting with other techniques we've covered so far (like chain-of-thought prompting or few-shot examples) to create more effective educational content for your students?",
        height=150,
        key="reflection3"
    )
    
    # Check if at least one field has content for validation
    has_content = any([reflection1, reflection2, reflection3])

    # Calculate the next lesson path for direct navigation
    next_lesson_id = get_next_lesson_id(PAGE_INFO["lesson"])  # Should return "13"
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
    
    # Connecting to Application Lessons
    st.markdown("## Looking Ahead: Applying Advanced Techniques")
    
    st.markdown("""
    Congratulations! You've now completed the advanced prompting techniques section of our course:
    
    - **Zero-Shot Prompting**: Using the model's existing knowledge without examples (Lesson 9)
    
    - **Few-Shot Prompting**: Providing examples to guide the model's responses (Lesson 10)
    
    - **Chain-of-Thought Prompting**: Guiding the model through step-by-step reasoning (Lesson 11)
    
    - **Role Prompting**: Using persona descriptions to shape responses (this lesson)
    
    In the next set of lessons, we'll focus on applying these techniques to specific educational tasks:
    
    - **Lesson 13**: Lesson Planning and Assessment Creation
    - **Lesson 14**: Student Feedback and Writing Prompts
    - **Lesson 15**: Discussion Questions and Content Creation
    - **Lesson 16**: Email Composition and Presentation Outlines
    - **Lesson 17**: Comprehensive Review and Integration
    
    These application-focused lessons will help you put your prompt engineering skills to work
    in practical contexts that directly support your teaching.
    """)
    
    # Key takeaways
    st.markdown("## Key Takeaways")
    
    st.markdown("""
    * **Personas shape content:** The right persona can naturally create age-appropriate, engaging content
      
    * **Specificity matters:** Detailed persona descriptions are more effective than generic roles
      
    * **Match persona to purpose:** Different educational goals call for different types of personas
      
    * **Combine techniques:** Role prompting works well with other prompting strategies
      
    * **Voice creates connection:** The right voice can make content more relatable and memorable for students
    """)
    
    # Encouraging remark and segue
    st.markdown("---")
    st.markdown("""
    ## Excellent work on mastering role prompting!
    
    You now have a powerful technique for generating educational content with specific voices and 
    characteristics that can enhance engagement and effectiveness. By selecting the right persona 
    for each educational purpose, you can create more tailored, relevant content for your students.
    
    In the next lesson, we'll begin applying all these techniques to specific educational tasks, 
    starting with lesson planning and assessment creation. You'll see how the PTC-FREI framework 
    and advanced techniques can help you create high-quality educational resources more efficiently.
    """)
    
    # Mark this page as viewed (completion is handled by save_reflection_and_navigate)
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator 
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Discussion Prompts:**
    
    * Ask participants to share creative personas they've identified for their specific teaching contexts
    * Discuss how different personas might work better for different student populations or needs
    * Explore how role prompting can help address representation and inclusivity in educational content
    * Consider how role prompting might be used in collaborative or peer learning contexts
    
    **Looking Ahead:**
    
    In the next lesson on Lesson Planning and Assessment Creation, make connections to this lesson by:
    - Highlighting how different personas can be useful for different aspects of lesson planning
    - Discussing how role prompting can help create assessments with consistent voice and structure
    - Encouraging participants to combine role prompting with other techniques for complex planning tasks
    
    **Assessment Opportunity:**
    
    The reflection questions provide insight into participants' understanding of role prompting. Look for:
    - Specific applications to their teaching context (demonstrating transfer)
    - Thoughtfully developed personas with detailed characteristics (demonstrating understanding of specificity)
    - Creative combinations with other techniques (demonstrating integration of learning)
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