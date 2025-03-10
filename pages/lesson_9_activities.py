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
    page_title="Lesson 9: Activities",
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
    "title": "Zero-Shot Prompting: Activities",
    "lesson": "9",
    "section": "activities",
    "order": 3
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_9_activities"
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
    "lesson_9_activities",
    "activities",
    "Lesson 9 Activities",
    """
    **This section provides hands-on practice with zero-shot prompting.**
    
    You'll:
    - Transform basic prompts into effective zero-shot prompts
    - Craft zero-shot prompts for different educational contexts
    - Apply the PCTFREI framework to zero-shot prompting
    
    Complete these activities to strengthen your zero-shot prompting skills before
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
    
    Complete the activities below to practice creating effective zero-shot prompts.
    After finishing these activities, proceed to the Reflection section to consolidate your learning 
    and unlock the next lesson.
    """)
    
    # Activity 1
    st.markdown("## Activity 1: Transforming Basic Prompts into Effective Zero-Shot Prompts")
    
    st.markdown("""
    In this activity, you'll practice transforming basic prompts into more effective zero-shot prompts
    by adding specificity and structure without adding examples.
    """)
    
    # Create tabs for different prompt types
    prompt_tabs = st.tabs(["Prompt 1: Lesson Plan", "Prompt 2: Assessment", "Prompt 3: Parent Communication"])
    
    with prompt_tabs[0]:
        st.markdown("""
        **Basic Prompt:**
        ```
        Create a lesson plan on fractions.
        ```
        
        **Your Task:** Transform this basic prompt into an effective zero-shot prompt by adding:
        - Grade level and standards alignment
        - Specific fractions topic
        - Time constraints
        - Required components
        - Special considerations
        
        Don't provide examples of what you want - focus on clear parameters that guide the AI to draw
        on its existing knowledge of educational best practices.
        """)
        
        # User input for transformed prompt
        transformed_prompt1 = st.text_area(
            "Write your transformed zero-shot prompt:",
            height=200,
            placeholder="Create a 3rd-grade math lesson plan on...",
            key="transform_prompt1"
        )
        
        # Analysis of transformation
        prompt1_analysis = st.text_area(
            "Explain your transformation strategy:",
            height=100,
            placeholder="Describe what specific elements you added to make this an effective zero-shot prompt...",
            key="prompt1_analysis"
        )
        
        if transformed_prompt1 and prompt1_analysis:
            st.success("Great job transforming the lesson plan prompt!")
            
            st.markdown("""
            **Example of an Effective Transformation:**
            ```
            Create a 3rd-grade math lesson plan on comparing fractions with like denominators that:
            
            1. Aligns with Common Core standard 3.NF.A.3 (Compare fractions with the same denominator)
            2. Can be completed in a 45-minute class period
            3. Begins with a visual representation using fraction strips
            4. Includes a collaborative activity with fraction cards
            5. Ends with a quick 5-minute exit ticket for assessment
            6. Addresses common misconceptions about fraction size and comparison
            7. Provides differentiation options for struggling and advanced learners
            ```
            
            This transformation adds specificity about grade level, standards, duration, content, and structure
            without providing examples of the actual content.
            """)
    
    with prompt_tabs[1]:
        st.markdown("""
        **Basic Prompt:**
        ```
        Create a quiz on the water cycle.
        ```
        
        **Your Task:** Transform this basic prompt into an effective zero-shot prompt by adding:
        - Grade level and subject
        - Quiz length and format
        - Types of questions
        - Specific water cycle concepts to cover
        - Assessment purpose
        
        Remember to focus on parameters, not examples.
        """)
        
        # User input for transformed prompt
        transformed_prompt2 = st.text_area(
            "Write your transformed zero-shot prompt:",
            height=200,
            placeholder="Create a 5th-grade science quiz on...",
            key="transform_prompt2"
        )
        
        # Analysis of transformation
        prompt2_analysis = st.text_area(
            "Explain your transformation strategy:",
            height=100,
            placeholder="Describe what specific elements you added to make this an effective zero-shot prompt...",
            key="prompt2_analysis"
        )
        
        if transformed_prompt2 and prompt2_analysis:
            st.success("Great job transforming the assessment prompt!")
            
            st.markdown("""
            **Example of an Effective Transformation:**
            ```
            Create a 5th-grade science formative assessment on the water cycle that:
            
            1. Contains 8 questions total (6 multiple-choice and 2 short-answer)
            2. Covers evaporation, condensation, precipitation, collection, and transpiration
            3. Includes at least one question with a diagram for students to label
            4. Features questions at different levels of difficulty (knowledge, application, analysis)
            5. Will take students approximately 15-20 minutes to complete
            6. Provides an answer key with brief explanations
            7. Will be used to identify misconceptions before a hands-on lab activity
            ```
            
            This transformation creates clear parameters for an appropriate formative assessment
            without providing specific question examples.
            """)
    
    with prompt_tabs[2]:
        st.markdown("""
        **Basic Prompt:**
        ```
        Write a letter to parents.
        ```
        
        **Your Task:** Transform this basic prompt into an effective zero-shot prompt by adding:
        - Specific communication purpose
        - Grade level and subject
        - Content requirements
        - Tone and style guidance
        - Expected components
        
        Remember to focus on parameters, not examples.
        """)
        
        # User input for transformed prompt
        transformed_prompt3 = st.text_area(
            "Write your transformed zero-shot prompt:",
            height=200,
            placeholder="Write a letter to parents of 8th-grade students...",
            key="transform_prompt3"
        )
        
        # Analysis of transformation
        prompt3_analysis = st.text_area(
            "Explain your transformation strategy:",
            height=100,
            placeholder="Describe what specific elements you added to make this an effective zero-shot prompt...",
            key="prompt3_analysis"
        )
        
        if transformed_prompt3 and prompt3_analysis:
            st.success("Great job transforming the parent communication prompt!")
            
            st.markdown("""
            **Example of an Effective Transformation:**
            ```
            Write a letter to parents/guardians of 8th-grade language arts students that:
            
            1. Introduces the upcoming poetry unit (2 weeks long)
            2. Explains the key learning objectives and skills students will develop
            3. Describes the final project (a student poetry anthology)
            4. Lists 3-4 ways families can support their students during this unit
            5. Maintains a warm, encouraging, and professional tone
            6. Is approximately 1 page in length
            7. Includes contact information and a brief FAQ section
            8. Avoids educational jargon that might confuse parents
            ```
            
            This transformation creates a specific context and clear parameters for the communication
            without providing an example letter.
            """)
    
    # Activity 2
    st.markdown("## Activity 2: Create Subject-Specific Zero-Shot Prompts")
    
    st.markdown("""
    In this activity, you'll create a zero-shot prompt for your specific subject area and grade level.
    Choose a content type you frequently need to create.
    """)
    
    # Subject area selection
    subject_area = st.selectbox(
        "Select your subject area:",
        [
            "Elementary (Multiple Subjects)",
            "Secondary Math",
            "Secondary Science",
            "Secondary Language Arts/English",
            "Secondary Social Studies/History",
            "World Languages",
            "Arts Education",
            "Physical Education/Health",
            "Special Education",
            "Other (specify in your prompt)"
        ],
        key="subject_area"
    )
    
    # Content type selection
    content_type = st.selectbox(
        "Select the type of content you want to create:",
        [
            "Lesson Plan",
            "Assessment",
            "Student Handout/Worksheet",
            "Discussion Guide",
            "Project Instructions",
            "Rubric",
            "Study Guide",
            "Parent Communication",
            "Differentiated Activities",
            "Other (specify in your prompt)"
        ],
        key="content_type"
    )
    
    # Zero-shot prompt creation
    custom_prompt = st.text_area(
        "Write a zero-shot prompt for your selected subject and content type:",
        height=250,
        placeholder=f"Create a [grade level] {subject_area} {content_type} that: \n1. [First parameter] \n2. [Second parameter] \n...",
        key="custom_prompt"
    )
    
    # Analysis of choices
    prompt_choices = st.text_area(
        "Explain your prompt design choices:",
        height=150,
        placeholder="Explain why you included specific parameters and how they would help the AI generate effective content for your teaching context...",
        key="prompt_choices"
    )
    
    if custom_prompt and prompt_choices:
        st.success("You've created a custom zero-shot prompt for your teaching context!")
        
        st.markdown("""
        ### Tips for Effective Subject-Specific Zero-Shot Prompts
        
        1. **Include subject-specific terminology** - Terms like "claim-evidence-reasoning" for science or "close reading" for ELA help tap into domain knowledge
        
        2. **Reference relevant standards** - Mentioning specific standards helps align content accurately
        
        3. **Specify cognitive level** - Clarify whether you need recall, application, analysis, etc.
        
        4. **Consider your student population** - Note any specific needs of your student demographic
        
        5. **Add subject-specific scaffolding** - Include scaffolding approaches common in your discipline
        """)
    
    # Activity 3
    st.markdown("## Activity 3: Applying PCTFREI to Zero-Shot Prompting")
    
    st.markdown("""
    In this activity, you'll practice incorporating elements of the PCTFREI framework into a zero-shot prompt.
    This combination leverages both the structure of PCTFREI and the efficiency of zero-shot prompting.
    """)
    
    # Original basic prompt
    st.markdown("""
    **Basic Prompt:**
    ```
    Create a reading guide.
    ```
    
    **Your Task:** Transform this basic prompt using the PCTFREI framework, while keeping it zero-shot (no examples).
    """)
    
    # P - Persona
    st.markdown("### Step 1: Add Persona (P)")
    persona_addition = st.text_area(
        "Add a specific persona to the prompt:",
        height=80,
        placeholder="Example: As a 10th-grade literature teacher...",
        key="persona_addition"
    )
    
    # T - Task
    st.markdown("### Step 2: Add Task Specification (T)")
    task_addition = st.text_area(
        "Add specific task details:",
        height=80,
        placeholder="Example: ...create a reading guide for Chapter 5 of 'To Kill a Mockingbird'...",
        key="task_addition"
    )
    
    # C - Context
    st.markdown("### Step 3: Add Context (C)")
    context_addition = st.text_area(
        "Add relevant context:",
        height=80,
        placeholder="Example: ...for a mixed-ability class that includes several English language learners and students who struggle with reading comprehension...",
        key="context_addition"
    )
    
    # F - Format
    st.markdown("### Step 4: Add Format Specifications (F)")
    format_addition = st.text_area(
        "Add format requirements:",
        height=100,
        placeholder="Example: Format the reading guide to include:\n- Pre-reading vocabulary section with 8-10 key terms\n- 3-4 focus questions for each major scene\n- A character tracking section\n- Post-reading reflection prompts",
        key="format_addition"
    )
    
    # R - Reference
    st.markdown("### Step 5: Add Reference Materials (R)")
    reference_addition = st.text_area(
        "Add reference materials or standards alignment:",
        height=80,
        placeholder="Example: Align the guide with Common Core ELA standards RL.9-10.1 through RL.9-10.4, particularly focusing on character development and symbolism.",
        key="reference_addition"
    )
    
    # Put it all together
    st.markdown("### Step 6: Create the Complete PCTFREI Zero-Shot Prompt")
    
    complete_pctfrei = st.text_area(
        "Combine all elements into a cohesive zero-shot prompt:",
        height=250,
        placeholder="Combine the PCTFREI elements you added above into a well-structured, complete prompt...",
        key="complete_pctfrei"
    )
    
    if (persona_addition and task_addition and context_addition and format_addition and 
        reference_addition and complete_pctfrei):
        st.success("You've successfully created a PCTFREI-enhanced zero-shot prompt!")
        
        st.markdown("""
        ### Benefits of Combining PCTFREI with Zero-Shot
        
        This approach gives you the best of both worlds:
        
        - **Structure of PCTFREI**: The framework ensures you consider all important aspects of the prompt
        
        - **Efficiency of Zero-Shot**: You don't need to provide specific examples
        
        - **Clarity and Specificity**: The combination produces highly targeted content
        
        - **Contextual Relevance**: Persona and context elements customize the output to your specific needs
        
        - **Educational Alignment**: Reference materials ensure curricular alignment
        
        Remember that while this prompt is longer than a basic prompt, the additional specificity leads to higher quality results that need less editing, saving you time overall.
        """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * For Activity 1, encourage participants to consider the specific needs of their classrooms when transforming the prompts
    * For Activity 2, suggest starting with content types they regularly create to make the activity immediately practical
    * For Activity 3, emphasize that combining PCTFREI with zero-shot prompting offers a powerful balance of structure and efficiency
    
    **Common Challenges:**
    
    * Some participants may struggle to add specificity without adding examples - remind them to focus on parameters, not samples
    * Others may create overly complex prompts - encourage clarity and focus on the most important elements
    * Participants may need to be reminded that different subject areas benefit from different types of parameters
    
    **Extension Ideas:**
    
    * Have participants exchange zero-shot prompts and evaluate them for specificity and likely effectiveness
    * Challenge participants to create a "prompt template" with key parameters for a content type they frequently create
    * Encourage experimentation with different combinations of PCTFREI elements to find the optimal balance
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