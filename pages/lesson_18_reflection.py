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
from components.progress_manager import render_teacher_controls_sidebar

# Configure page
st.set_page_config(
    page_title="Lesson 18: Reflection",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Get the current directory and add to path if needed
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Page metadata
PAGE_INFO = {
    "title": "Interdisciplinary Unit Design: Reflection",
    "lesson": "18",
    "section": "reflection",
    "order": 4
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_18_reflection"
st.session_state.current_page = current_page

# Get all available pages for navigation
try:
    all_pages = get_all_pages()
except Exception as e:
    st.error(f"Error loading pages: {str(e)}")
    all_pages = []

# Scroll to top when page loads
scroll_to_top()

# Course completion page path
completion_page_path = "/home/tsilver/code/workflowBuilder/electricShepherdUI/prompting-courseV2/pages/lesson_Complete.py"

# Show the first visit dialog if this is the first time visiting this page
show_first_visit_dialog(
    "lesson_18_reflection",
    "reflection",
    "Lesson 18: Reflection",
    """
    **This is where you reflect on what you've learned about interdisciplinary unit design.**
    
    ✨ **Important:** Completing this reflection by saving your responses will:
    - Mark Lesson 18 as complete
    - Complete the entire course
    - Save your progress
    
    Take a moment to consider how you can apply prompt engineering to enhance interdisciplinary learning
    in your teaching practice.
    """
)

# Check if the user has completed the course
already_completed = current_page in st.session_state.get("completed_pages", [])

# Render the teacher controls in the sidebar
render_teacher_controls_sidebar()

# Create main layout with content area on the left and navigation on the right
content_col, nav_col = st.columns([4, 1])

# Render the main content area
with content_col:
    # Display the normal reflection content
    # Render breadcrumb navigation at the top
    render_breadcrumb(current_page)
    
    # Render section navigation at the top
    render_top_navigator(PAGE_INFO["lesson"], PAGE_INFO["section"])
    
    # Main content
    st.markdown("## Reflection: Interdisciplinary Unit Design")
    
    st.info("✏️ **Note:** Completing this reflection marks your completion of Lesson 18 and the entire course. Take a moment to consolidate what you've learned before finishing the course.")
    
    st.markdown("""
    To conclude this lesson on interdisciplinary unit design, reflect on what you've 
    learned and how you might apply it in your teaching practice.
    """)
    
    # Reflection questions
    reflection1 = st.text_area(
        "What opportunities for interdisciplinary connections exist in your teaching context? Which subject areas or concepts would be most beneficial to integrate, and why?",
        height=150,
        key="reflection1"
    )
    
    reflection2 = st.text_area(
        "What challenges do you anticipate when designing interdisciplinary units, and how might prompt engineering help you address these challenges?",
        height=150,
        key="reflection2"
    )
    
    reflection3 = st.text_area(
        "Select one specific interdisciplinary connection you could implement in your teaching. Describe how you would use the PCTFR framework to create a prompt for an integrated learning experience that maintains the integrity of each discipline while creating meaningful connections.",
        height=200,
        key="reflection3"
    )
    
    # Check if at least one field has content for validation
    has_content = any([reflection1, reflection2, reflection3])

    # If already completed, show the completion page button
    if already_completed:
        st.success(f"🎉 You've already completed this reflection and the entire course!")
        if st.button("View Course Completion Certificate", key="view_completion", type="primary", use_container_width=True):
            try:
                st.switch_page(completion_page_path)
            except Exception as e:
                st.error(f"Error navigating to completion page: {str(e)}")
                st.error(f"Path tried: {completion_page_path}")
    else:
        # Save and navigate to completion page button with validation
        if st.button("Save Reflections & Complete Course", key="save_reflections", 
                    type="primary", use_container_width=True, disabled=not has_content):
            if has_content:
                # Prepare reflection data
                reflection_data = {
                    "reflection1": reflection1,
                    "reflection2": reflection2,
                    "reflection3": reflection3
                }
                
                # Save reflection data
                if "lesson_reflections" not in st.session_state:
                    st.session_state.lesson_reflections = {}
                
                st.session_state.lesson_reflections[PAGE_INFO["lesson"]] = reflection_data
                
                # Mark this page as completed
                if "completed_pages" not in st.session_state:
                    st.session_state.completed_pages = []
                
                if current_page not in st.session_state.completed_pages:
                    st.session_state.completed_pages.append(current_page)
                
                # Navigate to the completion page
                try:
                    st.switch_page(completion_page_path)
                except Exception as e:
                    st.error(f"Error navigating to completion page: {str(e)}")
                    st.error(f"Path tried: {completion_page_path}")
            else:
                st.warning("Please fill in at least one of the reflection fields.")
        
        # Implementation Planning
        st.markdown("## Implementation Planning")
        
        st.markdown("""
        As you prepare to implement interdisciplinary unit design in your teaching practice,
        consider this implementation framework:
        
        ### 1. Identify Meaningful Connection Points
        - Look for natural conceptual overlaps between disciplines
        - Focus on big ideas, essential questions, or shared processes
        - Consider standards from different subjects that complement each other
        - Identify topics that benefit from multiple disciplinary perspectives
        
        ### 2. Maintain Disciplinary Integrity
        - Ensure each subject's key standards and skills are addressed
        - Define clear learning goals for each discipline involved
        - Avoid sacrificing depth for breadth in connections
        - Keep the authentic methodologies of each discipline
        
        ### 3. Design Clear Learning Progressions
        - Create logical sequences that build understanding across disciplines
        - Develop assessments that evaluate both disciplinary and integrated learning
        - Build in checkpoints to ensure all subject areas are being addressed
        - Plan for how disciplines will converge and diverge throughout the unit
        
        ### 4. Collaborate Effectively
        - Partner with colleagues from different subject areas when possible
        - Anticipate logistical challenges in scheduling and coordination
        - Develop shared vocabulary for interdisciplinary concepts
        - Create systems for co-planning and co-assessment
        
        This systematic approach helps you implement interdisciplinary learning that maintains
        disciplinary rigor while creating meaningful connections for students.
        """)
        
        # Key takeaways
        st.markdown("## Key Takeaways")
        
        st.markdown("""
        * **Authentic connections matter** - Effective interdisciplinary units focus on natural conceptual relationships rather than forced connections
          
        * **Disciplinary integrity remains crucial** - Integrated learning should strengthen rather than dilute subject-specific learning
          
        * **Clear frameworks provide structure** - Organizing structures like essential questions, themes, or problems help frame integrated learning
          
        * **Prompt engineering facilitates integration** - Well-designed prompts can help generate materials that maintain both disciplinary integrity and meaningful connections
          
        * **Balance is essential** - Successful interdisciplinary units balance breadth of connections with depth of disciplinary understanding
        """)
        
        # Course Completion Note
        st.markdown("## Course Completion")
        
        st.markdown("""
        ### Congratulations on Reaching the End of the Course!
        
        This reflection marks the final lesson in our Prompt Engineering for Educators course. 
        By completing this reflection, you'll have finished the entire curriculum and gained a 
        comprehensive understanding of how to use AI prompting techniques to enhance your teaching 
        practice.
        
        After saving your reflection, you'll be directed to a course completion page with additional 
        resources and opportunities to continue your AI in education journey.
        
        We hope this course has provided valuable insights and practical skills that you can apply 
        immediately in your classroom!
        """)
        
        # Mark this page as viewed (completion is handled separately)
        mark_page_completed(current_page)
        
        # Add horizontal bottom navigator 
        render_bottom_navigator(PAGE_INFO)
        
        # Teacher-specific notes
        render_teacher_notes("""
        **Discussion Prompts:**
        
        * Ask participants which interdisciplinary connections they found most promising
        * Discuss logistical challenges of implementing interdisciplinary units and potential solutions
        * Explore how colleagues from different departments might collaborate on prompt development
        * Consider how to assess both disciplinary and interdisciplinary learning
        
        **Course Reflection:**
        
        As this is the final lesson of the course, encourage participants to:
        - Create an implementation plan for incorporating prompt engineering into their practice
        - Set specific goals for applying various techniques from the course
        - Connect with other course participants to share ideas and experiences
        - Consider how they might share their new knowledge with colleagues
        
        **Assessment Opportunity:**
        
        The reflection questions provide insight into participants' understanding and application plans. Look for:
        - Recognition of authentic connection points between disciplines
        - Thoughtful analysis of implementation challenges and potential solutions
        - Application of the PCTFR framework to specific interdisciplinary contexts
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
        st.write(f"Already Completed: {already_completed}")
        st.write(f"Completion Page Path: {completion_page_path}") 