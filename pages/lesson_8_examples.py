import streamlit as st
import os
import sys
from utils.navigation import scroll_to_top, get_all_pages
from utils.state_management import initialize_session_state, mark_page_completed
from utils.teacher_client import TeacherClient
from components.teacher_notes import render_teacher_notes
from components.bottom_navigator import render_bottom_navigator
from components.breadcrumb_navigator import render_breadcrumb
from components.course_navigation import render_course_navigation
from components.top_navigator import render_top_navigator
from components.first_visit_dialog import show_first_visit_dialog
from components.progress_manager import render_teacher_controls_sidebar

# Initialize the TeacherClient
client = TeacherClient()

# Configure page
st.set_page_config(
    page_title="Lesson 8: Examples",
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
    "title": "Iteration: Examples",
    "lesson": "8",
    "section": "examples",
    "order": 2
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_8_examples"
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
    "lesson_8_examples",
    "examples",
    "Lesson 8: Examples of Iteration",
    """
    **This section provides real-world examples of prompt iteration.**
    
    You'll see:
    - Step-by-step iteration examples in various educational contexts
    - Before-and-after comparisons showing how iteration improves results
    - Different iteration strategies applied to common teaching tasks
    
    These examples will demonstrate how to systematically refine your prompts
    based on evaluation results.
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
    st.markdown("## Iteration Examples")
    
    st.markdown("""
    The following examples demonstrate how to apply iteration techniques to refine prompts in 
    various educational contexts. Each example shows the progression of prompts and results 
    through multiple iterations.
    """)
    
    # Example 1: Iterative Refinement of a Lesson Plan Prompt
    st.markdown("### Example 1: Iterative Refinement of a Science Lesson Plan")
    
    st.markdown("""
    This example demonstrates how to iteratively improve a prompt for creating a science lesson plan.
    
    **Original Prompt:**
    ```
    Create a science lesson about planets.
    ```
    
    **Initial Response:** *(summary)*
    
    A basic overview of the eight planets in our solar system with facts about each planet's 
    size, distance from the sun, and composition. No grade level specified, no clear learning 
    objectives, and no structured activities.
    
    **Evaluation:**
    - Too general - no grade level or standards alignment
    - Lacks specific learning objectives
    - No instructional components (activities, assessments)
    - Content is factually correct but not tailored to any specific age group
    
    **Iteration 1:**
    ```
    Create a 4th-grade science lesson plan about the planets in our solar system. 
    Include learning objectives and a hands-on activity.
    ```
    
    **Response after Iteration 1:** *(summary)*
    
    A lesson plan for 4th-grade with basic learning objectives (identify planets, describe 
    their properties) and a simple solar system model activity. Includes a list of materials 
    needed and basic instructions for the activity.
    
    **Evaluation:**
    - Better grade-level focus, but still not aligned to specific standards
    - Learning objectives present but not clearly measurable
    - Activity included but lacks detailed instructions and assessment
    - No differentiation or extensions
    
    **Iteration 2:**
    ```
    Create a 4th-grade science lesson plan about the planets in our solar system that:
    
    1. Aligns with NGSS standard 4-ESS1-1 (Earth's place in the universe)
    2. Includes 3 specific, measurable learning objectives
    3. Features a 30-minute hands-on solar system modeling activity with detailed instructions
    4. Provides differentiation options for advanced and struggling students
    5. Includes a formative assessment method
    ```
    
    **Response after Iteration 2:** *(summary)*
    
    A comprehensive lesson plan with:
    - Clear alignment to NGSS 4-ESS1-1
    - Three specific learning objectives with measurable outcomes
    - Detailed solar system scale model activity with materials, setup, and facilitation notes
    - Differentiation options (simplified model for struggling students, comparative research for advanced students)
    - Exit ticket assessment with specific questions tied to learning objectives
    
    **Evaluation:**
    - Strong standards alignment
    - Clear, measurable objectives
    - Structured, detailed activity
    - Appropriate differentiation
    - Assessment aligned with objectives
    
    **Key Iteration Strategies Used:**
    1. **Specificity**: Added grade level, standards, time constraints
    2. **Structure**: Used numbered list for clear requirements
    3. **Parameter tuning**: Specified number of objectives and activity length
    4. **Gap filling**: Added differentiation and assessment components
    """)
    
    # Example 2: Iterative Refinement Through Subtractive Approach
    st.markdown("### Example 2: Subtractive Iteration for Assessment Creation")
    
    st.markdown("""
    This example shows how to refine an overly complex prompt by removing and focusing elements.
    
    **Original Prompt:**
    ```
    Create a comprehensive high school assessment for The Great Gatsby, including multiple-choice questions, 
    short answer questions, essay prompts, creative projects, group activities, differentiation options, 
    grading rubrics, and extensions for advanced students. Include questions about symbolism, character 
    development, themes, historical context, literary devices, author's purpose, and modern relevance.
    ```
    
    **Initial Response:**
    
    An extremely long, unfocused assessment with:
    - 20 multiple-choice questions covering too many aspects
    - 10 short answer questions
    - 5 essay prompts
    - 3 creative projects
    - 2 group activities
    - Differentiation options
    - Multiple rubrics
    - Extension activities
    
    **Evaluation:**
    - Overwhelming length (would take students multiple days to complete)
    - Lack of focus makes assessment purpose unclear
    - Too many different types of assessments combined
    - Difficult to implement in a typical class period
    
    **Iteration 1:**
    ```
    Create a focused 40-minute in-class assessment for 11th-grade students on The Great Gatsby. 
    Include only multiple-choice and short answer questions focusing on symbolism and character 
    development. Provide a simple grading key.
    ```
    
    **Response after Iteration 1:**
    
    A more manageable assessment with:
    - 10 multiple-choice questions (5 on symbolism, 5 on character development)
    - 3 short answer questions requiring paragraph responses
    - A straightforward answer key with grading guidelines
    - Estimated completion time: 40 minutes
    
    **Evaluation:**
    - Much more focused and practical for classroom use
    - Still covers multiple skills, making analysis of student understanding difficult
    - Some questions still too general
    
    **Iteration 2:**
    ```
    Create a focused 30-minute formative assessment for 11th-grade students on symbolism in 
    The Great Gatsby. Include 8 multiple-choice questions specifically addressing the symbolism 
    of the green light, the eyes of Dr. T.J. Eckleburg, and the valley of ashes. Add 1 short 
    paragraph question asking students to explain how Fitzgerald uses these symbols to develop 
    the theme of the American Dream.
    ```
    
    **Response after Iteration 2:**
    
    A highly focused assessment with:
    - 8 targeted multiple-choice questions on specific symbols
    - Questions progressing from identification to interpretation of symbols
    - 1 short paragraph question connecting symbols to a central theme
    - Clear answer key with sample response for the paragraph question
    
    **Evaluation:**
    - Excellent focus on a single literary element (symbolism)
    - Appropriate length for a class period with time for discussion
    - Allows for specific analysis of student understanding
    - Builds from basic identification to higher-order thinking
    
    **Key Iteration Strategies Used:**
    1. **Scope reduction**: Narrowed from comprehensive to focused assessment
    2. **Parameter tuning**: Adjusted time limit and question quantity
    3. **Focus refinement**: Narrowed content to specific symbols and theme
    4. **Simplification**: Reduced assessment types and complexity
    """)
    
    # Example 3: Iteration Based on Student Needs
    st.markdown("### Example 3: Iteration Based on Student Needs")
    
    st.markdown("""
    This example demonstrates iterating a prompt to better address the needs of diverse students.
    
    **Original Prompt:**
    ```
    Create a worksheet on solving linear equations for middle school math.
    ```
    
    **Initial Response:** *(summary)*
    
    A basic worksheet with 10 linear equations to solve (e.g., 2x + 5 = 15, -3x = 12).
    No instructions, examples, or scaffolding provided.
    
    **Evaluation:**
    - No clear instructions or examples
    - No scaffolding for struggling students
    - One-size-fits-all approach doesn't address diverse needs
    - Lacks real-world context or application
    
    **Iteration 1:**
    ```
    Create a 7th-grade math worksheet on solving linear equations that includes:
    1. Clear step-by-step instructions
    2. Worked examples
    3. Problems that gradually increase in difficulty
    4. Real-world word problems
    ```
    
    **Response after Iteration 1:** *(summary)*
    
    An improved worksheet with:
    - Step-by-step instructions for solving linear equations
    - 2 worked examples showing the solution process
    - 12 problems arranged from simple to complex
    - 3 word problems involving real-world scenarios
    
    **Evaluation:**
    - Better scaffolding through examples and progression
    - Includes real-world applications
    - Still lacks differentiation for diverse learners
    - No self-check opportunities
    
    **Iteration 2:**
    ```
    Create a differentiated 7th-grade math worksheet on solving linear equations that includes:
    
    1. A "Remember" box with key steps and formulas
    2. Three worked examples showing different equation types
    3. Three difficulty levels of practice problems (Basic, Intermediate, Challenge)
    4. At least 4 real-world application problems related to student interests (sports, gaming, social media)
    5. A self-check section with answers to odd-numbered problems
    6. A reflection question asking students to explain their problem-solving process
    ```
    
    **Response after Iteration 2:** *(summary)*
    
    A comprehensive, differentiated worksheet with:
    - "Remember" box summarizing the steps to solve linear equations
    - Three clearly worked examples (one-step, two-step, and variables on both sides)
    - Three distinct sections:
      * Basic: 6 one-step equations
      * Intermediate: 6 two-step equations
      * Challenge: 4 equations with variables on both sides
    - Real-world problems involving calculation of game scores, social media metrics, sports statistics, and allowance
    - Answer key for odd-numbered problems
    - Reflection prompt: "Explain which type of equation was most challenging for you and why"
    
    **Evaluation:**
    - Excellent scaffolding through examples and tiered difficulty
    - Addresses diverse learning needs
    - Incorporates student interests
    - Supports independent learning through self-check
    - Promotes metacognition through reflection
    
    **Key Iteration Strategies Used:**
    1. **Differentiation enhancement**: Added tiered difficulty levels
    2. **Relevance improvement**: Incorporated student interests
    3. **Metacognitive addition**: Added reflection component
    4. **Self-regulation support**: Added self-check capability
    """)
    
    # Example 4: Iterative Refinement Through Addition and Clarification
    st.markdown("### Example 4: Iteration Through Addition and Clarification")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Original Prompt:**
        ```
        Create discussion questions about climate change.
        ```
        
        **Initial Response:**
        
        1. What is climate change?
        2. What causes climate change?
        3. How does climate change affect our planet?
        4. What can we do to prevent climate change?
        5. Why is climate change important?
        6. What are some effects of climate change?
        7. How does climate change impact wildlife?
        8. What are governments doing about climate change?
        
        **Evaluation:**
        - No grade level or subject focus
        - Questions are basic and recall-oriented
        - Many questions are redundant (3 and 6)
        - Lacks critical thinking or analysis
        - No connection to curriculum standards
        """)
        
    with col2:
        st.markdown("""
        **Iteration 1:**
        ```
        Create high school science discussion questions 
        about climate change that promote critical thinking 
        and analysis of data.
        ```
        
        **Response after Iteration 1:**
        
        1. How do we distinguish between climate change 
           and normal weather variations?
        
        2. What evidence supports the scientific consensus 
           on human-caused climate change?
        
        3. How might climate change affect different 
           geographical regions differently?
        
        4. What are the potential economic impacts of 
           addressing or not addressing climate change?
        
        5. How can we evaluate the effectiveness of 
           different solutions to climate change?
        
        6. How do politics influence climate change policy 
           and public perception?
        
        **Evaluation:**
        - Better critical thinking orientation
        - High school level appropriate
        - Still lacks specific curriculum alignment
        - No structure for facilitating discussion
        - Could use more data analysis focus as mentioned
        """)
        
    with col3:
        st.markdown("""
        **Iteration 2:**
        ```
        Create a structured set of discussion questions for 
        an 11th-grade AP Environmental Science class about 
        climate change that:
        
        1. Aligns with AP ENV standard 9.5 (Global Climate Change)
        2. Includes data analysis questions using graphs/charts
        3. Progresses from fact-based to evaluative questions
        4. Incorporates ethical considerations
        5. Provides teacher facilitation notes
        ```
        
        **Response after Iteration 2:**
        
        **Climate Change Discussion Framework**
        
        *Aligned with AP ENV 9.5: Global Climate Change*
        
        **Fact-Based Questions (10 min)**
        1. Based on the provided CO2 concentration graph, what 
           has been the rate of increase since 1950?
        2. What correlation can you identify between the 
           temperature and CO2 data in the second chart?
        
        **Analysis Questions (15 min)**
        3. How do feedback loops in Earth's systems potentially 
           amplify climate change effects?
        4. Compare the projected impacts of a 1.5°C vs. 3°C 
           temperature increase based on the provided data table.
        
        **Evaluative Questions (15 min)**
        5. Evaluate the effectiveness of carbon pricing versus 
           regulatory approaches in reducing emissions.
        6. How might different societal values influence climate 
           policy decisions?
        
        **Ethical Consideration (10 min)**
        7. Discuss the concept of climate justice: who bears the 
           greatest responsibility for addressing climate change, 
           and why?
        
        **Teacher Facilitation Notes:**
        - Begin by displaying the CO2 concentration graph and 
          temperature data chart
        - Consider using think-pair-share for questions 1-2
        - For questions 3-4, divide into small analysis groups
        - Questions 5-7 work best as full class discussion
        - Ensure balanced participation using equity sticks
        
        **Evaluation:**
        - Excellent curriculum alignment
        - Structured progression of thinking
        - Incorporates data analysis
        - Includes facilitation guidance
        - Appropriate timing considerations
        - Balances science with ethical dimensions
        """)
    
    # Example 5: Iterative Improvement Through Error Correction
    st.markdown("### Example 5: Iteration to Address Errors and Misconceptions")
    
    st.markdown("""
    This example shows how to iterate a prompt to correct errors and misconceptions in the AI's response.
    
    **Original Prompt:**
    ```
    Create a one-page handout on common grammar mistakes for 9th grade English.
    ```
    
    **Initial Response:** *(summary)*
    
    A handout covering run-on sentences, sentence fragments, subject-verb agreement, apostrophe use, 
    and who/whom usage. Each section includes explanations and examples.
    
    **Evaluation:**
    - Contains several errors (e.g., incorrect example of subject-verb agreement)
    - Some explanations are confusing or overly complex for 9th graders
    - Examples are not relevant to teen interests or experiences
    - No practice exercises
    - The who/whom explanation uses grammatical terminology students might not know
    
    **Iteration 1:**
    ```
    Create a one-page handout on common grammar mistakes for 9th grade English that:
    
    1. Focuses on ONLY these four areas: run-on sentences, sentence fragments, subject-verb agreement, and apostrophe use
    2. Provides clear, simple explanations with accurate examples
    3. Includes 1-2 practice exercises for each grammar rule
    ```
    
    **Response after Iteration 1:** *(summary)*
    
    A more focused handout with the four requested grammar areas, simpler explanations, 
    and practice exercises. However, some examples still feel disconnected from student experiences.
    
    **Evaluation:**
    - Accurate explanations and examples
    - Better focus on fewer topics
    - Practice exercises included
    - Examples still not engaging for teens
    - No error correction guide for students
    
    **Iteration 2:**
    ```
    Create a one-page handout on common grammar mistakes for 9th grade English that:
    
    1. Covers ONLY these four areas: run-on sentences, sentence fragments, subject-verb agreement, and apostrophe use
    2. Uses examples relevant to teen life (social media, sports, high school, entertainment)
    3. Includes exactly 2 practice sentences for each grammar rule
    4. Adds a simple self-check guide showing how to identify and fix each mistake
    5. Uses 9th-grade accessible language (avoid terms like "subordinate clause" or "predicate")
    ```
    
    **Response after Iteration 2:** *(summary)*
    
    A highly effective handout with:
    - Teen-relevant examples ("When Taylor Swift released her new album, millions of fans streamed it immediately")
    - Simplified explanations avoiding complex grammatical terminology
    - Consistent structure with 2 practice items per section
    - A "How to Fix It" box for each grammar mistake
    - Appropriate 9th-grade language throughout
    
    **Key Iteration Strategies Used:**
    1. **Error correction**: Specified need for accurate examples
    2. **Scope limitation**: Reduced to four specific grammar topics
    3. **Audience alignment**: Required teen-relevant examples
    4. **Structural enhancement**: Added self-check component
    5. **Accessibility improvement**: Specified appropriate language level
    """)
    
    # Example 6: PCTFREI Framework in Action
    st.markdown("### Example 6: Complete PCTFREI Framework in Action")
    
    st.markdown("""
    This example demonstrates the entire PCTFREI framework applied to an iterative prompt engineering process.
    
    **Original Prompt:**
    ```
    Create a project about ecosystems.
    ```
    
    **Initial Response:** *(brief summary)*
    
    A general ecosystem project where students research a biome, create a poster, and present to the class.
    
    **Evaluation:**
    - Too general and unstructured
    - No specific learning objectives or standards
    - Not targeted to a specific grade level
    - Lacks assessment criteria
    - Traditional "poster project" lacks innovation
    
    **Iteration Process Using PCTFREI Framework:**
    
    **Iteration 1: Adding Persona, Task & Context**
    ```
    As a middle school science teacher (P) designing a two-week ecology unit (C),
    create a project-based learning activity about ecosystems (T) for 7th-grade students
    who have already learned basic ecosystem concepts.
    ```
    
    **Iteration 2: Adding Format**
    ```
    As a middle school science teacher (P) designing a two-week ecology unit (C),
    create a project-based learning activity about ecosystems (T) for 7th-grade students
    who have already learned basic ecosystem concepts.
    
    Format the response with (F):
    - Learning objectives
    - Materials needed
    - Step-by-step procedure
    - Assessment criteria
    - Estimated timeline
    ```
    
    **Iteration 3: Adding Reference Materials**
    ```
    As a middle school science teacher (P) designing a two-week ecology unit (C),
    create a project-based learning activity about ecosystems (T) for 7th-grade students
    who have already learned basic ecosystem concepts.
    
    Format the response with (F):
    - Learning objectives
    - Materials needed
    - Step-by-step procedure
    - Assessment criteria
    - Estimated timeline
    
    Align the project with NGSS standard MS-LS2: Ecosystems: Interactions, Energy, and Dynamics,
    specifically MS-LS2-5: Evaluate competing design solutions for maintaining biodiversity (R).
    ```
    
    **Iteration 4: After Evaluation (E)**
    ```
    As a middle school science teacher (P) designing a two-week ecology unit (C),
    create a project-based learning activity about ecosystems (T) for 7th-grade students
    who have already learned basic ecosystem concepts.
    
    Format the response with (F):
    - Learning objectives
    - Materials needed
    - Step-by-step procedure
    - Assessment criteria
    - Estimated timeline
    
    Align the project with NGSS standard MS-LS2: Ecosystems: Interactions, Energy, and Dynamics,
    specifically MS-LS2-5: Evaluate competing design solutions for maintaining biodiversity (R).
    
    Based on previous evaluation (E), please ensure:
    1. The project involves students designing solutions to a local ecosystem problem
    2. Digital tools are incorporated (not just a physical poster)
    3. Collaborative group work is structured with clear role assignments
    4. Assessment includes both peer and teacher evaluation components
    5. Differentiation options are provided for various learning needs
    ```
    
    **Final Response:** *(summary)*
    
    A comprehensive "Ecosystem Guardians" project where student teams:
    - Investigate a local ecosystem threat
    - Research and evaluate competing solutions using digital tools
    - Design and model their proposed solution
    - Create a digital presentation with specified components
    - Participate in a solutions showcase with structured peer feedback
    
    The response includes clear learning objectives aligned with NGSS MS-LS2-5, detailed materials list, 
    day-by-day procedure over two weeks, differentiation options, and multi-faceted assessment criteria 
    including rubrics for both teacher and peer evaluation.
    
    **Key Iteration Takeaways:**
    
    1. Each component of PCTFREI adds crucial specificity:
       - Persona established the teacher perspective
       - Context set the curricular situation
       - Task defined the core activity
       - Format structured the response
       - References aligned with standards
       - Evaluation identified gaps
       - Iteration addressed those gaps
    
    2. The final prompt is significantly longer than the original but produces a much more usable,
       comprehensive, and educationally sound project plan.
    
    3. Iteration based on evaluation ensured the final output addressed specific pedagogical needs
       (local relevance, digital tools, collaboration, diverse assessment, differentiation).
    """)
    
    # Takeaways from Examples
    st.markdown("## Key Lessons from Iteration Examples")
    
    st.markdown("""
    1. **Start simple, then add complexity** - Begin with a basic prompt and refine through iteration
    
    2. **Be specific about what you want** - Clearly specify requirements, formats, and parameters
    
    3. **Evaluate systematically** - Identify specific areas for improvement in each response
    
    4. **Targeted refinements work best** - Focus on addressing one or two issues at a time
    
    5. **Both addition and subtraction are valuable** - Sometimes removing elements is as important as adding them
    
    6. **Document your progress** - Track changes across iterations to identify what works
    
    7. **The complete PCTFREI framework produces the best results** - While simple prompts can work, 
       incorporating all framework elements leads to optimal outcomes
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific guidance
    render_teacher_notes("""
    **Key Points to Emphasize:**
    
    * Iteration is a normal part of the prompt engineering process, not a sign of failure
    * The examples demonstrate how each iteration builds on evaluation of the previous response
    * Different types of content (lesson plans, assessments, worksheets) may require different iteration approaches
    * The complete PCTFREI framework provides a systematic approach to comprehensive iteration
    
    **Discussion Questions:**
    
    * Which example most closely relates to content you create in your teaching practice?
    * What patterns do you notice across the various iteration examples?
    * How might you apply these iteration techniques to improve your own prompts?
    * What specific areas of your prompt writing could benefit most from systematic iteration?
    
    **Extension Activity:**
    
    Have participants select one of their existing prompts and apply two iterations to it based on 
    the examples shown. Then have them compare the results of the original prompt with the final iteration.
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