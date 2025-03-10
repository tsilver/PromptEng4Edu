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
    page_title="Lesson 16: Introduction",
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
    "title": "Collaborative Learning Activities: Introduction",
    "lesson": "16",
    "section": "introduction",
    "order": 1
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_16_introduction"
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
    "lesson_16_introduction",
    "introduction",
    "Lesson 16: Collaborative Learning Activities",
    """
    **Welcome to Lesson 16: Collaborative Learning Activities!**
    
    In this lesson, you'll learn how to:
    - Use prompt engineering to design effective collaborative learning experiences
    - Create structured group activities that promote meaningful interaction
    - Develop protocols for student collaboration that maximize participation
    - Generate collaborative assessment strategies that balance individual and group accountability
    
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
    ## Designing Effective Collaborative Learning Experiences
    
    Collaborative learning is a powerful instructional approach that encourages students to work 
    together to construct knowledge, solve problems, and create products. When designed effectively,
    collaborative activities promote deeper understanding, develop social skills, and increase 
    student engagement. In this lesson, we'll explore how prompt engineering can help you create 
    high-quality collaborative learning experiences efficiently.
    """)
    
    # Why This Matters
    st.markdown("""
    ## Why This Matters
    
    Well-designed collaborative learning activities offer numerous benefits:
    
    * **Deeper cognitive processing** through explanation, debate, and co-construction of knowledge
    * **Development of essential social skills** including communication, negotiation, and leadership
    * **Increased student engagement** through peer interaction and shared responsibility
    * **Authentic preparation for future work** in collaborative professional environments
    * **Opportunities for peer teaching** that benefit both the "teacher" and "learner"
    * **Enhanced perspective-taking** as students encounter diverse viewpoints
    
    However, collaborative learning can fall short of these benefits when activities lack clear 
    structure, fail to ensure individual accountability, or don't promote meaningful interdependence.
    Prompt engineering helps address these challenges by enabling you to design more effective 
    collaborative experiences.
    """)
    
    # Types of Collaborative Learning Structures
    st.markdown("""
    ## Types of Collaborative Learning Structures
    
    Collaborative learning encompasses a wide range of formats and approaches:
    
    | Structure | Description | Example Applications |
    | --- | --- | --- |
    | **Think-Pair-Share** | Students think individually, discuss with a partner, then share with the larger group | Quick concept checks, initial responses to complex questions |
    | **Jigsaw** | Students become "experts" on one aspect of content, then teach others in mixed groups | Content exploration across multiple topics or perspectives |
    | **Collaborative Inquiry** | Groups investigate questions or problems together using structured protocols | Scientific investigations, historical analyses, case studies |
    | **Project-Based Teams** | Long-term collaboration to create a product or presentation | Design challenges, research projects, multimedia presentations |
    | **Peer Feedback Groups** | Students provide structured feedback on each other's work | Writing workshops, art critiques, practice presentations |
    | **Problem-Solving Teams** | Groups work together to solve complex problems with defined solutions | Math word problems, engineering challenges, case analyses |
    | **Debate and Discussion** | Structured formats for arguing positions and exploring perspectives | Ethical dilemmas, policy questions, textual interpretations |
    
    Each structure has unique strengths and is suited to different learning goals, content areas, and student needs.
    """)
    
    # Key Elements of Effective Collaborative Learning
    st.markdown("""
    ## Key Elements of Effective Collaborative Learning
    
    Research has identified several essential elements that make collaborative learning effective:
    
    ### 1. Positive Interdependence
    
    Students must perceive that they are linked with others in such a way that they cannot succeed unless 
    the others do (and vice versa). This can be created through:
    
    - **Goal interdependence**: The group has a common goal
    - **Resource interdependence**: Materials or information are divided among members
    - **Role interdependence**: Each member has a specific responsibility
    - **Identity interdependence**: The group has a name, flag, or other symbol of unity
    
    ### 2. Individual Accountability
    
    Each student must be held responsible for their own learning and contribution. This prevents "social loafing"
    (when some group members do all the work while others contribute little). Strategies include:
    
    - **Individual assessments** following group work
    - **Random selection** of one group member to explain or present
    - **Visible individual contributions** (e.g., using different colored pens)
    - **Self and peer assessment** of individual contributions
    
    ### 3. Promotive Interaction
    
    Students need to actively help and support each other's learning through explanation, discussion,
    and encouragement. This is enhanced by:
    
    - **Face-to-face seating arrangements**
    - **Explicit expectations** for helping behavior
    - **Structured discussion protocols**
    - **Collaborative rather than competitive grading**
    
    ### 4. Interpersonal Skills
    
    Collaboration requires social skills that must be explicitly taught and practiced:
    
    - **Communication skills** (active listening, clear expression)
    - **Decision-making strategies** (consensus building, voting)
    - **Conflict resolution approaches** (respectful disagreement, compromise)
    - **Leadership and followership skills** (facilitating, supporting)
    
    ### 5. Group Processing
    
    Groups need opportunities to reflect on their functioning and identify improvements:
    
    - **Regular check-ins** on progress and process
    - **Structured reflection protocols**
    - **Feedback on group dynamics**
    - **Goal-setting for future collaboration**
    """)
    
    # Challenges in Collaborative Learning Design
    st.markdown("""
    ## Common Challenges in Collaborative Learning Design
    
    Despite its benefits, collaborative learning presents several design challenges:
    
    ### 1. Ensuring Meaningful Participation
    
    Without careful design, group work can result in unequal participation, with some students dominating 
    while others remain passive. This challenge is particularly acute for students who are shy, English 
    language learners, or have social difficulties.
    
    ### 2. Balancing Structure and Autonomy
    
    Too much structure can limit student creativity and ownership, while too little structure can lead to 
    confusion, inefficiency, or off-task behavior. Finding the right balance is essential but challenging.
    
    ### 3. Designing Complex but Accessible Tasks
    
    Collaborative tasks should be complex enough to require multiple perspectives but accessible enough 
    that all group members can contribute meaningfully.
    
    ### 4. Creating Effective Groups
    
    Decisions about group size, composition, and duration significantly impact collaborative outcomes. 
    Different grouping strategies serve different purposes and require different support structures.
    
    ### 5. Assessing Individual and Group Learning
    
    Determining individual contributions to group work, balancing individual and group assessments, and 
    providing meaningful feedback on collaboration itself all present assessment challenges.
    """)
    
    # Prompt Engineering for Collaborative Learning
    st.markdown("""
    ## Prompt Engineering for Collaborative Learning
    
    Prompt engineering can help address these challenges by generating well-designed collaborative 
    activities, protocols, and assessment strategies. When creating AI prompts for collaborative learning, 
    consider:
    
    ### For Collaborative Activity Design:
    
    * **Specifying the collaborative structure** (e.g., "Create a jigsaw activity" or "Design a peer feedback protocol")
    * **Clarifying learning objectives** for both content and collaboration skills
    * **Requesting interdependence mechanisms** (e.g., "Include resource distribution that ensures all members must participate")
    * **Including accountability structures** (e.g., "Add individual assessment components that verify individual learning")
    * **Requesting time allocations** for different phases of the activity
    
    ### For Collaborative Protocols:
    
    * **Specifying interaction patterns** (e.g., "Create turn-taking structures that ensure equal participation")
    * **Requesting role definitions** with clear responsibilities
    * **Including discussion scaffolds** like sentence starters or question frames
    * **Requesting conflict resolution strategies** appropriate to the age group
    * **Including reflection prompts** for group processing
    
    ### For Collaborative Assessment:
    
    * **Clarifying assessment focus** (process vs. product, individual vs. group)
    * **Requesting rubrics** that address both content and collaboration skills
    * **Including self and peer assessment tools**
    * **Specifying observation protocols** for teacher monitoring
    * **Requesting formative feedback strategies** for ongoing improvement
    """)
    
    # Application in the PCTFR Framework
    st.markdown("""
    ## Applying the PCTFR Framework
    
    The PCTFR framework (Persona, Context, Task, Format, Reference Materials) can be applied to
    create effective prompts for collaborative learning activities:
    
    ### Example for a Science Investigation:
    
    ```
    Persona: Act as an experienced science educator who specializes in inquiry-based, collaborative learning approaches for middle school students
    
    Context: I'm teaching a unit on ecosystems to 7th graders in a diverse classroom with varied reading levels and English language proficiency. Students have basic understanding of food chains and energy transfer but need to develop deeper understanding of ecosystem interactions and interdependence.
    
    Task: Create a collaborative investigation activity where student teams explore how changes to one component of an ecosystem affect other components. The activity should promote scientific thinking skills while ensuring all team members participate meaningfully.
    
    Format: Design a 2-3 day cooperative investigation with:
    1. Clear student roles with defined responsibilities
    2. A structured protocol for making predictions and testing them
    3. Data collection tools that distribute responsibility
    4. Discussion questions for teams to process their findings
    5. Individual accountability measures to ensure all students engage with the content
    6. Scaffolding for different readiness levels
    7. A culminating team presentation format with individual components
    
    Reference Materials: The activity should align with NGSS MS-LS2-4: "Construct an argument supported by empirical evidence that changes to physical or biological components of an ecosystem affect populations." Key concepts include interdependence, carrying capacity, and population dynamics. Students have access to simple lab equipment, computers for research, and outdoor space for observations.
    ```
    
    ### Example for a Literature Circle:
    
    ```
    Persona: Act as a high school English teacher who uses collaborative learning to deepen text analysis and develop discussion skills
    
    Context: I'm teaching "The Crucible" by Arthur Miller to 10th grade students. We've just finished reading Act 2, and I want students to collaboratively analyze how Miller develops themes of reputation, power, and hysteria through character development and dramatic techniques.
    
    Task: Create a literature circle activity where students take on different analytical roles to examine the text from multiple perspectives, then synthesize their insights into a deeper collective understanding.
    
    Format: Design a literature circle protocol with:
    1. 4-5 distinct analytical roles with clear responsibilities (beyond the basic "discussion director" and "vocabulary finder")
    2. Role-specific worksheets that guide each student's preparation
    3. A structured discussion protocol that ensures all perspectives are heard
    4. Follow-up questions that promote connections between perspectives
    5. A collaborative product that synthesizes the group's analysis
    6. Individual reflection questions to assess personal understanding
    
    Reference Materials: Key scenes in Act 2 include John and Elizabeth's tense conversation about her suspicions, Reverend Hale's questioning, and Mary Warren's return from court with the poppet. The major characters in focus are John Proctor, Elizabeth Proctor, Reverend Hale, and Mary Warren. Key dramatic techniques include dramatic irony, foreshadowing, and symbolism (particularly the poppet).
    ```
    """)
    
    # Strategic Considerations
    st.markdown("""
    ## Strategic Considerations
    
    When using prompt engineering for collaborative learning design:
    
    ### 1. Consider Student Readiness for Collaboration
    
    * **Assess collaboration skills**: Start with simpler structures for students new to collaboration
    * **Build progressively**: Develop more complex collaborative experiences over time
    * **Teach explicitly**: Include prompts for direct instruction on collaborative skills
    * **Anticipate challenges**: Request guidance for common collaboration problems
    
    ### 2. Balance Content and Process Goals
    
    * **Clarify priorities**: Decide whether content mastery or collaboration skill development is primary
    * **Integrate objectives**: Request activities that develop both simultaneously when possible
    * **Consider sequence**: Sometimes focusing first on content then on process (or vice versa) is more effective
    
    ### 3. Adapt to Your Teaching Context
    
    * **Consider physical space**: Request activities suited to your classroom arrangement
    * **Account for time constraints**: Be realistic about what can be accomplished in available time
    * **Address technology access**: Include or exclude tech-dependent elements based on availability
    * **Respect school culture**: Align collaborative approaches with school norms and expectations
    
    ### 4. Plan for Assessment
    
    * **Determine assessment focus**: Decide what aspects of collaboration and content you'll assess
    * **Prepare monitoring strategies**: Request observation tools or check-in protocols
    * **Balance formative and summative**: Include both ongoing feedback and final evaluation
    * **Consider multiple perspectives**: Include self, peer, and teacher assessment when appropriate
    """)
    
    # Connection to Previous and Next Lessons
    st.markdown("""
    ## Connections to Other Lessons
    
    This lesson builds on concepts from previous lessons:
    
    * **Lesson 15 (Discussion Questions and Content Creation)**: The skills developed for creating 
      effective discussion questions and instructional content serve as a foundation for designing 
      collaborative activities. The PCTFR framework continues to provide structure for prompt creation.
    
    * **Earlier Lessons on Prompt Engineering Techniques**: The structural approaches and attention to
      detail practiced throughout the course are essential for creating the complex, multi-faceted
      prompts needed for effective collaborative learning design.
    
    In the next section, you'll see examples of effective prompts for generating various types of
    collaborative learning activities across different subject areas and grade levels.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Connect this lesson to participants' existing collaborative learning practices
    * Acknowledge the challenges of implementing collaborative learning and how prompt engineering can help
    * Emphasize that designing good prompts for collaborative activities requires careful consideration of structure
    * Encourage teachers to start with one collaborative format they're comfortable with before expanding
    
    **Discussion Prompts:**
    
    * What are your biggest challenges when implementing collaborative learning?
    * How do you currently balance individual accountability and group interdependence?
    * What types of collaborative structures have been most successful in your classroom?
    
    **Extension Opportunities:**
    
    * Invite teachers to analyze a challenging collaborative activity they've used and redesign it using prompt engineering
    * Suggest creating a department-wide collection of effective collaborative protocols for different purposes
    * Explore how prompt engineering might support remote or hybrid collaborative learning
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