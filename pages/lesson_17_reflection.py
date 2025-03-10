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
    page_title="Lesson 17: Reflection",
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
    "title": "Personalized Learning Pathways: Reflection",
    "lesson": "17",
    "section": "reflection",
    "order": 4
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_17_reflection"
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
    "lesson_17_reflection",
    "reflection",
    "Lesson 17: Reflection",
    """
    **This is where you reflect on what you've learned about personalized learning pathways.**
    
    ✨ **Important:** Completing this reflection by saving your responses will:
    - Mark Lesson 17 as complete
    - Unlock Lesson 18 on Interdisciplinary Unit Design
    - Save your progress in the course
    
    Take a moment to consider how you can apply prompt engineering to enhance personalized learning
    in your teaching practice.
    """
)

# Calculate the next lesson path for direct navigation
next_lesson_id = get_next_lesson_id(PAGE_INFO["lesson"])  # Should return "18"
next_lesson_path = get_next_lesson_path(next_lesson_id)

# Create a session state flag for showing the completion page
# This will be used in Lesson 18's reflection page, but we keep it here for compatibility
if "show_completion_page" not in st.session_state:
    st.session_state.show_completion_page = False

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
    st.markdown("## Reflection: Personalized Learning Pathways")
    
    st.info("✏️ **Note:** Completing this reflection marks your completion of Lesson 17. Take a moment to consolidate what you've learned before moving on to the next lesson.")
    
    st.markdown("""
    To conclude this lesson on personalized learning pathways, reflect on what you've 
    learned and how you might apply it in your teaching practice.
    """)
    
    # Reflection questions
    reflection1 = st.text_area(
        "What specific aspects of your teaching would most benefit from personalization, and which personalization approaches (differentiated content, adaptive pathways, interest-based choices, etc.) would be most appropriate for those aspects? Explain your reasoning.",
        height=150,
        key="reflection1"
    )
    
    reflection2 = st.text_area(
        "What are the biggest challenges you face (or anticipate facing) when implementing personalized learning in your teaching context? How might prompt engineering help you address these challenges?",
        height=150,
        key="reflection2"
    )
    
    reflection3 = st.text_area(
        "Select one specific unit or lesson you teach and describe how you would use the PCTFR framework to create a prompt for a personalized learning experience. What key elements would you include in each part of the framework?",
        height=200,
        key="reflection3"
    )
    
    # Check if at least one field has content for validation
    has_content = any([reflection1, reflection2, reflection3])

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
    As you prepare to implement personalized learning in your teaching practice,
    consider this implementation framework:
    
    ### 1. Identify High-Impact Areas for Personalization
    - Look for content where student readiness levels vary significantly
    - Focus on key skills that are foundational to future learning
    - Consider areas where student engagement or success has been problematic
    - Target units where students have diverse interests that could be leveraged
    
    ### 2. Start with a Single Approach to Personalization
    - Choose one approach (tiered assignments, choice boards, etc.) to implement first
    - Apply it to a limited context before expanding
    - Create templates that can be reused across units or lessons
    - Develop routines and procedures to manage the logistics
    
    ### 3. Design Clear Learning Pathways
    - Create visual maps of how students will navigate options
    - Develop tools for determining appropriate placements or choices
    - Build in checkpoints to monitor progress and adjust as needed
    - Ensure all paths lead to essential learning outcomes
    
    ### 4. Balance Structure with Agency
    - Provide appropriate guidance for student decision-making
    - Develop metacognitive prompts to help students reflect on their choices
    - Create systems for tracking progress across different paths
    - Gradually release more responsibility to students as they develop skills
    
    This systematic approach helps you implement personalized learning in manageable stages
    while maintaining instructional coherence and addressing practical constraints.
    """)
    
    # Key takeaways
    st.markdown("## Key Takeaways")
    
    st.markdown("""
    * **Personalization has multiple dimensions** - Content, process, product, and environment can all be personalized to meet student needs
      
    * **Clear learning goals remain essential** - Effective personalization maintains consistent outcomes while varying paths to mastery
      
    * **Student variables guide approach selection** - Different personalization strategies address readiness, interests, and learning preferences
      
    * **Prompt engineering makes personalization manageable** - Creating differentiated and adaptive resources becomes more efficient with effective prompts
      
    * **Strategic implementation is key** - Starting small, focusing on high-impact areas, and building systems gradually leads to sustainable personalization
    """)
    
    # Connection to next lesson
    st.markdown("## Connection to Lesson 18: Interdisciplinary Unit Design")
    
    st.markdown("""
    In our next lesson, we'll explore how to apply prompt engineering to create interdisciplinary 
    learning experiences that connect multiple subject areas. This builds on what you've learned 
    about personalized learning:
    
    - **From individual pathways to integrated experiences** - Just as personalized learning creates 
      tailored paths for individual students, interdisciplinary design creates connections across 
      traditionally separate content areas
    
    - **From learner profiles to content integration** - The careful analysis of learner needs you've 
      practiced applies to the thoughtful integration of disciplinary concepts and skills
    
    - **From structure with flexibility to purposeful connections** - The balance of structure and 
      responsiveness in personalized learning transfers to designing interdisciplinary units that 
      maintain disciplinary integrity while creating meaningful connections
    
    As you move into Lesson 18, consider how interdisciplinary approaches can provide rich contexts 
    for personalized learning while helping students see connections between different areas of study.
    """)
    
    # Encouraging remark and segue
    st.markdown("---")
    st.markdown("""
    ## Excellent work on mastering personalized learning design!
    
    You've now learned how to apply prompt engineering to create personalized learning experiences 
    that address diverse student needs, interests, and preferences. These approaches will help you 
    design more engaging, accessible learning pathways that support all students in reaching 
    essential learning goals.
    
    In the next lesson, we'll explore Interdisciplinary Unit Design. You'll discover how to 
    create learning experiences that meaningfully connect multiple subject areas, helping students 
    develop integrated understanding while building transferable skills and concepts.
    """)
    
    # Mark this page as viewed (completion is handled by save_reflection_and_navigate)
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator 
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Discussion Prompts:**
    
    * Ask participants which personalization approach resonated most with their teaching context
    * Discuss how schools or departments might collaborate to create banks of personalized resources
    * Explore how to balance personalization with standardized curriculum requirements
    * Consider how to communicate the value of personalization to parents and students
    
    **Looking Ahead:**
    
    In the next lesson on Interdisciplinary Unit Design, make connections to this lesson by emphasizing:
    - How personalized learning can be integrated into interdisciplinary approaches
    - The parallel complexity of designing both personalized and interdisciplinary experiences
    - The shared focus on meaningful connections and coherent learning progressions
    
    **Assessment Opportunity:**
    
    The reflection questions provide insight into participants' understanding and application plans. Look for:
    - Recognition of appropriate contexts for different personalization approaches
    - Thoughtful analysis of implementation challenges and potential solutions
    - Application of the PCTFR framework to specific teaching scenarios
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