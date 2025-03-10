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
    page_title="Lesson 18: Activities",
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
    "title": "Interdisciplinary Unit Design: Activities",
    "lesson": "18",
    "section": "activities",
    "order": 3
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_18_activities"
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
    "lesson_18_activities",
    "activities",
    "Interdisciplinary Unit Design: Activities",
    """
    **This section provides hands-on practice with creating prompts for interdisciplinary learning experiences.**
    
    You'll practice:
    - Identifying meaningful connections between different subject areas
    - Designing integrated learning experiences that maintain disciplinary integrity
    - Creating assessment approaches that evaluate both discipline-specific and integrated learning
    - Applying the PCTFR framework to interdisciplinary contexts
    
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
    
    Complete the activities below to practice creating effective prompts for interdisciplinary unit design.
    After finishing these activities, proceed to the Reflection section to consolidate your learning 
    and complete the course.
    """)
    
    # Activity 1: Identifying Meaningful Connection Points
    st.markdown("## Activity 1: Identifying Meaningful Connection Points")
    
    st.markdown("""
    In this activity, you'll identify authentic connection points between different disciplines that 
    could serve as foundations for interdisciplinary learning experiences.
    """)
    
    st.markdown("### Types of Disciplinary Connections")
    
    st.markdown("""
    Effective interdisciplinary units are built on meaningful connections between disciplines. 
    These connections can take different forms:
    
    | Connection Type | Description | Example |
    | --- | --- | --- |
    | **Conceptual Connections** | Big ideas that span multiple disciplines | Systems and interactions in science, social systems, ecosystems, number systems |
    | **Skill Connections** | Processes and skills used across subjects | Analysis, evaluation, modeling, problem-solving |
    | **Content Connections** | Topics addressed in multiple disciplines | Water studied in science (properties), geography (resources), history (civilizations) |
    | **Question Connections** | Inquiries that require multiple perspectives | "How do we determine value?" in economics, ethics, art |
    | **Tool Connections** | Methods and tools used across disciplines | Data visualization in science, social studies, mathematics |
    """)
    
    # Subject area selection
    st.markdown("### Select your primary subject area:")
    
    primary_subject = st.selectbox(
        "Primary teaching area:",
        ["Select a subject...", "Elementary (multiple subjects)", "English/Language Arts", "Mathematics", 
         "Science", "Social Studies/History", "Arts (Visual, Music, Drama, etc.)", "Physical Education", 
         "World Languages", "Career/Technical Education", "Special Education"],
        key="primary_subject"
    )
    
    if primary_subject and primary_subject != "Select a subject...":
        # Secondary subject selection
        st.markdown("### Select a subject to integrate with your primary area:")
        
        # Filter out the primary subject from secondary options
        secondary_options = ["Select a subject...", "English/Language Arts", "Mathematics", 
                           "Science", "Social Studies/History", "Arts (Visual, Music, Drama, etc.)", 
                           "Physical Education", "World Languages", "Career/Technical Education"]
        if primary_subject in secondary_options:
            secondary_options.remove(primary_subject)
        
        secondary_subject = st.selectbox(
            "Secondary subject area:",
            secondary_options,
            key="secondary_subject"
        )
        
        if secondary_subject and secondary_subject != "Select a subject...":
            st.markdown("### Identify Connection Points")
            
            st.markdown(f"""
            Identify at least one potential connection point of each type between 
            {primary_subject} and {secondary_subject}:
            """)
            
            # Connection identification
            conceptual_connection = st.text_area(
                "Conceptual Connection: What big ideas or core concepts exist in both disciplines?",
                height=80,
                key="conceptual_connection"
            )
            
            skill_connection = st.text_area(
                "Skill Connection: What processes or skills are developed in both disciplines?",
                height=80,
                key="skill_connection"
            )
            
            content_connection = st.text_area(
                "Content Connection: What specific topics or content areas overlap?",
                height=80,
                key="content_connection"
            )
            
            question_connection = st.text_area(
                "Question Connection: What essential questions could be explored through both disciplines?",
                height=80,
                key="question_connection"
            )
            
            tool_connection = st.text_area(
                "Tool Connection: What methods, resources, or tools are used in both disciplines?",
                height=80,
                key="tool_connection"
            )
            
            # Check if all connection types are addressed
            if (conceptual_connection and skill_connection and content_connection and
                question_connection and tool_connection):
                
                st.success("""
                Excellent job identifying meaningful connection points!
                
                These authentic connections will serve as the foundation for effective interdisciplinary 
                learning experiences. The strongest interdisciplinary units are built on connections that:
                
                - Exist naturally rather than being forced
                - Deepen understanding in both disciplines
                - Create opportunities for applying knowledge in new contexts
                - Help students see relationships between seemingly separate subjects
                
                When creating prompts for interdisciplinary units, be specific about these connection 
                points to ensure the generated materials maintain disciplinary integrity while creating 
                meaningful integration.
                """)
    
    # Activity 2: Designing an Interdisciplinary Unit Framework
    st.markdown("## Activity 2: Designing an Interdisciplinary Unit Framework")
    
    st.markdown("""
    In this activity, you'll create a framework for an interdisciplinary unit based on the connection 
    points you identified or other disciplines of your choice.
    """)
    
    st.markdown("### Organizational Frameworks")
    
    st.markdown("""
    Effective interdisciplinary units need organizing structures to create coherence. 
    Common organizing frameworks include:
    
    - **Essential Questions**: Open-ended questions that guide inquiry across disciplines
    - **Themes/Concepts**: Big ideas that appear in multiple subject areas
    - **Problems/Issues**: Real-world challenges that require multiple perspectives
    - **Processes/Skills**: Common methodologies applied across disciplines
    - **Products/Performances**: Culminating tasks that synthesize learning
    """)
    
    # Unit topic selection
    unit_topic = st.text_input(
        "Interdisciplinary unit topic or focus:",
        placeholder="e.g., Water Resources, Renaissance Period, Data and Society, etc.",
        key="unit_topic"
    )
    
    if unit_topic:
        # Framework selection
        framework_type = st.radio(
            "Select a primary organizing framework for your unit:",
            ["Essential Questions", "Themes/Concepts", "Problems/Issues", "Processes/Skills", "Products/Performances"],
            key="framework_type"
        )
        
        st.markdown("### Design your unit framework:")
        
        # Framework elements based on selection
        if framework_type == "Essential Questions":
            st.markdown("""
            **Essential Questions** are open-ended, thought-provoking questions that guide inquiry and 
            promote deep understanding across disciplines.
            """)
            
            main_question = st.text_area(
                "Primary Essential Question (overarching question that connects disciplines):",
                height=80,
                key="main_question"
            )
            
            discipline1_questions = st.text_area(
                f"Discipline-Specific Questions for Subject 1 (questions that explore the topic through the lens of one discipline):",
                height=100,
                key="discipline1_questions"
            )
            
            discipline2_questions = st.text_area(
                f"Discipline-Specific Questions for Subject 2 (questions that explore the topic through the lens of the other discipline):",
                height=100,
                key="discipline2_questions"
            )
            
            if main_question and discipline1_questions and discipline2_questions:
                st.success("""
                You've created an effective essential questions framework!
                
                Strong essential questions:
                - Cannot be answered with simple facts
                - Require exploration from multiple perspectives
                - Promote sustained inquiry over time
                - Connect to students' lives and experiences
                - Lead to meaningful transferable understandings
                
                These questions will serve as guideposts for your interdisciplinary unit, helping maintain 
                focus while encouraging exploration from different disciplinary lenses.
                """)
        
        elif framework_type == "Themes/Concepts":
            st.markdown("""
            **Themes/Concepts** are big ideas that transcend individual disciplines and provide 
            conceptual organizers for integrated learning.
            """)
            
            main_theme = st.text_area(
                "Primary Theme/Concept (overarching idea that connects disciplines):",
                height=80,
                key="main_theme"
            )
            
            subthemes = st.text_area(
                "Sub-themes (related concepts that help organize the unit):",
                height=100,
                key="subthemes"
            )
            
            discipline_applications = st.text_area(
                "Disciplinary Applications (how each discipline addresses these themes):",
                height=100,
                key="discipline_applications"
            )
            
            if main_theme and subthemes and discipline_applications:
                st.success("""
                You've created an effective thematic framework!
                
                Strong thematic frameworks:
                - Organize content around meaningful big ideas
                - Show how concepts manifest differently across disciplines
                - Create natural connection points between subjects
                - Help students develop transferable conceptual understanding
                - Provide structure while allowing disciplinary exploration
                
                These themes will help students see patterns and connections across subject boundaries 
                while maintaining the integrity of disciplinary content.
                """)
        
        elif framework_type == "Problems/Issues":
            st.markdown("""
            **Problems/Issues** are authentic challenges or situations that require multiple 
            disciplinary perspectives to fully understand and address.
            """)
            
            central_problem = st.text_area(
                "Central Problem/Issue (authentic challenge that connects disciplines):",
                height=80,
                key="central_problem"
            )
            
            discipline1_perspectives = st.text_area(
                "Discipline 1 Perspectives (how one subject area addresses this problem):",
                height=100,
                key="discipline1_perspectives"
            )
            
            discipline2_perspectives = st.text_area(
                "Discipline 2 Perspectives (how the other subject area addresses this problem):",
                height=100,
                key="discipline2_perspectives"
            )
            
            if central_problem and discipline1_perspectives and discipline2_perspectives:
                st.success("""
                You've created an effective problem-based framework!
                
                Strong problem-based frameworks:
                - Center on authentic, meaningful challenges
                - Demonstrate why multiple perspectives are necessary
                - Provide natural contexts for applying disciplinary knowledge
                - Engage students in real-world application
                - Show how disciplines complement each other
                
                This approach helps students understand the value of different disciplinary lenses 
                and develops their ability to integrate knowledge to address complex problems.
                """)
        
        elif framework_type == "Processes/Skills":
            st.markdown("""
            **Processes/Skills** frameworks focus on common methodologies, thinking skills, or 
            practices that span multiple disciplines.
            """)
            
            shared_processes = st.text_area(
                "Shared Processes/Skills (common methodologies across disciplines):",
                height=80,
                key="shared_processes"
            )
            
            discipline1_applications = st.text_area(
                "Discipline 1 Applications (how these processes are used in one subject):",
                height=100,
                key="discipline1_applications"
            )
            
            discipline2_applications = st.text_area(
                "Discipline 2 Applications (how these processes are used in the other subject):",
                height=100,
                key="discipline2_applications"
            )
            
            if shared_processes and discipline1_applications and discipline2_applications:
                st.success("""
                You've created an effective process-based framework!
                
                Strong process-based frameworks:
                - Focus on transferable skills and methodologies
                - Show how similar processes are applied in different contexts
                - Develop metacognitive awareness of thinking strategies
                - Promote deeper procedural understanding
                - Support skill transfer across domains
                
                This approach helps students recognize patterns in how knowledge is created and applied 
                across different fields, developing sophisticated thinking strategies.
                """)
        
        elif framework_type == "Products/Performances":
            st.markdown("""
            **Products/Performances** frameworks organize learning around culminating tasks that 
            require synthesis of knowledge and skills from multiple disciplines.
            """)
            
            culminating_product = st.text_area(
                "Culminating Product/Performance (final task that integrates disciplines):",
                height=80,
                key="culminating_product"
            )
            
            discipline1_elements = st.text_area(
                "Discipline 1 Elements (components from one subject area):",
                height=100,
                key="discipline1_elements"
            )
            
            discipline2_elements = st.text_area(
                "Discipline 2 Elements (components from the other subject area):",
                height=100,
                key="discipline2_elements"
            )
            
            if culminating_product and discipline1_elements and discipline2_elements:
                st.success("""
                You've created an effective product-based framework!
                
                Strong product-based frameworks:
                - Center on authentic, meaningful culminating tasks
                - Require application of knowledge and skills from multiple disciplines
                - Provide clear purpose and direction for learning
                - Allow for creative synthesis of learning
                - Create natural assessment opportunities
                
                This approach helps students integrate their learning across disciplines through 
                application to a meaningful challenge or creative task.
                """)
    
    # Activity 3: PCTFR Framework for Interdisciplinary Unit Design
    st.markdown("## Activity 3: PCTFR Framework for Interdisciplinary Unit Design")
    
    st.markdown("""
    In this activity, you'll apply the PCTFR framework to create a comprehensive prompt for 
    generating an interdisciplinary unit that connects multiple subject areas.
    """)
    
    # PCTFR components for interdisciplinary units
    st.markdown("### Complete each component of the PCTFR framework:")
    
    persona_inter = st.text_area(
        "**Persona:** What type of educational specialist should the AI model embody?",
        height=80,
        placeholder="Example: Act as an interdisciplinary curriculum specialist who designs integrated learning experiences that...",
        key="persona_inter"
    )
    
    context_inter = st.text_area(
        "**Context:** What's the specific teaching situation, student background, and integration goals?",
        height=100,
        placeholder="Example: I teach both 8th grade science and language arts, and I'm developing a unit that integrates...",
        key="context_inter"
    )
    
    task_inter = st.text_area(
        "**Task:** What specific type of interdisciplinary unit do you need?",
        height=80,
        placeholder="Example: Create a 3-week integrated unit that connects scientific inquiry about ecosystems with...",
        key="task_inter"
    )
    
    format_inter = st.text_area(
        "**Format:** How should the unit be structured to maintain disciplinary integrity while creating connections?",
        height=120,
        placeholder="Example: Design a unit plan that includes: 1) Essential questions that bridge both disciplines, 2) Learning objectives from both subject areas...",
        key="format_inter"
    )
    
    reference_inter = st.text_area(
        "**Reference Materials:** What specific content, standards, or disciplinary elements should inform the unit?",
        height=120,
        placeholder="Example: Science standards include MS-LS2-1... ELA standards focus on argumentative writing W.8.1...",
        key="reference_inter"
    )
    
    # Assembling the complete prompt
    if persona_inter and context_inter and task_inter and format_inter and reference_inter:
        st.success("You've created all components for a comprehensive PCTFR prompt. Here's your complete prompt:")
        
        st.markdown("### Your Complete PCTFR Prompt for an Interdisciplinary Unit:")
        
        st.code(f"""
{persona_inter}

{context_inter}

{task_inter}

{format_inter}

{reference_inter}
        """)
        
        st.markdown("""
        #### Analyzing Your Prompt's Effectiveness
        
        Review your prompt and check if it includes these characteristics of effective interdisciplinary unit prompts:
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.checkbox("Specifies the integration approach or philosophy", key="check_approach")
            st.checkbox("Identifies specific subject areas to be integrated", key="check_subjects")
            st.checkbox("Notes organizational framework (questions, themes, etc.)", key="check_framework")
            st.checkbox("Addresses student background and readiness", key="check_readiness")
        
        with col2:
            st.checkbox("Requests standards or objectives from each discipline", key="check_standards")
            st.checkbox("Includes assessment of both disciplinary and integrated learning", key="check_assessment")
            st.checkbox("Specifies culminating product or performance", key="check_product")
            st.checkbox("Addresses logistics and implementation considerations", key="check_logistics")
    
    # Activity 4: Interdisciplinary Assessment Design
    st.markdown("## Activity 4: Interdisciplinary Assessment Design")
    
    st.markdown("""
    In this activity, you'll design an assessment approach for an interdisciplinary unit that evaluates 
    both discipline-specific learning and integrated understanding.
    """)
    
    st.markdown("### Assessment Challenges in Interdisciplinary Learning")
    
    st.markdown("""
    Assessing interdisciplinary learning presents unique challenges:
    
    - **Balancing disciplinary and integrated assessment**
    - **Evaluating both content knowledge and connection-making**
    - **Determining individual mastery within collaborative contexts**
    - **Creating authentic assessments that require integration**
    - **Developing rubrics that address multiple sets of standards**
    """)
    
    # Assessment design activity
    st.markdown("### Design an Interdisciplinary Assessment Approach")
    
    st.markdown("""
    For an interdisciplinary unit of your choice, design a comprehensive assessment approach 
    that addresses both disciplinary and integrated learning.
    """)
    
    assessment_unit = st.text_input(
        "Interdisciplinary unit focus:",
        placeholder="e.g., Sustainable Urban Planning, Renaissance Art and Science, etc.",
        key="assessment_unit"
    )
    
    if assessment_unit:
        st.markdown("### Design your assessment components:")
        
        disciplinary_assessments = st.text_area(
            "Discipline-Specific Assessments: How will you evaluate learning in each subject area?",
            height=100,
            key="disciplinary_assessments"
        )
        
        integration_assessments = st.text_area(
            "Integration Assessments: How will you evaluate students' ability to make connections across disciplines?",
            height=100,
            key="integration_assessments"
        )
        
        culminating_assessment = st.text_area(
            "Culminating Assessment: Describe a final product or performance that requires synthesis across disciplines:",
            height=120,
            key="culminating_assessment"
        )
        
        rubric_approach = st.text_area(
            "Rubric Design: How will your evaluation criteria address both disciplinary standards and integration skills?",
            height=100,
            key="rubric_approach"
        )
        
        # Check if assessment components are complete
        if (disciplinary_assessments and integration_assessments and 
            culminating_assessment and rubric_approach):
            
            st.success("""
            Excellent work designing a comprehensive interdisciplinary assessment approach!
            
            Effective interdisciplinary assessment:
            - Maintains accountability to disciplinary standards
            - Evaluates students' ability to make meaningful connections
            - Uses authentic tasks that require integration of knowledge and skills
            - Balances formative and summative approaches
            - Provides clear criteria for both disciplinary and integrated learning
            
            When creating prompts for interdisciplinary units, include specific assessment requests 
            to ensure the generated materials include appropriate evaluation approaches for both 
            disciplinary and integrated learning.
            """)
            
            st.markdown("### Creating a Complete Assessment Prompt")
            
            st.markdown("""
            Using the components you've designed, craft a specific prompt section focused on 
            assessment for an interdisciplinary unit.
            """)
            
            assessment_prompt = st.text_area(
                "Assessment Section for Interdisciplinary Unit Prompt:",
                height=200,
                placeholder="Include specific requests for disciplinary assessments, integration assessments, and culminating performance tasks...",
                key="assessment_prompt"
            )
            
            if assessment_prompt:
                st.success("""
                Well done! This assessment section will help ensure that your generated interdisciplinary 
                unit includes appropriate evaluation approaches that maintain disciplinary integrity while 
                also assessing students' ability to make meaningful connections across subject areas.
                
                Remember that assessment in interdisciplinary settings should:
                - Make both disciplinary and integration learning visible
                - Provide feedback on multiple dimensions of learning
                - Evaluate both content knowledge and thinking processes
                - Include authentic applications that require synthesis
                - Balance individual and collaborative assessment
                """)
    
    # Reflection and key takeaways
    st.markdown("## Activity Reflection")
    
    st.markdown("""
    Take a moment to reflect on what you've learned from these activities:
    
    1. **Meaningful connection points** serve as the foundation for effective interdisciplinary learning. 
       The strongest interdisciplinary units are built on authentic overlaps between disciplines rather 
       than forced connections.
    
    2. **Organizing frameworks** such as essential questions, themes, problems, processes, or culminating 
       tasks provide structure and coherence for interdisciplinary units, helping students navigate 
       learning across subject boundaries.
    
    3. **The PCTFR framework** provides a comprehensive structure for generating interdisciplinary units 
       that maintain disciplinary integrity while creating meaningful connections.
    
    4. **Interdisciplinary assessment** requires thoughtful design to evaluate both discipline-specific 
       learning and students' ability to make connections across subject boundaries.
    
    As you incorporate these approaches into your prompt engineering, you'll create more effective 
    interdisciplinary learning experiences that deepen understanding across subject areas.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Encourage participants to start with small interdisciplinary connections before attempting full integration
    * Remind participants that the degree of integration can vary based on their teaching context
    * Suggest partnering with colleagues from other disciplines when possible
    * Emphasize that maintaining disciplinary integrity is essential for effective integration
    
    **Common Challenges:**
    
    * Finding time for interdisciplinary planning and teaching
    * Balancing breadth and depth when covering multiple disciplines
    * Coordinating with colleagues who have different teaching approaches
    * Addressing assessment requirements while implementing integrated learning
    
    **Extension Ideas:**
    
    * Have participants create a template for a specific type of interdisciplinary unit they'd implement regularly
    * Encourage developing a collaborative planning protocol for working with colleagues from other disciplines
    * Suggest creating a bank of essential questions that span multiple subject areas in their curriculum
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