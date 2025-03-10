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
    page_title="Lesson 14: Activities",
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
    "title": "Student Feedback and Writing Prompts: Activities",
    "lesson": "14",
    "section": "activities",
    "order": 3
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_14_activities"
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
    "lesson_14_activities",
    "activities",
    "Student Feedback and Writing Prompts: Activities",
    """
    **This section provides hands-on practice with prompt engineering for student feedback and writing prompts.**
    
    You'll:
    - Analyze and improve feedback examples
    - Create feedback templates for different contexts
    - Design engaging writing prompts using structured frameworks
    - Develop differentiation strategies for diverse learners
    
    Complete these activities to strengthen your skills before moving to the reflection section.
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
    st.markdown(f"# Activities: {PAGE_INFO['title']}")
    
    # Add a progress note
    st.info("""
    **📝 Course Progression Note:** 
    
    Complete the activities below to practice creating effective feedback and writing prompts.
    After finishing these activities, proceed to the Reflection section to consolidate your learning 
    and unlock the next lesson.
    """)
    
    # Activity 1: Feedback Analysis and Transformation
    st.markdown("## Activity 1: Feedback Analysis and Transformation")
    
    st.markdown("""
    In this activity, you'll analyze a piece of basic feedback and transform it into more effective,
    growth-oriented feedback using the principles we've discussed.
    """)
    
    # Sample feedback to analyze
    st.markdown("### Sample Feedback to Analyze:")
    
    st.markdown("""
    > "Your essay needs improvement. There are several grammar errors throughout. Your thesis statement
    > is unclear and your evidence is not convincing. You should revise this and turn it in again."
    """)
    
    st.markdown("### What makes this feedback ineffective?")
    
    st.markdown("""
    Identify the issues with this feedback by checking all that apply:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.checkbox("Focuses only on weaknesses", key="issue1")
        st.checkbox("Uses discouraging language", key="issue2")
        st.checkbox("Lacks specific examples", key="issue3")
        st.checkbox("Provides no actionable guidance", key="issue4")
    
    with col2:
        st.checkbox("Has a negative, judgmental tone", key="issue5")
        st.checkbox("Doesn't reference learning goals", key="issue6")
        st.checkbox("Lacks personalization", key="issue7")
        st.checkbox("Offers no clear next steps", key="issue8")
    
    st.markdown("### Now, transform this feedback:")
    
    st.markdown("""
    Rewrite the feedback to make it more effective using these principles:
    1. Start with specific positive aspects
    2. Address areas for growth with specific examples
    3. Provide actionable guidance for improvement
    4. Use an encouraging, growth-oriented tone
    5. Connect to learning goals and success criteria
    """)
    
    transformed_feedback = st.text_area(
        "Your improved feedback:",
        height=200,
        key="transformed_feedback"
    )
    
    if transformed_feedback:
        st.success("""
        Great work transforming this feedback! Effective feedback should always balance recognition of 
        strengths with clear guidance for improvement. Remember that tone matters significantly - students 
        are more likely to engage with feedback that feels supportive rather than judgmental.
        
        As you review your transformed feedback, consider:
        - Did you provide specific examples from the student's work?
        - Are your suggestions actionable and clear?
        - Does your feedback maintain a growth mindset approach?
        - Would the student know exactly what to do next?
        """)
    
    # Activity 2: Feedback Template Builder
    st.markdown("## Activity 2: Feedback Template Builder")
    
    st.markdown("""
    Creating feedback templates can help you provide consistent, comprehensive feedback efficiently.
    In this activity, you'll build a feedback template for a specific assignment type.
    """)
    
    # Assignment type selection
    assignment_type = st.selectbox(
        "Choose an assignment type for your feedback template:",
        [
            "Select an assignment type...",
            "Elementary creative writing",
            "Middle school lab report",
            "High school argumentative essay",
            "Mathematics problem set",
            "Group project presentation",
            "Digital portfolio submission"
        ],
        key="assignment_type"
    )
    
    if assignment_type and assignment_type != "Select an assignment type...":
        st.markdown(f"### Building a Feedback Template for: {assignment_type}")
        
        st.markdown("""
        Create a structured feedback template by defining components for each section below.
        A good template maintains consistency while allowing for personalization.
        """)
        
        # Template sections
        st.markdown("#### 1. Opening Acknowledgment")
        opening = st.text_area(
            "How will you start your feedback? (e.g., recognition of effort, specific strength)",
            height=80,
            key="opening"
        )
        
        st.markdown("#### 2. Strengths Section")
        strengths_approach = st.text_area(
            "How will you highlight strengths? (e.g., '2-3 specific strengths with examples')",
            height=80,
            key="strengths"
        )
        
        st.markdown("#### 3. Growth Areas Section")
        growth_approach = st.text_area(
            "How will you address areas for improvement? (e.g., 'Focus on 1-2 priority areas with specific examples')",
            height=80,
            key="growth"
        )
        
        st.markdown("#### 4. Next Steps Section")
        next_steps = st.text_area(
            "How will you guide future improvement? (e.g., specific actions, resources, strategies)",
            height=80,
            key="next_steps"
        )
        
        st.markdown("#### 5. Closing Encouragement")
        closing = st.text_area(
            "How will you end your feedback? (e.g., positive reinforcement, future-focused comment)",
            height=80,
            key="closing"
        )
        
        # Template display
        if opening and strengths_approach and growth_approach and next_steps and closing:
            st.success("Your feedback template is complete! Here's how it looks:")
            
            st.markdown(f"""
            ### {assignment_type} Feedback Template
            
            **Opening Acknowledgment:**
            {opening}
            
            **Strengths:**
            {strengths_approach}
            
            **Areas for Growth:**
            {growth_approach}
            
            **Next Steps:**
            {next_steps}
            
            **Closing Encouragement:**
            {closing}
            """)
            
            st.markdown("""
            #### How to Use This Template
            
            1. **Save this structure** as a reusable template
            2. **Customize the content** for each student while maintaining the structure
            3. **Be specific** about strengths and growth areas for each student
            4. **Refer to success criteria** or learning objectives
            5. **Personalize next steps** based on individual student needs
            
            A good template balances efficiency with personalization. The structure remains consistent,
            while the specific feedback is tailored to each student's work.
            """)
    
    # Activity 3: Writing Prompt Creation
    st.markdown("## Activity 3: Writing Prompt Creation")
    
    st.markdown("""
    In this activity, you'll create an engaging writing prompt for a specific grade level and writing type,
    focusing on incorporating effective scaffolding and clear success criteria.
    """)
    
    # Writing type and grade level
    col1, col2 = st.columns(2)
    
    with col1:
        writing_type = st.selectbox(
            "Select a writing type:",
            [
                "Narrative (story)",
                "Informative/Explanatory",
                "Argumentative/Persuasive",
                "Analytical Response",
                "Creative Expression",
                "Reflective Writing"
            ],
            key="writing_type"
        )
    
    with col2:
        grade_band = st.selectbox(
            "Select a grade level:",
            [
                "Elementary (K-2)",
                "Elementary (3-5)",
                "Middle School (6-8)",
                "High School (9-12)"
            ],
            key="grade_band"
        )
    
    # Writing prompt components
    st.markdown("### Create Your Writing Prompt:")
    
    st.markdown("#### Topic or Scenario")
    topic = st.text_area(
        "What will students write about? Provide a specific topic, question, or scenario:",
        height=100,
        key="topic"
    )
    
    st.markdown("#### Purpose and Audience")
    purpose = st.text_area(
        "What is the purpose of the writing? Who is the audience?",
        height=80,
        key="purpose"
    )
    
    st.markdown("#### Scaffolding Elements")
    scaffolding = st.text_area(
        "What scaffolding will you include? (planning questions, graphic organizers, sentence starters, etc.)",
        height=100,
        key="scaffolding"
    )
    
    st.markdown("#### Success Criteria")
    criteria = st.text_area(
        "How will students know they've been successful? List specific criteria:",
        height=100,
        key="criteria"
    )
    
    # Assemble writing prompt
    if topic and purpose and scaffolding and criteria:
        st.success("You've created a complete writing prompt! Here's how it looks:")
        
        st.markdown(f"""
        ### {writing_type} Writing Prompt for {grade_band}
        
        **Writing Task:**
        {topic}
        
        **Purpose and Audience:**
        {purpose}
        
        **Planning and Organization:**
        {scaffolding}
        
        **Success Criteria:**
        {criteria}
        """)
        
        st.markdown("""
        #### What Makes This Prompt Effective:
        
        - **Clear Focus**: Students understand exactly what to write about
        - **Authentic Purpose**: The writing has a real audience and purpose
        - **Built-in Support**: Scaffolding helps all students access the task
        - **Transparent Expectations**: Success criteria clarify what quality looks like
        
        Consider how you might adapt this prompt for different learners in your classroom,
        perhaps by varying the complexity, adding additional supports, or offering choice
        in how students respond.
        """)
    
    # Activity 4: Differentiation Strategies
    st.markdown("## Activity 4: Differentiation Strategies")
    
    st.markdown("""
    In this activity, you'll explore strategies for differentiating feedback and writing prompts
    to meet diverse student needs.
    """)
    
    st.markdown("### Select a student learning profile to focus on:")
    
    learning_profile = st.selectbox(
        "Choose a learning profile:",
        [
            "English language learner",
            "Student with learning disability in reading/writing",
            "Highly advanced/gifted learner",
            "Student with attention challenges",
            "Student who struggles with motivation"
        ],
        key="learning_profile"
    )
    
    if learning_profile:
        st.markdown(f"### Differentiation Strategies for: {learning_profile}")
        
        st.markdown("#### Feedback Differentiation")
        st.markdown("""
        How would you modify your feedback approach for this student? Consider:
        - Feedback length and complexity
        - Balance of written vs. verbal feedback
        - Visual supports or examples
        - Focus areas (what to prioritize)
        - Follow-up approach
        """)
        
        feedback_diff = st.text_area(
            "Your feedback differentiation strategy:",
            height=150,
            key="feedback_diff"
        )
        
        st.markdown("#### Writing Prompt Differentiation")
        st.markdown("""
        How would you modify a writing prompt for this student? Consider:
        - Task complexity or scope
        - Scaffolding and supports
        - Options for demonstration of learning
        - Product variations
        - Process adaptations
        """)
        
        prompt_diff = st.text_area(
            "Your writing prompt differentiation strategy:",
            height=150,
            key="prompt_diff"
        )
        
        if feedback_diff and prompt_diff:
            st.success("""
            Excellent differentiation strategies! Effective differentiation isn't about creating
            entirely different experiences, but rather about providing the right level of challenge
            and support for each learner to access the same essential content and skills.
            
            Remember that these differentiation approaches can be built into your prompt engineering
            process from the beginning by creating templates with built-in options or by developing
            a set of modification strategies that you can apply consistently.
            """)
    
    # Reflection and key takeaways
    st.markdown("## Activity Reflection")
    
    st.markdown("""
    Take a moment to reflect on what you've learned from these activities:
    
    1. **Effective feedback** should balance strengths and growth areas, provide specific examples,
       and offer clear guidance for improvement. It should foster a growth mindset and connect to
       learning goals.
    
    2. **Using templates** can help maintain consistency and efficiency while still allowing for
       personalization. Good templates provide a structure, not a script.
    
    3. **Engaging writing prompts** combine clear tasks with appropriate scaffolding and transparent
       success criteria. They give students both structure and creative space.
    
    4. **Differentiation strategies** should be integrated into your approach to both feedback and
       writing prompts, ensuring all students can access and benefit from these essential learning tools.
    
    As you apply these principles in your teaching, remember that prompt engineering allows you to
    leverage AI assistance while maintaining your professional judgment and expertise.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Encourage participants to adapt these activities based on their specific teaching context and student needs
    * Suggest maintaining a library of effective feedback phrases and templates organized by assignment type
    * Remind participants that differentiation strategies should be planned in advance, not improvised
    * Emphasize that prompt engineering for feedback and writing tasks gets more efficient with practice
    
    **Common Challenges:**
    
    * Finding the right balance between structure and personalization in feedback templates
    * Creating writing prompts that are appropriately challenging yet accessible
    * Managing the time investment in detailed feedback (prompt engineering helps address this)
    * Ensuring differentiation strategies maintain high expectations for all students
    
    **Extension Ideas:**
    
    * Have participants exchange feedback templates and writing prompts for peer review
    * Suggest creating a grade-level or department feedback protocol based on these principles
    * Encourage development of a writing prompt library organized by writing type and standard
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