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
    page_title="Lesson 14: Reflection",
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
    "title": "Student Feedback and Writing Prompts: Reflection",
    "lesson": "14",
    "section": "reflection",
    "order": 4
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_14_reflection"
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
    "lesson_14_reflection",
    "reflection",
    "Lesson 14: Reflection",
    """
    **This is where you reflect on what you've learned about student feedback and writing prompts.**
    
    ✨ **Important:** Completing this reflection by saving your responses will:
    - Mark Lesson 14 as complete
    - Unlock Lesson 15
    - Save your progress in the course
    
    Take a moment to consider how you can apply prompt engineering to create more effective feedback and writing tasks.
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
    st.markdown("## Reflection: Student Feedback and Writing Prompts")
    
    st.info("✏️ **Note:** Completing this reflection marks your completion of Lesson 14. Take a moment to consolidate what you've learned before moving on to the next lesson.")
    
    st.markdown("""
    To conclude this lesson on student feedback and writing prompts, reflect on what you've 
    learned and how you might apply it in your teaching practice.
    """)
    
    # Reflection questions
    reflection1 = st.text_area(
        "What current feedback practices do you use, and how could you enhance them using the prompt engineering techniques you've learned? Be specific about which techniques would be most valuable and why.",
        height=150,
        key="reflection1"
    )
    
    reflection2 = st.text_area(
        "Describe a writing task you regularly assign to your students. How could you redesign the prompt using the principles covered in this lesson to make it more engaging, scaffolded, and accessible to diverse learners?",
        height=200,
        key="reflection2"
    )
    
    reflection3 = st.text_area(
        "What specific challenges do you face in providing quality feedback or creating effective writing prompts? How do you plan to use prompt engineering to address these challenges?",
        height=150,
        key="reflection3"
    )
    
    # Check if at least one field has content for validation
    has_content = any([reflection1, reflection2, reflection3])

    # Calculate the next lesson path for direct navigation
    next_lesson_id = get_next_lesson_id(PAGE_INFO["lesson"])  # Should return "15"
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
    
    # Implementation Planning
    st.markdown("## Implementation Planning")
    
    st.markdown("""
    As you prepare to implement effective feedback and writing prompt strategies in your teaching,
    consider this implementation framework:
    
    ### 1. Audit Current Practices
    - Review your current feedback approach and identify strengths/limitations
    - Examine existing writing prompts for opportunities to enhance
    - Identify specific pain points or challenges in your current practice
    
    ### 2. Develop Templates and Systems
    - Create feedback templates for common assignment types
    - Build a library of effective writing prompts organized by type/standard
    - Establish differentiation protocols for diverse learners
    
    ### 3. Implement Incrementally
    - Start with one class or assignment type
    - Test new approaches and gather student feedback
    - Refine based on results and expand to other contexts
    
    ### 4. Monitor Impact and Refine
    - Track changes in student engagement and performance
    - Collect student feedback on the helpfulness of your feedback
    - Continuously improve templates and approaches
    
    This systematic approach helps you integrate new practices effectively while managing
    the time investment and allowing for continuous improvement.
    """)
    
    # Key takeaways
    st.markdown("## Key Takeaways")
    
    st.markdown("""
    * **Balanced feedback** combines specific strengths and growth areas with clear next steps
      
    * **Strategic templates** create consistency and efficiency while allowing personalization
      
    * **Effective writing prompts** include clear tasks, appropriate scaffolding, and transparent success criteria
      
    * **Differentiation strategies** ensure all students can access and benefit from writing tasks
      
    * **Prompt engineering** allows you to leverage AI assistance while maintaining professional judgment
    """)
    
    # Connection to next lesson
    st.markdown("## Connection to Discussion Questions and Content Creation")
    
    st.markdown("""
    In our next lesson, we'll explore how to apply prompt engineering to create engaging discussion
    questions and instructional content. This builds directly on what you've learned about student
    feedback and writing prompts:
    
    - **From feedback to discussion:** Just as effective feedback encourages student reflection and growth,
      well-crafted discussion questions promote deeper thinking and engagement.
    
    - **From writing prompts to content creation:** The principles of clear structure, appropriate
      scaffolding, and differentiation apply equally to creating instructional content.
    
    - **Continuing the instructional cycle:** Discussion questions and content creation represent
      additional points in the teaching and learning cycle where prompt engineering can enhance effectiveness.
    
    As you move into Lesson 15, consider how these interconnected instructional practices work
    together to create coherent, engaging learning experiences for your students.
    """)
    
    # Encouraging remark and segue
    st.markdown("---")
    st.markdown("""
    ## Excellent work on mastering feedback and writing prompt techniques!
    
    You've now learned how to apply prompt engineering to two critical instructional tasks:
    providing effective feedback and creating engaging writing prompts. These skills will help
    you support student growth while managing your workload efficiently.
    
    In the next lesson, we'll continue applying prompt engineering to instructional tasks by
    exploring discussion questions and content creation. You'll discover how to generate
    thought-provoking questions and engaging instructional materials that promote deep learning.
    """)
    
    # Mark this page as viewed (completion is handled by save_reflection_and_navigate)
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator 
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Discussion Prompts:**
    
    * Ask participants to share their biggest "aha moment" about feedback or writing prompts from this lesson
    * Discuss how school or department-wide feedback protocols might be enhanced using these approaches
    * Explore how educators might collaborate on building shared prompt libraries for common assignments
    * Consider how these techniques might impact students' perceptions of assessment and writing tasks
    
    **Looking Ahead:**
    
    In the next lesson on Discussion Questions and Content Creation, make connections to this lesson by emphasizing:
    - How feedback and discussion questions both serve to deepen student thinking
    - The parallels between crafting writing prompts and creating instructional content
    - The importance of maintaining consistent standards across all aspects of instruction
    
    **Assessment Opportunity:**
    
    The reflection questions provide insight into participants' understanding and application plans. Look for:
    - Specific mentions of prompt engineering techniques they plan to implement (demonstrating understanding)
    - Thoughtful integration with existing practices (demonstrating transfer)
    - Awareness of implementation challenges and realistic solutions (demonstrating critical thinking)
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