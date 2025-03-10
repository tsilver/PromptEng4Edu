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
    page_title="Lesson 16: Reflection",
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
    "title": "Collaborative Learning Activities: Reflection",
    "lesson": "16",
    "section": "reflection",
    "order": 4
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_16_reflection"
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
    "lesson_16_reflection",
    "reflection",
    "Lesson 16: Reflection",
    """
    **This is where you reflect on what you've learned about collaborative learning activities.**
    
    ✨ **Important:** Completing this reflection by saving your responses will:
    - Mark Lesson 16 as complete
    - Unlock Lesson 17
    - Save your progress in the course
    
    Take a moment to consider how you can apply prompt engineering to enhance collaborative 
    learning in your teaching practice.
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
    st.markdown("## Reflection: Collaborative Learning Activities")
    
    st.info("✏️ **Note:** Completing this reflection marks your completion of Lesson 16. Take a moment to consolidate what you've learned before moving on to the next lesson.")
    
    st.markdown("""
    To conclude this lesson on collaborative learning activities, reflect on what you've 
    learned and how you might apply it in your teaching practice.
    """)
    
    # Reflection questions
    reflection1 = st.text_area(
        "What specific challenges have you faced when implementing collaborative learning activities, and how might prompt engineering help you address these challenges? Be specific about the strategies you would employ.",
        height=150,
        key="reflection1"
    )
    
    reflection2 = st.text_area(
        "Select a collaborative structure (Think-Pair-Share, Jigsaw, Problem-Based Learning, etc.) that you'd like to implement or improve in your teaching. How would you use the PCTFR framework to create an effective prompt for this structure? What elements would you include to ensure both positive interdependence and individual accountability?",
        height=200,
        key="reflection2"
    )
    
    reflection3 = st.text_area(
        "How might designing more effective collaborative learning experiences impact student engagement and learning outcomes in your classroom? Provide specific examples related to your teaching context.",
        height=150,
        key="reflection3"
    )
    
    # Check if at least one field has content for validation
    has_content = any([reflection1, reflection2, reflection3])

    # Calculate the next lesson path for direct navigation
    next_lesson_id = get_next_lesson_id(PAGE_INFO["lesson"])  # Should return "17"
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
    As you prepare to implement effective collaborative learning strategies in your teaching,
    consider this implementation framework:
    
    ### 1. Assess Current Practice and Readiness
    - Review your current approaches to collaborative learning
    - Identify specific challenges or pain points
    - Assess your students' collaboration skills and readiness
    - Determine what structures would best fit your content and context
    
    ### 2. Start with Structured, Short-Term Collaboration
    - Begin with highly structured formats (e.g., Think-Pair-Share)
    - Practice basic collaboration skills in brief activities
    - Establish clear protocols and expectations
    - Build student comfort and confidence gradually
    
    ### 3. Develop Comprehensive Collaboration Systems
    - Create templates for your most-used collaborative structures
    - Design flexible interdependence and accountability measures
    - Develop protocols that can be used across multiple contexts
    - Create a library of collaborative prompts for different purposes
    
    ### 4. Monitor, Reflect, and Refine
    - Observe group dynamics and participation patterns
    - Collect student feedback on collaborative experiences
    - Assess both content learning and collaboration skills
    - Refine your approach based on outcomes
    
    This systematic approach helps you integrate new practices effectively while building
    your students' capacity for meaningful collaboration over time.
    """)
    
    # Key takeaways
    st.markdown("## Key Takeaways")
    
    st.markdown("""
    * **Structure matters** - Well-designed collaborative activities balance structure and flexibility to promote meaningful interaction
      
    * **Interdependence is essential** - True collaboration requires designing situations where students genuinely need each other to succeed
      
    * **Balance group and individual accountability** - Effective collaborative learning assesses both collective and individual learning
      
    * **Collaboration skills require explicit teaching** - Don't assume students know how to collaborate effectively; teach and scaffold these skills
      
    * **The PCTFR framework enables comprehensive design** - This approach ensures all essential elements of collaborative learning are addressed
    """)
    
    # Connection to next lesson
    st.markdown("## Connection to Lesson 17: Personalized Learning Pathways")
    
    st.markdown("""
    In our next lesson, we'll explore how to apply prompt engineering to create personalized learning 
    experiences for students. This builds directly on what you've learned about collaborative learning:
    
    - **From group to individual** - While collaborative learning focuses on group experiences, 
      personalized learning tailors education to individual needs, preferences, and paths
    
    - **From single structure to multiple paths** - The principles of designing effective structures 
      will help you create multiple learning pathways that address diverse student needs
    
    - **From collective to individual accountability** - The accountability measures you've explored 
      for collaborative work transfer to monitoring and assessing individual progress through 
      personalized paths
    
    As you move into Lesson 17, consider how personalized learning complements collaborative 
    approaches to create a balanced instructional program that addresses both social learning 
    and individual growth.
    """)
    
    # Encouraging remark and segue
    st.markdown("---")
    st.markdown("""
    ## Excellent work on mastering collaborative learning design!
    
    You've now learned how to apply prompt engineering to create effective collaborative learning 
    experiences that promote both content mastery and social skill development. These approaches 
    will help you design more engaging, productive group work that benefits all students.
    
    In the next lesson, we'll explore Personalized Learning Pathways. You'll discover how to 
    design tailored learning experiences that address individual student needs, preferences, and 
    readiness levels while maintaining efficiency in your teaching practice.
    """)
    
    # Mark this page as viewed (completion is handled by save_reflection_and_navigate)
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator 
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Discussion Prompts:**
    
    * Ask participants to share one collaborative structure they plan to implement or improve
    * Discuss common barriers to effective collaboration in schools and potential solutions
    * Explore how departments or grade-level teams might collaborate on developing shared protocols
    * Consider how these approaches might be adapted for remote or hybrid learning environments
    
    **Looking Ahead:**
    
    In the next lesson on Personalized Learning Pathways, make connections to this lesson by emphasizing:
    - The complementary nature of collaborative and personalized approaches
    - How differentiation can occur within collaborative structures
    - The transferability of design principles from group to individual learning experiences
    
    **Assessment Opportunity:**
    
    The reflection questions provide insight into participants' understanding and application plans. Look for:
    - Specific connections between collaborative challenges and prompt engineering solutions
    - Thoughtful application of the PCTFR framework to a particular structure
    - Recognition of the impact of well-designed collaboration on student outcomes
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