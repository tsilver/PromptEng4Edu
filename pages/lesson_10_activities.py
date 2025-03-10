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
    page_title="Lesson 10: Activities",
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
    "title": "Few-Shot Prompting: Activities",
    "lesson": "10",
    "section": "activities",
    "order": 3
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_10_activities"
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
    "lesson_10_activities",
    "activities",
    "Lesson 10 Activities",
    """
    **This section provides hands-on practice with few-shot prompting.**
    
    You'll:
    - Create examples for few-shot prompts
    - Convert zero-shot prompts to few-shot prompts
    - Design few-shot prompts for your specific teaching needs
    
    Complete these activities to strengthen your few-shot prompting skills before
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
    
    Complete the activities below to practice creating effective few-shot prompts.
    After finishing these activities, proceed to the Reflection section to consolidate your learning 
    and unlock the next lesson.
    """)
    
    # Activity 1
    st.markdown("## Activity 1: Creating Effective Examples for Few-Shot Prompts")
    
    st.markdown("""
    In this activity, you'll practice creating high-quality examples for few-shot prompts. Remember that
    the examples you provide serve as models that the AI will attempt to match in style, format, and content.
    """)
    
    # Context setting
    activity1_context = st.selectbox(
        "Select an educational context for your examples:",
        [
            "Student Feedback Comments",
            "Discussion Questions",
            "Exit Tickets/Formative Assessments",
            "Instructional Objectives",
            "Lesson Hooks/Engagement Strategies"
        ],
        key="activity1_context"
    )
    
    # Display guidance based on selection
    if activity1_context == "Student Feedback Comments":
        st.markdown("""
        **Creating Examples for Student Feedback Comments**
        
        Effective student feedback should be:
        - Specific and actionable
        - Balanced between praise and growth areas
        - Appropriate for the student's age/grade
        - Focused on the work, not the student personally
        
        Create two example feedback comments that demonstrate these characteristics.
        """)
        
    elif activity1_context == "Discussion Questions":
        st.markdown("""
        **Creating Examples for Discussion Questions**
        
        Effective discussion questions should:
        - Be open-ended with no single "right" answer
        - Encourage higher-order thinking
        - Connect to learning objectives
        - Prompt students to use evidence or reasoning
        
        Create two example discussion questions that demonstrate these characteristics.
        """)
        
    elif activity1_context == "Exit Tickets/Formative Assessments":
        st.markdown("""
        **Creating Examples for Exit Tickets/Formative Assessments**
        
        Effective exit tickets should:
        - Be quick to complete (1-3 minutes)
        - Target a specific learning outcome
        - Provide actionable information about student understanding
        - Be easy to evaluate quickly
        
        Create two example exit tickets that demonstrate these characteristics.
        """)
        
    elif activity1_context == "Instructional Objectives":
        st.markdown("""
        **Creating Examples for Instructional Objectives**
        
        Effective instructional objectives should:
        - Be specific and measurable
        - Include an observable action verb
        - Specify conditions and criteria for success
        - Align with standards
        
        Create two example instructional objectives that demonstrate these characteristics.
        """)
        
    elif activity1_context == "Lesson Hooks/Engagement Strategies":
        st.markdown("""
        **Creating Examples for Lesson Hooks/Engagement Strategies**
        
        Effective lesson hooks should:
        - Capture student attention
        - Connect to prior knowledge or student interests
        - Introduce the key concept in an engaging way
        - Take 3-5 minutes to implement
        
        Create two example lesson hooks that demonstrate these characteristics.
        """)
    
    # User inputs for examples
    st.markdown("### Your Examples")
    
    example1 = st.text_area(
        f"Example 1 - {activity1_context}:",
        height=150,
        placeholder="Write your first example here...",
        key="example1"
    )
    
    example2 = st.text_area(
        f"Example 2 - {activity1_context}:",
        height=150,
        placeholder="Write your second example here...",
        key="example2"
    )
    
    # Optional third example
    show_third = st.checkbox("Add a third example?")
    
    if show_third:
        example3 = st.text_area(
            f"Example 3 - {activity1_context}:",
            height=150,
            placeholder="Write your third example here...",
            key="example3"
        )
    
    # Prompt instruction
    prompt_instruction = st.text_area(
        "Instructions to accompany your examples:",
        height=100,
        placeholder="Please create 3 more [type of content] that follow the pattern in my examples...",
        key="prompt_instruction"
    )
    
    # Self-evaluation checklist
    st.markdown("### Self-Evaluation Checklist")
    
    st.markdown("Review your examples against these criteria:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.checkbox("My examples have consistent formatting", key="check1")
        st.checkbox("My examples demonstrate the quality I expect", key="check2")
        st.checkbox("My examples show a clear pattern", key="check3")
    
    with col2:
        st.checkbox("My examples use similar length and style", key="check4")
        st.checkbox("My examples are diverse enough to show range", key="check5")
        st.checkbox("My instructions clearly state what to generate", key="check6")
    
    if example1 and example2 and prompt_instruction:
        st.success("You've created examples for a few-shot prompt!")
        
        complete_prompt = f"""
        {prompt_instruction}
        
        Example 1:
        {example1}
        
        Example 2:
        {example2}
        """
        
        if show_third and 'example3' in locals():
            complete_prompt += f"""
            
            Example 3:
            {example3}
            """
        
        st.markdown("### Your Complete Few-Shot Prompt")
        st.code(complete_prompt, language="text")
        
        st.markdown("""
        **Tip:** When using this prompt with an AI:
        1. Include any additional context before your examples
        2. Be specific about what you want generated after your examples
        3. Consider adding format guidance if needed
        """)
    
    # Activity 2
    st.markdown("## Activity 2: Converting Zero-Shot to Few-Shot Prompts")
    
    st.markdown("""
    In this activity, you'll practice converting zero-shot prompts into few-shot prompts by adding
    relevant examples. This skill helps when your initial zero-shot prompt isn't producing the results
    you want.
    """)
    
    # Create tabs for different prompt types to convert
    zero_shot_tabs = st.tabs(["Question Stems", "Learning Activities", "Rubric Criteria"])
    
    with zero_shot_tabs[0]:
        st.markdown("""
        **Original Zero-Shot Prompt:**
        ```
        Create 5 question stems for teaching critical thinking about primary source documents in a high school history class.
        ```
        
        **Your Task:** Convert this into a few-shot prompt by:
        1. Creating 2-3 examples of high-quality critical thinking question stems
        2. Making sure your examples demonstrate a consistent structure
        3. Adding clear instructions for what you want generated
        """)
        
        # User input for examples
        question_example1 = st.text_area(
            "Example Question Stem 1:",
            height=100,
            placeholder="Example: After examining the political cartoon from 1876, what evidence suggests the artist's opinion on Reconstruction policies?",
            key="question_example1"
        )
        
        question_example2 = st.text_area(
            "Example Question Stem 2:",
            height=100,
            placeholder="Example: How do the language choices in Lincoln's second inaugural address reflect the nation's mood in 1865?",
            key="question_example2"
        )
        
        # Converted prompt creation
        question_instruction = st.text_area(
            "Instructions to accompany your examples:",
            height=100,
            placeholder="Create 5 more question stems following this pattern for analyzing primary source documents from the Civil Rights Movement.",
            key="question_instruction"
        )
        
        if question_example1 and question_example2 and question_instruction:
            st.success("You've converted the zero-shot prompt into a few-shot prompt!")
            
            converted_prompt = f"""
            {question_instruction}
            
            Example 1:
            {question_example1}
            
            Example 2:
            {question_example2}
            """
            
            st.markdown("### Your Converted Few-Shot Prompt")
            st.code(converted_prompt, language="text")
            
            st.markdown("""
            **What Changed?**
            - Added specific examples that demonstrate the question style you want
            - Showed the level of critical thinking and the structure for questions
            - Made the pattern clearer through concrete examples
            """)
    
    with zero_shot_tabs[1]:
        st.markdown("""
        **Original Zero-Shot Prompt:**
        ```
        Create 3 learning activities for teaching fractions to 4th-grade students.
        ```
        
        **Your Task:** Convert this into a few-shot prompt by:
        1. Creating 2 examples of engaging, well-structured learning activities
        2. Making sure your examples follow a consistent format
        3. Adding clear instructions for what you want generated
        """)
        
        # User input for examples
        activity_example1 = st.text_area(
            "Example Learning Activity 1:",
            height=150,
            placeholder="Example: Fraction Pizza Parlor\nMaterials: Paper plates, colored paper, scissors\nDuration: 25 minutes\nDescription: Students create paper pizzas and divide them into equal parts to represent fractions. They label each slice with the appropriate fraction and practice combining different fractions by putting slices together.\nObjective: Students will represent and identify equivalent fractions using visual models.",
            key="activity_example1"
        )
        
        activity_example2 = st.text_area(
            "Example Learning Activity 2:",
            height=150,
            placeholder="Example: Fraction Number Line Jump\nMaterials: Masking tape, index cards, measuring tape\nDuration: 20 minutes\nDescription: Create a life-size number line on the floor using tape. Students take turns drawing fraction cards and physically jumping to that position on the number line. Classmates verify the position is correct.\nObjective: Students will locate fractions on a number line and compare their relative values.",
            key="activity_example2"
        )
        
        # Converted prompt creation
        activity_instruction = st.text_area(
            "Instructions to accompany your examples:",
            height=100,
            placeholder="Create 3 more hands-on learning activities following this same format for teaching fraction addition and subtraction to 4th-grade students.",
            key="activity_instruction"
        )
        
        if activity_example1 and activity_example2 and activity_instruction:
            st.success("You've converted the zero-shot prompt into a few-shot prompt!")
            
            converted_prompt = f"""
            {activity_instruction}
            
            Example 1:
            {activity_example1}
            
            Example 2:
            {activity_example2}
            """
            
            st.markdown("### Your Converted Few-Shot Prompt")
            st.code(converted_prompt, language="text")
            
            st.markdown("""
            **What Changed?**
            - Added structured examples that show the format for each activity
            - Demonstrated the level of detail you expect
            - Made clear what components should be included (materials, duration, etc.)
            """)
    
    with zero_shot_tabs[2]:
        st.markdown("""
        **Original Zero-Shot Prompt:**
        ```
        Create a rubric for evaluating student presentations in middle school.
        ```
        
        **Your Task:** Convert this into a few-shot prompt by:
        1. Creating 2 examples of well-crafted rubric criteria
        2. Making sure your examples use a consistent format and scoring system
        3. Adding clear instructions for what you want generated
        """)
        
        # User input for examples
        rubric_example1 = st.text_area(
            "Example Rubric Criterion 1:",
            height=150,
            placeholder="Example: ORGANIZATION\n1 - Beginning: Presentation lacks clear structure; information is presented randomly with no logical sequence.\n2 - Developing: Presentation has a basic structure but some content is out of logical order or connections between sections are unclear.\n3 - Proficient: Presentation has a clear beginning, middle, and end with logical transitions between most sections.\n4 - Exemplary: Presentation is exceptionally well-organized with a compelling introduction, strategically sequenced main points, smooth transitions, and a strong conclusion.",
            key="rubric_example1"
        )
        
        rubric_example2 = st.text_area(
            "Example Rubric Criterion 2:",
            height=150,
            placeholder="Example: VISUAL AIDS\n1 - Beginning: Visual aids are missing, inappropriate, or distract from the presentation.\n2 - Developing: Basic visual aids are used but may be disorganized, contain errors, or not clearly support the content.\n3 - Proficient: Clear, relevant visual aids support key points and enhance audience understanding.\n4 - Exemplary: Exceptionally effective visual aids significantly enhance the presentation with appropriate design elements, clear purpose, and seamless integration with spoken content.",
            key="rubric_example2"
        )
        
        # Converted prompt creation
        rubric_instruction = st.text_area(
            "Instructions to accompany your examples:",
            height=100,
            placeholder="Create 4 more rubric criteria following this exact 4-point scale format for evaluating middle school student presentations on science topics. Include criteria for Content Knowledge, Voice and Delivery, Audience Engagement, and Response to Questions.",
            key="rubric_instruction"
        )
        
        if rubric_example1 and rubric_example2 and rubric_instruction:
            st.success("You've converted the zero-shot prompt into a few-shot prompt!")
            
            converted_prompt = f"""
            {rubric_instruction}
            
            Example 1:
            {rubric_example1}
            
            Example 2:
            {rubric_example2}
            """
            
            st.markdown("### Your Converted Few-Shot Prompt")
            st.code(converted_prompt, language="text")
            
            st.markdown("""
            **What Changed?**
            - Added detailed examples that show the specific format for each criterion
            - Established the scoring system and level of detail for each performance level
            - Demonstrated the analytical approach and language style
            """)
    
    # Activity 3
    st.markdown("## Activity 3: Creating a Few-Shot Prompt for Your Teaching Context")
    
    st.markdown("""
    In this activity, you'll create a complete few-shot prompt tailored to your specific teaching needs.
    Focus on a content type that you create regularly where consistency in format is important.
    """)
    
    # Content type selection
    teaching_content = st.text_input(
        "What type of educational content do you need to create?",
        placeholder="e.g., 'Word problems for 3rd-grade multiplication' or 'Lab safety procedures for chemistry'",
        key="teaching_content"
    )
    
    # Introduction and context
    prompt_intro = st.text_area(
        "Introduction and context for your prompt:",
        height=100,
        placeholder="I need to create several [content type] for my [grade/subject] class that follow a consistent format...",
        key="prompt_intro"
    )
    
    # Examples
    st.markdown("### Your Examples")
    
    teaching_example1 = st.text_area(
        "Example 1:",
        height=150,
        placeholder="Your first high-quality example...",
        key="teaching_example1"
    )
    
    teaching_example2 = st.text_area(
        "Example 2:",
        height=150,
        placeholder="Your second high-quality example...",
        key="teaching_example2"
    )
    
    # Final instruction
    final_instruction = st.text_area(
        "Final instruction after your examples:",
        height=100,
        placeholder="Please create 5 more [content type] following this exact format for [specific topic/purpose]...",
        key="final_instruction"
    )
    
    # Why few-shot is appropriate
    few_shot_justification = st.text_area(
        "Why is few-shot prompting particularly appropriate for this content?",
        height=100,
        placeholder="Explain why providing examples is better than just describing what you want...",
        key="few_shot_justification"
    )
    
    if teaching_content and prompt_intro and teaching_example1 and teaching_example2 and final_instruction and few_shot_justification:
        st.success("You've created a complete few-shot prompt for your teaching context!")
        
        complete_teaching_prompt = f"""
        {prompt_intro}
        
        Example 1:
        {teaching_example1}
        
        Example 2:
        {teaching_example2}
        
        {final_instruction}
        """
        
        st.markdown("### Your Complete Few-Shot Prompt")
        st.code(complete_teaching_prompt, language="text")
        
        st.markdown("""
        ### Few-Shot vs. Zero-Shot for Your Content
        
        Few-shot prompting is particularly effective when:
        - You need precise control over formatting
        - You want to demonstrate specific approaches or styles
        - You're creating a set of related materials that should be consistent
        - You've found that general descriptions alone (zero-shot) don't give you exactly what you want
        
        The examples you've created serve as concrete models rather than abstract descriptions,
        making it easier for the AI to match your expectations exactly.
        """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * For Activity 1, encourage participants to focus on the most important elements they want to see in the AI's responses
    * For Activity 2, suggest that participants think about what was missing or inconsistent in their previous zero-shot attempts
    * For Activity 3, remind participants that they can save these prompts and reuse them as templates
    
    **Common Challenges:**
    
    * Some participants may create examples that are too different from each other, making the pattern unclear
    * Others may struggle with determining how many examples are sufficient - suggest starting with two and adding a third only if needed
    * Participants may need help focusing on format consistency across examples
    
    **Extension Ideas:**
    
    * Have participants exchange few-shot prompts and evaluate whether the pattern is clear from the examples
    * Challenge participants to create a "few-shot prompt library" for their most frequently created content types
    * Encourage experimentation with deliberately varied examples to show the AI the range of acceptable variations
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