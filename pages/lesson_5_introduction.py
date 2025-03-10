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
    page_title="Lesson 5: Persona Engineering (P)",
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
    "title": "Persona Engineering (P)",
    "lesson": "5",
    "section": "introduction",
    "order": 1
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_5_introduction"
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
    "lesson_5_introduction",
    "introduction",
    "Lesson 5: Persona Engineering",
    """
    **Welcome to Lesson 5 on Persona Engineering in Prompting.**
    
    In this lesson, you'll learn:
    - How to assign roles and perspectives to AI using personas
    - Techniques for adjusting tone, voice, and expertise level
    - Strategic uses of personas for different educational purposes
    
    Navigate through the sections using the tabs at the top.
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
    st.markdown(f"# Lesson 5: {PAGE_INFO['title']}")
    
    # Objective
    st.markdown("## Objective")
    st.markdown("""
    To teach educators how to use persona engineering in prompts to control the tone, style, and 
    perspective of AI responses for more effective and appropriate educational content.
    """)
    
    # Real-world hook
    st.info("""
    ### Real-World Hook
    
    When explaining a complex concept, you might take different approaches: a physics teacher explains gravity 
    differently than a children's show host, even though both are covering the same topic. Similarly, by giving 
    the AI a specific persona, you can control how information is communicated to best serve your students.
    """)
    
    # Jargon-Free Explanation
    st.markdown("## Understanding Persona in Prompting")
    
    st.markdown("""
    Persona engineering in prompting means assigning a role, character, or perspective to the AI. 
    It's like asking the AI to "act as" or "speak as" a specific type of communicator or expert.
    
    Using personas helps you:
    
    - Control the tone and voice of the response
    - Adjust the complexity and language level
    - Create content from specific perspectives
    - Generate responses with appropriate expertise
    """)
    
    # Illustrative diagram
    st.markdown("## The Impact of Persona Engineering")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("""
        **🔍 Without Persona:**
        ```
        "Explain the water cycle."
        ```
        
        ⬇️
        
        **Default, generic tone**
        - Standard informational voice
        - Unpredictable complexity level
        - Neutral perspective
        - Generic engagement style
        """)
        
    with col_b:
        st.markdown("""
        **🌟 With Persona:**
        ```
        "As an enthusiastic 4th-grade science teacher
        who uses simple analogies and asks guiding 
        questions, explain the water cycle."
        ```
        
        ⬇️
        
        **Tailored communication style**
        - Enthusiastic, encouraging tone
        - Age-appropriate complexity
        - Educational perspective with analogies
        - Interactive questioning approach
        """)
    
    # Components of an Effective Persona
    st.markdown("## Key Components of an Effective Persona")
    
    st.markdown("""
    A well-defined persona typically includes:
    
    ### 1. Role or Identity
    - Professional title ("As a kindergarten teacher...")
    - Character type ("As a curious scientist...")
    - Specific expertise area ("As a marine biologist...")
    
    ### 2. Communication Style
    - Tone indicators ("...who explains things patiently and enthusiastically")
    - Language preferences ("...who uses simple language and analogies")
    - Engagement approach ("...who asks thought-provoking questions")
    
    ### 3. Perspective or Mindset
    - Philosophical stance ("...with a growth mindset approach")
    - Teaching philosophy ("...who believes in constructivist learning")
    - Value emphasis ("...who prioritizes creativity and critical thinking")
    """)
    
    # Examples of Educational Personas
    st.markdown("## Educational Personas for Different Purposes")
    
    st.markdown("""
    Different educational goals may call for different personas:
    
    | Educational Purpose | Effective Persona |
    |---------------------|-------------------|
    | Simplifying complex concepts | "An enthusiastic science communicator who explains complex ideas using everyday analogies" |
    | Creating engaging content | "A storyteller who weaves facts into narrative form with suspense and vivid imagery" |
    | Providing supportive feedback | "A encouraging mentor who focuses on growth and balances critique with specific praise" |
    | Creating critical thinking prompts | "A Socratic questioner who challenges assumptions and asks thought-provoking questions" |
    | Differentiating instruction | "A tutor who adapts explanations based on learning styles and builds on existing knowledge" |
    """)
    
    # Relationship to previous lessons
    st.markdown("## Progress in the PTC-FREI Framework")
    
    st.markdown("""
    So far, we've covered:
    
    - **Context (C)** - Lesson 2: The background information that shapes understanding
    - **Task (T)** - Lesson 3: The specific action you want the AI to perform
    - **Format (F)** - Lesson 4: How you want the response structured
    - **Persona (P)** - Lesson 5 (Today): The voice and perspective for the response
    
    Let's see how persona works with the other components:
    
    ```
    Persona: "As an experienced history teacher who specializes in making historical connections relevant to today's teenagers"
    
    Context: "For an 11th-grade U.S. history class that has been studying the Great Depression"
    
    Task: "Create a comparative analysis"
    
    Format: "Using a two-column table with 5 rows, each row highlighting a different economic or social parallel"
    ```
    
    The persona defines WHO is speaking, while the context sets the situation, the task defines WHAT is being created, and the format determines HOW it's structured.
    """)
    
    # When to Use Personas
    st.markdown("## Strategic Use of Personas in Education")
    
    st.markdown("""
    Persona engineering is particularly valuable when:
    
    ### 1. Adapting for Audience
    When content needs to be delivered at a specific language or complexity level (e.g., elementary vs. high school)
    
    ### 2. Modeling Expert Thinking
    When you want to demonstrate how an expert in a field approaches problems or explains concepts
    
    ### 3. Creating Engagement
    When you need content that captures student interest through storytelling or enthusiasm
    
    ### 4. Ensuring Appropriate Tone
    When communicating sensitive topics or providing feedback that needs to be delivered thoughtfully
    
    ### 5. Differentiating Instruction
    When creating materials that address different learning styles or needs
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Have participants recall teachers or instructors who had particularly effective communication styles - these can serve as inspiration for personas
    * Discuss how changing persona can dramatically change the accessibility of content for different learners
    * Connect persona engineering to the concept of "teacher voice" that educators already develop
    * Emphasize that personas allow for creative and strategic communication choices
    
    **Common Challenges:**
    
    * Creating overly complex personas that are difficult for the AI to maintain
    * Confusing persona (who is communicating) with context (background/situation)
    * Not being specific enough about communication style in persona definitions
    * Using personas that aren't appropriate for the educational purpose
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