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
    page_title="Lesson 7: Examples",
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
    "title": "Evaluation: Examples",
    "lesson": "7",
    "section": "examples",
    "order": 2
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_7_examples"
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
    "lesson_7_examples",
    "examples",
    "Lesson 7: Examples of Evaluation",
    """
    **This section provides practical examples of evaluation techniques for AI responses.**
    
    You'll see:
    - Sample evaluation rubrics for different educational contexts
    - Before-and-after examples showing how evaluation improves AI outputs
    - Practical techniques for assessing different aspects of AI-generated content
    
    These examples will help you develop your own evaluation strategies 
    for assessing AI outputs in your teaching practice.
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
    st.markdown("## Evaluation Examples")
    
    st.markdown("""
    The following examples demonstrate how to evaluate AI-generated content for educational use.
    Each example showcases different evaluation techniques and how they can be applied in various
    educational contexts.
    """)
    
    # Example 1: ACRE Framework in Action
    st.markdown("### Example 1: ACRE Framework in Action")
    
    st.markdown("""
    This example demonstrates the ACRE framework (Accuracy, Curriculum Alignment, Readability, Engagement)
    applied to an elementary science lesson.
    
    **Original Prompt:**
    ```
    Create a 4th-grade science lesson about the water cycle.
    ```
    
    **AI Response (Excerpt):**
    
    # The Water Cycle
    
    The water cycle is the way water moves around our planet. It includes several important stages:
    
    1. Evaporation: The sun heats up water on Earth's surface, turning it into water vapor.
    
    2. Condensation: As water vapor rises, it cools and forms clouds.
    
    3. Precipitation: Water falls back to Earth as rain, snow, sleet, or hail.
    
    4. Collection: Water collects in oceans, lakes, rivers, or soaks into the ground.
    
    This cycle repeats continuously, recycling Earth's water supply.
    
    **ACRE Evaluation:**
    
    | Criterion | Rating | Notes |
    |---|---|---|
    | **Accuracy** | 4/5 | Content is factually correct, but lacks mention of transpiration |
    | **Curriculum Alignment** | 2/5 | Missing NGSS standard 4-ESS2-1 connections; no mention of the role of energy |
    | **Readability** | 5/5 | Vocabulary and sentence structure appropriate for 4th grade |
    | **Engagement** | 2/5 | No hands-on activities, visuals, or inquiry-based learning components |
    
    **Evaluation Summary:**
    
    The response provides basic accurate information but needs improvement in curriculum alignment
    and student engagement. It lacks specific connections to grade-level standards and doesn't include
    interactive learning elements that would make the content engaging for 4th-grade students.
    """)
    
    # Example 2: Dimensional Evaluation
    st.markdown("### Example 2: Dimensional Evaluation of a Math Worksheet")
    
    st.markdown("""
    This example uses a dimensional approach to evaluate a math worksheet, examining both
    content and pedagogical dimensions.
    
    **Original Prompt:**
    ```
    Create a 7th-grade math worksheet on solving one-step equations.
    ```
    
    **AI Response Excerpts:**
    
    # One-Step Equations Worksheet
    
    ## Instructions
    Solve each equation for the variable. Show your work.
    
    1. x + 5 = 12
    2. y - 3 = 9
    3. 7z = 28
    4. m/4 = 6
    5. 3 + p = -2
    6. q - 8 = -3
    7. 5r = -20
    8. h/2 = -4
    ...
    
    **Dimensional Evaluation:**
    
    **Content Dimension:**
    
    | Criterion | Rating | Notes |
    |---|---|---|
    | Mathematical Accuracy | 5/5 | All equations and expected solutions are mathematically correct |
    | Appropriate Difficulty | 3/5 | Problems are appropriate but lack progression from simple to complex |
    | Comprehensiveness | 2/5 | Only covers basic one-step equations; missing word problems and context |
    | Standards Alignment | 3/5 | Aligns with standard 7.EE.B.4a but doesn't address real-world problems |
    
    **Pedagogical Dimension:**
    
    | Criterion | Rating | Notes |
    |---|---|---|
    | Clarity of Instructions | 4/5 | Instructions are clear, but lack examples or guidance |
    | Scaffolding | 1/5 | No scaffolding; jumps directly to problems |
    | Student Engagement | 1/5 | Purely procedural; no context or real-world connections |
    | Assessment Value | 3/5 | Works for basic skill practice, but not for deeper understanding |
    
    **Evaluation Summary:**
    
    The worksheet is mathematically accurate but lacks pedagogical strength. It needs better 
    scaffolding, real-world contexts, and a thoughtful progression of problem difficulty to be
    an effective learning tool. The worksheet functions as a basic practice tool but doesn't
    support deeper conceptual understanding or engagement.
    """)
    
    # Example 3: Before and After Evaluation
    st.markdown("### Example 3: Before and After Evaluation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Original Prompt:**
        ```
        Create a high school history discussion on the
        Civil Rights Movement.
        ```
        
        **Initial AI Response:**
        
        # Civil Rights Movement Discussion
        
        The Civil Rights Movement was a struggle for 
        social justice that took place mainly during 
        the 1950s and 1960s for Black Americans to 
        gain equal rights under the law in the United 
        States.
        
        **Discussion Questions:**
        
        1. What were the major events of the Civil 
        Rights Movement?
        
        2. Who were the key leaders in the movement?
        
        3. How did the Civil Rights Movement change 
        America?
        
        4. Why was this movement important?
        
        5. What challenges did activists face?
        
        **Evaluation:**
        - Generic content lacking depth
        - No specific historical contexts or documents
        - Surface-level questions without critical thinking
        - Missing connections to present-day relevance
        - No guidance for facilitating discussion
        """)
        
    with col2:
        st.markdown("""
        **Revised Prompt Based on Evaluation:**
        ```
        Create a 11th-grade history discussion guide on the 
        Civil Rights Movement that:
        1. Focuses on primary source analysis
        2. Includes 3-4 higher-order thinking questions
        3. Makes connections to contemporary civil rights issues
        4. Provides teacher facilitation notes
        5. Aligns with AP US History standards on social movements
        ```
        
        **Improved AI Response (Excerpt):**
        
        # Civil Rights Movement Primary Source Analysis
        
        ## Historical Context (1954-1968)
        
        This discussion examines the strategies, philosophies, 
        and impacts of the Civil Rights Movement through primary 
        source analysis, connecting historical activism to 
        contemporary civil rights issues.
        
        ## Primary Sources for Analysis
        
        1. **Letter from Birmingham Jail** (1963) - Martin Luther King Jr.
        2. **Speech at the March on Washington** (1963) - John Lewis
        3. **Executive Order 10730** (1957) - President Eisenhower
        
        ## Higher-Order Discussion Questions
        
        1. **Comparative Analysis**: How did King's philosophy of 
        nonviolent resistance compare with more confrontational 
        approaches advocated by Malcolm X and later the Black 
        Panthers? What evidence supports the effectiveness of each?
        
        2. **Document-Based Question**: Using the primary sources 
        provided, evaluate how different branches of government 
        responded to civil rights activism. What constitutional 
        principles were at stake?
        
        3. **Contemporary Connection**: Identify a current civil 
        rights movement and analyze how it employs strategies 
        either similar to or different from the 1960s movement. 
        What factors influence these strategic choices?
        
        ## Teacher Facilitation Notes
        
        * Begin by having students read excerpts independently 
        with annotation guides
        * Consider a "silent discussion" protocol where students 
        respond in writing before verbal discussion
        * Be prepared to address regional differences in how 
        this history is taught and received
        * AP Connection: This discussion supports Key Concept 8.2
        
        **Evaluation of Revised Response:**
        - Historically specific and accurate
        - Incorporates primary sources
        - Features complex, analytical questions
        - Includes contemporary connections
        - Provides practical teaching guidance
        - Aligns with AP curriculum standards
        """)
    
    # Example 4: Specialized Rubric for Language Arts
    st.markdown("### Example 4: Specialized Rubric for Language Arts")
    
    st.markdown("""
    This example demonstrates a specialized rubric for evaluating a literature response prompt.
    
    **Original Prompt:**
    ```
    Create discussion questions about Shakespeare's "Romeo and Juliet" for 9th grade English.
    ```
    
    **AI Response:**
    
    # Romeo and Juliet Discussion Questions
    
    1. What are the main themes of Romeo and Juliet?
    
    2. How do Romeo and Juliet's characters develop throughout the play?
    
    3. What role does fate play in the tragedy?
    
    4. How does Shakespeare use language to create emotion?
    
    5. Why do you think this play has remained popular for centuries?
    
    6. How would the story be different if set in modern times?
    
    7. What messages about love does Shakespeare convey?
    
    8. What impact do the families' feud have on the other characters?
    
    **Specialized Literature Response Evaluation Rubric:**
    
    | Dimension | Criteria | Score (1-5) | Notes |
    |---|---|---|---|
    | **Textual Analysis** | Questions direct students to analyze specific text passages and literary elements | 2 | Questions are too general; don't reference specific scenes or passages |
    | **Critical Thinking** | Questions promote interpretation, evaluation, and synthesis beyond recall | 3 | Some higher-order questions (fate, modernization) but many are basic recall |
    | **Developmental Appropriateness** | Content aligns with 9th-grade reading standards and cognitive development | 4 | Topics are appropriate but lack scaffolding for different ability levels |
    | **Literary Context** | Questions connect to literary periods, author's intent, and historical context | 1 | No questions about Elizabethan context, Shakespeare's craft, or dramatic conventions |
    | **Diverse Perspectives** | Questions encourage multiple interpretations and cultural viewpoints | 2 | Limited opportunity to explore diverse perspectives on the text |
    
    **Overall Evaluation Score: 12/25**
    
    **Recommendations for Improvement:**
    1. Include questions that reference specific scenes, lines, or soliloquies
    2. Add questions that connect to Elizabethan theatrical conventions and historical context
    3. Incorporate questions that invite diverse cultural interpretations of the themes
    4. Include questions that scaffold analysis for different reading abilities
    5. Add questions that compare Shakespeare's treatment of themes with other texts students may have read
    """)
    
    # Example 5: Template for Educational Game Evaluation
    st.markdown("### Example 5: Evaluating an Educational Game Activity")
    
    st.markdown("""
    This template demonstrates how to evaluate AI-generated educational games or activities.
    
    **Original Prompt:**
    ```
    Create a vocabulary game for 5th-grade science students learning about ecosystems.
    ```
    
    **AI Response (Excerpt):**
    
    # Ecosystem Vocabulary Challenge
    
    ## Game Overview
    "Ecosystem Explorers" is a team-based vocabulary game where students match ecological terms with definitions, examples, and visual representations.
    
    ## Materials Needed
    - Vocabulary cards with terms
    - Definition cards
    - Example cards
    - Pictures representing each term
    - Timer
    - Score sheet
    
    ## Vocabulary Included
    Ecosystem, habitat, population, community, producer, consumer, decomposer, food chain, food web, photosynthesis, predator, prey, adaptation, biodiversity, niche
    
    ## Game Rules
    1. Divide students into teams of 3-4
    2. Distribute cards face down in separate piles
    3. Teams take turns selecting one card from each category
    4. Teams earn points by correctly matching terms with definitions, examples, and images
    5. Bonus points for creating a correct sentence using the term
    
    ## Extensions
    - Create a physical food web using string to connect vocabulary terms
    - Challenge round where students add new examples not included in the cards
    - "Ecosystem builder" where teams design an ecosystem using the vocabulary
    
    **Educational Game Evaluation Rubric:**
    
    | Criterion | Rating (1-5) | Notes |
    |---|---|---|
    | **Learning Alignment** | 5 | Directly supports vocabulary acquisition for grade-level science standards |
    | **Engagement** | 4 | Multiple game mechanics; could benefit from more movement-based elements |
    | **Inclusivity** | 3 | Works for most learning styles but may challenge students with reading difficulties |
    | **Practicality** | 4 | Reasonable prep time; reusable materials |
    | **Differentiation** | 3 | Extensions provide some differentiation but lacks built-in tiered options |
    | **Assessment Value** | 4 | Provides opportunities to observe student understanding; formative assessment potential |
    | **Time Efficiency** | 4 | Appropriate use of class time for the learning value |
    
    **Overall Score: 27/35**
    
    **Strengths:**
    - Strong alignment with curriculum vocabulary needs
    - Multiple learning modalities (visual, verbal, written)
    - Social learning component through team structure
    - Extensions allow for deeper application
    
    **Areas for Improvement:**
    - Add tiered vocabulary cards for differentiation (basic, intermediate, advanced)
    - Include modifications for students with reading difficulties
    - Add a movement-based component to engage kinesthetic learners
    """)
    
    # Example 6: Holistic Evaluation with Concrete Improvements
    st.markdown("### Example 6: Holistic Evaluation with Concrete Improvements")
    
    st.markdown("""
    This example demonstrates a holistic evaluation approach with specific recommendations for improvement.
    
    **Original Prompt:**
    ```
    Create a formative assessment on Newton's Laws of Motion for high school physics.
    ```
    
    **AI Response (Summarized):**
    A 10-question quiz with multiple-choice and short-answer questions testing recall and basic application of Newton's three laws of motion.
    
    **Holistic Evaluation:**
    
    ```
    STRENGTHS:
    ✓ Covers all three Newton's Laws
    ✓ Includes both recall and application questions
    ✓ Content is factually accurate
    ✓ Questions are clearly worded
    
    WEAKNESSES:
    ✗ Lacks real-world scenario applications
    ✗ No visual components or data interpretation
    ✗ Doesn't assess deeper conceptual understanding
    ✗ Missing opportunities for students to explain reasoning
    ✗ No tiered questions to assess different levels of understanding
    ✗ Doesn't include any phenomenon-based questions
    
    OVERALL ASSESSMENT:
    This formative assessment functions as a basic check for factual recall and simple 
    application but doesn't adequately assess conceptual understanding or scientific 
    reasoning. It needs substantial enhancement to function as an effective formative 
    assessment for high school physics.
    ```
    
    **Specific Recommendations for Improvement:**
    
    1. **Add Visual Analysis**: Include a question with a force diagram for students to analyze
       ```
       Looking at the force diagram below, explain which forces must be larger than others 
       for the object to accelerate in the direction shown. Apply Newton's laws in your explanation.
       ```
    
    2. **Include Real-World Scenario**:
       ```
       A 1500 kg car accelerates from 0 to 25 m/s in 10 seconds. 
       a) Calculate the net force acting on the car. 
       b) If the engine applies 5000 N of force, calculate the total resistance force.
       c) Explain how this scenario demonstrates Newton's Second Law.
       ```
    
    3. **Add Conceptual Reasoning**:
       ```
       Two students are discussing Newton's Third Law. Student A says, "If action equals reaction, 
       then when I push on a wall, the wall pushes back equally, so I should never be able to move 
       anything." Student B disagrees. Who is correct and why? Use Newton's Laws in your explanation.
       ```
    
    4. **Incorporate Phenomenon Observation**:
       ```
       When a tablecloth is quickly pulled from under dishes on a table, the dishes barely move. 
       Explain this phenomenon using Newton's Laws and the concept of inertia. Include a discussion 
       of what variables would affect the success of this demonstration.
       ```
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific guidance
    render_teacher_notes("""
    **Key Points to Emphasize:**
    
    * The evaluation examples demonstrate different approaches suitable for various content types
    * Evaluation should be constructive and specific, leading to actionable improvements
    * Effective evaluation rubrics reflect both content quality and pedagogical effectiveness
    * Evaluation doesn't need to be complex - even simple frameworks like ACRE provide structure
    
    **Discussion Questions:**
    
    * Which evaluation approach seems most relevant to your teaching context?
    * How might you adapt the rubrics shown to better match your subject area or grade level?
    * What criteria are most important when evaluating AI content for your specific educational needs?
    * How could you involve students in evaluating AI-generated content as a critical thinking exercise?
    
    **Extension Activity:**
    
    Have participants select one of the evaluation rubrics and customize it for a specific 
    content type they frequently create, adding or modifying criteria to make it more relevant
    to their needs.
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