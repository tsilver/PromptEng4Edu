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
    page_title="Lesson 17: Examples",
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
    "title": "Personalized Learning Pathways: Examples",
    "lesson": "17",
    "section": "examples",
    "order": 2
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_17_examples"
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
    "lesson_17_examples",
    "examples",
    "Lesson 17: Examples",
    """
    **This section provides examples of effective prompts for personalized learning pathways.**
    
    Each example demonstrates how to:
    - Structure prompts for different aspects of personalization
    - Design learning materials for diverse student needs
    - Create adaptive pathways that respond to individual progress
    - Apply the PCTFR framework to personalized learning contexts
    
    Pay attention to how each prompt is constructed and what makes it effective.
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
    st.markdown(f"# {PAGE_INFO['title']}")
    
    st.markdown("""
    Below are examples of well-crafted prompts for creating personalized learning materials and pathways 
    across various subjects and grade levels. Each example includes an analysis of the prompt's key elements 
    and what makes it effective for addressing diverse student needs.
    """)
    
    # Example 1: Tiered Reading Comprehension Activities
    st.markdown("## Example 1: Tiered Reading Comprehension Activities")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as a literacy specialist who designs differentiated reading comprehension materials 
    that support diverse learners while maintaining high expectations and engagement for all students.
    
    Context: I teach 4th grade ELA in a classroom with reading levels ranging from 1st to 6th grade. 
    We're reading the novel "Because of Winn-Dixie" by Kate DiCamillo as a class read-aloud, but 
    students need differentiated comprehension activities to process the text at their individual 
    levels. I want all students to engage with the same themes and character development while having 
    appropriately challenging tasks.
    
    Task: Create a set of tiered comprehension activities for Chapter 5 of "Because of Winn-Dixie," 
    where Opal meets Miss Franny Block at the library and hears the story about the bear. The 
    activities should address the same key events and themes but provide different levels of 
    scaffolding and complexity for struggling, on-level, and advanced readers.
    
    Format: Design three tiered comprehension activity sets (Tier 1 for struggling readers, Tier 2 
    for on-level readers, Tier 3 for advanced readers). Each tier should include:
    1. A set of 5-7 comprehension questions that progress from literal to inferential to evaluative
    2. A character analysis activity focused on either Opal, Winn-Dixie, or Miss Franny Block
    3. A creative response option that connects to the theme of friendship or storytelling
    4. Key vocabulary support appropriate to the tier level
    
    Tier 1 should include sentence starters, word banks, simplified language, and visual supports. 
    Tier 2 should include some supportive elements but expect more independent thinking and writing. 
    Tier 3 should include extension questions that connect to broader themes, require synthesis, 
    and challenge students to make deeper literary connections.
    
    Reference Materials: In Chapter 5, Opal goes to the library where she meets Miss Franny Block, 
    who is initially frightened by Winn-Dixie. Miss Franny shares the story of a bear who once came 
    into the library and her prized possession—a book given to her by her father. Key themes include 
    the power of stories to connect people, unexpected friendships, and misjudging others based on 
    appearances. Essential vocabulary includes: Herman W. Block Memorial Library, congregate, narrate, 
    peculiar, advanced, and literate. The comprehension activities should address reading standard 
    RL.4.3 (describe in depth a character, setting, or event in a story).
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Literacy-Focused Persona:**
        - Specifies differentiation expertise
        - Emphasizes maintaining high expectations
        - Notes focus on diverse learners
        
        **Detailed Reading Context:**
        - Identifies specific text and chapter
        - Notes wide range of reading levels
        - Establishes shared read-aloud approach
        
        **Clear Differentiation Task:**
        - Specifies tiered activity approach
        - Focuses on same content with different support
        - Targets specific chapter content
        """)
    
    with col2:
        st.markdown("""
        **Comprehensive Format Structure:**
        - Outlines three clear tiers
        - Includes multiple activity types
        - Specifies scaffolding approaches for each tier
        - Details progression from concrete to abstract
        
        **Rich Literary Reference Materials:**
        - Summarizes key chapter events
        - Identifies important themes
        - Lists essential vocabulary
        - Connects to specific standards
        """)
    
    # Example 2: Personalized Math Pathway with Entry Points
    st.markdown("## Example 2: Personalized Math Pathway with Entry Points")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as a mathematics education specialist who designs adaptive learning pathways that 
    help students master essential math concepts through personalized routes based on readiness and 
    learning needs.
    
    Context: I teach a 6th grade math class with students at varying levels of algebraic thinking. 
    We're beginning a unit on expressions and equations, and I need a system that allows students to 
    start at different entry points based on their current understanding while ensuring all students 
    eventually master the grade-level standards. Some students still struggle with basic operations 
    with variables, while others are ready for more complex multi-step equations.
    
    Task: Create a personalized learning pathway for algebraic expressions and equations that includes 
    multiple entry points, adaptive practice, formative checks, and clear progression routes. The 
    pathway should accommodate students who need remediation on prerequisite skills while providing 
    appropriate challenge for students ready for grade-level or advanced work.
    
    Format: Design a learning pathway system that includes:
    1. A diagnostic pre-assessment to place students at the appropriate entry point
    2. Three entry points:
       - Entry Point A: Foundational (operations with whole numbers, introduction to variables)
       - Entry Point B: Developing (simple equations, properties of operations)
       - Entry Point C: Grade-Level (writing and solving one-step equations)
    3. Learning modules for each concept with:
       - Instructional content including worked examples and visual models
       - Guided practice with immediate feedback
       - Independent practice with adaptive difficulty
       - Formative assessment checkpoints with decision rules for advancement
    4. Extension activities for students who demonstrate early mastery
    5. A pathway map that students can use to track their progress
    
    Each entry point should lead students through a coherent sequence toward the end target of 
    writing and solving one- and two-step equations (grade-level standard). Include specific criteria 
    for when students should move from one module to the next, and provide guidance for supporting 
    students who struggle at any point in the pathway.
    
    Reference Materials: The pathway should address the following standards: 6.EE.A.2 (write, read, 
    and evaluate expressions with variables), 6.EE.A.3 (apply properties of operations to generate 
    equivalent expressions), and 6.EE.B.7 (solve real-world problems by writing and solving equations 
    of the form x + p = q and px = q). Common misconceptions include confusion between expressions and 
    equations, difficulty understanding the meaning of variables, and errors in the order of operations. 
    Students should ultimately be able to translate between word problems, visual models, and symbolic 
    representations of algebraic situations.
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Mathematics Specialist Persona:**
        - Emphasizes adaptive learning expertise
        - Focuses on mastery through personalization
        - Notes responsiveness to readiness levels
        
        **Specific Mathematical Context:**
        - Identifies varied algebraic thinking levels
        - Names specific content area
        - Notes particular student challenges
        
        **Clear Pathway Design Task:**
        - Specifies multiple entry points
        - Focuses on eventual mastery for all
        - Addresses both remediation and extension
        """)
    
    with col2:
        st.markdown("""
        **Adaptive Pathway Format:**
        - Includes diagnostic placement
        - Provides three specific entry points
        - Incorporates decision rules for progression
        - Balances structure with responsiveness
        
        **Comprehensive Math References:**
        - Lists specific math standards
        - Identifies common misconceptions
        - Establishes clear end goals
        - Notes multiple representations
        """)
    
    # Example 3: Learning Style-Based Science Materials
    st.markdown("## Example 3: Learning Style-Based Science Materials")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as a science education specialist who designs multimodal learning resources that 
    present scientific concepts through different representational formats to accommodate diverse 
    learning preferences and processing styles.
    
    Context: I teach middle school life science to a diverse group of 7th graders. We're studying 
    cell structure and function, and I want to provide students with options for how they engage 
    with this content based on their learning preferences. Some students learn best through visual 
    representations, others through text, others through hands-on activities, and others through 
    auditory/verbal processing.
    
    Task: Create a set of learning materials on cell organelles and their functions that presents 
    the same essential content through different modalities/formats. The materials should allow 
    students to choose learning approaches that match their preferences while ensuring all students 
    master the same key concepts.
    
    Format: Design a learning package with four parallel approaches to learning about cell organelles:
    1. Visual Guide: A heavily visual approach featuring detailed diagrams, infographics, color-coding 
       systems, and visual analogies (like cell as a factory)
    2. Text-Based Guide: A well-structured text approach with clear explanations, examples, analogies, 
       and organizational frameworks expressed primarily through words
    3. Interactive Investigation: A hands-on approach featuring manipulatives, model-building activities, 
       interactive simulations, and tactile learning experiences
    4. Auditory/Discussion Guide: A verbal processing approach featuring recorded explanations, discussion 
       protocols, verbal analogies, and opportunities for students to explain concepts aloud
    
    Each approach should cover the same essential content: the structure and function of the cell membrane, 
    nucleus, mitochondria, chloroplasts (in plant cells), ribosomes, endoplasmic reticulum, Golgi apparatus, 
    lysosomes, and cytoplasm. Include a student self-assessment tool that helps them identify which approach(es) 
    might work best for them, and a common assessment that can verify mastery regardless of which approach(es) 
    students used.
    
    Reference Materials: This content addresses NGSS MS-LS1-2: "Develop and use a model to describe the 
    function of a cell as a whole and ways the parts of cells contribute to the function." Students should 
    understand both the structure of each organelle and its function within the cell system. They should 
    also understand differences between plant and animal cells. The summary assessment should require 
    students to explain relationships between structure and function for each organelle.
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Science Education Persona:**
        - Emphasizes multimodal approach
        - Notes expertise in representational formats
        - Focuses on diverse learning preferences
        
        **Specific Learning Context:**
        - Identifies particular science content
        - Acknowledges diverse learning styles
        - Establishes personalization goal
        
        **Clear Multimodal Task:**
        - Requests same content in different formats
        - Emphasizes student choice
        - Maintains consistent learning goals
        """)
    
    with col2:
        st.markdown("""
        **Comprehensive Format Structure:**
        - Outlines four distinct approaches
        - Details specific elements of each format
        - Includes self-assessment component
        - Incorporates common assessment mechanism
        
        **Focused Science References:**
        - Lists specific organelles to include
        - Cites relevant science standards
        - Emphasizes structure-function relationships
        - Notes plant/animal cell distinctions
        """)
    
    # Example 4: Interest-Based History Project Options
    st.markdown("## Example 4: Interest-Based History Project Options")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as a history education specialist who designs project-based learning experiences 
    that allow students to explore historical topics through their personal interests and strengths 
    while maintaining rigorous historical thinking skills.
    
    Context: I teach 8th grade U.S. History, and we're completing a unit on the Civil War and 
    Reconstruction. Rather than a single standardized assessment, I want to offer students personalized 
    project options that allow them to demonstrate their understanding through different approaches 
    based on their interests. My students have diverse strengths—some are strong writers, others are 
    artistic, others are technology-focused, and others excel at oral presentation.
    
    Task: Create a set of interest-based project options that allow students to demonstrate their 
    understanding of the causes, events, and outcomes of the Civil War and Reconstruction period 
    through different modes that align with their strengths and interests. Each option should 
    require the same level of historical thinking and content knowledge while allowing for 
    personalized expression.
    
    Format: Design a menu of project options with:
    1. At least 6 distinct project types that appeal to different student interests and strengths:
       - Option for students who enjoy writing/research
       - Option for visually/artistically oriented students
       - Option for students who prefer multimedia/technology
       - Option for students who excel at public speaking/performance
       - Option for students who enjoy hands-on creation/building
       - Option for students who prefer collaborative work
    2. For each project option, include:
       - Detailed description of the project
       - Required historical content that must be addressed
       - Step-by-step creation process
       - Examples of what excellence looks like
       - Evaluation criteria/rubric
    3. A guided project selection tool that helps students choose the option that best fits their 
       interests and learning style
    4. A common planning template that students complete regardless of project choice to ensure 
       historical thinking processes
    
    All project options should require students to address key historical concepts including: the 
    economic, social, and political causes of the Civil War; major turning points in the conflict; 
    the impact of the war on different groups; key Reconstruction policies; and the long-term legacy 
    of this period. Each option should also require students to use primary sources as evidence and 
    to consider multiple perspectives on historical events.
    
    Reference Materials: This project addresses social studies standards on analyzing the causes and 
    effects of the Civil War (8.USH.4.1), evaluating the impact of Reconstruction policies (8.USH.5.2), 
    and using primary and secondary sources to construct historical arguments (8.USH.1.3). Key historical 
    content includes: slavery as the central cause of the conflict, the Emancipation Proclamation, major 
    battles (Fort Sumter, Gettysburg, etc.), surrender at Appomattox, Lincoln's assassination, 
    Reconstruction amendments (13th, 14th, 15th), the rise of Jim Crow laws, and the contested legacy 
    of the Civil War. Students have already constructed timelines of major events and analyzed several 
    primary sources, including the Gettysburg Address and excerpts from slave narratives.
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **History Education Persona:**
        - Emphasizes project-based approach
        - Notes focus on personal interests
        - Maintains historical thinking rigor
        
        **Detailed Classroom Context:**
        - Identifies specific historical period
        - Acknowledges diverse student strengths
        - Establishes assessment alternative goal
        
        **Interest-Based Task Design:**
        - Requests multiple project options
        - Focuses on equivalent demonstration of learning
        - Emphasizes alignment with student strengths
        """)
    
    with col2:
        st.markdown("""
        **Comprehensive Project Structure:**
        - Outlines six distinct project types
        - Includes detailed components for each option
        - Incorporates selection guidance
        - Maintains common planning elements
        
        **Rich Historical References:**
        - Lists key historical concepts to address
        - Cites specific content requirements
        - Notes primary source requirement
        - Connects to multiple social studies standards
        """)
    
    # Example 5: Scaffolded Writing Assignment
    st.markdown("## Example 5: Scaffolded Writing Assignment")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as a writing instruction specialist who designs scaffolded writing assignments 
    that support diverse learners in developing composition skills through appropriately challenging 
    tasks based on individual readiness levels.
    
    Context: I teach 9th grade English in an inclusive classroom with a wide range of writing abilities. 
    Some students write below grade level and struggle with basic paragraph structure, while others write 
    at or above grade level and are working on more sophisticated elements like style and voice. We've 
    been studying argumentative writing, and I want to assign a persuasive essay that allows all students 
    to engage with the same basic task but with different levels of scaffolding and expectations.
    
    Task: Create a scaffolded persuasive essay assignment on whether schools should require school 
    uniforms, with three different versions that provide varying levels of support based on student 
    writing readiness. Each version should help students create an effective persuasive essay while 
    providing appropriate scaffolding for their current skill level.
    
    Format: Design three versions of the assignment:
    1. Highly Scaffolded Version: For students significantly below grade level, including:
       - Paragraph-by-paragraph template with sentence starters
       - Guided planning organizers with specific prompts
       - List of transition words and persuasive techniques
       - Step-by-step writing process guide
       - Model paragraphs as examples
    2. Moderately Scaffolded Version: For students approaching grade level, including:
       - Essay structure guide without sentence starters
       - Planning templates with more flexibility
       - Checklists for self-assessment during writing
       - Examples of effective and ineffective persuasive techniques
       - Peer review guidelines
    3. Minimally Scaffolded Version: For students at or above grade level, including:
       - Open-ended planning suggestions
       - Advanced rhetorical techniques to consider
       - Criteria for excellence that focus on style and audience awareness
       - Self-directed revision process
       - Opportunities for creative approaches to the standard format
    
    All three versions should require students to take a clear position, provide logical reasons supported 
    by evidence, address counterarguments, and include an effective introduction and conclusion. Each 
    version should also include a rubric appropriate to the scaffold level that maintains high expectations 
    while acknowledging different starting points.
    
    Reference Materials: This assignment addresses writing standards W.9-10.1 (Write arguments to support 
    claims), W.9-10.4 (Produce clear and coherent writing), and W.9-10.5 (Develop and strengthen writing 
    through planning, revising, and editing). We've studied persuasive techniques including ethos, pathos, 
    and logos, and analyzed several argumentative essays together as a class. Common challenges for struggling 
    writers include developing sufficient supporting evidence, organizing ideas logically, and addressing 
    counterarguments effectively. The topic of school uniforms allows for multiple perspectives and 
    connects to students' lives, making it accessible while still offering complexity for deeper analysis.
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Writing Specialist Persona:**
        - Emphasizes scaffolded approach
        - Notes focus on diverse learners
        - Maintains appropriate challenge
        
        **Detailed Writing Context:**
        - Acknowledges wide ability range
        - Identifies specific writing genre
        - Notes current instructional focus
        
        **Clear Differentiation Task:**
        - Specifies common topic and genre
        - Requests varying scaffold levels
        - Maintains consistent core requirements
        """)
    
    with col2:
        st.markdown("""
        **Comprehensive Scaffold Structure:**
        - Outlines three distinct support levels
        - Details specific components for each version
        - Includes appropriate tools for each level
        - Balances support with independence
        
        **Specific Writing References:**
        - Connects to writing standards
        - Notes persuasive techniques studied
        - Identifies common writing challenges
        - Explains topic selection rationale
        """)
    
    # Example 6: Adaptive Digital Learning Module
    st.markdown("## Example 6: Adaptive Digital Learning Module")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as an educational technology specialist who designs adaptive digital learning 
    experiences that respond to individual student performance to provide personalized instruction, 
    practice, and assessment.
    
    Context: I teach a high school chemistry course with students who have varied math backgrounds 
    and conceptual understanding. We're beginning a unit on stoichiometry, which requires both 
    procedural fluency with calculations and conceptual understanding of chemical reactions. Many 
    students struggle with connecting the mathematical procedures to the underlying chemical concepts, 
    and they need different levels of support depending on their specific challenges.
    
    Task: Create an adaptive digital learning module on stoichiometry that assesses student understanding 
    at multiple points and provides personalized learning paths based on performance. The module should 
    adapt both the content presented and the scaffolding provided based on how students respond to 
    questions and activities.
    
    Format: Design an adaptive learning module with:
    1. An initial diagnostic assessment that evaluates:
       - Prerequisite math skills (balancing equations, unit conversions, etc.)
       - Understanding of mole concept and Avogadro's number
       - Interpretation of chemical reactions and balanced equations
    2. Personalized learning paths that branch based on assessment results, with:
       - Targeted instruction for identified gaps
       - Varied examples based on student performance
       - Progressive release of scaffolding as students demonstrate understanding
    3. Adaptive practice sets where:
       - Questions adjust in difficulty based on student success
       - Hints and supports appear when students struggle
       - Alternative explanation formats are provided when needed
    4. Embedded formative assessments that:
       - Check for conceptual understanding at critical points
       - Provide immediate corrective feedback
       - Determine subsequent content presentation
    5. A system flowchart showing possible pathways through the module based on different 
       student response patterns
    
    The module should address both procedural and conceptual aspects of stoichiometry, including 
    mole-to-mole conversions, mass-to-mass calculations, limiting reactants, and percent yield. At 
    each point, the system should adapt to provide additional support for students who struggle or 
    advanced extensions for students who demonstrate mastery.
    
    Reference Materials: This module addresses chemistry standards HS-PS1-7 (use mathematical 
    representations to support the claim that atoms, and therefore mass, are conserved during a 
    chemical reaction). Key concepts include the mole concept (6.022 × 10^23 particles), balanced 
    chemical equations, mole ratios, conversion factors, limiting reactants, and percent yield. Common 
    misconceptions include confusion about the difference between coefficients and subscripts in 
    chemical formulas, difficulty connecting symbolic equations to molecular-level processes, and 
    challenges with setting up conversion factors. Students have varied math backgrounds, with some 
    still developing algebraic reasoning skills while others have completed calculus.
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **EdTech Specialist Persona:**
        - Emphasizes adaptive learning expertise
        - Focuses on personalized instruction
        - Notes responsiveness to performance
        
        **Specific Chemistry Context:**
        - Identifies challenging chemistry topic
        - Notes varied math backgrounds
        - Acknowledges conceptual-procedural connection
        
        **Adaptive Module Task:**
        - Requests responsive learning paths
        - Focuses on both assessment and instruction
        - Addresses varied student challenges
        """)
    
    with col2:
        st.markdown("""
        **Comprehensive Adaptive Structure:**
        - Includes diagnostic assessment
        - Outlines branching learning paths
        - Incorporates progressive scaffolding
        - Requests system flowchart for pathways
        
        **Detailed Chemistry References:**
        - Lists specific stoichiometry topics
        - Cites relevant chemistry standards
        - Identifies common misconceptions
        - Notes mathematical prerequisites
        """)
    
    # Key Takeaways Section
    st.markdown("## Key Takeaways from Examples")
    
    st.markdown("""
    ### Effective Prompts for Personalized Learning:
    
    * **Specify the dimensions of personalization** (content, process, product, etc.)
    * **Identify student variables** being addressed (readiness, interests, learning preferences)
    * **Request appropriate scaffold levels** for different learner profiles
    * **Maintain consistent learning goals** across personalized versions
    * **Include guidance for determining** which options/paths are appropriate for individual students
    * **Request adaptive elements** that respond to student performance
    * **Balance structure and flexibility** appropriate to student needs
    
    ### The Power of the PCTFR Framework for Personalization:
    
    * **Persona:** Defines the educational approach to personalization and expertise lens
    * **Context:** Establishes student diversity factors and classroom constraints
    * **Task:** Specifies the type of personalization and its learning goals
    * **Format:** Provides detailed structure for the personalized options and their components
    * **Reference Materials:** Ensures content accuracy and alignment with standards for all students
    
    In the next section, you'll have the opportunity to practice creating your own prompts for
    personalized learning materials and pathways that address your specific teaching context.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Encourage participants to note which personalization approaches most closely align with their current teaching needs
    * Point out how each example maintains rigorous learning goals while varying supports and approaches
    * Emphasize that personalization does not mean having completely different learning goals for each student
    * Highlight how these prompts create starting points that teachers should always review and adapt
    
    **Common Questions:**
    
    * "How do I manage all these different versions in my classroom?" — Suggest starting with just 2-3 options/levels
    * "What's the difference between differentiation and personalization?" — Note that personalization adds student choice and agency
    * "Does this mean more work for me as the teacher?" — Discuss how prompt engineering can make personalization more manageable
    
    **Extension Activity:**
    
    Have participants identify one example that most closely aligns with their teaching needs, then modify it by:
    1. Changing the content to match their current unit
    2. Adjusting the personalization approach to suit their students' needs
    3. Adding specific elements to address challenges they've encountered with meeting diverse needs
    
    This creates a personalized template they can use immediately in their planning.
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