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
    page_title="Lesson 15: Examples",
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
    "title": "Discussion Questions and Content Creation: Examples",
    "lesson": "15",
    "section": "examples",
    "order": 2
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_15_examples"
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
    "lesson_15_examples",
    "examples",
    "Lesson 15: Examples",
    """
    **This section provides examples of effective prompts for discussion questions and content creation.**
    
    Each example demonstrates how to:
    - Structure prompts using the PCTFR framework
    - Target specific cognitive levels and learning objectives
    - Create materials that engage diverse learners
    - Generate different types of instructional content
    
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
    Below are examples of well-crafted prompts for creating discussion questions and instructional 
    content across various subjects and grade levels. Each example includes an analysis of the 
    prompt's key elements and what makes it effective.
    """)
    
    # Section 1: Discussion Question Examples
    st.markdown("## Discussion Question Examples")
    
    # Example 1: Literature Discussion Questions
    st.markdown("### Example 1: Literature Discussion Questions")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as an experienced high school literature teacher who specializes in facilitating 
    student-led discussions using the Socratic method.
    
    Context: I'm teaching George Orwell's "1984" to 11th-grade students. We've just completed reading 
    Part 1 of the novel (Chapters 1-8), where Winston begins his rebellion by writing in his diary, 
    meets Julia, and starts to question the Party's control.
    
    Task: Create a sequence of discussion questions for a 45-minute Socratic seminar that explores 
    themes of surveillance, individuality, truth, and psychological manipulation.
    
    Format: Provide 10-12 questions organized into three categories:
    1. Opening questions (2-3 accessible questions to get all students engaged)
    2. Core analysis questions (6-7 questions exploring key scenes, characters, and themes)
    3. Connecting questions (2-3 questions linking the text to contemporary issues or other texts)
    
    Include brief notes on the purpose of each question and possible follow-up questions if students 
    need prompting. Also note which questions align with higher-order thinking skills from Bloom's 
    Taxonomy.
    
    Reference Materials: Key scenes from Part 1 include Winston's first act of rebellion (writing in 
    the diary), the Two Minutes Hate, interactions with O'Brien, the existence of the telescreen, 
    Winston's job rewriting history at the Ministry of Truth, and his early encounters with Julia. 
    Important symbols include the telescreen, the glass paperweight, and the diary. The novel was 
    published in 1949, after World War II and during the rise of totalitarian states.
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Strong Persona Definition:**
        - Specifies expertise in Socratic method
        - Sets clear instructional approach
        - Establishes educational philosophy
        
        **Detailed Context:**
        - Identifies specific text and chapters
        - Notes where students are in the learning sequence
        - Establishes what content students have encountered
        
        **Clear Task Description:**
        - Specifies type of activity (Socratic seminar)
        - Sets time parameters (45 minutes)
        - Identifies key themes to explore
        """)
    
    with col2:
        st.markdown("""
        **Structured Format:**
        - Organizes questions into logical categories
        - Requests specific number of questions
        - Asks for pedagogical notes on question purpose
        - Includes request for differentiation strategy (follow-ups)
        
        **Comprehensive Reference Materials:**
        - Lists key scenes students have encountered
        - Identifies important symbols and themes
        - Provides historical context for the work
        - Helps ensure questions will be text-based
        """)
    
    # Example 2: Elementary Science Discussion Questions
    st.markdown("### Example 2: Elementary Science Discussion Questions")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as an elementary science specialist who uses inquiry-based methods and focuses on 
    developing scientific thinking skills in young learners.
    
    Context: I'm teaching a unit on habitats and ecosystems to 3rd-grade students. We've completed 
    lessons on basic ecosystem components (producers, consumers, decomposers) and have observed our 
    classroom terrarium for two weeks, recording changes.
    
    Task: Create discussion questions that will guide students in analyzing their terrarium observations 
    and developing understanding of ecosystem interactions.
    
    Format: Provide three sets of questions:
    1. Observation Questions (4-5 questions focusing on what students have observed, using scientific 
       language of producers/consumers/decomposers)
    2. Relationship Questions (3-4 questions exploring how different organisms in the terrarium interact)
    3. Prediction Questions (2-3 questions asking students to predict what might happen next in the 
       terrarium and why)
    
    For each question, indicate the thinking skill it targets (observation, inference, comparison, 
    prediction) and provide a simple visual cue (emoji) that I can use when displaying these questions.
    
    Reference Materials: Our classroom terrarium contains small plants (grass, moss), isopods (roly-polies), 
    earthworms, and leaf litter. Students have observed plant growth, isopod movement, and decomposition of 
    leaves. The unit's vocabulary includes: habitat, ecosystem, producer, consumer, decomposer, food chain, 
    interdependence, and adaptation. NGSS standard 3-LS4-3 focuses on organisms' adaptations to survival 
    in particular habitats.
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Age-Appropriate Persona:**
        - Specifies elementary education expertise
        - Emphasizes inquiry-based approaches
        - Focuses on developing scientific thinking
        
        **Clear Instructional Context:**
        - Identifies prior knowledge (producers, consumers)
        - References specific classroom activity (terrarium)
        - Establishes time frame of learning (two weeks)
        
        **Developmentally Appropriate Task:**
        - Connects discussion to hands-on observation
        - Builds on concrete experience
        - Focuses on analysis appropriate for grade level
        """)
    
    with col2:
        st.markdown("""
        **Structured Question Format:**
        - Organizes by cognitive process (observe → relate → predict)
        - Requests specific number of questions for each category
        - Includes visual supports (emoji cues) for young learners
        
        **Specific Reference Materials:**
        - Details actual terrarium contents
        - Lists vocabulary students are familiar with
        - Connects to relevant science standards
        - Ensures questions will build on students' experience
        """)
    
    # Section 2: Content Creation Examples
    st.markdown("## Instructional Content Examples")
    
    # Example 3: Math Guided Notes
    st.markdown("### Example 3: Math Guided Notes")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as a middle school math curriculum specialist who designs structured yet engaging materials 
    for diverse learners with a focus on conceptual understanding.
    
    Context: I'm teaching a 7th-grade unit on proportional relationships. Students have already learned 
    to identify proportional relationships in tables and graphs, but they struggle with writing and solving 
    proportional equations, especially when the unit rate isn't explicitly given.
    
    Task: Create a guided notes template that helps students develop a step-by-step process for writing 
    proportional equations in the form y = kx, identifying the constant of proportionality (k), and using 
    these equations to solve problems.
    
    Format: Design a 2-page guided notes document with:
    1. A clear title and learning objective
    2. Key vocabulary with space for student definitions
    3. Step-by-step procedure for finding the constant of proportionality and writing an equation
    4. 2-3 worked examples with some solution steps partially completed for students to fill in
    5. 2-3 practice problems with scaffolded guidance
    6. A visual representation of proportional relationships (graph, table, and equation)
    7. A self-check section for students to assess their understanding
    
    Include strategic blank spaces for student note-taking and problem-solving. Use a mix of representation
    types (words, symbols, tables, graphs) to support different learning modalities. Add margin notes for
    common misconceptions or helpful hints.
    
    Reference Materials: The guided notes should align with Common Core Standard 7.RP.2: "Recognize and 
    represent proportional relationships between quantities." Students have been working with contexts like 
    unit pricing, constant speed, and recipe conversions. Common misconceptions include confusing the constant 
    of proportionality with the y-coordinate and setting up incorrect ratios.
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Specialized Persona:**
        - Specifies middle school math expertise
        - Emphasizes conceptual understanding
        - Notes focus on diverse learners
        
        **Detailed Learning Context:**
        - Identifies prior knowledge and skills
        - Notes specific student challenges
        - Establishes clear learning progression
        
        **Targeted Content Task:**
        - Specifies exact content to be created (guided notes)
        - Focuses on specific skill development
        - Addresses identified student needs
        """)
    
    with col2:
        st.markdown("""
        **Comprehensive Format Specification:**
        - Outlines exact components needed
        - Specifies length and structure
        - Requests multiple representation types
        - Includes metacognitive elements (self-check)
        
        **Specific Reference Materials:**
        - Cites exact learning standard
        - Lists relevant application contexts
        - Identifies common misconceptions
        - Ensures content will address learning gaps
        """)
    
    # Example 4: History Case Study
    st.markdown("### Example 4: History Case Study")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as a high school history teacher who uses primary sources and case studies to help 
    students develop critical analysis skills and understand multiple perspectives on historical events.
    
    Context: I'm teaching a unit on the Civil Rights Movement to 10th-grade students. We've covered the 
    broad timeline and major figures, but students need to develop deeper understanding of specific events 
    and the various tactics used by activists.
    
    Task: Create a case study on the Greensboro Lunch Counter Sit-Ins of 1960 that helps students analyze 
    the effectiveness of nonviolent direct action as a strategy for social change.
    
    Format: Design a 3-4 page case study packet that includes:
    1. An engaging introduction that provides historical context for the Greensboro sit-ins
    2. A timeline of key events from the first sit-in through the desegregation of the Woolworth lunch counter
    3. Short excerpts (100-150 words each) from primary sources representing multiple perspectives:
       - A participant in the sit-ins
       - A Woolworth's employee or manager
       - A local newspaper editorial
       - A statement from a civil rights organization
    4. A graphic organizer for students to analyze each source for perspective, motivation, and reliability
    5. Discussion questions that guide students in evaluating the effectiveness of the sit-in strategy
    6. An extension activity that asks students to compare this tactic to other civil rights strategies
    
    The case study should present multiple perspectives while remaining historically accurate and aligned 
    with scholarly consensus about the significance and impact of the Greensboro sit-ins.
    
    Reference Materials: The Greensboro sit-ins began on February 1, 1960, when four North Carolina A&T 
    students (Ezell Blair Jr., David Richmond, Franklin McCain, and Joseph McNeil) sat at a whites-only 
    lunch counter at Woolworth's. The protests spread to other locations and continued for months until 
    Woolworth's desegregated the lunch counter on July 25, 1960. The sit-ins inspired similar protests 
    across the South and led to the formation of the Student Nonviolent Coordinating Committee (SNCC). 
    This case study should connect to our unit's essential question: "What factors make different methods 
    of pursuing social change effective or ineffective in different contexts?"
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Focused Pedagogical Persona:**
        - Emphasizes primary source analysis
        - Establishes multiple-perspectives approach
        - Sets critical thinking as a priority
        
        **Clear Instructional Context:**
        - Notes what has already been covered
        - Identifies specific learning needs
        - Places lesson within larger unit
        
        **Focused Historical Task:**
        - Specifies exact case study topic
        - Identifies clear analytical focus
        - Targets specific historical thinking skills
        """)
    
    with col2:
        st.markdown("""
        **Detailed Format Specifications:**
        - Outlines comprehensive case study structure
        - Specifies exact components to include
        - Requests balance of information and analysis
        - Incorporates primary source analysis
        
        **Rich Reference Materials:**
        - Provides key historical details and dates
        - Identifies specific historical figures
        - Places event in broader historical context
        - Connects to unit's essential question
        """)
    
    # Example 5: Elementary Differentiated Activity
    st.markdown("### Example 5: Elementary Differentiated Activity")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as an elementary education specialist who designs inclusive, differentiated learning 
    experiences for diverse classrooms, with expertise in Universal Design for Learning principles.
    
    Context: I teach a diverse 2nd-grade classroom with students at various reading levels (from pre-primer 
    to 3rd grade), including three English language learners and two students with IEPs for reading support. 
    We're beginning a unit on community helpers and the jobs people do in our community.
    
    Task: Create a differentiated learning center activity about community helpers that can accommodate 
    multiple readiness levels while ensuring all students work toward the same core learning objectives.
    
    Format: Design a learning center activity with:
    1. A clear title and visual instructions
    2. Core learning objectives for all students
    3. Materials list with preparation instructions
    4. Basic instructions for the activity
    5. Three differentiated task cards or pathways:
       - Tier 1: For students reading below grade level
       - Tier 2: For students reading at grade level
       - Tier 3: For students reading above grade level
    6. Visual supports and scaffolds for English language learners
    7. An assessment component to check for understanding
    8. Extension questions for early finishers
    
    Each tier should use the same core materials and address the same learning objectives but adjust 
    the complexity, abstraction, and support level appropriately. Include a brief teacher guide explaining 
    how to introduce the center and manage students working at different levels.
    
    Reference Materials: The unit's core objectives focus on:
    - Identifying different jobs in the community
    - Understanding how community helpers contribute to meeting our needs
    - Connecting job responsibilities to necessary skills and tools
    Key community helpers we're focusing on include: firefighters, teachers, doctors, postal workers, 
    sanitation workers, and grocery store employees. The activity should align with social studies 
    standard SS.2.4: "Describe the roles and responsibilities of people in various jobs and how they 
    contribute to the community."
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Specialized Inclusive Persona:**
        - Specifies elementary education expertise
        - Emphasizes Universal Design for Learning
        - Focuses on inclusive, differentiated practices
        
        **Detailed Classroom Context:**
        - Describes specific student population
        - Provides reading level ranges
        - Notes presence of ELLs and IEP students
        
        **Clear Instructional Task:**
        - Specifies learning center format
        - Focuses on specific content area
        - Emphasizes differentiation needs
        """)
    
    with col2:
        st.markdown("""
        **Comprehensive Format Structure:**
        - Outlines all learning center components
        - Specifies three-tiered differentiation
        - Requests specific supports for ELLs
        - Includes assessment component
        
        **Relevant Reference Materials:**
        - Lists specific learning objectives
        - Identifies key content (community helpers)
        - Cites relevant academic standards
        - Ensures targeted skill development
        """)
    
    # Example 6: Complete PCTFR Example for Inquiry-Based Science 
    st.markdown("### Example 6: Inquiry-Based Science Investigation")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as an experienced middle school science curriculum developer who specializes in 
    inquiry-based learning, with expertise in designing hands-on investigations that develop scientific 
    practices and critical thinking.
    
    Context: I'm planning a unit on weather patterns and climate for 6th grade students who have basic 
    understanding of the water cycle but limited experience with data analysis and scientific investigation. 
    Our school has access to basic weather tools (thermometers, barometers, anemometers) and computers for 
    accessing online weather data.
    
    Task: Create a multi-day inquiry investigation that guides students in collecting and analyzing local 
    weather data to identify patterns and make predictions. The investigation should develop students' 
    skills in data collection, graphing, pattern recognition, and evidence-based reasoning.
    
    Format: Design a 5-day investigation plan that includes:
    1. Daily learning objectives and connections to science practices
    2. Step-by-step procedures for data collection and analysis
    3. Data recording sheets with scaffolded prompts
    4. Guiding questions for each stage of the investigation
    5. Visual supports (diagrams, examples of completed graphs)
    6. Extensions for advanced students
    7. Modifications for struggling learners
    8. Formative assessment checkpoints
    9. A culminating task where students create evidence-based weather predictions
    
    The investigation should follow a 5E instructional model (Engage, Explore, Explain, Elaborate, 
    Evaluate) with clear transitions between phases. Include teacher notes for facilitation, common 
    misconceptions, and safety considerations.
    
    Reference Materials: This investigation should align with NGSS MS-ESS2-5: "Collect data to provide 
    evidence for how the motions and complex interactions of air masses result in changes in weather 
    conditions." Students should develop understanding of these key concepts:
    - Weather is influenced by interactions of air masses, fronts, and pressure systems
    - Weather data can reveal patterns that allow for prediction
    - Different weather variables (temperature, pressure, humidity, wind) are interrelated
    Common student misconceptions include confusing weather and climate, assuming weather changes are 
    random rather than following patterns, and misunderstanding the relationship between air pressure 
    and weather conditions.
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Comprehensive Persona:**
        - Specifies middle school science expertise
        - Emphasizes inquiry-based methodology
        - Notes focus on hands-on learning and scientific practices
        
        **Detailed Educational Context:**
        - Identifies student prior knowledge
        - Notes available resources and tools
        - Establishes skill development priorities
        
        **Clearly Defined Task:**
        - Specifies multi-day investigation format
        - Identifies specific scientific skills to develop
        - Sets clear learning progression
        """)
    
    with col2:
        st.markdown("""
        **Structured Format Specification:**
        - Organizes by 5E instructional model
        - Outlines comprehensive components
        - Includes differentiation for multiple learners
        - Incorporates formative assessment
        
        **Comprehensive Reference Materials:**
        - Cites specific NGSS standard
        - Lists key scientific concepts
        - Identifies common misconceptions
        - Ensures content accuracy and alignment
        """)
    
    # Key Takeaways Section
    st.markdown("## Key Takeaways from Examples")
    
    st.markdown("""
    ### Effective Prompts for Discussion Questions:
    
    * **Target specific cognitive levels** (factual, analytical, evaluative)
    * **Structure questions in logical progressions** (opening → core → connecting)
    * **Request multiple categories of questions** for diverse learning needs
    * **Include notes on question purpose** and follow-up strategies
    * **Ground questions in specific content** or student experiences
    * **Differentiate questions** for various student readiness levels
    
    ### Effective Prompts for Instructional Content:
    
    * **Specify exact format and components** of the desired content
    * **Request built-in scaffolding and differentiation**
    * **Include reference to standards and learning objectives**
    * **Acknowledge student misconceptions and learning challenges**
    * **Request visual supports and multiple representations**
    * **Ask for assessment components** to check for understanding
    
    ### The Power of the PCTFR Framework:
    
    * **Persona:** Defines the educational approach and expertise lens
    * **Context:** Establishes student needs, prior knowledge, and available resources
    * **Task:** Specifies exactly what type of content you need
    * **Format:** Provides detailed structure for the requested materials
    * **Reference Materials:** Ensures accuracy and alignment with standards and objectives
    
    In the next section, you'll have the opportunity to practice creating your own prompts for 
    discussion questions and instructional content.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Encourage participants to compare these examples to their current approaches for creating discussion questions and content
    * Point out how the prompts become more specific and detailed for more complex content
    * Emphasize that these prompts create starting points that teachers should always review and refine
    * Highlight how the PCTFR framework adapts to different content areas and grade levels
    
    **Common Questions:**
    
    * "How much detail is too much in a prompt?" — Balance is important; start with more detail until you find what works
    * "What if the AI doesn't understand my subject area terminology?" — Include definitions or examples of specialized terms
    * "How do I ensure the content matches my teaching style?" — Include examples of your preferred approach in the prompt
    
    **Extension Activity:**
    
    Have participants identify one example that most closely aligns with their teaching needs, then modify it by:
    1. Changing the subject/topic to their own
    2. Adjusting the format specifications to match their preferred structure
    3. Updating reference materials to reflect their curriculum standards
    
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