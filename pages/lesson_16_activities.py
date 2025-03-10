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
    page_title="Lesson 16: Activities",
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
    "title": "Collaborative Learning Activities: Activities",
    "lesson": "16",
    "section": "activities",
    "order": 3
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_16_activities"
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
    "lesson_16_activities",
    "activities",
    "Collaborative Learning Activities: Activities",
    """
    **This section provides hands-on practice with creating prompts for collaborative learning activities.**
    
    You'll practice:
    - Designing structured collaborative experiences for different purposes
    - Creating protocols that ensure meaningful participation from all students
    - Building in mechanisms for positive interdependence and individual accountability
    - Applying the PCTFR framework to your specific teaching context
    
    Complete these activities to strengthen your skills before moving to the reflection section.
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
    st.markdown(f"# Activities: {PAGE_INFO['title']}")
    
    # Add a progress note
    st.info("""
    **📝 Course Progression Note:** 
    
    Complete the activities below to practice creating effective prompts for collaborative learning activities.
    After finishing these activities, proceed to the Reflection section to consolidate your learning 
    and unlock the next lesson.
    """)
    
    # Activity 1: Collaborative Structure Selection
    st.markdown("## Activity 1: Collaborative Structure Selection")
    
    st.markdown("""
    In this activity, you'll analyze different collaborative structures and identify which would be most
    appropriate for specific learning goals and contexts.
    """)
    
    st.markdown("### Collaborative Structures and Their Purposes")
    
    st.markdown("""
    Below are common collaborative learning structures, each with specific strengths and ideal applications:
    
    | Structure | Best For | Key Features |
    | --- | --- | --- |
    | **Think-Pair-Share** | Quick processing, ensuring all voices are heard | Individual thinking, paired discussion, whole-group sharing |
    | **Jigsaw** | Covering multiple aspects of content efficiently | Expert groups, teaching groups, distributed responsibility |
    | **Peer Feedback** | Improving drafts, developing critical analysis | Structured critique protocols, revision focus |
    | **Problem-Based Learning** | Authentic application, multiple solution paths | Complex problem scenarios, team-based investigation |
    | **Collaborative Inquiry** | Research skills, question investigation | Question development, investigation protocols, synthesis |
    | **Literature Circles** | Deep text analysis, multiple perspectives | Role-based reading, structured discussion |
    | **Project Teams** | Extended creation, authentic tasks | Sustained collaboration, product development |
    """)
    
    # Matching scenarios to structures
    st.markdown("### Match Scenarios to Collaborative Structures")
    
    st.markdown("""
    For each teaching scenario below, select the collaborative structure that would be most appropriate,
    and explain your reasoning.
    """)
    
    # Scenario 1
    st.markdown("""
    #### Scenario 1: 
    You're teaching a high school chemistry unit on chemical reactions. Students need to understand multiple 
    types of reactions (synthesis, decomposition, single replacement, double replacement, combustion) and 
    be able to identify them from equations and demonstrations.
    """)
    
    scenario1_structure = st.selectbox(
        "Best collaborative structure for Scenario 1:",
        ["Select a structure...", "Think-Pair-Share", "Jigsaw", "Peer Feedback", 
         "Problem-Based Learning", "Collaborative Inquiry", "Literature Circles", "Project Teams"],
        key="scenario1_structure"
    )
    
    scenario1_reasoning = st.text_area(
        "Explain why this structure is appropriate for the learning goals and context:",
        height=100,
        key="scenario1_reasoning"
    )
    
    # Scenario 2
    st.markdown("""
    #### Scenario 2: 
    You're teaching a 4th-grade writing unit on personal narratives. Students have completed first drafts 
    and need to improve their use of descriptive language, dialogue, and narrative structure.
    """)
    
    scenario2_structure = st.selectbox(
        "Best collaborative structure for Scenario 2:",
        ["Select a structure...", "Think-Pair-Share", "Jigsaw", "Peer Feedback", 
         "Problem-Based Learning", "Collaborative Inquiry", "Literature Circles", "Project Teams"],
        key="scenario2_structure"
    )
    
    scenario2_reasoning = st.text_area(
        "Explain why this structure is appropriate for the learning goals and context:",
        height=100,
        key="scenario2_reasoning"
    )
    
    # Scenario 3
    st.markdown("""
    #### Scenario 3: 
    You're teaching a middle school social studies unit on current events. Students need to understand 
    complex global issues from multiple perspectives and develop informed opinions based on evidence.
    """)
    
    scenario3_structure = st.selectbox(
        "Best collaborative structure for Scenario 3:",
        ["Select a structure...", "Think-Pair-Share", "Jigsaw", "Peer Feedback", 
         "Problem-Based Learning", "Collaborative Inquiry", "Literature Circles", "Project Teams"],
        key="scenario3_structure"
    )
    
    scenario3_reasoning = st.text_area(
        "Explain why this structure is appropriate for the learning goals and context:",
        height=100,
        key="scenario3_reasoning"
    )
    
    # Check if all scenarios are addressed
    if (scenario1_structure != "Select a structure..." and scenario1_reasoning and
        scenario2_structure != "Select a structure..." and scenario2_reasoning and
        scenario3_structure != "Select a structure..." and scenario3_reasoning):
        
        st.success("""
        Great job matching collaborative structures to specific learning contexts!
        
        When selecting a collaborative structure, consider:
        - The specific learning goals and content
        - The complexity of the material
        - Students' collaboration readiness
        - Available time and resources
        - The balance of content learning and collaboration skill development
        
        Different structures serve different purposes, and the best choice depends on your specific
        context and objectives.
        """)
    
    # Activity 2: Designing for Positive Interdependence
    st.markdown("## Activity 2: Designing for Positive Interdependence")
    
    st.markdown("""
    Positive interdependence—when students perceive that they can only succeed if their teammates succeed—is
    a crucial element of effective collaborative learning. In this activity, you'll explore different ways
    to create positive interdependence in collaborative activities.
    """)
    
    st.markdown("### Types of Positive Interdependence")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Goal Interdependence**
        - Common group goal or outcome
        - Shared performance targets
        - Group recognition/rewards
        
        **Resource Interdependence**
        - Materials divided among members
        - Each person has unique information
        - Combined resources needed for completion
        """)
    
    with col2:
        st.markdown("""
        **Role Interdependence**
        - Complementary, interconnected roles
        - Each role essential to completion
        - Clear responsibilities for each member
        
        **Task Interdependence**
        - Work divided sequentially
        - Each portion builds on others
        - Multiple steps requiring different members
        """)
    
    # Interdependence design activity
    st.markdown("### Design Interdependence Strategies")
    
    st.markdown("""
    Select a collaborative structure and content area from your teaching, then describe how you would
    implement each type of positive interdependence.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        collab_structure = st.selectbox(
            "Select a collaborative structure:",
            ["Select a structure...", "Think-Pair-Share", "Jigsaw", "Peer Feedback", 
             "Problem-Based Learning", "Collaborative Inquiry", "Literature Circles", "Project Teams"],
            key="collab_structure"
        )
    
    with col2:
        content_area = st.text_input(
            "Content topic/area:",
            placeholder="e.g., Fractions, Civil War, Cell Biology, Poetry Analysis",
            key="content_area"
        )
    
    if collab_structure != "Select a structure..." and content_area:
        st.markdown("### Describe your interdependence strategies:")
        
        goal_strategy = st.text_area(
            "Goal Interdependence: How will you create shared goals?",
            height=80,
            key="goal_strategy"
        )
        
        resource_strategy = st.text_area(
            "Resource Interdependence: How will you distribute resources or information?",
            height=80,
            key="resource_strategy"
        )
        
        role_strategy = st.text_area(
            "Role Interdependence: What complementary roles will students take?",
            height=80,
            key="role_strategy"
        )
        
        task_strategy = st.text_area(
            "Task Interdependence: How will you structure sequential or interconnected tasks?",
            height=80,
            key="task_strategy"
        )
        
        # Check if all interdependence types are addressed
        if goal_strategy and resource_strategy and role_strategy and task_strategy:
            st.success("""
            Excellent work designing multiple forms of positive interdependence!
            
            Strong collaborative activities typically incorporate at least 2-3 types of interdependence
            to ensure that students truly need to work together. The most effective collaborative experiences
            create situations where:
            
            - Individual success is impossible without group success
            - Each member has a unique and essential contribution
            - The process requires genuine interaction and cooperation
            
            By designing with interdependence in mind, you help prevent common issues like one student
            doing all the work or group members working independently without true collaboration.
            """)
    
    # Activity 3: Individual Accountability Design
    st.markdown("## Activity 3: Individual Accountability Design")
    
    st.markdown("""
    Individual accountability ensures that each student is responsible for their own learning and
    contribution to the group. Without it, collaborative learning can lead to unequal participation
    and uneven learning outcomes.
    """)
    
    st.markdown("### Individual Accountability Strategies")
    
    st.markdown("""
    Review these common strategies for building individual accountability into collaborative activities:
    
    | Strategy | Description | Implementation Example |
    | --- | --- | --- |
    | **Individual Pre-work** | Each student completes preparation before group work | Reading response, initial solution attempt, research notes |
    | **Assigned Roles** | Each student has specific responsibilities within the group | Facilitator, recorder, resource manager, questioner |
    | **Individual Products** | Each student creates their own artifact alongside group work | Personal reflection, individual write-up, unique contribution |
    | **Random Reporter** | Any group member may be randomly selected to explain | Teacher randomly calls on one member to present group work |
    | **Visible Contributions** | Individual contributions are visibly tracked | Color-coded additions to chart paper, signed contributions |
    | **Individual Assessment** | Individual testing or evaluation follows group work | Individual quiz on content explored in groups |
    | **Self & Peer Evaluation** | Students assess their own and others' contributions | Rubric-based evaluation of collaboration quality |
    """)
    
    # Accountability design activity
    st.markdown("### Design an Accountability System")
    
    st.markdown("""
    Think about a collaborative activity you use or would like to use in your teaching. Design a 
    comprehensive accountability system that ensures all students are responsible for their learning and contribution.
    """)
    
    activity_description = st.text_area(
        "Briefly describe the collaborative activity:",
        height=100,
        placeholder="Include the subject area, grade level, and type of collaborative structure",
        key="activity_description"
    )
    
    if activity_description:
        st.markdown("### Design your accountability strategies:")
        
        before_strategies = st.text_area(
            "Before Collaboration: What individual accountability will you build in before group work begins?",
            height=80,
            key="before_strategies"
        )
        
        during_strategies = st.text_area(
            "During Collaboration: How will you monitor and ensure individual participation during the group work?",
            height=80,
            key="during_strategies"
        )
        
        after_strategies = st.text_area(
            "After Collaboration: How will you assess individual learning or contribution after the group work?",
            height=80,
            key="after_strategies"
        )
        
        # Check if all accountability phases are addressed
        if before_strategies and during_strategies and after_strategies:
            st.success("""
            Well-designed individual accountability system!
            
            Effective accountability measures:
            - Are transparent to students from the beginning
            - Occur throughout the collaborative process (before, during, after)
            - Balance individual responsibility with group interdependence
            - Fairly assess both process contributions and content learning
            
            When students know they'll be individually accountable, they're more likely to engage
            actively in the collaborative process, resulting in more equitable participation and
            better learning outcomes for all.
            """)
    
    # Activity 4: PCTFR Framework for Collaborative Learning
    st.markdown("## Activity 4: PCTFR Framework for Collaborative Learning")
    
    st.markdown("""
    In this activity, you'll apply the PCTFR framework to create a comprehensive prompt for 
    generating a collaborative learning activity tailored to your teaching context.
    """)
    
    # PCTFR components for collaborative learning
    st.markdown("### Complete each component of the PCTFR framework:")
    
    persona_collab = st.text_area(
        "**Persona:** What type of teacher or educational specialist should the AI model embody?",
        height=80,
        placeholder="Example: Act as an experienced science teacher who specializes in collaborative inquiry...",
        key="persona_collab"
    )
    
    context_collab = st.text_area(
        "**Context:** What's the specific teaching situation, student background, and collaboration readiness?",
        height=100,
        placeholder="Example: I teach 8th grade physical science to students with varied academic abilities and limited experience with collaborative work...",
        key="context_collab"
    )
    
    task_collab = st.text_area(
        "**Task:** What specific type of collaborative activity do you need?",
        height=80,
        placeholder="Example: Create a jigsaw activity that helps students understand the different forms of energy transfer...",
        key="task_collab"
    )
    
    format_collab = st.text_area(
        "**Format:** How should the collaborative activity be structured?",
        height=120,
        placeholder="Example: Design a 2-day jigsaw with expert groups on conduction, convection, radiation, and energy transformation. Include specific roles, worksheets for expert groups...",
        key="format_collab"
    )
    
    reference_collab = st.text_area(
        "**Reference Materials:** What specific content, standards, or collaborative considerations should inform the activity?",
        height=120,
        placeholder="Example: The activity should address NGSS MS-PS3-2. Students have textbooks with basic information on each energy transfer type and access to simple lab materials...",
        key="reference_collab"
    )
    
    # Assembling the complete prompt
    if persona_collab and context_collab and task_collab and format_collab and reference_collab:
        st.success("You've created all components for a comprehensive PCTFR prompt. Here's your complete prompt:")
        
        st.markdown("### Your Complete PCTFR Prompt for a Collaborative Learning Activity:")
        
        st.code(f"""
{persona_collab}

{context_collab}

{task_collab}

{format_collab}

{reference_collab}
        """)
        
        st.markdown("""
        #### Analyzing Your Prompt's Effectiveness
        
        Review your prompt and check if it includes these characteristics of effective collaborative learning prompts:
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.checkbox("Specifies the collaborative structure clearly", key="check_structure")
            st.checkbox("Addresses student collaboration readiness", key="check_readiness")
            st.checkbox("Includes positive interdependence mechanisms", key="check_interdependence")
            st.checkbox("Incorporates individual accountability measures", key="check_accountability")
        
        with col2:
            st.checkbox("Requests specific protocols or procedures", key="check_protocols")
            st.checkbox("Addresses differentiation for diverse learners", key="check_differentiation")
            st.checkbox("Includes time allocations or pacing guidance", key="check_timing")
            st.checkbox("References content standards or learning goals", key="check_goals")
    
    # Reflection and key takeaways
    st.markdown("## Activity Reflection")
    
    st.markdown("""
    Take a moment to reflect on what you've learned from these activities:
    
    1. **Collaborative structure selection** should be based on specific learning goals, content complexity,
       and student needs. Different structures serve different purposes, and no single approach works
       for all situations.
    
    2. **Positive interdependence** is essential for true collaboration. By designing activities with
       multiple forms of interdependence (goal, resource, role, task), you ensure that students must
       work together to succeed.
    
    3. **Individual accountability** prevents "hitchhiking" and ensures that all students learn. Effective
       accountability systems include measures before, during, and after collaboration.
    
    4. **The PCTFR framework** provides a comprehensive structure for designing collaborative learning
       activities that address both content learning and collaboration skill development.
    
    As you incorporate these principles into your prompt engineering for collaborative activities,
    you'll create more effective group experiences that maximize learning for all students.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Encourage participants to save their PCTFR prompt as a template for future collaborative activity design
    * Remind participants that scaffolding collaboration itself is just as important as scaffolding content
    * Suggest starting with simpler collaborative structures and gradually increasing complexity as students develop skills
    * Emphasize that effective collaborative learning requires explicit teaching of collaboration skills
    
    **Common Challenges:**
    
    * Balancing structure with student autonomy in collaborative activities
    * Managing uneven participation without micromanaging groups
    * Finding time for both individual accountability and meaningful group work
    * Designing authentic tasks that truly require collaboration rather than simply dividing work
    
    **Extension Ideas:**
    
    * Have participants design a mini-lesson on a specific collaboration skill (active listening, respectful disagreement, etc.)
    * Encourage creation of a progressive series of collaborative activities that build skills over a semester
    * Suggest developing a collaborative skills rubric for ongoing assessment and feedback
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