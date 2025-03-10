import streamlit as st
import os
import sys
from utils.navigation import scroll_to_top
from utils.state_management import initialize_session_state, mark_page_completed
from utils.teacher_client import TeacherClient
from components.breadcrumb_navigator import render_breadcrumb
from components.bottom_navigator import render_bottom_navigator
from components.course_navigation import render_course_navigation
from components.top_navigator import render_top_navigator
from components.teacher_notes import render_teacher_notes
from components.first_visit_dialog import show_first_visit_dialog, PAGE_DESCRIPTIONS

# Initialize the TeacherClient
client = TeacherClient()

# Configure page
st.set_page_config(
    page_title="Course Activities",
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
    "title": "Course Activities",
    "lesson": "intro",
    "section": "activities",
    "order": 2
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "course_activities"
st.session_state.current_page = current_page

# Get all available pages for navigation
try:
    from utils.navigation import get_all_pages
    all_pages = get_all_pages()
except Exception as e:
    st.error(f"Error loading pages: {str(e)}")
    all_pages = []

# Scroll to top when page loads
scroll_to_top()

# Render teacher controls in the sidebar
st.sidebar.title("Teacher Controls")
st.sidebar.markdown("---")

# Teacher/Student toggle
st.sidebar.checkbox(
    "Show Teacher Content",
    value=st.session_state.show_teacher_content,
    key="toggle_teacher_content"
)

# Debug toggle in sidebar - Note the unique key
debug_key = f"toggle_debug_{PAGE_INFO['lesson']}_{PAGE_INFO['section']}"
st.sidebar.checkbox(
    "Show Debug Info",
    value=st.session_state.get("show_debug", False),
    key=debug_key
)

# Create main layout with content on the left and navigation on the right
content_col, nav_col = st.columns([4, 1])

# Render the main content area
with content_col:
    # Render breadcrumb navigation at the top
    render_breadcrumb(current_page)
    
    # Render section navigation at the top
    render_top_navigator(PAGE_INFO["lesson"], PAGE_INFO["section"])
    
    # Show first visit dialog with current section
    page_desc = PAGE_DESCRIPTIONS.get(current_page, {})
    show_first_visit_dialog(
        current_page,
        PAGE_INFO["section"],
        page_desc.get("title", "Welcome!"), 
        page_desc.get("message", "Welcome to this page!")
    )
    
    # Main content
    st.title("Course Activities")
    
    st.markdown("""
    In this section, you'll get hands-on experience with prompt engineering before diving into the course. 
    These introductory activities will help you understand your current approach to interacting with AI 
    and set a baseline for your learning journey.
    """)
    
    # Course progression note
    st.info("""
    **📚 Course Progression:** 
    
    These activities help establish your baseline skills. After completing these activities:
    
    1. Save your responses for each exercise to track your progress
    2. Complete the Reflection section (marked with ✨) to unlock Lesson 1
    """)
    
    # Activity 1: Your First Prompt Analysis
    st.markdown("## Activity 1: Analyze Your Current Prompting Style")
    
    st.markdown("""
    Let's start by analyzing how you currently interact with AI. This will give you a baseline 
    to measure your growth throughout this course.
    """)
    
    st.info("""
    **Instructions:**
    
    1. Think of a recent prompt you've given to an AI (like ChatGPT, Claude, or similar tool)
    2. Type that prompt in the box below
    3. Analyze your own prompt using the questions provided
    """)
    
    # Input for user's existing prompt
    existing_prompt = st.text_area(
        "Enter a prompt you've used recently:",
        height=100,
        placeholder="Example: Create a lesson plan for teaching fractions to 4th graders.",
        key="existing_prompt"
    )
    
    # Self-analysis questions
    if existing_prompt:
        st.markdown("### Analyze Your Prompt")
        
        st.markdown("""
        Answer these questions about your prompt:
        """)
        
        specificity = st.radio(
            "1. How specific is your prompt?",
            ["Very vague", "Somewhat vague", "Somewhat specific", "Very specific"],
            key="specificity"
        )
        
        structure = st.radio(
            "2. How structured is your prompt?",
            ["No clear structure", "Minimal structure", "Some structure", "Highly structured"],
            key="structure"
        )
        
        context = st.radio(
            "3. How much context did you provide?",
            ["No context", "Minimal context", "Some context", "Rich context"],
            key="context"
        )
        
        expectations = st.text_area(
            "4. What could you add to make your expectations clearer?",
            height=100,
            key="expectations"
        )
        
        if st.button("Save Analysis", key="save_analysis"):
            st.session_state.setdefault("intro_activities", {})
            st.session_state.intro_activities["prompt_analysis"] = {
                "existing_prompt": existing_prompt,
                "specificity": specificity,
                "structure": structure,
                "context": context,
                "expectations": expectations
            }
            st.success("Your analysis has been saved!")
    
    # Activity 2: Prompt Engineering Preview
    st.markdown("## Activity 2: Experiment with a Simple Framework")
    
    st.markdown("""
    Now, let's experiment with a simple prompt engineering framework to see how it impacts 
    the AI's response. We'll use a basic version of the framework you'll learn in this course.
    """)
    
    st.info("""
    **Instructions:**
    
    1. Choose an educational topic you're interested in
    2. Fill in the Task, Audience, and Format fields below
    3. Generate a prompt using this simple framework
    4. Test your engineered prompt with the AI
    """)
    
    # Simple framework inputs
    topic = st.text_input(
        "Educational Topic:",
        placeholder="Example: Photosynthesis, Civil War, Fractions, Literary Devices...",
        key="topic"
    )
    
    if topic:
        task = st.text_input(
            "Task: What do you want the AI to do?",
            placeholder="Example: Create, explain, summarize, generate questions...",
            key="task"
        )
        
        audience = st.text_input(
            "Audience: Who is this for?",
            placeholder="Example: 3rd graders, high school biology students, new teachers...",
            key="audience"
        )
        
        format_input = st.text_input(
            "Format: How should the output be structured?",
            placeholder="Example: 5-item list, 3-paragraph summary, table with examples...",
            key="format_input"
        )
        
        # Generate the engineered prompt
        if task and audience and format_input:
            engineered_prompt = f"{task} about {topic} for {audience}. Present the information as {format_input}."
            
            st.markdown("### Your Engineered Prompt:")
            st.code(engineered_prompt)
            
            # Test the prompt
            if st.button("Test This Prompt", key="test_prompt"):
                try:
                    with st.spinner("Getting response from AI..."):
                        response = client.send_prompt(engineered_prompt)
                        
                        # Store in session state
                        st.session_state.setdefault("intro_activities", {})
                        st.session_state.intro_activities["engineered_prompt"] = {
                            "prompt": engineered_prompt,
                            "response": response['response']
                        }
                        
                        # Display the response
                        st.markdown("### AI Response:")
                        st.markdown(response['response'])
                        
                        # Reflection questions
                        st.markdown("### Reflect:")
                        st.markdown("""
                        - How does this response compare to what you might have received with a simpler prompt?
                        - What impact did specifying the audience have?
                        - How did the format specification help structure the output?
                        """)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    # Activity 3: Course Goals
    st.markdown("## Activity 3: Set Your Learning Goals")
    
    st.markdown("""
    Finally, let's set some personal learning goals for this course to help you focus your learning.
    """)
    
    goal1 = st.text_area(
        "What specific skill related to prompt engineering do you most want to develop?",
        height=100,
        key="goal1"
    )
    
    goal2 = st.text_area(
        "How do you plan to apply prompt engineering in your professional practice?",
        height=100,
        key="goal2"
    )
    
    goal3 = st.text_area(
        "What specific challenge or task are you hoping to solve with better prompt engineering?",
        height=100,
        key="goal3"
    )
    
    if st.button("Save My Goals", key="save_goals") and (goal1 or goal2 or goal3):
        st.session_state.setdefault("intro_activities", {})
        st.session_state.intro_activities["learning_goals"] = {
            "skill_development": goal1,
            "application_plans": goal2,
            "specific_challenge": goal3
        }
        # Mark page as completed when goals are saved
        mark_page_completed(current_page)
        st.success("Your learning goals have been saved!")
    
    # Next steps
    st.success("""
    **Next Steps:**
    
    Now that you've completed these activities, take time to reflect on your experience and 
    set your learning goals in the Reflection section to unlock Lesson 1.
    """)
    
    # Button for reflection
    if st.button("Complete Reflection ✨", key="go_to_reflection", type="primary", use_container_width=False):
        try:
            st.switch_page("pages/course_reflection.py")
        except Exception as e:
            st.error(f"Error navigating to Reflection: {str(e)}")
    
    # Add bottom navigator - mirrors the top navigator
    render_bottom_navigator(PAGE_INFO)
    
    # Mark page as completed when viewed
    mark_page_completed(current_page)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Facilitation Notes:**
    
    * These introductory activities help establish baseline prompting habits and set personal learning goals
    * Activity 1 encourages metacognition about current prompting practices
    * Activity 2 provides a simple taste of how framework-based prompting improves results
    * Activity 3 helps personalize the learning journey for each participant
    
    **Discussion Prompts:**
    
    * Ask participants to share insights from analyzing their own prompts
    * Discuss common patterns in how people naturally prompt AI systems
    * Have participants share their learning goals to identify common themes
    
    **Key Points to Emphasize:**
    
    * Most people start with very simple, unstructured prompts
    * Even minimal structure dramatically improves results
    * Prompt engineering is a skill that develops with practice and reflection
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