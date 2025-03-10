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
    page_title="Lesson 5: Activities",
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
    "title": "Persona Engineering: Activities",
    "lesson": "5",
    "section": "activities",
    "order": 3
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_5_activities"
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
    "lesson_5_activities",
    "activities",
    "Lesson 5 Activities",
    """
    **This section provides hands-on practice with persona engineering in prompting.**
    
    You'll:
    - Create and analyze different AI personas
    - Match personas to educational purposes
    - Build complete prompts with effective personas
    
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
    
    Complete the activities below to practice engineering personas in your prompts.
    After finishing these activities, proceed to the Reflection section to solidify your learning 
    and unlock the next lesson.
    """)
    
    # Activity 1
    st.markdown("## Activity 1: Craft Educational Personas")
    
    st.markdown("""
    For each educational scenario, craft an effective persona that would create the most appropriate
    response. Be specific about communication style, expertise, and perspective.
    """)
    
    # Scenario 1
    st.markdown("### Scenario 1: Teaching a complex scientific concept to young children")
    
    persona1 = st.text_area(
        "Create a persona:", 
        height=100,
        placeholder="Example: As an enthusiastic science educator for young children who uses simple analogies, asks guiding questions, expresses wonder, incorporates playful language, and connects concepts to everyday experiences that children can relate to",
        key="persona1"
    )
    
    if persona1:
        st.success("You've created a teaching persona! Let's analyze its components:")
        
        st.markdown("""
        **Persona Elements to Check:**
        - Did you specify a clear role or identity?
        - Did you include communication style elements (tone, language approach)?
        - Did you mention perspective or mindset characteristics?
        - Is the persona appropriate for the specific audience (young children)?
        - Would this persona make complex science more accessible?
        """)
    
    # Scenario 2
    st.markdown("### Scenario 2: Providing constructive feedback on a high school student's essay")
    
    persona2 = st.text_area(
        "Create a persona:", 
        height=100,
        placeholder="Example: As a supportive writing mentor who balances specific critique with genuine encouragement, focuses on the most impactful areas for improvement, provides concrete examples and revision strategies, maintains a respectful tone, and emphasizes the iterative nature of the writing process",
        key="persona2"
    )
    
    if persona2:
        st.success("You've created a feedback persona! Let's analyze its components:")
        
        st.markdown("""
        **Persona Elements to Check:**
        - Does your persona balance encouragement with honest feedback?
        - Does it specify a tone that would build trust with students?
        - Does it include elements that focus on growth rather than just criticism?
        - Is the expertise level appropriate for evaluating high school writing?
        - Does it include how feedback should be delivered (specific strategies, examples, etc.)?
        """)
    
    # Activity 2
    st.markdown("## Activity 2: Persona Matching")
    
    st.markdown("""
    Match each educational purpose with the most appropriate persona.
    Consider what voice, tone, and perspective would best serve each goal.
    """)
    
    # Educational Purpose 1
    st.markdown("### Educational Purpose: Simplifying a complex math concept for struggling students")
    
    persona_choice1 = st.radio(
        "Which persona would be most effective?",
        ["a. An academic mathematician who emphasizes theoretical foundations and precise terminology",
         "b. A patient tutor who uses step-by-step explanations, visual models, and checks for understanding",
         "c. A historical scholar who explains how the concept developed over time",
         "d. A debate moderator who presents arguments for and against different approaches"],
        key="persona_choice1"
    )
    
    if persona_choice1.startswith("b."):
        st.success("Great choice! A patient tutor with step-by-step explanations and visual models would best support struggling students by breaking down complexity and ensuring understanding at each step.")
    else:
        st.info("Consider how a patient tutor with step-by-step explanations and visual models might best support struggling students by breaking down complexity and ensuring understanding at each step.")
    
    # Educational Purpose 2
    st.markdown("### Educational Purpose: Encouraging critical thinking about a controversial historical event")
    
    persona_choice2 = st.radio(
        "Which persona would be most effective?",
        ["a. An authoritative historian who presents the definitive interpretation of events",
         "b. A passionate advocate who argues strongly for one perspective",
         "c. A friendly storyteller who simplifies the narrative for easy comprehension",
         "d. A balanced historian who presents multiple perspectives, asks thought-provoking questions, and encourages evidence-based reasoning"],
        key="persona_choice2"
    )
    
    if persona_choice2.startswith("d."):
        st.success("Great choice! A balanced historian who presents multiple perspectives and encourages evidence-based reasoning aligns with developing critical thinking skills about complex historical events.")
    else:
        st.info("Consider how a balanced historian who presents multiple perspectives and encourages evidence-based reasoning might best align with developing critical thinking skills about complex historical events.")
    
    # Activity 3
    st.markdown("## Activity 3: Complete PCTF Prompt Builder")
    
    st.markdown("""
    Create a complete prompt that includes Persona, Context, Task, and Format specifications.
    This activity brings together what you've learned through the first five lessons.
    """)
    
    # Educational purpose selection
    ed_purpose = st.selectbox(
        "Select an educational purpose:",
        [
            "Explaining a difficult concept",
            "Providing student feedback",
            "Creating an engaging lesson",
            "Developing assessment materials",
            "Supporting diverse learners"
        ],
        key="ed_purpose"
    )
    
    # PCTF components
    persona = st.text_area("Persona (role, communication style, perspective):", 
                         placeholder="Example: As a patient and encouraging math coach who explains concepts using real-world examples, breaks down complex procedures into manageable steps, celebrates progress, and anticipates common misconceptions",
                         height=80,
                         key="persona")
    
    context = st.text_area("Context (background, audience, situation):", 
                          placeholder="Example: For a 7th-grade pre-algebra class with mixed ability levels, including several students who struggle with math anxiety and some who are advanced. The class has learned the basic concept of variables but is now facing challenges with multi-step equations.",
                          height=80,
                          key="context")
    
    task = st.text_area("Task (what you want the AI to do):", 
                       placeholder="Example: Create a scaffolded introduction to solving two-step equations that addresses math anxiety while providing sufficient challenge for advanced students.",
                       height=80,
                       key="task")
    
    format_spec = st.text_area("Format (how you want it structured):", 
                             placeholder="Example: Structure the introduction as a 5-part lesson with: 1) A real-world problem that shows the practical application, 2) A visual model showing the step-by-step process, 3) Three worked examples of increasing difficulty with thinking aloud, 4) Common mistakes with non-judgmental corrections, and 5) Three practice problems with hints for struggling students and extension questions for advanced learners.",
                             height=100,
                             key="format_spec")
    
    # Show the complete prompt
    if persona and context and task and format_spec:
        st.markdown("### Your Complete PCTF Prompt:")
        
        complete_prompt = f"""Persona: {persona}

Context: {context}

Task: {task}

Format: {format_spec}"""
        
        st.code(complete_prompt)
        
        st.markdown("""
        **Prompt Effectiveness Analysis:**
        
        Your prompt now combines all four essential elements:
        - **Persona** establishes who is communicating and how
        - **Context** provides the background information that shapes understanding
        - **Task** specifies what you want the AI to create
        - **Format** details exactly how you want the output structured
        
        This comprehensive approach creates highly tailored, appropriate content that communicates in the right voice for your specific educational needs.
        """)
    
    # Activity 4
    st.markdown("## Activity 4: Persona Element Builder")
    
    st.markdown("""
    Instead of creating a complete persona at once, let's build one element by element.
    Select options from each category to construct a targeted educational persona.
    """)
    
    # Role/Identity
    st.markdown("### Step 1: Select a Role/Identity")
    role = st.selectbox(
        "Choose a base role:",
        ["Teacher/Educator", "Coach/Mentor", "Tutor", "Subject Expert", "Facilitator", "Storyteller"],
        key="role"
    )
    
    subject = st.text_input("Optional: Add subject specialty (e.g., 'science', 'writing', 'history'):", key="subject_specialty")
    
    # Communication Style
    st.markdown("### Step 2: Select Communication Style Elements")
    
    tone_options = ["enthusiastic", "patient", "supportive", "authoritative", "curious", "engaging", "thoughtful"]
    tone = st.multiselect("Choose tone descriptors (select 1-2):", tone_options, key="tone")
    
    approach_options = [
        "uses simple language", 
        "explains step-by-step", 
        "asks guiding questions",
        "uses analogies and metaphors", 
        "provides concrete examples",
        "connects to real-world applications",
        "uses precise terminology with explanations"
    ]
    approach = st.multiselect("Choose communication approaches (select 2-3):", approach_options, key="approach")
    
    # Perspective/Mindset
    st.markdown("### Step 3: Select Perspective/Mindset Elements")
    
    mindset_options = [
        "emphasizes growth mindset principles",
        "values critical thinking",
        "considers multiple perspectives",
        "focuses on practical application",
        "balances depth with accessibility",
        "encourages creativity and exploration",
        "prioritizes building student confidence"
    ]
    mindset = st.multiselect("Choose perspective elements (select 1-2):", mindset_options, key="mindset")
    
    # Generate the complete persona
    if role and (len(tone) > 0 or len(approach) > 0 or len(mindset) > 0):
        st.markdown("### Your Constructed Persona:")
        
        persona_parts = ["As a"]
        
        # Add tone
        if tone:
            persona_parts.append(" and ".join(tone))
        
        # Add role with subject
        if subject:
            persona_parts.append(f"{role.lower()} specializing in {subject}")
        else:
            persona_parts.append(role.lower())
        
        # Add who clause if we have approaches
        if approach:
            persona_parts.append("who")
            persona_parts.append(", ".join(approach))
        
        # Add mindset
        if mindset:
            if approach:  # If we already have "who" clause
                persona_parts.append("and")
            else:  # Need to add "who" for the first time
                persona_parts.append("who")
            
            persona_parts.append(", ".join(mindset))
        
        constructed_persona = " ".join(persona_parts)
        
        st.code(constructed_persona)
        
        st.success("""
        You've built a structured persona step by step! This methodical approach helps ensure your 
        persona covers key elements: identity, communication style, and perspective. You can use 
        this same structured approach whenever you need to create effective personas for educational prompts.
        """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * For Activity 1, encourage participants to think about teachers they've known who were particularly effective at teaching specific types of content - what made their approach work?
    * For Activity 2, discuss what makes certain personas more appropriate for different educational purposes
    * For Activity 3, have participants compare PCTF prompts and analyze how the persona element changes the overall effect
    * For Activity 4, point out how building personas systematically helps ensure key elements aren't forgotten
    
    **Common Challenges:**
    
    * Creating personas that are too vague ("friendly teacher") versus specific communication approaches
    * Confusing persona elements with task instructions
    * Creating personas that are entertaining but don't serve the educational purpose
    * Forgetting to match the persona to the student audience and learning goals
    
    **Extension Ideas:**
    
    * Have participants analyze their own teaching persona and identify its key characteristics
    * Create a shared "persona library" for common educational needs in participants' subject areas
    * Discuss how different student populations might respond to different AI personas
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