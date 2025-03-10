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
    page_title="Lesson 11: Activities",
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
    "title": "Chain-of-Thought Prompting: Activities",
    "lesson": "11",
    "section": "activities",
    "order": 3
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_11_activities"
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
    "lesson_11_activities",
    "activities",
    "Lesson 11 Activities",
    """
    **This section provides hands-on practice with chain-of-thought prompting.**
    
    You'll:
    - Create chain-of-thought prompts for different educational purposes
    - Transform basic prompts into more effective chain-of-thought versions
    - Apply this technique to your specific teaching context
    
    Complete these activities to strengthen your chain-of-thought prompting skills before
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
    
    Complete the activities below to practice creating effective chain-of-thought prompts.
    After finishing these activities, proceed to the Reflection section to consolidate your learning 
    and unlock the next lesson.
    """)
    
    # Activity 1
    st.markdown("## Activity 1: Identifying Thinking Steps for Different Tasks")
    
    st.markdown("""
    Different educational tasks require different types of reasoning processes. In this activity, you'll identify
    the appropriate thinking steps for various educational tasks.
    """)
    
    # Create tabs for different subjects
    subject_tabs = st.tabs(["Mathematics", "Science", "Language Arts", "Social Studies"])
    
    with subject_tabs[0]:
        st.markdown("""
        ### Mathematics Reasoning Steps
        
        For mathematical problem-solving, what thinking steps would you want the AI to show?
        Select the steps that would be most useful for students learning mathematics:
        """)
        
        st.checkbox("Identifying given information and what needs to be found", key="math_step1")
        st.checkbox("Recalling relevant formulas or theorems", key="math_step2")
        st.checkbox("Drawing diagrams or visual representations", key="math_step3")
        st.checkbox("Setting up equations", key="math_step4")
        st.checkbox("Showing each calculation step", key="math_step5")
        st.checkbox("Checking the answer for reasonableness", key="math_step6")
        st.checkbox("Explaining connections to conceptual understanding", key="math_step7")
        
        st.markdown("""
        Now, craft a chain-of-thought prompt for a mathematical problem-solving task. Include explicit
        instructions for the AI to show the thinking steps you selected above:
        """)
        
        math_prompt = st.text_area(
            "Your chain-of-thought prompt for a math problem:",
            height=150,
            placeholder="Solve the following quadratic equation: 2x² - 5x - 3 = 0. Show your step-by-step thinking, including...",
            key="math_prompt"
        )
    
    with subject_tabs[1]:
        st.markdown("""
        ### Science Reasoning Steps
        
        For scientific explanation or analysis, what thinking steps would you want the AI to show?
        Select the steps that would be most useful for students learning science:
        """)
        
        st.checkbox("Identifying relevant scientific principles", key="science_step1")
        st.checkbox("Breaking down complex processes into stages", key="science_step2")
        st.checkbox("Connecting observations to underlying causes", key="science_step3")
        st.checkbox("Drawing and explaining models or diagrams", key="science_step4")
        st.checkbox("Making predictions based on scientific principles", key="science_step5")
        st.checkbox("Addressing common misconceptions", key="science_step6")
        st.checkbox("Connecting micro and macro levels of explanation", key="science_step7")
        
        st.markdown("""
        Now, craft a chain-of-thought prompt for a scientific explanation task. Include explicit
        instructions for the AI to show the thinking steps you selected above:
        """)
        
        science_prompt = st.text_area(
            "Your chain-of-thought prompt for a science explanation:",
            height=150,
            placeholder="Explain how an electrical circuit works. Break down your explanation by...",
            key="science_prompt"
        )
    
    with subject_tabs[2]:
        st.markdown("""
        ### Language Arts Reasoning Steps
        
        For literary analysis or writing tasks, what thinking steps would you want the AI to show?
        Select the steps that would be most useful for students in language arts:
        """)
        
        st.checkbox("Identifying key textual evidence", key="ela_step1")
        st.checkbox("Analyzing stylistic or literary devices", key="ela_step2")
        st.checkbox("Drawing inferences from the text", key="ela_step3")
        st.checkbox("Connecting to broader themes or contexts", key="ela_step4")
        st.checkbox("Evaluating multiple interpretations", key="ela_step5")
        st.checkbox("Developing a coherent argument from evidence", key="ela_step6")
        st.checkbox("Revising and refining ideas", key="ela_step7")
        
        st.markdown("""
        Now, craft a chain-of-thought prompt for a language arts analysis task. Include explicit
        instructions for the AI to show the thinking steps you selected above:
        """)
        
        ela_prompt = st.text_area(
            "Your chain-of-thought prompt for a language arts task:",
            height=150,
            placeholder="Analyze the characterization of Atticus Finch in 'To Kill a Mockingbird.' In your analysis, walk through...",
            key="ela_prompt"
        )
    
    with subject_tabs[3]:
        st.markdown("""
        ### Social Studies Reasoning Steps
        
        For historical analysis or civic understanding, what thinking steps would you want the AI to show?
        Select the steps that would be most useful for students in social studies:
        """)
        
        st.checkbox("Identifying historical context and time period", key="ss_step1")
        st.checkbox("Analyzing multiple causes and effects", key="ss_step2")
        st.checkbox("Evaluating primary and secondary sources", key="ss_step3")
        st.checkbox("Considering multiple perspectives", key="ss_step4")
        st.checkbox("Connecting to broader patterns or themes", key="ss_step5")
        st.checkbox("Distinguishing between facts and interpretations", key="ss_step6")
        st.checkbox("Drawing evidence-based conclusions", key="ss_step7")
        
        st.markdown("""
        Now, craft a chain-of-thought prompt for a social studies analysis task. Include explicit
        instructions for the AI to show the thinking steps you selected above:
        """)
        
        ss_prompt = st.text_area(
            "Your chain-of-thought prompt for a social studies task:",
            height=150,
            placeholder="Analyze the causes of the American Civil War. In your analysis, work through...",
            key="ss_prompt"
        )
    
    # Activity 2
    st.markdown("## Activity 2: Transforming Basic Prompts into Chain-of-Thought Prompts")
    
    st.markdown("""
    In this activity, you'll practice transforming basic prompts into more effective chain-of-thought prompts
    that generate step-by-step reasoning.
    """)
    
    # Create tabs for different prompt types
    prompt_tabs = st.tabs(["Problem Solving", "Conceptual Explanation", "Analysis Task"])
    
    with prompt_tabs[0]:
        st.markdown("""
        ### Transform a Problem-Solving Prompt
        
        **Basic Prompt:**
        ```
        Create a word problem about mixture percentages appropriate for 8th-grade math.
        ```
        
        This basic prompt might generate a word problem, but won't necessarily include the step-by-step
        solution process that would be valuable for teaching.
        
        **Your Task:** Transform this into a chain-of-thought prompt that will generate both a good word
        problem AND a clear step-by-step solution that models mathematical thinking.
        """)
        
        transform_problem = st.text_area(
            "Your transformed chain-of-thought prompt:",
            height=150,
            placeholder="Create a word problem about mixture percentages appropriate for 8th-grade math. Then...",
            key="transform_problem"
        )
        
        if transform_problem:
            st.success("Here's what makes an effective transformation for this type of prompt:")
            
            st.markdown("""
            **Key Elements to Include:**
            
            1. Request for a grade-appropriate word problem on the topic
            2. Instructions to solve the problem step-by-step
            3. Specification of the thinking process to show (identifying variables, setting up equations, etc.)
            4. Request to explain the reasoning behind each step
            5. Instructions to verify the solution
            
            **Example Transformation:**
            ```
            Create a word problem about mixture percentages appropriate for 8th-grade math. Then, provide a complete step-by-step solution that would help students understand the problem-solving process. In your solution:
            
            1. Identify the variables and what we're trying to find
            2. Show how to translate the word problem into mathematical expressions
            3. Demonstrate each calculation step clearly
            4. Explain the reasoning behind each step in student-friendly language
            5. Verify that the solution makes sense in the context of the problem
            
            The solution should model the thinking process that students should use when solving similar problems.
            ```
            """)
    
    with prompt_tabs[1]:
        st.markdown("""
        ### Transform a Conceptual Explanation Prompt
        
        **Basic Prompt:**
        ```
        Explain how weather fronts cause changes in weather patterns.
        ```
        
        This basic prompt might generate a factual explanation, but may not break down the causal
        relationships or process in a way that promotes deep understanding.
        
        **Your Task:** Transform this into a chain-of-thought prompt that will generate a clearer,
        more step-by-step explanation of the causal process.
        """)
        
        transform_explanation = st.text_area(
            "Your transformed chain-of-thought prompt:",
            height=150,
            placeholder="Explain how weather fronts cause changes in weather patterns by...",
            key="transform_explanation"
        )
        
        if transform_explanation:
            st.success("Here's what makes an effective transformation for this type of prompt:")
            
            st.markdown("""
            **Key Elements to Include:**
            
            1. Request for a sequential explanation of processes
            2. Instructions to break down complex cause-effect relationships
            3. Request to connect abstract concepts to observable phenomena
            4. Instructions to include clarifying examples or analogies
            5. Request to address common misconceptions
            
            **Example Transformation:**
            ```
            Explain how weather fronts cause changes in weather patterns, using a chain-of-thought approach. In your explanation:
            
            1. Start by defining what weather fronts are and the main types
            2. For each type of front, walk through the process of what happens when it moves into an area:
               - What happens at the boundary between air masses?
               - What physical processes occur (condensation, air movements, etc.)?
               - How do these processes translate to observable weather changes?
            3. Use clear cause-and-effect language to show how each stage leads to the next
            4. Include a simple analogy that helps visualize these processes
            5. Address the common misconception that fronts themselves are storms rather than boundaries
            
            Your explanation should help students visualize the sequential process from front formation to weather change.
            ```
            """)
    
    with prompt_tabs[2]:
        st.markdown("""
        ### Transform an Analysis Task Prompt
        
        **Basic Prompt:**
        ```
        Compare and contrast democracy and authoritarianism as systems of government.
        ```
        
        This basic prompt might generate a simple comparison, but may not provide the analytical
        depth or structured framework that would be educationally valuable.
        
        **Your Task:** Transform this into a chain-of-thought prompt that will guide a more thoughtful,
        methodical analysis with clear criteria and evaluation.
        """)
        
        transform_analysis = st.text_area(
            "Your transformed chain-of-thought prompt:",
            height=150,
            placeholder="Compare and contrast democracy and authoritarianism as systems of government by...",
            key="transform_analysis"
        )
        
        if transform_analysis:
            st.success("Here's what makes an effective transformation for this type of prompt:")
            
            st.markdown("""
            **Key Elements to Include:**
            
            1. Specific analytical framework or criteria for comparison
            2. Instructions to consider multiple dimensions
            3. Request to provide concrete examples
            4. Instructions to evaluate strengths and weaknesses
            5. Request to consider context and nuance
            
            **Example Transformation:**
            ```
            Compare and contrast democracy and authoritarianism as systems of government, using a structured analytical approach. In your analysis:
            
            1. First, establish clear definitions for both systems and identify their key characteristics
            
            2. Then, systematically compare these systems across multiple dimensions:
               - Distribution of power and decision-making processes
               - Citizen rights and civil liberties
               - Methods of leadership selection and transition
               - Accountability mechanisms and checks on power
               - Historical examples that demonstrate these characteristics
            
            3. For each dimension, analyze:
               - How each system typically functions in this area
               - The theoretical and practical strengths and weaknesses
               - How real-world implementations may differ from theoretical models
            
            4. Discuss how these systems exist on a spectrum rather than as absolute categories, using specific country examples to illustrate this nuance
            
            5. Conclude by synthesizing these comparisons into broader insights about governance
            
            This structured analysis should help students develop a nuanced understanding beyond simple binary comparisons.
            ```
            """)
    
    # Activity 3
    st.markdown("## Activity 3: Creating Chain-of-Thought Prompts for Your Teaching")
    
    st.markdown("""
    In this activity, you'll create a complete chain-of-thought prompt tailored to your specific teaching needs.
    Focus on a concept or skill where seeing the reasoning process would be particularly valuable for students.
    """)
    
    # Teaching context
    teaching_context = st.text_input(
        "What subject and grade level do you teach?",
        placeholder="e.g., '7th-grade science' or 'High school literature'",
        key="teaching_context"
    )
    
    # Educational need
    educational_need = st.text_input(
        "What concept or skill do your students need step-by-step guidance with?",
        placeholder="e.g., 'Balancing chemical equations' or 'Rhetorical analysis of speeches'",
        key="educational_need"
    )
    
    # Thinking steps
    st.markdown("### Thinking Steps to Include")
    
    st.markdown("""
    What specific thinking steps would you want the AI to show in its response?
    List 3-6 sequential steps that would model effective reasoning for this skill:
    """)
    
    thinking_step1 = st.text_input("Step 1:", key="thinking_step1")
    thinking_step2 = st.text_input("Step 2:", key="thinking_step2")
    thinking_step3 = st.text_input("Step 3:", key="thinking_step3")
    
    show_more_steps = st.checkbox("Add more steps?")
    
    if show_more_steps:
        thinking_step4 = st.text_input("Step 4:", key="thinking_step4")
        thinking_step5 = st.text_input("Step 5:", key="thinking_step5")
        thinking_step6 = st.text_input("Step 6:", key="thinking_step6")
    
    # Complete prompt
    st.markdown("### Your Complete Chain-of-Thought Prompt")
    
    prompt_instruction = st.text_area(
        "Write your complete chain-of-thought prompt, incorporating the thinking steps you identified:",
        height=200,
        key="prompt_instruction"
    )
    
    # Educational benefit
    educational_benefit = st.text_area(
        "How would this chain-of-thought approach benefit your students' learning?",
        height=100,
        placeholder="Explain how seeing this reasoning process would help students understand the concept or develop the skill...",
        key="educational_benefit"
    )
    
    # Show completed prompt with analysis
    if teaching_context and educational_need and thinking_step1 and thinking_step2 and thinking_step3 and prompt_instruction and educational_benefit:
        st.success("You've created a complete chain-of-thought prompt for your teaching context!")
        
        st.markdown("### Your Chain-of-Thought Prompt Analysis")
        
        st.markdown(f"""
        **Teaching Context:** {teaching_context}
        
        **Educational Need:** {educational_need}
        
        **Chain-of-Thought Elements Included:**
        - {"✓" if "step" in prompt_instruction.lower() or "steps" in prompt_instruction.lower() else "❌"} Explicit request for step-by-step reasoning
        - {"✓" if "why" in prompt_instruction.lower() or "explain" in prompt_instruction.lower() or "reasoning" in prompt_instruction.lower() else "❌"} Instructions to explain reasoning (not just steps)
        - {"✓" if "first" in prompt_instruction.lower() or "then" in prompt_instruction.lower() or "1." in prompt_instruction or "2." in prompt_instruction else "❌"} Sequential structure
        - {"✓" if educational_need.lower() in prompt_instruction.lower() else "❌"} Focus on the specific concept/skill
        
        **Educational Benefits Identified:**
        {educational_benefit}
        """)
        
        st.markdown("""
        ### Tips for Implementation
        
        1. **Test your prompt** to make sure it generates the kind of step-by-step reasoning you want
        
        2. **Refine as needed** if certain steps are missing or unclear
        
        3. **Consider using the output** as:
           - Worked examples for students
           - Scaffolded guidance for difficult problems
           - Models for students to emulate in their own work
           - Differentiation tools for various learning needs
        
        4. **Share your chain-of-thought approach** with colleagues to improve reasoning instruction
        """)
    
    # Activity 4
    st.markdown("## Activity 4: Combining Chain-of-Thought with Other Techniques")
    
    st.markdown("""
    In this activity, you'll explore how to combine chain-of-thought prompting with other techniques
    you've learned in this course, such as the PTC-FREI framework or few-shot prompting.
    """)
    
    # Choose a combination
    technique_combination = st.selectbox(
        "Which technique would you like to combine with Chain-of-Thought?",
        [
            "Few-Shot Prompting (providing examples)",
            "Persona (adopting a specific voice)",
            "Context (providing background information)",
            "Task (clearly defined objective)",
            "Format (specific output structure)",
            "Reference Materials (using sources)"
        ],
        key="technique_combination"
    )
    
    # Display guidance based on selection
    if technique_combination == "Few-Shot Prompting (providing examples)":
        st.markdown("""
        ### Combining Chain-of-Thought with Few-Shot Prompting
        
        This powerful combination uses examples to show the specific reasoning pattern you want,
        then asks for new content following the same pattern.
        
        **Example Structure:**
        ```
        I need [type of content] that shows step-by-step thinking. Here's an example:
        
        Example:
        [Problem/question]
        
        Step 1: [First step in reasoning]
        Step 2: [Second step in reasoning]
        ...
        Conclusion: [Final answer]
        
        Please create [number] more examples following this exact step-by-step pattern for [topic].
        ```
        """)
        
    elif technique_combination == "Persona (adopting a specific voice)":
        st.markdown("""
        ### Combining Chain-of-Thought with Persona
        
        This combination creates step-by-step explanations in a specific voice that resonates with your students.
        
        **Example Structure:**
        ```
        As a [specific type of instructor/mentor], explain [concept] using a step-by-step approach.
        
        Break down your explanation as if you were thinking aloud while teaching, showing each stage
        of reasoning clearly. Use language and examples that would engage [target audience].
        ```
        """)
        
    elif technique_combination == "Context (providing background information)":
        st.markdown("""
        ### Combining Chain-of-Thought with Context
        
        This combination ensures the step-by-step explanation is tailored to your students' specific background
        and learning situation.
        
        **Example Structure:**
        ```
        Context: My students are [description of students] who have already learned [prior knowledge]
        but struggle with [specific challenge].
        
        Create a step-by-step explanation of [concept/problem] that shows each stage of thinking.
        The explanation should build on their existing knowledge and specifically address their
        common misconceptions about [specific aspect].
        ```
        """)
        
    elif technique_combination == "Task (clearly defined objective)":
        st.markdown("""
        ### Combining Chain-of-Thought with Task
        
        This combination ensures the step-by-step explanation serves a specific educational purpose.
        
        **Example Structure:**
        ```
        Task: Create a worked example that demonstrates how to [specific skill/process] for the purpose
        of [educational objective].
        
        Show the complete thinking process step-by-step, including:
        1. [First specific thinking step]
        2. [Second specific thinking step]
        3. [Third specific thinking step]
        
        The example should help students learn to apply this process independently.
        ```
        """)
        
    elif technique_combination == "Format (specific output structure)":
        st.markdown("""
        ### Combining Chain-of-Thought with Format
        
        This combination ensures the step-by-step explanation is presented in a structure that's most
        effective for your teaching needs.
        
        **Example Structure:**
        ```
        Explain [concept/process] using a step-by-step approach. Format your explanation as:
        
        CONCEPT OVERVIEW: [Brief summary of the overall concept]
        
        STEP 1: [Title of first step]
        • Explanation: [Detailed explanation]
        • Why this matters: [Connection to overall concept]
        • Visual to imagine: [Metaphor or mental image]
        
        STEP 2: [Title of second step]
        • Explanation: [Detailed explanation]
        • Why this matters: [Connection to overall concept]
        • Visual to imagine: [Metaphor or mental image]
        
        [Continue for all steps]
        
        COMMON MISCONCEPTION: [Address a typical confusion]
        
        PRACTICE APPLICATION: [Simple exercise for students]
        ```
        """)
        
    elif technique_combination == "Reference Materials (using sources)":
        st.markdown("""
        ### Combining Chain-of-Thought with Reference Materials
        
        This combination ensures the step-by-step explanation incorporates and references specific
        source materials or standards.
        
        **Example Structure:**
        ```
        Using the following reference material:
        
        [Insert curriculum standard, text passage, or reference information]
        
        Create a step-by-step explanation of [concept/process] that explicitly shows the reasoning
        process. At each step, connect your explanation to specific elements from the reference
        material to show how they inform the thinking process.
        ```
        """)
    
    # Combined prompt creation
    st.markdown("### Create Your Combined Prompt")
    
    combined_prompt = st.text_area(
        f"Write a prompt that combines Chain-of-Thought with {technique_combination.split('(')[0].strip()}:",
        height=200,
        key="combined_prompt"
    )
    
    if combined_prompt:
        st.success(f"You've created a prompt that combines Chain-of-Thought with {technique_combination.split('(')[0].strip()}!")
        
        st.markdown("""
        ### Benefits of Combining Techniques
        
        Combining chain-of-thought prompting with other techniques allows you to:
        
        1. **Increase specificity** - Get exactly the kind of reasoning process you need
        
        2. **Enhance relevance** - Make explanations more tailored to your specific students
        
        3. **Improve quality** - Leverage the strengths of multiple techniques for better results
        
        4. **Create versatile resources** - Generate content that serves multiple educational purposes
        
        As you continue developing your prompting skills, these combinations will become powerful
        tools in your educational toolkit.
        """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * For Activity 1, encourage participants to focus on discipline-specific reasoning processes
    * For Activity 2, suggest that participants think about what's missing in typical AI responses to basic prompts
    * For Activity 3, remind participants to consider their students' specific learning needs and common misconceptions
    * For Activity 4, emphasize that effective prompting often requires combining multiple techniques
    
    **Common Challenges:**
    
    * Some participants may be too vague in requesting "steps" without specifying what kind of thinking they want to see
    * Others may request overly complex reasoning processes that wouldn't be appropriate for their students' level
    * Participants may need help balancing thoroughness with clarity in their step-by-step instructions
    
    **Extension Ideas:**
    
    * Have participants exchange chain-of-thought prompts and evaluate how well they would work for different learning objectives
    * Challenge participants to create a "reasoning process library" for common tasks in their subject area
    * Encourage experimentation with different combinations of techniques for specific educational challenges
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