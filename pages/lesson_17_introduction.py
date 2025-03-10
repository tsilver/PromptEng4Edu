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
    page_title="Lesson 17: Introduction",
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
    "title": "Personalized Learning Pathways: Introduction",
    "lesson": "17",
    "section": "introduction",
    "order": 1
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_17_introduction"
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
    "lesson_17_introduction",
    "introduction",
    "Lesson 17: Personalized Learning Pathways",
    """
    **Welcome to Lesson 17: Personalized Learning Pathways!**
    
    In this lesson, you'll learn how to:
    - Use prompt engineering to design personalized learning experiences
    - Create differentiated learning pathways based on student needs
    - Develop adaptive content that responds to individual progress
    - Generate learning materials that accommodate various preferences and styles
    
    Start with this introduction to understand the key concepts before moving to examples and hands-on activities.
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
    
    # Introduction
    st.markdown("""
    ## Designing Effective Personalized Learning Pathways
    
    Personalized learning is an educational approach that tailors instruction, content, and pacing to 
    individual student needs, preferences, and goals. When designed effectively, personalized learning 
    increases engagement, addresses learning gaps, and promotes student agency. In this lesson, we'll 
    explore how prompt engineering can help you create high-quality personalized learning experiences 
    efficiently.
    """)
    
    # Why This Matters
    st.markdown("""
    ## Why This Matters
    
    Effective personalized learning offers numerous benefits:
    
    * **Addresses diverse learning needs** by adapting instruction to individual readiness levels
    * **Increases student engagement** through relevant, appropriately challenging content
    * **Promotes student agency** by offering choices and building metacognitive skills
    * **Optimizes learning time** by focusing on each student's specific needs
    * **Supports mastery-based progression** rather than time-based advancement
    * **Builds persistence and self-regulation** through appropriate scaffolding and feedback
    
    However, personalized learning can be challenging to implement due to the significant time 
    required to create multiple pathways and resources. Prompt engineering helps address this 
    challenge by enabling you to efficiently generate differentiated materials and adaptive pathways.
    """)
    
    # Components of Personalized Learning
    st.markdown("""
    ## Key Components of Personalized Learning
    
    Personalized learning encompasses several interrelated components:
    
    ### 1. Learner Profiles
    
    Comprehensive understanding of each student's:
    - Academic strengths and needs
    - Learning preferences and interests
    - Background knowledge and experiences
    - Social-emotional factors
    - Goals and aspirations
    
    ### 2. Flexible Learning Paths
    
    Multiple routes to mastery that include:
    - Variable pacing appropriate to student needs
    - Different entry points based on readiness
    - Multiple representations of content
    - Choice in how to demonstrate learning
    - Adaptive sequencing based on performance
    
    ### 3. Competency-Based Progression
    
    Advancement based on demonstrated mastery:
    - Clear learning targets and success criteria
    - Ongoing formative assessment
    - Multiple opportunities to demonstrate learning
    - Feedback focused on improvement
    - Flexible timing for assessment
    
    ### 4. Flexible Learning Environments
    
    Settings that support personalization:
    - Physical spaces that accommodate different learning modes
    - Time structures that allow for variable pacing
    - Grouping strategies based on needs and goals
    - Technology integration to support individual paths
    - Resource allocation aligned with student needs
    """)
    
    # Personalization Dimensions
    st.markdown("""
    ## Dimensions of Personalization
    
    When designing personalized learning experiences, consider these key dimensions along which content, 
    instruction, and assessment can be personalized:
    
    | Dimension | Description | Examples |
    | --- | --- | --- |
    | **Content** | What students learn | Reading level, complexity, topics, contexts, cultural relevance |
    | **Process** | How students learn | Instructional strategies, grouping, pacing, degree of guidance |
    | **Product** | How students demonstrate learning | Format, complexity, presentation mode, degree of scaffolding |
    | **Environment** | Where and when learning occurs | Physical space, time allocation, resources, technology |
    | **Pathway** | Sequence and progression | Prerequisite ordering, branching options, remediation loops |
    
    A comprehensive approach to personalization considers multiple dimensions rather than focusing on just one.
    """)
    
    # Approaches to Personalization
    st.markdown("""
    ## Common Approaches to Personalization
    
    Educators use various strategies to personalize learning, each with unique strengths and applications:
    
    ### 1. Differentiated Instruction
    
    **Approach:** Teacher-designed variations in content, process, and product based on student readiness, 
    interests, and learning profiles.
    
    **Example Applications:**
    - Tiered assignments with varied complexity
    - Learning centers with different entry points
    - Flexible grouping based on needs
    - Choice boards offering multiple options
    
    ### 2. Adaptive Learning
    
    **Approach:** Technology-driven systems that automatically adjust content and difficulty based on 
    student performance.
    
    **Example Applications:**
    - Adaptive digital platforms with built-in algorithms
    - Programs that provide targeted practice based on performance
    - Systems that generate personalized learning paths
    - Tools that recommend resources based on learner profile
    
    ### 3. Mastery-Based Learning
    
    **Approach:** Progress based on demonstration of specific competencies rather than time spent learning.
    
    **Example Applications:**
    - Self-paced modules with clear mastery criteria
    - Flexible assessment opportunities
    - Learning progressions with multiple paths
    - Standards-based grading systems
    
    ### 4. Project-Based Personalization
    
    **Approach:** Authentic projects that allow for student choice and differentiation within a common framework.
    
    **Example Applications:**
    - Open-ended challenges with multiple solution paths
    - Projects with student choice in topic, process, or product
    - Scaffolded independent inquiries
    - Role-based collaborative projects
    """)
    
    # Challenges in Personalized Learning Design
    st.markdown("""
    ## Common Challenges in Personalized Learning Design
    
    Despite its benefits, implementing personalized learning presents several challenges:
    
    ### 1. Resource Development Burden
    
    Creating multiple versions of learning materials, assessments, and pathways requires significant 
    time and effort, often beyond what is practical for individual teachers.
    
    ### 2. Managing Complexity
    
    Tracking student progress across diverse pathways, coordinating different learning activities, 
    and ensuring coverage of all necessary content becomes increasingly complex as personalization increases.
    
    ### 3. Balancing Structure and Flexibility
    
    Providing enough structure to guide learning while maintaining flexibility for personalization 
    requires careful design and ongoing adjustment.
    
    ### 4. Maintaining Quality and Rigor
    
    Ensuring that all pathways maintain high expectations and lead to the same rigorous learning 
    outcomes, regardless of route or pace.
    
    ### 5. Supporting Student Agency
    
    Helping students develop the metacognitive skills needed to make good choices about their 
    learning and navigate personalized pathways effectively.
    """)
    
    # Prompt Engineering for Personalized Learning
    st.markdown("""
    ## Prompt Engineering for Personalized Learning
    
    Prompt engineering can help address these challenges by generating well-designed personalized 
    learning materials, pathways, and assessments. When creating AI prompts for personalized learning, 
    consider:
    
    ### For Differentiated Content:
    
    * **Specifying learner profiles** (e.g., "Create content for students reading two years below grade level")
    * **Requesting multiple versions** at different levels or with different approaches
    * **Defining specific adaptations** (e.g., "Simplify vocabulary while maintaining key concepts")
    * **Including accessibility requirements** for diverse learners

    ### For Learning Pathway Design:
    
    * **Clarifying learning progression** with key milestones and competencies
    * **Requesting branch points** for different routes based on student performance
    * **Specifying pre-assessment strategies** to determine appropriate entry points
    * **Including guidance for navigating pathway options**
    
    ### For Adaptive Assessment:
    
    * **Requesting question banks at multiple levels** of difficulty
    * **Specifying decision rules** for adapting based on responses
    * **Including varied question formats** to accommodate different demonstration methods
    * **Requesting formative check-ins** to guide pathway adjustments
    
    ### For Supporting Student Agency:
    
    * **Including metacognitive prompts** for student reflection
    * **Requesting self-assessment tools** aligned with learning goals
    * **Designing choice frameworks** with appropriate constraints
    * **Developing goal-setting and progress-monitoring tools**
    """)
    
    # Application in the PCTFR Framework
    st.markdown("""
    ## Applying the PCTFR Framework
    
    The PCTFR framework (Persona, Context, Task, Format, Reference Materials) can be applied to
    create effective prompts for personalized learning materials:
    
    ### Example for Differentiated Reading Materials:
    
    ```
    Persona: Act as a literacy specialist who designs differentiated reading materials that maintain 
    high engagement while addressing diverse reading levels and background knowledge
    
    Context: I teach 5th grade ELA in a classroom with reading levels ranging from 2nd to 8th grade. 
    We're studying a unit on informational text about space exploration, and I need materials that all 
    students can access while learning the same key concepts and text structures.
    
    Task: Create a set of differentiated reading passages about the Mars rover missions that address 
    the same content but at three different reading levels (below grade level, at grade level, above 
    grade level). Each passage should teach the same key concepts while being appropriately accessible 
    and challenging for the target reading level.
    
    Format: Design three 1-2 page reading passages that include:
    1. The same key information about Mars rover missions and their scientific objectives
    2. Appropriate vocabulary and sentence complexity for each level
    3. Text features (headings, captions, etc.) appropriate to informational text
    4. 3-5 comprehension questions for each level that address both literal and inferential understanding
    5. A brief reading guide for each level with pre-reading activities and vocabulary support
    
    The below-grade-level passage should use simpler vocabulary, shorter sentences, more visual supports, 
    and explicit text structures. The at-grade-level passage should align with typical 5th grade text 
    complexity. The above-grade-level passage should include more technical vocabulary, complex sentence 
    structures, and higher-level concepts while still covering the same core content.
    
    Reference Materials: Key information to include: Mars rovers (Sojourner, Spirit, Opportunity, 
    Curiosity, Perseverance), their missions, important discoveries, challenges they've faced, and how 
    they help scientists learn about Mars. The reading should address standard RI.5.2 (determine two or 
    more main ideas and explain how they are supported by key details) and RI.5.4 (determine the meaning 
    of domain-specific words and phrases).
    ```
    
    ### Example for Personalized Math Pathways:
    
    ```
    Persona: Act as a mathematics curriculum designer who specializes in creating personalized learning 
    pathways that address individual student needs while ensuring mastery of essential concepts
    
    Context: I teach a mixed-ability 7th grade math class where students have significant gaps in their 
    understanding of fractions. Some students struggle with basic fraction concepts while others are 
    ready for more advanced applications. I need a personalized learning system that helps all students 
    master essential fraction operations regardless of their starting point.
    
    Task: Create a personalized learning pathway for fraction operations (addition, subtraction, 
    multiplication, division) that adapts to different student readiness levels. The pathway should 
    include appropriate entry points, formative assessments, and branching options to guide students 
    toward mastery regardless of their starting point.
    
    Format: Design a learning pathway system that includes:
    1. A diagnostic assessment to determine initial placement
    2. Three entry points (foundational, grade-level, advanced)
    3. Learning modules for each concept with:
       - Instructional content (explanations, examples, practice)
       - Formative checks to assess understanding
       - Decision points for advancement or remediation
       - Extension activities for students who demonstrate mastery
    4. Progress tracking tools for students and teacher
    5. A final assessment to verify mastery of all essential concepts
    
    Each module should include both procedural and conceptual understanding, and materials should use 
    multiple representations (visual models, numerical expressions, word problems, etc.). Include guidance 
    for how students navigate the pathway and make decisions about next steps.
    
    Reference Materials: The pathway should address standards 7.NS.1 (apply operations with fractions) 
    and 7.NS.3 (solve real-world problems with rational numbers). Key concepts include equivalent 
    fractions, common denominators, fraction-decimal-percent conversions, and operations with mixed 
    numbers. Common misconceptions include applying whole number thinking to fractions, struggles with 
    unlike denominators, and confusion about multiplication/division procedures.
    ```
    """)
    
    # Strategic Considerations
    st.markdown("""
    ## Strategic Considerations
    
    When using prompt engineering for personalized learning design:
    
    ### 1. Start with Clear Learning Goals
    
    * **Identify essential outcomes** for all students regardless of pathway
    * **Distinguish "must know" from "nice to know"** content
    * **Establish clear success criteria** for each learning target
    * **Design backward** from desired outcomes to learning activities
    
    ### 2. Balance Personalization with Practicality
    
    * **Begin with manageable levels** of differentiation (e.g., 2-3 versions rather than completely individualized)
    * **Prioritize high-impact areas** for personalization
    * **Create modular resources** that can be mixed and matched
    * **Develop templates** that streamline personalization
    
    ### 3. Incorporate Strategic Assessment
    
    * **Use pre-assessment** to determine appropriate pathways
    * **Include frequent formative checks** to guide adjustments
    * **Design flexible summative assessments** that accommodate different paths
    * **Collect evidence of learning** throughout the process
    
    ### 4. Support Student Navigation
    
    * **Provide clear guidance** for how students move through options
    * **Develop self-assessment tools** to help students make good choices
    * **Create visual representations** of learning pathways
    * **Build in reflection points** to develop metacognition
    """)
    
    # Connection to Previous and Next Lessons
    st.markdown("""
    ## Connections to Other Lessons
    
    This lesson builds on concepts from previous lessons:
    
    * **Lesson 16 (Collaborative Learning Activities)**: While collaborative learning focuses on group 
      experiences, personalized learning applies similar design principles to individual learning paths. 
      The concepts of structure, accountability, and thoughtful design transfer from group to individual contexts.
    
    * **Earlier Lessons on Prompt Engineering Techniques**: The PCTFR framework continues to provide 
      structure for creating complex, multi-faceted prompts that address diverse learning needs.
    
    In the next section, you'll see examples of effective prompts for generating various types of
    personalized learning materials and pathways across different subject areas and grade levels.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Connect this lesson to participants' existing differentiation practices
    * Acknowledge the real challenges of implementing personalization at scale
    * Emphasize that personalization exists on a spectrum—even small steps toward personalization can benefit students
    * Encourage teachers to start with one dimension of personalization before attempting to personalize everything
    
    **Discussion Prompts:**
    
    * What aspects of your teaching do you currently personalize, and what aspects are most challenging to personalize?
    * How do you currently manage the logistics of providing multiple learning paths or materials?
    * What types of data do you use to make decisions about personalization?
    
    **Extension Opportunities:**
    
    * Invite teachers to analyze a challenging concept in their curriculum and design a personalized approach
    * Suggest creating a personalized learning template that could be applied across multiple units
    * Explore how prompt engineering might support the development of learner profiles
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