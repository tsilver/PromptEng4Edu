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
    page_title="Lesson 4: Activities",
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
    "title": "Specifying Format: Activities",
    "lesson": "4",
    "section": "activities",
    "order": 3
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_4_activities"
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
    "lesson_4_activities",
    "activities",
    "Lesson 4 Activities",
    """
    **This section provides hands-on practice with format specification in prompting.**
    
    You'll:
    - Transform basic prompts by adding format specifications
    - Match different educational needs with appropriate formats
    - Create complete prompts combining context, task, and format
    
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
    
    Complete the activities below to practice specifying formats in your prompts.
    After finishing these activities, proceed to the Reflection section to solidify your learning 
    and unlock the next lesson.
    """)
    
    # Activity 1
    st.markdown("## Activity 1: Add Format Specifications")
    
    st.markdown("""
    For each basic prompt below, add a specific format specification to make the output more useful.
    Consider what structure would best suit the content and purpose.
    """)
    
    # Basic prompt 1
    st.markdown("### Basic Prompt 1: 'List benefits of project-based learning.'")
    
    format_spec1 = st.text_area(
        "Add format specification:", 
        height=100,
        placeholder="Example: Format as a two-column table with 'Benefit' in the first column and 'Classroom Application' in the second column. Include 5 benefits, and organize them from most to least impactful.",
        key="format_spec1"
    )
    
    if format_spec1:
        st.success("You've added format specifications! Let's analyze your addition:")
        
        st.markdown("""
        **Complete Prompt with Your Format:**
        ```
        List benefits of project-based learning. """ + format_spec1 + """
        ```
        
        **Format Elements to Check:**
        - Did you specify a structure (list, table, etc.)?
        - Did you include any organizational principles?
        - Did you specify any quantities or parameters?
        - Would this format make the content more usable?
        """)
    
    # Basic prompt 2
    st.markdown("### Basic Prompt 2: 'Create a vocabulary study guide for literary terms.'")
    
    format_spec2 = st.text_area(
        "Add format specification:", 
        height=100,
        placeholder="Example: Format as flashcards with the term on one side and the definition and an example on the other side. Include 10 essential literary terms for high school students, and organize them alphabetically.",
        key="format_spec2"
    )
    
    if format_spec2:
        st.success("You've added format specifications! Let's analyze your addition:")
        
        st.markdown("""
        **Complete Prompt with Your Format:**
        ```
        Create a vocabulary study guide for literary terms. """ + format_spec2 + """
        ```
        
        **Format Elements to Check:**
        - Did you specify a learning-friendly structure?
        - Did you include organizational elements?
        - Did you specify what elements should be included for each term?
        - Would this format be practical for student use?
        """)
    
    # Activity 2
    st.markdown("## Activity 2: Format Matching")
    
    st.markdown("""
    Match each educational purpose with the most appropriate format specification.
    Consider what structure would best serve each educational need.
    """)
    
    # Educational Purpose 1
    st.markdown("### Educational Purpose: Helping students compare and contrast two historical events")
    
    format_choice1 = st.radio(
        "Which format would be most effective?",
        ["a. A numbered list of facts about both events",
         "b. A Venn diagram with unique and shared characteristics",
         "c. A timeline showing when each event occurred",
         "d. A paragraph summary of each event"],
        key="format_choice1"
    )
    
    if format_choice1.startswith("b."):
        st.success("Great choice! A Venn diagram is ideal for compare/contrast tasks because it visually organizes both similarities and differences.")
    else:
        st.info("Consider how a Venn diagram might be particularly effective for comparison tasks, as it visually shows both unique and shared characteristics.")
    
    # Educational Purpose 2
    st.markdown("### Educational Purpose: Providing step-by-step instructions for a science experiment")
    
    format_choice2 = st.radio(
        "Which format would be most effective?",
        ["a. A narrative description of the experiment",
         "b. A concept map showing relationships between components",
         "c. A numbered procedure list with materials section at the top",
         "d. A table showing variables and outcomes"],
        key="format_choice2"
    )
    
    if format_choice2.startswith("c."):
        st.success("Great choice! A numbered procedure list with a materials section is the standard format for experiments, providing clear sequential steps and preparation requirements.")
    else:
        st.info("Consider how a numbered procedure list with a materials section provides both preparation information and clear sequential instructions.")
    
    # Activity 3
    st.markdown("## Activity 3: Complete CTF Prompt Builder")
    
    st.markdown("""
    Create a complete prompt that includes Context, Task, and Format specifications.
    This activity brings together what you've learned in Lessons 2, 3, and 4.
    """)
    
    # Educational purpose selection
    ed_purpose = st.selectbox(
        "Select an educational purpose:",
        [
            "Creating a quiz or assessment",
            "Developing a lesson plan",
            "Generating student feedback",
            "Creating a study guide",
            "Designing a classroom activity"
        ],
        key="ed_purpose"
    )
    
    # CTF components
    context = st.text_area("Context (background, audience, situation):", 
                           placeholder="Example: For a diverse 8th-grade U.S. history class that has just completed a unit on the Civil War. Students have varying reading levels and include several English language learners.",
                           height=80,
                           key="context")
    
    task = st.text_area("Task (what you want the AI to do):", 
                        placeholder="Example: Create a unit review activity that assesses students' understanding of the key causes, events, and outcomes of the Civil War.",
                        height=80,
                        key="task")
    
    format_spec = st.text_area("Format (how you want it structured):", 
                              placeholder="Example: Format as a gallery walk with 5 stations. For each station, include: 1) A primary source image or short text, 2) 3 analysis questions of increasing difficulty, and 3) A brief background information card. Include a student answer sheet template.",
                              height=100,
                              key="format_spec")
    
    # Show the complete prompt
    if context and task and format_spec:
        st.markdown("### Your Complete CTF Prompt:")
        
        complete_prompt = f"""Context: {context}

Task: {task}

Format: {format_spec}"""
        
        st.code(complete_prompt)
        
        st.markdown("""
        **Prompt Effectiveness Analysis:**
        
        Your prompt combines all three essential elements:
        - **Context** provides the background information that shapes understanding
        - **Task** specifies what you want the AI to create
        - **Format** details exactly how you want the output structured
        
        This combination creates highly tailored, immediately usable content for your specific educational needs.
        """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * For Activity 1, encourage participants to think about what formats they already use in their teaching materials
    * For Activity 2, discuss why certain formats are better suited to particular educational purposes
    * For Activity 3, have participants share their CTF prompts and discuss how the components work together
    
    **Common Mistakes to Address:**
    
    * Confusing format specifications with task instructions
    * Being too vague in format requests
    * Creating formats that are too complex for AI to maintain consistently
    * Not considering the end use when selecting a format
    
    **Extension Ideas:**
    
    * Have participants create a "format library" document with their most commonly used educational formats
    * Challenge participants to think of a teaching resource they regularly create and specify its format for AI
    * Discuss how different subject areas might require specialized format specifications
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