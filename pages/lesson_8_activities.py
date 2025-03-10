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
    page_title="Lesson 8: Activities",
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
    "title": "Iteration: Activities",
    "lesson": "8",
    "section": "activities",
    "order": 3
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_8_activities"
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
    "lesson_8_activities",
    "activities",
    "Lesson 8 Activities",
    """
    **This section provides hands-on practice with iteration techniques.**
    
    You'll:
    - Apply different iteration strategies to improve prompts
    - Track changes and improvements across iterations
    - Learn to identify which changes had the biggest impact
    
    Complete these activities to strengthen your iteration skills before
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
    
    Complete the activities below to practice iterative prompt improvement.
    After finishing these activities, proceed to the Reflection section to consolidate your learning 
    and unlock the next lesson.
    """)
    
    # Activity 1
    st.markdown("## Activity 1: Analyzing and Improving a Basic Prompt")
    
    st.markdown("""
    In this activity, you'll analyze a simple prompt and create two improved iterations based on 
    your evaluation of its weaknesses.
    """)
    
    # Original prompt to improve
    st.markdown("""
    ### Original Prompt
    
    ```
    Create a quiz on fractions.
    ```
    
    **What's wrong with this prompt?** 
    
    This prompt lacks specificity in multiple areas:
    - No grade level or student information
    - No indication of quiz length or format
    - No standards alignment or learning objectives
    - No guidance on difficulty level
    - No specification of fraction topics to cover
    """)
    
    # First iteration
    st.markdown("### Your First Iteration")
    
    st.markdown("""
    For your first iteration, focus on adding basic specificity such as grade level, 
    quiz length, and content focus. What would you add to improve this prompt?
    """)
    
    iteration1 = st.text_area(
        "Write your first improved version of the prompt:",
        height=100,
        placeholder="Example: Create a 10-question quiz on fractions for 5th-grade students, focusing on addition and subtraction of fractions with different denominators...",
        key="iteration1"
    )
    
    # Analysis of first iteration
    improvement_analysis1 = st.text_area(
        "What specific improvements did you make and why?",
        height=80,
        placeholder="Explain what elements you added to the prompt and how they address the shortcomings of the original...",
        key="analysis1"
    )
    
    # Second iteration
    st.markdown("### Your Second Iteration")
    
    st.markdown("""
    For your second iteration, build on your first version by adding more sophisticated elements such as 
    format specifications, standards alignment, or differentiation options.
    """)
    
    iteration2 = st.text_area(
        "Write your second improved version of the prompt:",
        height=150,
        placeholder="Example: Create a 5th-grade math quiz on fractions aligned with Common Core standard 5.NF.A.1 that includes...",
        key="iteration2"
    )
    
    # Analysis of second iteration
    improvement_analysis2 = st.text_area(
        "What additional improvements did you make and why?",
        height=80,
        placeholder="Explain what elements you added in this iteration and how they further enhance the prompt...",
        key="analysis2"
    )
    
    # Reflection on the iteration process
    iteration_reflection = st.text_area(
        "What did you learn from this iterative process?",
        height=80,
        placeholder="Reflect on how your thinking about prompt construction changed through the iterations...",
        key="reflection1"
    )
    
    if iteration1 and iteration2 and improvement_analysis1 and improvement_analysis2 and iteration_reflection:
        st.success("You've completed the iterative improvement activity!")
        
        st.markdown("""
        ### Example of Excellent Iteration
        
        For comparison, here's an example of how this prompt might be iteratively improved:
        
        **Original:** 
        ```
        Create a quiz on fractions.
        ```
        
        **First Iteration:**
        ```
        Create a 10-question quiz on fractions for 4th-grade students, 
        focusing on comparing fractions and equivalent fractions.
        ```
        
        **Second Iteration:**
        ```
        Create a 4th-grade math quiz on fractions that:
        1. Aligns with Common Core standard 4.NF.A.2 (comparing fractions)
        2. Includes 6 multiple-choice and 4 short-answer questions
        3. Progresses from simple to more challenging problems
        4. Incorporates visual models for fraction comparisons
        5. Includes an answer key with explanations
        6. Can be completed in 20 minutes
        ```
        
        Notice how each iteration adds specificity, structure, and educational context.
        """)
    
    # Activity 2
    st.markdown("## Activity 2: Targeted Iteration Strategy Practice")
    
    st.markdown("""
    In this activity, you'll practice using specific iteration strategies on a provided prompt.
    """)
    
    # Original prompt
    st.markdown("""
    ### Original Prompt
    
    ```
    Create a lesson on multiplication for students.
    ```
    """)
    
    # Select iteration strategy
    iteration_strategy = st.selectbox(
        "Choose an iteration strategy to practice:",
        [
            "Additive Iteration (adding elements)",
            "Subtractive Iteration (removing or focusing elements)",
            "Parameter Tuning (adjusting specific aspects)",
            "Structural Reframing (reorganizing presentation)",
            "Example-Driven Refinement (adding examples)"
        ],
        key="strategy_select"
    )
    
    # Display guidance based on selected strategy
    if iteration_strategy == "Additive Iteration (adding elements)":
        st.markdown("""
        **Additive Iteration** involves improving a prompt by adding specific elements that were missing.
        
        Consider adding:
        - Grade level or student information
        - Specific multiplication topics
        - Learning objectives
        - Timing and structure
        - Activity types
        """)
    
    elif iteration_strategy == "Subtractive Iteration (removing or focusing elements)":
        st.markdown("""
        **Subtractive Iteration** involves narrowing focus or removing unnecessary elements.
        
        Consider:
        - Focusing on a specific multiplication concept (e.g., just multiplication by 10)
        - Limiting the lesson to a specific grade level
        - Focusing on just one type of activity or approach
        - Limiting the scope to a single, clear learning objective
        """)
    
    elif iteration_strategy == "Parameter Tuning (adjusting specific aspects)":
        st.markdown("""
        **Parameter Tuning** involves adjusting specific variables within the prompt.
        
        Consider tuning:
        - Complexity level (basic to advanced)
        - Time allocation (10-minute activity to full lesson)
        - Approach style (direct instruction vs. inquiry-based)
        - Output format (detailed vs. concise)
        """)
    
    elif iteration_strategy == "Structural Reframing (reorganizing presentation)":
        st.markdown("""
        **Structural Reframing** involves changing how the prompt is organized or presented.
        
        Consider reframing as:
        - A step-by-step template
        - A bulleted list of requirements
        - A scenario-based request
        - A comparative format (e.g., "Create two approaches to teaching multiplication...")
        """)
    
    elif iteration_strategy == "Example-Driven Refinement (adding examples)":
        st.markdown("""
        **Example-Driven Refinement** involves adding examples of what you want.
        
        Consider adding:
        - An example of a multiplication activity you like
        - A sample explanation of a multiplication concept
        - An example of how you want students to practice
        - A model of the expected output format
        """)
    
    # Apply the selected strategy
    improved_prompt = st.text_area(
        f"Apply {iteration_strategy.split('(')[0].strip()} to improve the prompt:",
        height=150,
        placeholder="Write your improved prompt here, applying the selected strategy...",
        key="strategy_application"
    )
    
    # Explain your approach
    strategy_explanation = st.text_area(
        "Explain how you applied this strategy and what improvements you expect:",
        height=100,
        placeholder="Describe how you used the selected strategy and what specific improvements you expect in the AI's response...",
        key="strategy_explanation"
    )
    
    if improved_prompt and strategy_explanation:
        st.success(f"You've successfully applied {iteration_strategy.split('(')[0].strip()}!")
        
        st.markdown(f"""
        ### Example of {iteration_strategy.split('(')[0].strip()}
        
        For comparison, here's an example of how the strategy might be applied:
        
        **Original:** 
        ```
        Create a lesson on multiplication for students.
        ```
        """)
        
        if iteration_strategy == "Additive Iteration (adding elements)":
            st.markdown("""
            **Additive Iteration Example:**
            ```
            Create a 3rd-grade lesson on multiplication for students that includes:
            1. A connection to multiplication as repeated addition
            2. Visual models using arrays
            3. A hands-on activity with manipulatives
            4. Practice problems using single-digit multipliers
            5. A formative assessment check
            ```
            """)
        
        elif iteration_strategy == "Subtractive Iteration (removing or focusing elements)":
            st.markdown("""
            **Subtractive Iteration Example:**
            ```
            Create a focused 15-minute lesson specifically on multiplication by 10 for 2nd-grade students.
            ```
            """)
        
        elif iteration_strategy == "Parameter Tuning (adjusting specific aspects)":
            st.markdown("""
            **Parameter Tuning Example:**
            ```
            Create an advanced 45-minute inquiry-based multiplication lesson for gifted 4th-grade students who have already mastered basic multiplication facts.
            ```
            """)
        
        elif iteration_strategy == "Structural Reframing (reorganizing presentation)":
            st.markdown("""
            **Structural Reframing Example:**
            ```
            Create a multiplication lesson using this template:
            
            LESSON TITLE:
            GRADE LEVEL:
            LEARNING OBJECTIVE:
            WARM-UP ACTIVITY (5 min):
            MAIN INSTRUCTION (15 min):
            GUIDED PRACTICE (15 min):
            INDEPENDENT PRACTICE (10 min):
            ASSESSMENT (5 min):
            ```
            """)
        
        elif iteration_strategy == "Example-Driven Refinement (adding examples)":
            st.markdown("""
            **Example-Driven Refinement Example:**
            ```
            Create a lesson on multiplication for 3rd-grade students. Include an activity similar to this example:
            
            "Multiplication Scavenger Hunt: Students find real-world examples of arrays (e.g., egg cartons, muffin tins) and write the multiplication equation that represents them (e.g., a 2×6 egg carton represents 2×6=12)."
            
            The lesson should include similar hands-on, real-world connections to multiplication concepts.
            ```
            """)
    
    # Activity 3
    st.markdown("## Activity 3: PCTFREI Iterative Improvement")
    
    st.markdown("""
    In this activity, you'll practice applying the complete PCTFREI framework to iteratively improve a prompt.
    """)
    
    # Original prompt
    st.markdown("""
    ### Original Prompt
    
    ```
    Create a writing assignment.
    ```
    
    This extremely basic prompt lacks all elements of the PCTFREI framework. Your task is to improve it by 
    adding each component of the framework one by one.
    """)
    
    # P - Persona
    st.markdown("### Step 1: Add Persona (P)")
    persona_addition = st.text_area(
        "Add a specific persona to the prompt:",
        height=80,
        placeholder="Example: As a 6th-grade English Language Arts teacher...",
        key="persona_addition"
    )
    
    # T - Task
    st.markdown("### Step 2: Add Task Specification (T)")
    task_addition = st.text_area(
        "Add specific task details:",
        height=80,
        placeholder="Example: ...create a narrative writing assignment that focuses on character development...",
        key="task_addition"
    )
    
    # C - Context
    st.markdown("### Step 3: Add Context (C)")
    context_addition = st.text_area(
        "Add relevant context:",
        height=80,
        placeholder="Example: ...for students who have just finished reading 'The Giver' and are learning about dystopian fiction...",
        key="context_addition"
    )
    
    # F - Format
    st.markdown("### Step 4: Add Format Specifications (F)")
    format_addition = st.text_area(
        "Add format requirements:",
        height=100,
        placeholder="Example: Format the assignment with the following sections:\n- Assignment overview\n- Learning objectives\n- Writing prompt\n- Requirements (length, elements to include)\n- Grading criteria\n- Timeline",
        key="format_addition"
    )
    
    # R - Reference
    st.markdown("### Step 5: Add Reference Materials (R)")
    reference_addition = st.text_area(
        "Add reference materials or standards alignment:",
        height=80,
        placeholder="Example: Align the assignment with Common Core standard W.6.3 (Write narratives to develop real or imagined experiences using effective technique, relevant descriptive details, and well-structured event sequences).",
        key="reference_addition"
    )
    
    # E - Evaluation
    st.markdown("### Step 6: Add Evaluation Considerations (E)")
    evaluation_addition = st.text_area(
        "Based on an evaluation of previous writing assignments, add specific requirements:",
        height=100,
        placeholder="Example: Based on previous writing assignments, ensure that:\n- The prompt encourages creative thinking while providing enough structure\n- Clear examples of character development techniques are included\n- Explicit connections to themes in 'The Giver' are required\n- Differentiation options for struggling and advanced writers are provided",
        key="evaluation_addition"
    )
    
    # I - Iteration
    st.markdown("### Step 7: Final Iteration (I)")
    
    st.markdown("""
    Now, put together all components into a cohesive, well-structured prompt. You can make additional
    refinements to ensure the prompt flows well and all elements work together.
    """)
    
    final_prompt = st.text_area(
        "Write your final, comprehensive prompt incorporating all PCTFREI elements:",
        height=250,
        placeholder="Combine all the elements you've developed into a final, polished prompt...",
        key="final_prompt"
    )
    
    if (persona_addition and task_addition and context_addition and format_addition and 
        reference_addition and evaluation_addition and final_prompt):
        st.success("Congratulations! You've completed the PCTFREI framework application!")
        
        st.markdown("""
        ### The Power of the PCTFREI Framework
        
        Compare your original prompt:
        ```
        Create a writing assignment.
        ```
        
        With your comprehensive final prompt that includes:
        - Persona: Establishes who is creating the content
        - Task: Clearly defines what is being created
        - Context: Provides background and situational information
        - Format: Specifies how the content should be structured
        - Reference: Incorporates standards or source materials
        - Evaluation: Addresses known issues or concerns
        - Iteration: Refines all elements into a cohesive whole
        
        While your final prompt is longer, it will produce a much more specific, useful, and educationally sound result.
        """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * For Activity 1, encourage participants to think about how each iteration addresses specific weaknesses in the original prompt
    * For Activity 2, suggest that participants try multiple strategies on the same prompt to see which works best
    * For Activity 3, emphasize that the PCTFREI framework provides a systematic approach to prompt improvement
    
    **Common Challenges:**
    
    * Participants may make too many changes at once, making it difficult to identify what worked
    * Some may find the full PCTFREI framework overwhelming - remind them that they can start simple and build up
    * Others may worry about prompt length - reassure them that comprehensive prompts produce better results
    
    **Extension Ideas:**
    
    * Have participants apply the PCTFREI framework to a prompt they use regularly in their teaching
    * Create a collaborative prompt library where participants can share their iteratively improved prompts
    * Conduct a "prompt critique circle" where colleagues review and suggest iterations for each other's prompts
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