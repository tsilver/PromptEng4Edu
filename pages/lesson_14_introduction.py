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
    page_title="Lesson 14: Student Feedback and Writing Prompts",
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
    "title": "Student Feedback and Writing Prompts",
    "lesson": "14",
    "section": "introduction",
    "order": 1
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_14_introduction"
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
    "lesson_14_introduction",
    "introduction",
    "Lesson 14: Student Feedback and Writing Prompts",
    """
    **Welcome to Lesson 14 on Student Feedback and Writing Prompts!**
    
    In this lesson, you'll learn:
    - How to apply prompt engineering techniques to generate effective student feedback
    - Strategies for creating engaging, standards-aligned writing prompts
    - Techniques for personalizing feedback while maintaining consistency
    - Approaches for differentiating writing tasks for diverse learners
    
    These applications help you support student growth through targeted feedback and meaningful writing opportunities.
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
    st.markdown(f"# Lesson 14: {PAGE_INFO['title']}")
    
    # Objective
    st.markdown("## Objective")
    st.markdown("""
    To apply prompt engineering techniques to generate effective student feedback and create engaging
    writing prompts that develop students' skills, support their growth, and align with educational goals.
    """)
    
    # Real-world hook
    st.info("""
    ### Real-World Hook
    
    Research shows that specific, actionable feedback is one of the most powerful tools for improving 
    student learning, with effect sizes ranging from 0.5 to 0.7 (Hattie & Timperley, 2007). However, 
    providing personalized, high-quality feedback to every student is time-consuming. Similarly, creating 
    engaging writing prompts that develop specific skills requires significant creative energy. With effective 
    prompt engineering, you can generate individualized feedback and powerful writing tasks more efficiently, 
    allowing you to maintain high-quality instructional practices while saving valuable time.
    """)
    
    # Application Focus
    st.markdown("## Applying Your Prompt Engineering Skills")
    
    st.markdown("""
    In this lesson, we'll focus on applying prompt engineering techniques to two essential teaching tasks:
    
    1. **Student Feedback**: Providing personalized, growth-oriented responses to student work
    2. **Writing Prompts**: Creating engaging writing tasks that develop specific skills and knowledge
    
    These applications build on the techniques you've learned throughout the course:
    
    - **The PTC-FREI Framework**: Especially valuable for structuring complex feedback and writing tasks
    - **Role Prompting**: Creating appropriate voice and tone for different feedback situations
    - **Chain-of-Thought**: Modeling thinking processes for students in feedback
    - **Few-Shot Examples**: Ensuring consistency across multiple feedback instances
    """)
    
    # Student Feedback Strategies
    st.markdown("## Prompt Engineering for Student Feedback")
    
    st.markdown("""
    Effective feedback should:
    
    - Be specific and actionable
    - Focus on the task, process, or self-regulation (not just the person)
    - Connect to learning goals and success criteria
    - Identify strengths as well as areas for growth
    - Provide clear next steps for improvement
    
    By using prompt engineering techniques, you can generate feedback that incorporates 
    these principles while tailoring responses to individual students and assignments.
    """)
    
    # Feedback prompting strategies
    st.markdown("### Key Strategies for Feedback Prompting")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Effective Techniques
        
        **🔹 Use Role Prompting**
        - Select an appropriate feedback persona (e.g., supportive coach, subject expert)
        - Specify tone (encouraging, straightforward, conversational)
        
        **🔹 Provide Context**
        - Include assignment details and success criteria
        - Specify student characteristics or needs
        
        **🔹 Use Few-Shot Examples**
        - Provide examples of high-quality feedback
        - Include samples of different feedback styles
        """)
    
    with col2:
        st.markdown("""
        #### Common Pitfalls to Avoid
        
        **🔸 Generic Feedback**
        - Request specific references to student work
        - Avoid general praise without specific examples
        
        **🔸 Overwhelming Feedback**
        - Set priorities for feedback (e.g., focus on 2-3 key areas)
        - Balance strengths and growth areas
        
        **🔸 One-Size-Fits-All Approach**
        - Specify student's prior performance or skill level
        - Include accommodations for diverse learners
        """)
    
    # Structure of effective feedback
    st.markdown("### Structure of Effective Feedback")
    
    st.markdown("""
    When designing prompts for feedback generation, consider including these elements:
    
    | Feedback Component | Description | Example Prompt Language |
    |-------------------|-------------|-------------------------|
    | **Acknowledgment** | Recognize effort or specific achievement | "Begin with recognition of the student's effort on [specific aspect]" |
    | **Strength Identification** | Highlight what was done well | "Identify 2-3 specific strengths in the work, with examples from their submission" |
    | **Growth Areas** | Identify opportunities for improvement | "Suggest 1-2 key areas for improvement that would have the most impact" |
    | **Specific Guidance** | Provide actionable next steps | "Offer concrete strategies or examples for addressing each growth area" |
    | **Connection to Goals** | Link feedback to learning objectives | "Connect feedback to the learning objective of [specific goal]" |
    | **Forward-Looking** | Focus on future application | "Include a challenge question or next step that extends their thinking" |
    
    Different assignments and grade levels may emphasize different components, but this 
    structure provides a comprehensive framework for effective feedback.
    """)
    
    # Writing Prompts Strategies
    st.markdown("## Prompt Engineering for Writing Prompts")
    
    st.markdown("""
    Effective writing prompts should:
    
    - Engage student interest and curiosity
    - Target specific writing skills or standards
    - Provide clear expectations and success criteria
    - Offer appropriate scaffolding
    - Allow for creativity and personal connection
    
    Creating prompts that balance these elements requires careful design, which can be 
    facilitated through prompt engineering techniques.
    """)
    
    # Writing prompt strategies
    st.markdown("### Key Strategies for Writing Prompt Creation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Effective Techniques
        
        **🔹 Specify Writing Type and Purpose**
        - Clarify genre (narrative, informational, argumentative)
        - Define audience and purpose
        
        **🔹 Include Cognitive Elements**
        - Request interesting hooks or thought experiments
        - Incorporate creative constraints or challenges
        
        **🔹 Provide Clear Success Criteria**
        - Specify length, structure, or required elements
        - Include assessment criteria or rubric elements
        """)
    
    with col2:
        st.markdown("""
        #### Common Pitfalls to Avoid
        
        **🔸 Overly Broad Topics**
        - Focus on specific aspects rather than general subjects
        - Provide context or scenario to focus writing
        
        **🔸 Insufficient Scaffolding**
        - Include planning questions or prewriting activities
        - Request examples or models for different skill levels
        
        **🔸 Disconnect from Standards**
        - Reference specific standards or skills being developed
        - Align with curriculum and instructional sequence
        """)
    
    # Types of writing prompts
    st.markdown("### Types of Writing Prompts")
    
    st.markdown("""
    Different writing purposes call for different types of prompts. You can generate a variety
    of writing tasks using prompt engineering:
    
    | Writing Type | Characteristics | Example Prompt Elements |
    |--------------|----------------|-------------------------|
    | **Narrative** | Tells a story, real or imagined | "Create a prompt with a compelling scenario, character, or conflict starter" |
    | **Informative/Explanatory** | Conveys information clearly | "Develop a prompt that requires explaining a concept, process, or phenomenon" |
    | **Argumentative** | Makes a claim supported by evidence | "Design a prompt with a debatable issue and requirements for evidence types" |
    | **Analytical** | Examines parts of a whole | "Create a prompt requiring analysis of text, data, or media with specific focus areas" |
    | **Creative** | Emphasizes imagination and expression | "Generate a prompt with creative constraints that spark imagination while developing skills" |
    | **Reflective** | Explores personal thoughts and experiences | "Design a prompt that connects content to personal experiences or learning journey" |
    
    By specifying the type of writing and its key characteristics in your prompt, you'll generate
    more focused and effective writing tasks for your students.
    """)
    
    # Combining Feedback and Writing
    st.markdown("## The Instructional Cycle: Connecting Feedback and Writing")
    
    st.markdown("""
    Feedback and writing prompts work together in the instructional cycle:
    
    1. **Planning**: Create standards-aligned writing prompts that target specific skills
    2. **Instruction**: Provide direct instruction and models for the writing task
    3. **Writing**: Students compose responses to the prompts
    4. **Feedback**: Provide specific, actionable feedback on student writing
    5. **Revision**: Students apply feedback in revised writing or new tasks
    
    Prompt engineering can support multiple points in this cycle, creating a coherent
    instructional approach that develops student writing skills systematically.
    """)
    
    # Examples preview
    st.markdown("""
    In the Examples section, you'll see specific prompts for generating both student feedback
    and writing tasks across different grade levels and subject areas. The Activities section
    will then give you hands-on practice creating your own prompts for these important
    teaching tasks.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Emphasize that AI-generated feedback should be reviewed and personalized by the teacher before being shared with students
    * Point out that prompt engineering for feedback can help ensure consistency across multiple students while still allowing for personalization
    * Suggest using these techniques for creating exemplars that show students what good writing looks like in response to prompts
    * Remind participants that effective feedback focuses on growth and improvement, not just evaluation
    
    **Implementation Ideas:**
    
    * Start with a smaller writing task or subset of student work to practice using AI for feedback
    * Consider creating a bank of writing prompts for different standards that can be used throughout the year
    * Use AI-generated writing prompts as starting points that can be refined and customized
    * Combine feedback templates with student-specific observations for efficient yet personalized responses
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