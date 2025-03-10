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
    page_title="Lesson 9: Examples",
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
    "title": "Zero-Shot Prompting: Examples",
    "lesson": "9",
    "section": "examples",
    "order": 2
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_9_examples"
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
    "lesson_9_examples",
    "examples",
    "Lesson 9: Examples of Zero-Shot Prompting",
    """
    **This section provides practical examples of zero-shot prompting in education.**
    
    You'll see:
    - Real-world examples of effective zero-shot prompts
    - Comparisons between basic and well-crafted zero-shot prompts
    - Different educational scenarios where zero-shot is particularly useful
    
    These examples will help you understand how to craft zero-shot prompts
    for your specific teaching needs.
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
    st.markdown("## Zero-Shot Prompting Examples")
    
    st.markdown("""
    The following examples demonstrate effective zero-shot prompting in various educational contexts. 
    Each example shows how to craft prompts that leverage the LLM's existing knowledge without providing 
    specific examples.
    """)
    
    # Example 1: Basic vs. Effective Zero-Shot Comparison
    st.markdown("### Example 1: Basic vs. Effective Zero-Shot Prompts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Basic Zero-Shot Prompt:**
        ```
        Write a lesson plan on photosynthesis.
        ```
        
        **Response:** *(Summary)*
        
        A generic lesson plan on photosynthesis with basic information about 
        the process, some discussion questions, and a simple activity. No specific 
        grade level, standards alignment, or detailed teaching strategies.
        
        **Issues:**
        - No specified grade level
        - Lacks clear objectives
        - Missing standards alignment
        - No specific timeframe
        - Generic activities
        - Limited assessment methods
        """)
        
    with col2:
        st.markdown("""
        **Effective Zero-Shot Prompt:**
        ```
        Create a 5th-grade science lesson plan on photosynthesis that:
        
        1. Aligns with NGSS standard 5-LS1-1 (Support plants get materials for growth from air and water)
        2. Can be completed in a 50-minute class period
        3. Includes a hands-on demonstration using elodea plants
        4. Features 3 clear learning objectives
        5. Incorporates formative assessment checks
        6. Provides differentiation strategies
        ```
        
        **Response:** *(Summary)*
        
        A detailed, grade-appropriate lesson plan with specific objectives tied to 
        NGSS standards, a structured timeline, detailed procedures for the elodea 
        demonstration, embedded formative assessments, and clear differentiation 
        strategies for different learning needs.
        
        **Improvements:**
        - Specific grade level
        - Clear standards alignment
        - Defined time constraints
        - Specific activity details
        - Required assessment components
        - Explicit request for differentiation
        """)
    
    st.markdown("""
    **Key Takeaway:** While both are zero-shot prompts (no examples provided), the effective version 
    sets clear parameters that help the LLM draw on its knowledge of educational best practices for 
    that specific context. The specificity guides the AI without requiring you to provide examples 
    of what a good lesson plan looks like.
    """)
    
    # Example 2: Subject Area Applications
    st.markdown("### Example 2: Zero-Shot Prompting Across Subject Areas")
    
    st.markdown("""
    These examples demonstrate how zero-shot prompting can be applied effectively across different subject areas.
    """)
    
    # Language Arts example
    st.markdown("#### Language Arts Example")
    
    st.markdown("""
    **Zero-Shot Prompt:**
    ```
    Create 10 open-ended discussion questions for a 9th-grade English class studying "To Kill a Mockingbird" that:
    
    1. Progress from basic comprehension to complex analysis
    2. Address themes of justice, prejudice, and moral growth
    3. Require students to cite specific textual evidence
    4. Connect the novel's themes to contemporary issues
    5. Include at least 2 questions about literary devices used in the novel
    ```
    
    **Response Excerpts:**
    
    **Comprehension Level:**
    1. How does Scout's perspective as the narrator shape our understanding of the events in Maycomb? Cite specific passages that reveal her biases or growth in understanding.
    
    **Analysis Level:**
    5. Analyze how Atticus Finch's approach to the trial conflicts with the prevailing attitudes in Maycomb. What does this reveal about the complexity of addressing systemic prejudice?
    
    **Thematic Connections:**
    7. How does Lee use the mockingbird as a symbol throughout the novel? Identify at least two characters who could be considered "mockingbirds" and explain why, using textual evidence.
    
    **Contemporary Relevance:**
    9. In what ways do the issues of racial inequality presented in the novel continue to resonate in our society today? Draw specific parallels between events in the book and contemporary situations.
    """)
    
    # Mathematics example
    st.markdown("#### Mathematics Example")
    
    st.markdown("""
    **Zero-Shot Prompt:**
    ```
    Create a real-world problem-solving activity for 8th-grade math students learning about linear equations that:
    
    1. Uses a scenario about planning a school fundraiser
    2. Requires students to write and solve a linear equation
    3. Incorporates multiple variables (cost, revenue, profit)
    4. Includes a graphing component
    5. Provides extension questions for advanced students
    ```
    
    **Response Excerpt:**
    
    **School Fundraiser Math Challenge**
    
    Your class is planning a school fundraiser selling custom water bottles. You need to determine how to price the bottles and how many you need to sell to reach your fundraising goal.
    
    **Scenario Information:**
    - Each water bottle costs $3.50 to produce
    - There is a one-time setup fee of $150 for the custom design
    - Your class needs to raise at least $500 for the field trip
    
    **Tasks:**
    1. Write a linear equation that represents the total cost (C) of producing x water bottles.
    2. Write a linear equation that represents the revenue (R) if you sell the water bottles for $p each.
    3. Write a linear equation that represents the profit (P).
    4. If you price the water bottles at $8 each, how many would you need to sell to reach your fundraising goal?
    5. Graph the cost and revenue equations on the same coordinate plane. Identify and interpret the break-even point.
    
    **Extension Questions:**
    1. How would changing the price affect the number of bottles you need to sell?
    2. Research shows that for each $1 increase in price, you would sell 20 fewer bottles. What price would maximize your profit?
    """)
    
    # Science example
    st.markdown("#### Science Example")
    
    st.markdown("""
    **Zero-Shot Prompt:**
    ```
    Design a lab activity for high school biology students investigating enzymes that:
    
    1. Can be completed in a single 90-minute class period
    2. Uses common materials (hydrogen peroxide, liver, potato, different pH solutions)
    3. Incorporates the scientific method with a clear hypothesis
    4. Includes data collection procedures and a provided data table template
    5. Features analysis questions that connect to cellular respiration concepts
    ```
    
    **Response Excerpt:**
    
    **Enzyme Action Lab: Investigating Catalase Activity**
    
    In this lab, you will investigate how enzymes work by observing the action of catalase, an enzyme found in many living tissues that breaks down hydrogen peroxide (H₂O₂) into water and oxygen gas.
    
    **Materials (per group):**
    - Fresh liver sample (2 cm cube)
    - Fresh potato (2 cm cube)
    - 3% hydrogen peroxide solution (50 mL)
    - Various pH solutions (vinegar, water, baking soda solution)
    - 3 test tubes and rack
    - Ruler
    - Stopwatch
    - Safety goggles and gloves
    
    **Procedure:**
    [Detailed step-by-step procedure provided]
    
    **Data Collection:**
    [Well-structured data table with columns for tissue type, pH condition, reaction time, and bubble height]
    
    **Analysis Questions:**
    1. Compare the catalase activity in liver versus potato. What does this suggest about the concentration of this enzyme in different tissues?
    2. How did pH affect enzyme function? Explain in terms of protein structure and function.
    3. How does the catalase reaction relate to cellular respiration processes in cells?
    4. What role do enzymes like catalase play in protecting cells from oxidative damage?
    """)
    
    # Example 3: Different Content Types
    st.markdown("### Example 3: Zero-Shot Prompting for Different Content Types")
    
    st.markdown("""
    This example shows how zero-shot prompting can be used to generate different types of educational content.
    """)
    
    tabs = st.tabs(["Assessment", "Rubric", "Lesson Materials", "Parent Communication"])
    
    with tabs[0]:
        st.markdown("""
        **Zero-Shot Assessment Prompt:**
        ```
        Create a formative assessment for 6th-grade geography students on the topic of climate zones that:
        
        1. Includes 8 multiple-choice questions and 2 short-answer questions
        2. Covers the characteristics of major climate zones (tropical, temperate, polar)
        3. Includes at least one map interpretation question
        4. Features questions at different levels of Bloom's taxonomy
        5. Provides an answer key with brief explanations for each answer
        ```
        
        **Response Excerpt:**
        
        **Climate Zones Formative Assessment**
        
        **Multiple Choice Questions:**
        
        1. Which climate zone is characterized by year-round high temperatures and high amounts of rainfall?
           a) Temperate
           b) Tropical
           c) Polar
           d) Desert
        
        4. [MAP QUESTION] Based on the world climate zone map, which letter (A, B, C, or D) indicates the location of a Mediterranean climate?
           a) A
           b) B
           c) C
           d) D
        
        7. Which of the following best explains why coastal areas often have milder temperatures than inland areas at the same latitude?
           a) Coastal areas have more vegetation
           b) Water heats and cools more slowly than land
           c) Ocean currents always bring warm water
           d) Coastal areas have lower elevation
        
        **Short Answer Questions:**
        
        9. Compare and contrast the temperate and tropical climate zones. Include at least three differences in your answer and explain how these differences affect plant life.
        
        10. Imagine you are moving from a polar climate to a tropical climate. Describe three specific ways your daily life would need to change and explain why these changes would be necessary.
        
        **Answer Key:**
        [Detailed answer key with explanations provided]
        """)
        
    with tabs[1]:
        st.markdown("""
        **Zero-Shot Rubric Prompt:**
        ```
        Create an assessment rubric for a 10th-grade history research project on a significant 20th century event that:
        
        1. Uses a 4-point scale (Beginning, Developing, Proficient, Exemplary)
        2. Evaluates 5 dimensions (research quality, historical accuracy, analysis, organization, presentation)
        3. Includes clear performance descriptors for each level and dimension
        4. Aligns with Common Core writing standards for history/social studies
        5. Provides specific examples of what constitutes evidence at each performance level
        ```
        
        **Response Excerpt:**
        
        **20th Century Historical Event Research Project Rubric**
        
        **Research Quality**
        
        *Beginning (1):* Uses very few sources (fewer than 3); sources lack variety and credibility; minimal primary sources; heavy reliance on general websites
        
        *Developing (2):* Uses adequate sources (at least 3); some variety in sources but may overrely on one type; includes at least 1 primary source; some academic sources
        
        *Proficient (3):* Uses diverse sources (4-5); good balance of primary and secondary sources; mostly credible academic sources; appropriate citation format with minor errors
        
        *Exemplary (4):* Uses comprehensive source collection (6+); excellent balance of primary and secondary sources; high-quality academic sources; perfect citation format
        
        **Historical Accuracy**
        
        [Detailed descriptors for each level provided]
        
        **Analysis**
        
        [Detailed descriptors for each level provided]
        
        **Organization**
        
        [Detailed descriptors for each level provided]
        
        **Presentation**
        
        [Detailed descriptors for each level provided]
        
        **Common Core Alignment:**
        This rubric aligns with CCSS.ELA-LITERACY.WHST.9-10.1 through WHST.9-10.9, with particular emphasis on:
        - WHST.9-10.1: Write arguments focused on discipline-specific content
        - WHST.9-10.2: Write informative/explanatory texts
        - WHST.9-10.7: Conduct short as well as more sustained research projects
        - WHST.9-10.8: Gather relevant information from multiple authoritative sources
        """)
        
    with tabs[2]:
        st.markdown("""
        **Zero-Shot Lesson Materials Prompt:**
        ```
        Create a set of differentiated vocabulary materials for 3rd-grade students learning about simple machines that:
        
        1. Covers 8 key terms (lever, pulley, inclined plane, wedge, screw, wheel and axle, force, work)
        2. Includes three difficulty levels (basic, intermediate, advanced)
        3. Provides simple definitions with visual cues for each term
        4. Includes examples of each simple machine from everyday life
        5. Features age-appropriate practice activities for each level
        ```
        
        **Response Excerpt:**
        
        **Simple Machines Vocabulary Materials**
        
        **Level 1: Basic**
        
        **Lever**
        *Definition:* A lever is a stiff bar that moves on a fixed point to lift objects.
        *Visual Cue:* Think of a seesaw that goes up and down.
        *Everyday Example:* A seesaw at the playground, scissors, or a bottle opener
        *Practice Activity:* Draw a line matching the simple machine picture to its name
        
        **Pulley**
        *Definition:* A pulley is a wheel with a rope that makes lifting easier.
        *Visual Cue:* Think of a flag being raised up a flagpole.
        *Everyday Example:* Flagpole, blinds on windows, construction cranes
        *Practice Activity:* Circle all the pulleys you can find in a picture of a construction site
        
        [Additional terms with similar structure]
        
        **Level 2: Intermediate**
        
        [More complex definitions, examples, and activities]
        
        **Level 3: Advanced**
        
        [Most sophisticated definitions, examples, and activities including applications and explanations of how they make work easier]
        """)
        
    with tabs[3]:
        st.markdown("""
        **Zero-Shot Parent Communication Prompt:**
        ```
        Write a parent/guardian email explaining a new project-based learning initiative in 7th-grade science that:
        
        1. Introduces a 3-week collaborative project on sustainable ecosystems
        2. Explains the learning objectives and alignment with Next Generation Science Standards
        3. Details the timeline, materials needed, and at-home support opportunities
        4. Addresses potential concerns about group work and assessment
        5. Maintains a positive, professional, and welcoming tone
        6. Includes a brief FAQ section
        ```
        
        **Response:**
        
        **Subject: Exciting New Science Project: Sustainable Ecosystems Initiative**
        
        Dear Parents and Guardians,
        
        I hope this message finds you well! I'm writing to share information about an exciting new project-based learning initiative that our 7th-grade science students will begin next Monday.
        
        **Sustainable Ecosystems Project Overview**
        
        Over the next three weeks, students will work in collaborative teams to design and construct model sustainable ecosystems. This hands-on project will allow students to apply their understanding of energy flow, resource cycling, and human environmental impact through a creative and scientific lens.
        
        **Learning Objectives**
        
        Through this project, students will:
        - Analyze the flow of energy through ecosystems
        - Model the cycling of matter within living systems
        - Evaluate human impacts on natural systems
        - Design solutions to minimize environmental disruption
        - Develop collaboration and scientific communication skills
        
        This project directly aligns with NGSS standards MS-LS2-1 through MS-LS2-5 (Ecosystems: Interactions, Energy, and Dynamics).
        
        **Timeline and Materials**
        
        *Week 1:* Research and planning phase
        *Week 2:* Model construction and testing
        *Week 3:* Refinement, documentation, and presentation
        
        Most materials will be provided in class. Students will need to bring:
        - A shoebox or clear plastic container (by next Wednesday)
        - Optional: Natural materials like small rocks, sticks, or soil from home
        
        **How You Can Support**
        
        While students will have adequate time to work during class, your support at home might include:
        - Asking your child to explain their ecosystem design
        - Helping collect simple materials if needed
        - Encouraging research using our online resources
        - Reviewing their project documentation
        
        **Group Work and Assessment**
        
        Students will work in teams of 3-4, carefully balanced to include different strengths. Each student will have specific individual responsibilities alongside team components. Assessment will include both group and individual elements, ensuring that each student's contribution and understanding are fairly evaluated.
        
        **Frequently Asked Questions**
        
        *Q: What if my child is absent during part of the project?*
        A: We've built flexibility into the timeline. Please contact me directly if your child will miss more than two days during this unit.
        
        *Q: Will this project require Internet access at home?*
        A: No. While online research is helpful, all essential resources are available in class and in printed form.
        
        *Q: How can I see my child's finished project?*
        A: We'll host a "Sustainable Solutions Showcase" on Friday, October 15th from 3:30-4:30 PM. You're all invited!
        
        If you have any questions or would like to discuss the project further, please don't hesitate to reach out via email or during my office hours (Tuesdays and Thursdays, 3:00-4:00 PM).
        
        Thank you for your continued support of your child's science education!
        
        Sincerely,
        
        [Teacher Name]
        7th Grade Science
        Email: [email address]
        Phone: [phone number]
        """)
    
    # Example 4: Converting PCTFREI to Zero-Shot
    st.markdown("### Example 4: Integrating PCTFREI Elements into Zero-Shot Prompts")
    
    st.markdown("""
    This example demonstrates how to incorporate elements of the PCTFREI framework into zero-shot prompts
    without needing to provide specific examples.
    """)
    
    st.markdown("""
    **Zero-Shot Prompt with PCTFREI Elements:**
    ```
    As a 4th-grade math teacher preparing for a parent-teacher conference night (P+C),
    create a one-page handout explaining the key math concepts covered this semester (T).
    
    Format the handout with (F):
    - A brief introduction explaining your teaching approach
    - A bulleted list of the 5 main concepts with simple explanations
    - A "How to Help at Home" section with 3 practical activities
    - A "Resources" section with recommended websites and apps
    
    Align the content with Common Core Math Standards for Grade 4, particularly 
    4.OA.A (Operations & Algebraic Thinking) and 4.NBT (Number & Operations in Base Ten) (R).
    
    Design the handout to be accessible to parents without math backgrounds while 
    still conveying the curriculum rigor (additional context).
    ```
    
    **Response Excerpt:**
    
    **4th Grade Math: Semester Concepts & Home Support**
    
    **Dear Families,**
    
    In our 4th-grade math classroom, students build mathematical understanding through a balance of conceptual learning, procedural fluency, and real-world problem solving. We focus on developing mathematical thinkers who can explain their reasoning and approach problems with confidence.
    
    **Key Concepts This Semester:**
    
    • **Multi-Digit Multiplication** - Students learn to multiply multi-digit numbers using strategies based on place value and properties of operations, including the standard algorithm. (4.NBT.B.5)
    
    • **Division with Remainders** - Students solve division problems with remainders, interpreting what the remainder means in different situations. (4.OA.A.3)
    
    • **Factors & Multiples** - Students identify factor pairs, recognize that a whole number is a multiple of its factors, and determine whether a number is prime or composite. (4.OA.B.4)
    
    • **Fraction Equivalence** - Students recognize and generate equivalent fractions, using visual models and multiplication/division. (4.NF.A.1)
    
    • **Decimal Concepts** - Students understand decimal notation for fractions and compare decimal fractions. (4.NF.C.5-7)
    
    **How to Help at Home:**
    
    1. **Grocery Store Math** - When shopping, ask your child to estimate costs, calculate discounts, or find the better buy by comparing unit prices.
    
    2. **Cooking Fractions** - Involve your child in cooking to practice measuring with fractions. Try doubling or halving recipes for additional practice.
    
    3. **Pattern Investigation** - Look for and discuss patterns in everyday life – house numbers, floor tiles, natural objects – and predict what comes next in the pattern.
    
    **Recommended Resources:**
    
    *Websites:*
    • Khan Academy (www.khanacademy.org) - Free videos and practice for all 4th-grade topics
    • Math Playground (www.mathplayground.com) - Games that reinforce key concepts
    
    *Apps:*
    • Prodigy Math Game (free, with premium options)
    • ST Math (visual math approach)
    
    Please reach out with any questions about how to support your child's mathematical journey!
    
    [Teacher Name]
    """)
    
    st.markdown("""
    **Key Takeaway:** Even though this is a zero-shot prompt (no examples provided), it incorporates the key 
    elements of the PCTFREI framework to guide the AI. The result is a highly specific, well-structured 
    document tailored to the exact needs.
    """)
    
    # Key lessons from examples
    st.markdown("## Key Insights from Zero-Shot Examples")
    
    st.markdown("""
    From these examples, we can see that effective zero-shot prompts typically:
    
    1. **Provide clear parameters** - Grade level, subject area, specific topics
    
    2. **Use numbered lists** - Break down complex requirements into clear components
    
    3. **Specify output structure** - Indicate how the response should be organized
    
    4. **Incorporate standards** - Reference educational standards for alignment
    
    5. **Include purpose and audience** - Clarify who will use the content and how
    
    6. **Add constraints** - Time limits, material restrictions, or specific conditions
    
    7. **Use education-specific terminology** - Terms like "formative assessment," "Bloom's taxonomy," 
    or "differentiation" tap into the LLM's knowledge of educational concepts
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific guidance
    render_teacher_notes("""
    **Key Points to Emphasize:**
    
    * Zero-shot prompting works well for common educational content because LLMs have been trained on educational materials
    * The specificity of the prompt is critical - more detail generally leads to better results
    * Educational terminology helps tap into the LLM's specialized knowledge
    * Zero-shot prompting saves time but still requires thoughtful prompt construction
    
    **Discussion Questions:**
    
    * Which of the example prompt types would be most useful in your current teaching context?
    * What patterns do you notice in the structure of effective zero-shot prompts?
    * How could you adapt these examples for your specific subject area or grade level?
    * What additional parameters would you add to these prompts for your unique teaching needs?
    
    **Extension Idea:**
    
    Have participants identify a specific type of educational content they regularly create and develop 
    a zero-shot prompt for that content type using the patterns observed in these examples.
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