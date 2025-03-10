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
    page_title="Lesson 15: Reflection",
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
    "title": "Discussion Questions and Content Creation: Reflection",
    "lesson": "15",
    "section": "reflection",
    "order": 4
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_15_reflection"
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
    "lesson_15_reflection",
    "reflection",
    "Lesson 15: Reflection",
    """
    **This is where you reflect on what you've learned about discussion questions and content creation.**
    
    ✨ **Important:** Completing this reflection by saving your responses will:
    - Mark Lesson 15 as complete
    - Unlock Lesson 16
    - Save your progress in the course
    
    Take a moment to consider how you can apply prompt engineering to enhance discussion and content
    in your teaching practice.
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
    st.markdown("## Reflection: Discussion Questions and Content Creation")
    
    st.info("✏️ **Note:** Completing this reflection marks your completion of Lesson 15. Take a moment to consolidate what you've learned before moving on to the next lesson.")
    
    st.markdown("""
    To conclude this lesson on discussion questions and content creation, reflect on what you've 
    learned and how you might apply it in your teaching practice.
    """)
    
    # Reflection questions
    reflection1 = st.text_area(
        "What types of discussion questions do you find most challenging to create, and how might prompt engineering help you address these challenges? Be specific about how you would structure a prompt to generate these types of questions.",
        height=150,
        key="reflection1"
    )
    
    reflection2 = st.text_area(
        "Identify a specific upcoming unit or lesson where you could use prompt engineering to create instructional content. What type of content would you request, and what key elements would you include in your prompt?",
        height=150,
        key="reflection2"
    )
    
    reflection3 = st.text_area(
        "How might creating better discussion questions and instructional content using prompt engineering impact student engagement and learning outcomes in your classroom? Provide specific examples from your teaching context.",
        height=150,
        key="reflection3"
    )
    
    # Check if at least one field has content for validation
    has_content = any([reflection1, reflection2, reflection3])

    # Calculate the next lesson path for direct navigation
    next_lesson_id = get_next_lesson_id(PAGE_INFO["lesson"])  # Should return "16"
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
    As you prepare to implement effective discussion question and content creation strategies in your teaching,
    consider this implementation framework:
    
    ### 1. Analyze Current Practice
    - Review your current approach to discussion questions and instructional materials
    - Identify areas where differentiation is most needed
    - Note which types of content take the most time to create
    
    ### 2. Prioritize Applications
    - Start with one type of content that would have the greatest impact
    - Focus on discussion questions for key topics or challenging concepts
    - Select units where more differentiated materials would benefit students
    
    ### 3. Create Prompt Templates
    - Develop framework prompts for your most common content needs
    - Save successful prompts as templates for future use
    - Create a personal library organized by content type and purpose
    
    ### 4. Integrate with Planning Routine
    - Establish a workflow for incorporating prompt engineering
    - Schedule time for review and refinement of generated content
    - Develop a system for organizing and accessing your materials
    
    This systematic approach helps you integrate new practices effectively while managing
    your time and maximizing the impact on student learning.
    """)
    
    # Key takeaways
    st.markdown("## Key Takeaways")
    
    st.markdown("""
    * **Cognitive levels matter** - Effective discussion questions target multiple levels of thinking and follow a logical sequence
      
    * **PCTFR framework enhances quality** - This comprehensive approach ensures generated questions and content are aligned with your specific context
      
    * **Differentiation requires specificity** - Clearly articulated differentiation strategies in prompts lead to more inclusive content
      
    * **Content format affects learning** - Different instructional formats serve different purposes; choose intentionally based on learning goals
      
    * **Prompt engineering saves time** - Creating effective templates allows you to generate high-quality materials efficiently
    """)
    
    # Connection to next lesson
    st.markdown("## Connection to Lesson 16: Collaborative Learning Activities")
    
    st.markdown("""
    In our next lesson, we'll explore how to apply prompt engineering to create effective collaborative 
    learning experiences for students. This builds directly on what you've learned about discussion 
    questions and content creation:
    
    - **From discussion to collaboration:** The principles of crafting thought-provoking questions 
      transfer directly to designing collaborative tasks that promote meaningful interaction
    
    - **From content to activities:** The skills you've developed in creating instructional content 
      will help you design engaging collaborative activities with clear learning goals
    
    - **From individual to group learning:** You'll expand your prompt engineering toolkit to address 
      the unique challenges and opportunities of peer-to-peer learning
    
    As you move into Lesson 16, consider how collaborative learning builds on effective questions and 
    content to create powerful learning experiences for all students.
    """)
    
    # Encouraging remark and segue
    st.markdown("---")
    st.markdown("""
    ## Well done on mastering discussion questions and content creation!
    
    You've now learned how to apply prompt engineering to create thought-provoking discussion questions 
    and effective instructional content. These skills will help you engage students in deeper thinking 
    while saving valuable planning time.
    
    In the next lesson, we'll continue exploring applications of prompt engineering by focusing on 
    collaborative learning activities. You'll discover how to design effective group experiences that 
    promote meaningful interaction and collective knowledge construction.
    """)
    
    # Mark this page as viewed (completion is handled by save_reflection_and_navigate)
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator 
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Discussion Prompts:**
    
    * Ask participants to share one prompt they've created that they're particularly proud of
    * Discuss how departments or grade-level teams might collaborate on creating a shared prompt library
    * Explore how these techniques might transform planning processes and time allocation
    * Consider how these skills might support new teachers or those teaching new content
    
    **Looking Ahead:**
    
    In the next lesson on Collaborative Learning Activities, make connections to this lesson by emphasizing:
    - How effective discussion questions form the foundation of productive group activities
    - The importance of well-designed instructional content in scaffolding collaborative work
    - The transferability of differentiation strategies to group learning contexts
    
    **Assessment Opportunity:**
    
    The reflection questions provide insight into participants' understanding and application plans. Look for:
    - Specific mention of prompt components they found most valuable
    - Concrete plans for implementation in their own context
    - Recognition of the connection between quality questions/content and student outcomes
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