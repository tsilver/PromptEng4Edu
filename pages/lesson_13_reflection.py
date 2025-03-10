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
    page_title="Lesson 13: Reflection",
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
    "title": "Lesson Planning and Assessment Creation: Reflection",
    "lesson": "13",
    "section": "reflection",
    "order": 4
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_13_reflection"
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
    "lesson_13_reflection",
    "reflection",
    "Lesson 13: Reflection",
    """
    **This is where you reflect on what you've learned about prompt engineering for lesson planning and assessment creation.**
    
    ✨ **Important:** Completing this reflection by saving your responses will:
    - Mark Lesson 13 as complete
    - Unlock Lesson 14
    - Save your progress in the course
    
    Take a moment to consider how you can apply these techniques to make your curriculum development more efficient and effective.
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
    st.markdown("## Reflection: Lesson Planning and Assessment Creation")
    
    st.info("✏️ **Note:** Completing this reflection marks your completion of Lesson 13. Take a moment to consolidate what you've learned before moving on to the next lesson.")
    
    st.markdown("""
    To conclude this lesson on prompt engineering for curriculum development, reflect on what you've 
    learned and how you might apply it in your teaching practice.
    """)
    
    # Reflection questions
    reflection1 = st.text_area(
        "What types of lesson plans or assessments do you currently spend the most time creating? How could prompt engineering techniques help make this process more efficient?",
        height=150,
        key="reflection1"
    )
    
    reflection2 = st.text_area(
        "Which prompt engineering technique (role prompting, few-shot, chain-of-thought, etc.) do you think would be most valuable for your curriculum development work, and why?",
        height=150,
        key="reflection2"
    )
    
    reflection3 = st.text_area(
        "What specific prompt template or strategy from this lesson do you plan to implement first? How will you adapt it for your specific teaching context?",
        height=200,
        key="reflection3"
    )
    
    # Check if at least one field has content for validation
    has_content = any([reflection1, reflection2, reflection3])

    # Calculate the next lesson path for direct navigation
    next_lesson_id = get_next_lesson_id(PAGE_INFO["lesson"])  # Should return "14"
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
    
    # Curriculum Development Workflow
    st.markdown("## Curriculum Development Workflow")
    
    st.markdown("""
    As you continue to develop your prompt engineering skills, consider establishing a systematic
    workflow for curriculum development:
    
    1. **Planning Phase**
       - Identify clear learning objectives
       - Determine alignment with standards
       - Consider student characteristics and needs
       - Select appropriate prompt engineering techniques
    
    2. **Development Phase**
       - Create structured prompts with PTC-FREI elements
       - Generate initial materials
       - Review and evaluate outputs
       - Refine prompts for improved results
    
    3. **Implementation Phase**
       - Customize materials for your specific context
       - Add personal touches and expertise
       - Prepare supplementary resources
       - Implement in the classroom
    
    4. **Reflection and Iteration Phase**
       - Evaluate effectiveness with students
       - Identify areas for improvement
       - Refine prompt templates for future use
       - Share successful approaches with colleagues
    
    This systematic approach ensures that AI-assisted curriculum development becomes increasingly
    efficient and effective over time, saving you valuable time while maintaining high quality.
    """)
    
    # Key takeaways
    st.markdown("## Key Takeaways")
    
    st.markdown("""
    * **Structure matters:** Clear, specific prompt structures produce better curriculum materials
      
    * **Context is crucial:** Include details about students, resources, and prior knowledge
      
    * **Standards integration:** Explicitly reference standards to ensure alignment
      
    * **Differentiation focus:** Specifically request modifications for diverse learners
      
    * **Reusable templates:** Develop a personal library of effective prompt templates
    """)
    
    # Encouraging remark and segue
    st.markdown("---")
    st.markdown("""
    ## Excellent work on mastering prompt engineering for curriculum development!
    
    You've now learned how to apply prompt engineering techniques to create high-quality lesson plans
    and assessments that align with standards, engage students, and support diverse learning needs.
    These skills will help you save time on routine curriculum tasks while maintaining or even
    improving the quality of your instructional materials.
    
    In the next lesson, we'll explore how to apply prompt engineering to student feedback and writing
    prompts, two other key aspects of teaching that can benefit from effective AI assistance.
    """)
    
    # Mark this page as viewed (completion is handled by save_reflection_and_navigate)
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator 
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Discussion Prompts:**
    
    * Ask participants to share specific examples of curriculum materials they've created using the techniques in this lesson
    * Discuss the balance between efficiency (using AI) and personalization (adding teacher expertise)
    * Explore how departments or grade-level teams might collaborate on prompt development for curriculum coherence
    * Consider how these approaches might support new teachers who are developing curriculum for the first time
    
    **Looking Ahead:**
    
    In the next lesson on Student Feedback and Writing Prompts, make connections to this lesson by emphasizing:
    - How clear lesson objectives and assessments connect to effective feedback
    - The importance of maintaining consistent voice across curriculum materials and feedback
    - How prompt engineering can support the full instructional cycle from planning to assessment to feedback
    
    **Assessment Opportunity:**
    
    The reflection questions provide insight into participants' understanding and application plans. Look for:
    - Specific mentions of techniques they plan to implement (demonstrating understanding)
    - Thoughtful adaptations for their context (demonstrating transfer)
    - Recognition of time-saving potential balanced with quality considerations (demonstrating critical thinking)
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