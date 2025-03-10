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
    page_title="Lesson 16: Examples",
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
    "title": "Collaborative Learning Activities: Examples",
    "lesson": "16",
    "section": "examples",
    "order": 2
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_16_examples"
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
    "lesson_16_examples",
    "examples",
    "Lesson 16: Examples",
    """
    **This section provides examples of effective prompts for collaborative learning activities.**
    
    Each example demonstrates how to:
    - Structure prompts for different types of collaborative experiences
    - Incorporate key elements of effective collaboration
    - Address common challenges in collaborative learning
    - Apply the PCTFR framework to collaborative contexts
    
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
    Below are examples of well-crafted prompts for creating collaborative learning activities across 
    various subjects and grade levels. Each example includes an analysis of the prompt's key elements 
    and what makes it effective for promoting meaningful collaboration.
    """)
    
    # Example 1: Elementary Think-Pair-Share Activity
    st.markdown("## Example 1: Elementary Think-Pair-Share Protocol")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as an elementary education specialist who focuses on developing structured 
    collaborative learning experiences that support diverse learners, including English language 
    learners and students with varying social skills.
    
    Context: I teach 3rd grade in a diverse classroom where students are studying animal adaptations 
    in science. Many of my students are still developing their discussion skills and confidence in 
    sharing ideas. About 25% of my students are English language learners, and several have IEPs for 
    social-emotional or attention challenges.
    
    Task: Create a scaffolded Think-Pair-Share protocol that helps students collaboratively analyze 
    how different animals have adapted to their environments. The protocol should support productive 
    peer interaction while ensuring all students can participate successfully.
    
    Format: Design a 20-25 minute Think-Pair-Share activity that includes:
    1. A visually supported introduction with clear learning objectives
    2. Structured "Think" phase with individual thinking prompts at multiple levels
    3. Guided "Pair" phase with specific conversation roles, sentence starters, and time guidelines
    4. Inclusive "Share" phase with options for how pairs can report their ideas to the class
    5. Visual supports that can be displayed during each phase
    6. Teacher facilitation notes for supporting struggling students
    7. Extension questions for early finishers
    
    Reference Materials: Students have been learning about animal adaptations including camouflage, 
    body coverings, specialized limbs, and behavioral adaptations. We've studied examples like polar 
    bears (thick fur, blubber), desert lizards (burrowing behavior, water conservation), and rainforest 
    tree frogs (sticky toe pads, bright coloration). The science standard being addressed is NGSS 3-LS4-3: 
    "Construct an argument that in a particular habitat some organisms can survive well, some survive 
    less well, and some cannot survive at all."
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Developmentally Appropriate Persona:**
        - Specifies elementary education expertise
        - Emphasizes structured collaboration
        - Notes focus on supporting diverse learners
        
        **Detailed Classroom Context:**
        - Identifies specific student demographics
        - Notes varying collaboration readiness
        - Establishes existing content knowledge
        
        **Clear Collaborative Task:**
        - Specifies Think-Pair-Share structure
        - Focuses on specific science content
        - Emphasizes inclusive participation
        """)
    
    with col2:
        st.markdown("""
        **Comprehensive Format Elements:**
        - Includes all phases of the protocol
        - Requests specific scaffolds (sentence starters)
        - Incorporates visual supports
        - Addresses differentiation needs
        
        **Specific Reference Materials:**
        - Lists key science concepts
        - Provides concrete examples
        - Connects to specific standards
        - Ensures content alignment
        """)
    
    # Example 2: Middle School Jigsaw Activity
    st.markdown("## Example 2: Middle School Jigsaw Activity")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as a middle school social studies curriculum specialist who designs collaborative 
    learning activities that develop content knowledge while strengthening academic discussion 
    skills and cultural responsiveness.
    
    Context: I'm teaching a unit on ancient civilizations to 7th graders, focusing on comparing 
    the contributions and characteristics of several major civilizations. My students have varied 
    background knowledge about ancient history and different reading abilities. They've had some 
    experience with group work but need structure to stay on task and ensure equal participation.
    
    Task: Create a jigsaw activity where students become "experts" on one ancient civilization, 
    then teach others about it in mixed groups. The activity should develop deep understanding of 
    cultural contributions while practicing academic discussion, note-taking, and teaching skills.
    
    Format: Design a 2-day jigsaw activity with:
    1. Clear instructions for forming expert and teaching groups
    2. Four focused expert topics (one per civilization):
       - Government and Social Structure
       - Arts and Architecture
       - Science and Technology
       - Religious Beliefs and Practices
    3. Expert group worksheets that guide research and preparation
    4. A note-taking structure for teaching groups
    5. Accountability measures to ensure individual learning
    6. Discussion prompts for comparing civilizations
    7. A culminating synthesis activity
    
    Include time allocations for each phase, strategies for managing transitions between groups, 
    and guidance for supporting students who struggle with the social or academic demands of the 
    activity.
    
    Reference Materials: The civilizations being studied are Ancient Egypt, Mesopotamia, Indus Valley, 
    and Ancient China (Zhou Dynasty). Students have access to textbooks, a digital article database 
    at a 5th-8th grade reading level, and brief documentary videos on each civilization. The unit 
    addresses social studies standard SS.7.4: "Analyze the cultural, political, and economic 
    contributions of ancient civilizations and how they influence the modern world."
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Subject-Specific Persona:**
        - Specifies middle school social studies focus
        - Emphasizes academic discussion skills
        - References cultural responsiveness
        
        **Realistic Classroom Context:**
        - Notes mixed ability levels
        - Acknowledges varied background knowledge
        - Describes students' collaboration experience
        
        **Structured Collaborative Task:**
        - Specifies jigsaw format clearly
        - Sets content-specific learning goals
        - Identifies multiple skill development areas
        """)
    
    with col2:
        st.markdown("""
        **Comprehensive Activity Design:**
        - Outlines multi-day structure
        - Organizes content into focused subtopics
        - Includes transitions and time management
        - Incorporates accountability measures
        
        **Well-Defined Reference Materials:**
        - Specifies civilizations to be studied
        - Lists available learning resources
        - Notes reading level considerations
        - Connects to specific standards
        """)
    
    # Example 3: High School Problem-Based Learning
    st.markdown("## Example 3: High School Problem-Based Learning")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as an experienced high school mathematics educator who specializes in problem-based 
    learning and collaborative mathematical inquiry.
    
    Context: I'm teaching an Algebra 2 course to 10th and 11th graders who have strong procedural 
    skills but need development in applying mathematical concepts to real-world scenarios and 
    explaining their reasoning. Students have varied mathematical confidence levels but limited 
    experience with open-ended collaborative problem-solving.
    
    Task: Create a collaborative problem-based learning activity focused on quadratic functions 
    and their applications. The activity should require students to work in teams to analyze a 
    real-world scenario, develop a mathematical model using quadratic functions, and present their 
    solution with justification.
    
    Format: Design a structured 2-3 day collaborative investigation that includes:
    1. A complex, open-ended problem scenario with multiple solution paths
    2. Clear team roles with specific responsibilities (4 students per team)
    3. A structured protocol for mathematical modeling:
       - Problem analysis and identification of variables
       - Development of quadratic models
       - Testing and refinement of models
       - Application to answer the driving question
    4. Scaffolded worksheets that guide the process while allowing for creativity
    5. Structured checkpoints for teacher feedback
    6. Guidelines for preparing a team presentation
    7. Individual reflection questions that assess mathematical understanding
    8. A rubric that addresses both mathematical content and collaborative process
    
    Include guidance for addressing common misconceptions about quadratic functions and suggestions 
    for supporting teams that struggle with the collaborative process or mathematical concepts.
    
    Reference Materials: Students have learned to represent quadratic functions in standard, vertex, 
    and factored form. They can solve quadratic equations, find key features (vertex, intercepts), 
    and transform basic parabolas. They are less experienced with contextual applications and 
    mathematical modeling. The activity should address standards A-CED.1 (create equations in two 
    or more variables to represent relationships), F-IF.4 (interpret key features of graphs in context), 
    and MP.4 (model with mathematics).
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Specialized Mathematical Persona:**
        - Focuses on problem-based learning
        - Emphasizes mathematical inquiry
        - Establishes high school expertise
        
        **Detailed Learning Context:**
        - Identifies specific student strengths
        - Notes areas for development
        - Acknowledges varied confidence levels
        
        **Complex Collaborative Task:**
        - Centers on mathematical modeling
        - Connects to real-world applications
        - Requires multiple mathematical skills
        """)
    
    with col2:
        st.markdown("""
        **Structured Collaborative Format:**
        - Includes clear team roles
        - Provides process protocol
        - Balances scaffolding with openness
        - Incorporates individual accountability
        
        **Specific Mathematical References:**
        - Lists prerequisite knowledge
        - Identifies potential misconceptions
        - Connects to mathematical standards
        - Clarifies experience levels with modeling
        """)
    
    # Example 4: Elementary Collaborative Reading Roles
    st.markdown("## Example 4: Elementary Collaborative Reading Roles")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as an elementary literacy specialist who designs structured collaborative reading 
    experiences that develop comprehension strategies while supporting diverse readers.
    
    Context: I teach 4th grade in a classroom with reading levels ranging from 2nd to 6th grade. 
    We're reading chapter books in small groups, and I want to implement collaborative reading roles 
    to deepen comprehension and engagement. Students have limited experience with literature circles 
    and need clear guidance on their responsibilities.
    
    Task: Create a set of collaborative reading roles that support comprehension strategy development 
    while ensuring all students can participate meaningfully regardless of reading level. The roles 
    should work with any chapter book and help students focus on different aspects of comprehension.
    
    Format: Design a collaborative reading system that includes:
    1. 5-6 distinct role descriptions with clear, specific responsibilities
    2. Role-specific worksheets/task cards with step-by-step instructions
    3. Differentiated options within each role for students at different reading levels
    4. Visual supports and examples for each role
    5. A structured discussion protocol for group meetings
    6. Teacher facilitation guides for supporting each role
    7. A rotation system so students experience multiple comprehension strategies
    8. Accountability measures for individual preparation and participation
    
    Each role should focus on a specific comprehension strategy (e.g., questioning, visualizing, 
    connecting) and include both preparation tasks and discussion contributions. Include modifications 
    for struggling readers and extensions for advanced readers within each role.
    
    Reference Materials: Students are familiar with the following comprehension strategies: making 
    predictions, asking questions, making connections, visualizing, identifying main ideas, and 
    summarizing. The reading standard being addressed is CCSS.ELA-LITERACY.RL.4.2: "Determine a theme 
    of a story, drama, or poem from details in the text; summarize the text." Students meet in their 
    reading groups for 30 minutes three times per week.
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Literacy-Focused Persona:**
        - Specifies elementary literacy expertise
        - Emphasizes structured collaboration
        - Notes support for diverse readers
        
        **Specific Reading Context:**
        - Identifies wide range of reading levels
        - Establishes current instructional approach
        - Notes limited experience with literature circles
        
        **Clear Collaborative Task:**
        - Focuses on reading comprehension strategies
        - Establishes role-based approach
        - Emphasizes inclusive participation
        """)
    
    with col2:
        st.markdown("""
        **Comprehensive Role Structure:**
        - Requests multiple distinct roles
        - Includes step-by-step guidance
        - Incorporates differentiation options
        - Addresses rotation for strategy exposure
        
        **Relevant Reference Materials:**
        - Lists familiar comprehension strategies
        - Notes specific reading standards
        - Provides logistical information
        - Supports appropriate design decisions
        """)
    
    # Example 5: Secondary Peer Feedback Protocol
    st.markdown("## Example 5: Secondary Peer Feedback Protocol")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as a high school writing teacher who designs collaborative peer review processes 
    that develop students' critical analysis skills while improving writing quality.
    
    Context: I teach 11th grade English, and my students are working on argumentative research essays. 
    They have completed first drafts of 4-6 page papers and need structured peer feedback to improve 
    their arguments, evidence, and organization. Students have variable experience giving constructive 
    feedback and often struggle to provide specific, actionable comments.
    
    Task: Create a collaborative peer feedback protocol that helps students provide substantial, 
    constructive feedback on argumentative essays. The protocol should develop both writing and 
    analytical skills while ensuring feedback is specific, balanced, and improvement-oriented.
    
    Format: Design a peer review system that includes:
    1. A preparation guide for writers to help focus feedback requests
    2. A structured peer feedback form with specific questions for different essay elements:
       - Thesis statement and main argument
       - Evidence selection and integration
       - Counterargument and rebuttal
       - Organization and transitions
       - Introduction and conclusion effectiveness
    3. Guidelines for constructive comment framing (strengths and needs)
    4. A face-to-face discussion protocol for clarifying feedback
    5. A revision planning template for writers to process received feedback
    6. A reflection component for both giving and receiving feedback
    
    The process should take approximately 90 minutes (one block period) and include clear time 
    allocations for each stage. Include strategies for managing students who finish at different 
    rates and supporting those who struggle with giving or receiving critical feedback.
    
    Reference Materials: Students' essays respond to self-selected research questions on contemporary 
    issues. Essays are expected to include a clear thesis, organized body paragraphs with evidence from 
    credible sources, counterargument acknowledgment, and proper MLA citation. The activity addresses 
    writing standards W.11-12.1 (Write arguments to support claims), W.11-12.5 (Develop and strengthen 
    writing through revision), and SL.11-12.1 (Participate effectively in collaborative discussions).
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Writing-Focused Persona:**
        - Specifies high school writing expertise
        - Emphasizes peer review processes
        - Notes dual focus on writing and analysis
        
        **Specific Writing Context:**
        - Identifies exact assignment type and length
        - Notes current stage in writing process
        - Acknowledges feedback challenges
        
        **Structured Feedback Task:**
        - Focuses on specific essay elements
        - Balances strengths and needs
        - Incorporates discussion and planning
        """)
    
    with col2:
        st.markdown("""
        **Comprehensive Protocol Design:**
        - Includes preparation, feedback, and processing
        - Addresses specific argumentative elements
        - Incorporates face-to-face interaction
        - Includes reflection component
        
        **Detailed Reference Materials:**
        - Describes assignment parameters
        - Lists specific writing expectations
        - Connects to relevant standards
        - Provides time constraints
        """)
    
    # Example 6: Project-Based Learning Team Structure
    st.markdown("## Example 6: Project-Based Learning Team Structure")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as an experienced project-based learning coach who helps teachers design effective 
    team structures and collaborative protocols for sustained group projects.
    
    Context: I teach a STEM elective for 8th graders focused on environmental engineering. Students 
    will work in teams of 4 on a month-long project to design solutions for a local environmental 
    challenge. The class is diverse in terms of academic strengths, social skills, and prior knowledge. 
    This is many students' first experience with extended collaborative work, and previous group 
    projects have struggled with unequal participation and poor time management.
    
    Task: Create a comprehensive team structure and collaboration system for the environmental 
    engineering project that ensures positive interdependence, individual accountability, and 
    effective project management. The system should help students develop both STEM and collaboration 
    skills throughout the project.
    
    Format: Design a collaborative project system that includes:
    1. Team formation strategy with rationale (teacher-selected vs. self-selected)
    2. 4 complementary team roles with specific responsibilities that rotate weekly
    3. Team contract template with collaboration norms and conflict resolution procedures
    4. Weekly planning and reflection protocols (15-20 minutes each)
    5. Progress monitoring tools that track both individual and team accomplishments
    6. Structured checkpoints for teacher feedback (at least 3 throughout the project)
    7. Peer evaluation forms that assess specific collaborative behaviors
    8. Final reflection protocol addressing both project outcomes and team process
    
    Include specific strategies for addressing common project team challenges (dominance by one member, 
    social loafing, scope creep, interpersonal conflicts) and suggestions for supporting students with 
    social or executive functioning challenges.
    
    Reference Materials: The project challenge is to design and prototype a solution to reduce waste, 
    conserve resources, or address pollution in the school or local community. Project phases include: 
    1) Problem definition and research, 2) Brainstorming and solution selection, 3) Design and testing, 
    4) Refinement and final presentation. Class meets daily for 50 minutes with occasional access to 
    extended work periods. NGSS standards addressed include MS-ETS1-1 (Define criteria and constraints 
    of a design problem) and MS-ETS1-2 (Evaluate competing design solutions).
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Project-Based Learning Persona:**
        - Specifies PBL coaching expertise
        - Emphasizes team structures
        - Focuses on sustained collaboration
        
        **Detailed Project Context:**
        - Identifies specific course and grade level
        - Notes project duration and topic
        - Addresses previous collaboration challenges
        
        **Comprehensive Team System Task:**
        - Focuses on multiple collaboration elements
        - Addresses both structure and process
        - Incorporates project management
        """)
    
    with col2:
        st.markdown("""
        **Robust Collaborative Framework:**
        - Includes role definition and rotation
        - Addresses norm-setting and conflict resolution
        - Incorporates monitoring and reflection
        - Balances individual and team accountability
        
        **Specific Project References:**
        - Outlines project challenge and phases
        - Notes time constraints and resources
        - Connects to engineering standards
        - Addresses potential collaboration issues
        """)
    
    # Key Takeaways Section
    st.markdown("## Key Takeaways from Examples")
    
    st.markdown("""
    ### Effective Prompts for Collaborative Learning Activities:
    
    * **Specify the collaborative structure** (Think-Pair-Share, Jigsaw, Problem-Based Learning, etc.)
    * **Address both content learning and collaboration skill development**
    * **Include mechanisms for positive interdependence** (roles, resource distribution, common goals)
    * **Build in individual accountability** through specific structures or assessment approaches
    * **Provide clear protocols for interaction** that support productive communication
    * **Include scaffolds for different phases** of the collaborative process
    * **Address common collaboration challenges** proactively with preventive strategies
    * **Incorporate reflection** on both content learning and collaborative process
    
    ### The Power of the PCTFR Framework for Collaborative Design:
    
    * **Persona:** Defines the educational approach to collaboration and expertise lens
    * **Context:** Establishes student collaboration readiness and classroom constraints
    * **Task:** Specifies the type of collaborative experience and its learning goals
    * **Format:** Provides detailed structure for the collaborative process and its components
    * **Reference Materials:** Ensures content accuracy and alignment with standards and objectives
    
    In the next section, you'll have the opportunity to practice creating your own prompts for
    collaborative learning activities that address your specific teaching context.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Encourage participants to note which examples most closely align with their current teaching needs
    * Point out how each example balances structure with flexibility appropriate to the students' collaboration skills
    * Emphasize that these prompts create starting points that teachers should always review and adapt
    * Highlight how specific elements address common collaboration challenges (unequal participation, off-task behavior, etc.)
    
    **Common Questions:**
    
    * "How do I assess individual learning in collaborative activities?" — Note the various accountability mechanisms
    * "What if my students have very limited collaboration skills?" — Start with highly structured formats like Think-Pair-Share
    * "How do I manage groups that finish at different rates?" — Look for extension elements in the examples
    
    **Extension Activity:**
    
    Have participants identify one example that most closely aligns with their teaching needs, then modify it by:
    1. Changing the content to match their current unit
    2. Adjusting the structure to suit their students' collaboration readiness
    3. Adding specific elements to address challenges they've encountered with collaboration
    
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