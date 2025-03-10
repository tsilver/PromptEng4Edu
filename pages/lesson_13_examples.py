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
    page_title="Lesson 13: Examples",
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
    "title": "Lesson Planning and Assessment Creation: Examples",
    "lesson": "13",
    "section": "examples",
    "order": 2
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_13_examples"
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
    "lesson_13_examples",
    "examples",
    "Lesson Planning and Assessment Creation: Examples",
    """
    **This section provides practical examples of prompt engineering for curriculum development.**
    
    You'll see:
    - Real-world prompts for creating effective lesson plans
    - Examples of assessment generation using different techniques
    - Approaches for differentiating instruction through prompting
    - Applications of the PTC-FREI framework to curriculum tasks
    
    These examples demonstrate how to apply the techniques you've learned to create
    high-quality educational materials efficiently.
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
    st.markdown("## Practical Examples: Lesson Planning and Assessment Creation")
    
    st.markdown("""
    The following examples demonstrate how to use prompt engineering techniques to create
    effective lesson plans and assessments for various educational contexts.
    """)
    
    # Example 1: Elementary Lesson Plan
    st.markdown("### Example 1: Creating an Elementary Lesson Plan")
    
    st.markdown("""
    **Prompt Engineering Goal:** Generate a comprehensive, standards-aligned lesson plan for elementary science
    
    **Techniques Used:**
    - PTC-FREI Framework (complete application)
    - Role Prompting
    - Format Specification
    """)
    
    with st.expander("View the Detailed Prompt"):
        st.markdown("""
        ```
        [Persona] Act as an experienced elementary science teacher with expertise in inquiry-based learning 
        and a focus on engaging diverse learners through hands-on activities.
        
        [Task] Create a complete lesson plan on the water cycle for 3rd-grade students.
        
        [Context] This class has 24 students, including 4 English language learners and 3 students with IEPs 
        for reading support. They have prior knowledge about states of matter but haven't formally studied 
        the water cycle. The school has basic science supplies and access to tablets (1:3 ratio).
        
        [Format] Structure the lesson plan using the 5E instructional model with the following sections:
        
        1. LESSON OVERVIEW
           - Title
           - Grade level
           - Duration
           - Standards addressed (use NGSS 3-ESS2-1)
           - Objectives (use measurable language)
           - Key vocabulary
           - Materials needed
        
        2. ENGAGE (5-7 minutes)
           - Hook activity to capture interest
           - Connection to prior knowledge
        
        3. EXPLORE (15-20 minutes)
           - Hands-on investigation
           - Student-centered activity
           - Guiding questions
        
        4. EXPLAIN (10-15 minutes)
           - Key concepts and vocabulary introduction
           - Visual aids or demonstrations
           - Student sense-making opportunities
        
        5. ELABORATE (15-20 minutes)
           - Extension activity
           - Real-world connections
        
        6. EVALUATE (10 minutes)
           - Formative assessment strategy
           - Success criteria
        
        7. DIFFERENTIATION
           - Modifications for ELLs
           - Modifications for students needing extra support
           - Extensions for students needing extra challenge
        
        [Reference] Align with NGSS Standard 3-ESS2-1: "Represent data in tables and graphical displays to 
        describe typical weather conditions expected during a particular season."
        ```
        """)
    
    st.markdown("""
    **What Makes This Prompt Effective:**
    
    1. **Comprehensive Persona Specification**: Defines an experienced teacher with specific pedagogical approaches (inquiry-based learning, hands-on activities)
    
    2. **Detailed Context**: Provides essential information about student characteristics, resources, and prior knowledge
    
    3. **Structured Format**: Uses a specific instructional model (5E) with clear sections and time allocations
    
    4. **Standards Integration**: References a specific NGSS standard to ensure alignment
    
    5. **Differentiation Requirements**: Explicitly requests modifications for diverse learners
    
    **Result:** This prompt generates a complete, well-structured lesson plan that follows the 5E model, aligns with standards, and includes differentiation strategies. The detailed specifications ensure the plan is practical and classroom-ready.
    """)
    
    # Example 2: Secondary Assessment
    st.markdown("### Example 2: Creating a Secondary Social Studies Assessment")
    
    st.markdown("""
    **Prompt Engineering Goal:** Generate a varied assessment with questions at different cognitive levels
    
    **Techniques Used:**
    - Few-Shot Prompting
    - Chain-of-Thought Specification
    - PTC-FREI Framework (partial application)
    """)
    
    with st.expander("View the Detailed Prompt"):
        st.markdown("""
        ```
        Create a comprehensive assessment for a high school World History unit on the Industrial Revolution. 
        
        The assessment should include questions at different cognitive levels (knowledge, comprehension, 
        application, analysis, evaluation, and creation) and should measure students' understanding of:
        
        - Causes of the Industrial Revolution
        - Major technological innovations and their impacts
        - Social and economic changes resulting from industrialization
        - Working conditions and reform movements
        - Global spread and effects of industrialization
        
        Include the following question types:
        1. 5 multiple-choice questions
        2. 3 short answer questions
        3. 1 document analysis with primary source
        4. 1 extended response essay
        
        For each question, indicate:
        - The cognitive level being assessed
        - The specific learning objective addressed
        - An ideal response or scoring rubric
        
        Here are examples of questions at different cognitive levels to guide your response:
        
        KNOWLEDGE LEVEL EXAMPLE:
        Question: When did the Industrial Revolution begin in Great Britain?
        A) 1650-1700
        B) 1750-1800
        C) 1800-1850
        D) 1850-1900
        Cognitive Level: Knowledge/Recall
        Learning Objective: Students will identify the time period of the Industrial Revolution.
        Answer: B) 1750-1800
        
        ANALYSIS LEVEL EXAMPLE:
        Question: Analyze how the steam engine transformed both manufacturing and transportation during the Industrial Revolution. Provide specific examples of its application in each area and explain the resulting economic impacts.
        Cognitive Level: Analysis
        Learning Objective: Students will analyze the relationship between technological innovation and economic change.
        Ideal Response: [Include elements that should be present in a strong response]
        
        For the document analysis question, include step-by-step instructions for students on how to approach analyzing the primary source.
        ```
        """)
    
    st.markdown("""
    **What Makes This Prompt Effective:**
    
    1. **Clear Specifications**: Outlines exactly what types of questions are needed
    
    2. **Few-Shot Examples**: Provides models of questions at different cognitive levels
    
    3. **Request for Meta-Information**: Asks for cognitive levels, objectives, and scoring guidelines for each question
    
    4. **Chain-of-Thought Element**: Requests step-by-step instructions for the document analysis
    
    5. **Content Framework**: Outlines the key topics that should be covered in the assessment
    
    **Result:** This prompt generates a well-balanced assessment that measures understanding across all cognitive levels and provides clear guidance for scoring. The few-shot examples ensure the AI understands the different question types needed.
    """)
    
    # Example 3: Differentiated Materials
    st.markdown("### Example 3: Creating Differentiated Math Activities")
    
    st.markdown("""
    **Prompt Engineering Goal:** Generate tiered activities for a diverse math classroom
    
    **Techniques Used:**
    - Role Prompting
    - Context Specification
    - Format Requirements
    """)
    
    with st.expander("View the Detailed Prompt"):
        st.markdown("""
        ```
        Act as a mathematics instruction specialist who has expertise in differentiation and 
        Universal Design for Learning principles.
        
        Create a set of 3 tiered activities for teaching the concept of fractions to a 4th-grade 
        class with diverse learning needs. The class includes students working below grade level, 
        at grade level, and above grade level.
        
        The specific learning objective is: "Students will represent fractions with denominators of 
        2, 3, 4, 6, and 8 using visual models and explain the relationship between the numerator 
        and denominator."
        
        For each tier, please create:
        
        TIER 1 (FOUNDATIONAL LEVEL):
        - A concrete, hands-on activity using manipulatives
        - Step-by-step instructions for implementation
        - Key questions to guide understanding
        - Success criteria for this level
        - Visual supports needed
        
        TIER 2 (GRADE LEVEL):
        - A representational activity that bridges concrete and abstract understanding
        - Required materials and setup
        - Anticipated misconceptions and how to address them
        - Extension questions
        - Success criteria for this level
        
        TIER 3 (ADVANCED LEVEL):
        - A challenging activity that applies fraction concepts to solve problems
        - Higher-order thinking questions
        - Connections to real-world applications
        - Opportunities for student choice/creativity
        - Success criteria for this level
        
        For all activities, specify:
        - Time required
        - Grouping strategy (individual, pairs, small groups)
        - Assessment approach
        - Specific accommodations for ELLs and students with learning disabilities
        
        Format each tier as a separate, clearly labeled section with all components organized under clear headings.
        ```
        """)
    
    st.markdown("""
    **What Makes This Prompt Effective:**
    
    1. **Expert Persona**: Specifies a role with expertise in both the subject matter and differentiation
    
    2. **Clear Learning Objective**: Provides a specific, measurable objective aligned with grade-level standards
    
    3. **Structured Tiering**: Requests three clearly defined levels with specific components for each
    
    4. **Comprehensive Elements**: Includes implementation details, materials, and assessment approaches
    
    5. **Inclusive Design**: Explicitly requests accommodations for diverse learners
    
    **Result:** This prompt generates a complete set of differentiated activities that meet the needs of all students while targeting the same core learning objective. The detailed specifications ensure the activities are practical, well-scaffolded, and appropriate for different learning profiles.
    """)
    
    # Example 4: Formative Assessment Tools
    st.markdown("### Example 4: Creating a Formative Assessment Toolkit")
    
    st.markdown("""
    **Prompt Engineering Goal:** Generate diverse formative assessment strategies with implementation guides
    
    **Techniques Used:**
    - Task Specification
    - Format Requirements
    - Chain-of-Thought Elements
    """)
    
    with st.expander("View the Detailed Prompt"):
        st.markdown("""
        ```
        Create a toolkit of 5 diverse formative assessment strategies that middle school teachers 
        can use across different subject areas. For each assessment strategy, provide:
        
        1. NAME AND BRIEF DESCRIPTION
           - Clear, descriptive title
           - 1-2 sentence overview of what the strategy involves
        
        2. IMPLEMENTATION GUIDE
           - Step-by-step instructions for setting up and facilitating
           - Time required (preparation and class time)
           - Materials needed
           - Digital/remote options if applicable
        
        3. SAMPLE PROMPTS
           - 3 example prompts that could be used with the strategy
           - One each for ELA, science, and social studies
        
        4. DATA COLLECTION METHOD
           - How to capture student responses efficiently
           - What to look for as evidence of understanding
           - Example of how to track results
        
        5. FOLLOW-UP ACTIONS
           - How to use the results to inform teaching
           - Suggestions for interventions based on different outcomes
           - Connection to summative assessment
        
        The 5 strategies should include:
        - At least one strategy using visual representation
        - At least one discussion-based strategy
        - At least one strategy using technology
        - At least one strategy that can be completed in under 5 minutes
        - At least one strategy that involves peer feedback
        
        Format each strategy as a separate two-column table with category names in the left column 
        and detailed content in the right column.
        ```
        """)
    
    st.markdown("""
    **What Makes This Prompt Effective:**
    
    1. **Specific Requirements**: Clearly defines the five types of strategies needed
    
    2. **Comprehensive Structure**: Outlines five key components for each strategy
    
    3. **Cross-Curricular Application**: Requests examples across multiple subject areas
    
    4. **Implementation Focus**: Emphasizes practical details and ease of classroom use
    
    5. **Instructional Cycle Connection**: Includes using results to inform teaching decisions
    
    **Result:** This prompt generates a practical toolkit of diverse formative assessment strategies that teachers can immediately implement across subject areas. The detailed structure ensures each strategy is accompanied by clear guidance for implementation, data collection, and instructional response.
    """)
    
    # Example 5: Curriculum Unit Planning
    st.markdown("### Example 5: Planning a Cross-Curricular Unit")
    
    st.markdown("""
    **Prompt Engineering Goal:** Generate an integrated unit plan connecting multiple subject areas
    
    **Techniques Used:**
    - PTC-FREI Framework (complete application)
    - Role Prompting with Multiple Perspectives
    - Reference Materials Integration
    """)
    
    with st.expander("View the Detailed Prompt"):
        st.markdown("""
        ```
        [Persona] Act as a curriculum design team consisting of an ELA specialist, a science specialist, 
        and an educational technology coach collaborating on an integrated unit.
        
        [Task] Create a 2-week cross-curricular unit plan for 8th grade connecting English Language Arts 
        and Science through the theme of "Human Impact on the Environment."
        
        [Context] The school uses block scheduling (70-minute periods), has a 1:1 Chromebook program, 
        and serves students from diverse socioeconomic backgrounds. Teachers want to incorporate 
        project-based learning approaches and authentic assessment. The unit will culminate in students 
        creating multimedia presentations about local environmental issues.
        
        [Format] Structure the unit plan as follows:
        
        1. UNIT OVERVIEW
           - Title
           - Essential Questions
           - Enduring Understandings
           - Standards Addressed (include both ELA and Science standards)
           - Unit Objectives
           - Key Vocabulary
           - Culminating Assessment Description
        
        2. SCOPE AND SEQUENCE
           - Create a day-by-day outline of lessons across the 2-week period
           - For each day, specify:
             * Learning targets
             * Key activities (including which subject areas are integrated)
             * Formative assessments
             * Materials/resources needed
        
        3. DETAILED LESSON PLANS
           - Provide 3 detailed sample lesson plans from different points in the unit
           - Each lesson plan should include:
             * Objectives
             * Standards addressed
             * Instructional sequence with timing
             * Differentiation strategies
             * Formative assessment approach
             * Digital tools integration
        
        4. RESOURCES LIST
           - List of texts (fiction and nonfiction)
           - Digital resources and tools
           - Materials for hands-on activities
           - Assessment tools and rubrics
        
        5. EXTENSION AND SUPPORT OPTIONS
           - Strategies for students who need additional challenges
           - Support systems for struggling learners
           - Home-school connections
        
        [Reference] Use the following standards:
        CCSS.ELA-LITERACY.RI.8.1: Cite textual evidence that supports analysis of what the text says
        CCSS.ELA-LITERACY.W.8.1: Write arguments to support claims with clear reasons and evidence
        CCSS.ELA-LITERACY.SL.8.5: Integrate multimedia and visual displays into presentations
        MS-ESS3-3: Apply scientific principles to design a method for monitoring and minimizing human impact
        MS-ESS3-4: Construct an argument supported by evidence for how increases in human population and consumption impact Earth's systems
        
        Each specialist should contribute perspective from their area of expertise throughout the unit.
        ```
        """)
    
    st.markdown("""
    **What Makes This Prompt Effective:**
    
    1. **Collaborative Persona**: Specifies a team of specialists with different expertise areas
    
    2. **Integrated Approach**: Clearly defines how subject areas should connect through a thematic lens
    
    3. **Comprehensive Format**: Outlines a complete unit structure with all necessary components
    
    4. **Standards Integration**: Includes specific standards from multiple disciplines to ensure alignment
    
    5. **Authentic Assessment**: Incorporates project-based learning and real-world application
    
    **Result:** This prompt generates a comprehensive, integrated unit plan that meaningfully connects ELA and Science standards through a relevant environmental theme. The detailed specifications ensure the unit includes daily plans, sample lessons, and necessary resources while maintaining coherence across subject areas.
    """)
    
    # Summary of Strategies
    st.markdown("## Key Prompt Design Strategies for Curriculum Development")
    
    st.markdown("""
    From these examples, we can identify several effective prompt design strategies for creating
    lesson plans and assessments:
    
    ### 1. Be Specific About Format and Structure
    - Specify the exact template or model you want followed
    - Include section headers, time allocations, and required elements
    - Request specific components for each section
    
    ### 2. Include Relevant Educational Details
    - Describe student demographics and learning needs
    - Specify available resources and technologies
    - Include time constraints and scheduling information
    - Reference appropriate standards and learning objectives
    
    ### 3. Request Implementation Guidance
    - Ask for step-by-step instructions
    - Request anticipated challenges and solutions
    - Include materials lists and preparation notes
    - Specify assessment approaches and success criteria
    
    ### 4. Prioritize Differentiation and Inclusion
    - Explicitly request modifications for diverse learners
    - Ask for tiered activities or multilevel assessments
    - Include accommodations for specific learning needs
    - Request both support and extension options
    
    ### 5. Balance Structure and Flexibility
    - Provide clear parameters while allowing for creativity
    - Request options that can be adapted to different contexts
    - Include rationales for instructional decisions
    - Ask for modification suggestions for different scenarios
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Key Points to Emphasize:**
    
    * These examples can be modified to match specific grade levels, subject areas, and instructional approaches
    * The level of detail in the prompts corresponds directly to the specificity of the output - vague prompts produce generic materials
    * Curriculum development prompts work best when they incorporate your specific teaching context and student needs
    * These techniques are particularly valuable for collaborative planning, as they provide consistent structures that teams can build upon
    
    **Discussion Questions:**
    
    * Which of these example prompts could be most immediately useful in your context?
    * How might you adapt these templates for your specific grade level or subject area?
    * What components would you add or modify based on your school's curriculum requirements?
    * How could these prompting techniques support curriculum alignment across grade levels or departments?
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