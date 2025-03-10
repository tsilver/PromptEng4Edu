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
    page_title="Lesson 3: Activities",
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
    "title": "Defining the Task: Activities",
    "lesson": "3",
    "section": "activities",
    "order": 3
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_3_activities"
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
    "lesson_3_activities",
    "activities",
    "Lesson 3 Activities",
    """
    **This section provides hands-on practice with task definition in prompting.**
    
    You'll:
    - Transform vague tasks into specific, actionable ones
    - Practice selecting effective action verbs
    - Apply task definition principles to educational scenarios
    
    Complete these activities to strengthen your understanding before 
    moving to the reflection.
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
    st.markdown(f"# Activities: {PAGE_INFO['title']}")
    
    # Add a progress note 
    st.info("""
    **📝 Course Progression Note:** 
    
    Complete the activities below to practice defining tasks in your prompts.
    After finishing these activities, proceed to the Reflection section to solidify your learning 
    and unlock the next lesson.
    """)
    
    # Activity 1
    st.markdown("## Activity 1: Transform Vague Tasks")
    
    st.markdown("""
    For each vague task below, rewrite it to be more specific and actionable.
    Focus on using clear action verbs and adding appropriate parameters.
    """)
    
    # Vague task 1
    st.markdown("### Vague Task 1: 'Give me some writing prompts.'")
    
    improved_task1 = st.text_area(
        "Your improved task:", 
        height=100,
        placeholder="Example: Generate 5 creative writing prompts for high school students that focus on themes of identity and belonging. Each prompt should include a scenario, character suggestion, and a central conflict.",
        key="improved_task1"
    )
    
    if improved_task1:
        st.success("You've improved the task definition! Look for these elements in your rewrite:")
        
        st.markdown("""
        - Did you use a specific action verb? (e.g., generate, create, develop)
        - Did you specify a quantity? (how many prompts)
        - Did you add audience information? (what level/age)
        - Did you include topic or theme constraints?
        - Did you provide format details?
        """)
    
    # Vague task 2
    st.markdown("### Vague Task 2: 'Help with a science lesson.'")
    
    improved_task2 = st.text_area(
        "Your improved task:", 
        height=100,
        placeholder="Example: Design a 45-minute inquiry-based science lesson on the properties of magnets for 3rd-grade students. Include a hands-on experiment using common materials, 3 key learning objectives, and a formative assessment strategy.",
        key="improved_task2"
    )
    
    if improved_task2:
        st.success("You've improved the task definition! Look for these elements in your rewrite:")
        
        st.markdown("""
        - Did you specify what type of science and topic?
        - Did you include time constraints?
        - Did you clarify the teaching approach?
        - Did you specify grade level?
        - Did you add components that should be included?
        """)
    
    # Activity 2
    st.markdown("## Activity 2: Action Verb Practice")
    
    st.markdown("""
    Choose the most effective action verb for each educational scenario below.
    Consider what specific outcome you want from the AI.
    """)
    
    # Scenario 1
    st.markdown("### Scenario 1: You want the AI to help students understand a complex concept.")
    
    action_verb1 = st.radio(
        "Which action verb would be most effective?",
        ["Tell", "Write", "Explain", "Make"],
        key="action_verb1"
    )
    
    if action_verb1 == "Explain":
        st.success("Great choice! 'Explain' is ideal when you want the AI to break down complex concepts in an understandable way.")
    else:
        st.info(f"'{action_verb1}' could work, but 'Explain' might be more effective when you want the AI to break down complex concepts in an understandable way.")
    
    # Scenario 2
    st.markdown("### Scenario 2: You want the AI to provide a condensed version of key points from an article.")
    
    action_verb2 = st.radio(
        "Which action verb would be most effective?",
        ["Shorten", "Summarize", "Cut", "Review"],
        key="action_verb2"
    )
    
    if action_verb2 == "Summarize":
        st.success("Great choice! 'Summarize' specifically asks for a condensed version that retains the key points.")
    else:
        st.info(f"'{action_verb2}' could work, but 'Summarize' specifically asks for a condensed version that retains the key points.")
    
    # Activity 3
    st.markdown("## Activity 3: Educational Task Builder")
    
    st.markdown("""
    Build a well-defined task for an educational prompt by filling in each component below.
    You'll see your complete task take shape as you add each element.
    """)
    
    # Educational scenario selection
    scenario = st.selectbox(
        "Select an educational scenario:",
        [
            "Creating a lesson plan",
            "Developing assessment questions",
            "Providing student feedback",
            "Differentiating instruction",
            "Creating educational materials"
        ],
        key="ed_scenario"
    )
    
    # Task components
    action_verb = st.text_input("Action verb:", placeholder="Example: design, create, develop, analyze", key="action_verb")
    specifics = st.text_input("Specifics (what exactly):", placeholder="Example: a 30-minute lesson plan, 10 assessment questions", key="specifics")
    subject = st.text_input("Subject/Topic:", placeholder="Example: photosynthesis, World War II, fractions", key="subject")
    audience = st.text_input("Audience/Grade level:", placeholder="Example: 5th grade, high school AP students", key="audience")
    additional_params = st.text_area("Additional parameters:", placeholder="Example: using active learning strategies, including visual elements, with a formative assessment component", key="additional_params")
    
    # Show the complete task
    if action_verb and specifics:
        st.markdown("### Your Complete Task:")
        
        complete_task = f"{action_verb} {specifics}"
        if subject:
            complete_task += f" on {subject}"
        if audience:
            complete_task += f" for {audience}"
        if additional_params:
            complete_task += f" {additional_params}"
        
        st.code(complete_task)
        
        st.markdown("""
        **Task Effectiveness Analysis:**
        
        Rate your task on these criteria:
        - **Clarity**: Is it immediately clear what the AI should produce?
        - **Specificity**: Have you included enough detail to guide the output?
        - **Action-oriented**: Does it start with a strong action verb?
        - **Parameters**: Have you included important constraints or requirements?
        - **Relevance**: Is it tailored to your educational context?
        """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * For Activity 1, encourage participants to share their rewrites and discuss the differences
    * For Activity 2, discuss why certain verbs are more effective in different educational contexts
    * For Activity 3, consider having participants exchange their created tasks and evaluate each other's effectiveness
    
    **Common Mistakes to Address:**
    
    * Using vague verbs like "talk about" or "discuss" instead of precise actions
    * Creating tasks that are too broad or too narrow
    * Forgetting to include important parameters like grade level or time constraints
    * Writing overly complex tasks with too many requirements
    
    **Extension Ideas:**
    
    * Have participants create a personal "action verb library" specific to their teaching area
    * Challenge participants to identify the three most common tasks they might need AI assistance with
    * Discuss how task definition differs based on subject area (math vs. language arts vs. science)
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

# Debug section at the bottom (now controlled by the teacher controls sidebar)
if st.session_state.get("show_debug", False):
    with st.expander("Debug Information", expanded=True):
        st.write("### Debug Info")
        st.write(f"Current Page: {current_page}")
        st.write(f"Current Directory: {current_dir}")
        st.write(f"Pages Directory: {os.path.join(current_dir, 'pages')}")
        st.write(f"sys.path: {sys.path}")
        st.write(f"All Pages: {all_pages}")
        st.write(f"Session State: {dict(st.session_state)}") 