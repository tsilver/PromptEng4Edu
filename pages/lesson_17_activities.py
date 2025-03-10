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
    page_title="Lesson 17: Activities",
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
    "title": "Personalized Learning Pathways: Activities",
    "lesson": "17",
    "section": "activities",
    "order": 3
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_17_activities"
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
    "lesson_17_activities",
    "activities",
    "Personalized Learning Pathways: Activities",
    """
    **This section provides hands-on practice with creating prompts for personalized learning experiences.**
    
    You'll practice:
    - Designing differentiated materials for diverse learners
    - Creating adaptive learning pathways with multiple entry points
    - Developing choice-based learning experiences that respond to student interests
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
    
    Complete the activities below to practice creating effective prompts for personalized learning pathways.
    After finishing these activities, proceed to the Reflection section to consolidate your learning 
    and unlock the next lesson.
    """)
    
    # Activity 1: Learner Profile Analysis
    st.markdown("## Activity 1: Learner Profile Analysis")
    
    st.markdown("""
    In this activity, you'll analyze different learner profiles and identify which personalization 
    approaches would be most appropriate for each student's needs.
    """)
    
    st.markdown("### Understanding Learner Variables")
    
    st.markdown("""
    Effective personalization begins with a clear understanding of learner variables:
    
    | Variable | Description | Examples of Variation |
    | --- | --- | --- |
    | **Readiness** | Current academic level relative to learning goals | Below grade level, at grade level, above grade level; mastery of prerequisites |
    | **Interests** | Topics and contexts that engage the student | Subject preferences, real-world connections, cultural relevance |
    | **Learning Preferences** | Ways the student processes information most effectively | Visual, auditory, kinesthetic, verbal; social vs. independent |
    | **Background Knowledge** | Prior experiences and existing content knowledge | Cultural experiences, previous learning, out-of-school knowledge |
    | **Learning Challenges** | Specific barriers to accessing content | Language proficiency, learning disabilities, attention issues |
    """)
    
    # Learner profile analysis
    st.markdown("### Analyze Student Profiles and Match Personalization Approaches")
    
    st.markdown("""
    For each student profile below, identify which personalization approaches would best address 
    their needs and explain your reasoning.
    """)
    
    # Student 1
    st.markdown("""
    #### Student 1: Maya
    
    **Profile:**
    - 4th grade student reading at a 2nd grade level
    - Strong oral language skills and comprehension when material is read aloud
    - Enthusiastic about science topics, especially animals
    - Becomes frustrated and disengaged when faced with text-heavy materials
    - Visual learner who responds well to diagrams, videos, and hands-on activities
    """)
    
    maya_approaches = st.multiselect(
        "Select the personalization approaches that would best support Maya:",
        ["Differentiated reading levels", "Multi-modal content presentation", "Interest-based content selections", 
         "Extended time accommodations", "Scaffolded writing templates", "Audio text supports", 
         "Visual learning aids", "Collaborative group structures"],
        key="maya_approaches"
    )
    
    maya_reasoning = st.text_area(
        "Explain how your selected approaches would address Maya's specific needs:",
        height=120,
        key="maya_reasoning"
    )
    
    # Student 2
    st.markdown("""
    #### Student 2: Jamal
    
    **Profile:**
    - 7th grade student performing at or above grade level in all subjects
    - Completes assignments quickly and becomes bored with repetitive practice
    - Particularly interested in technology and engineering
    - Prefers to work independently at his own pace
    - Sometimes struggles with collaborative activities where he has to wait for others
    """)
    
    jamal_approaches = st.multiselect(
        "Select the personalization approaches that would best support Jamal:",
        ["Accelerated content pacing", "Interest-driven project options", "Self-directed learning modules", 
         "Advanced challenge extensions", "Flexible grouping strategies", "Technology-enhanced learning", 
         "Multi-step complex tasks", "Peer tutoring opportunities"],
        key="jamal_approaches"
    )
    
    jamal_reasoning = st.text_area(
        "Explain how your selected approaches would address Jamal's specific needs:",
        height=120,
        key="jamal_reasoning"
    )
    
    # Student 3
    st.markdown("""
    #### Student 3: Elena
    
    **Profile:**
    - 10th grade student new to the country with emerging English language skills
    - Strong academic background in her native language
    - Anxious about participating in class discussions
    - Excels in mathematics where language demands are lower
    - Benefits from visual supports and clear step-by-step instructions
    """)
    
    elena_approaches = st.multiselect(
        "Select the personalization approaches that would best support Elena:",
        ["Native language resources", "Visual vocabulary supports", "Graphic organizers", 
         "Modified language assignments", "Extended response time", "Alternative assessment formats", 
         "Sentence frames/starters", "Preview-review strategies"],
        key="elena_approaches"
    )
    
    elena_reasoning = st.text_area(
        "Explain how your selected approaches would address Elena's specific needs:",
        height=120,
        key="elena_reasoning"
    )
    
    # Check if all student analyses are completed
    if (maya_approaches and maya_reasoning and
        jamal_approaches and jamal_reasoning and
        elena_approaches and elena_reasoning):
        
        st.success("""
        Great job analyzing different learner profiles and matching appropriate personalization approaches!
        
        When designing personalized learning experiences, it's essential to:
        - Consider multiple dimensions of learner needs and preferences
        - Select approaches that directly address specific learning barriers
        - Build on student strengths while supporting areas of challenge
        - Maintain high expectations while providing appropriate support
        
        These analyses will help you design more targeted prompts for personalized learning materials.
        """)
    
    # Activity 2: Designing Tiered Assignments
    st.markdown("## Activity 2: Designing Tiered Assignments")
    
    st.markdown("""
    Tiered assignments are one of the most common and effective approaches to personalization. They provide 
    different versions of an assignment that vary in complexity, abstractness, or support level while 
    addressing the same essential concepts and skills.
    """)
    
    st.markdown("### Principles of Effective Tiering")
    
    st.markdown("""
    When designing tiered assignments, consider these key principles:
    
    1. **Same Essential Understanding:** All tiers focus on the same core concepts or skills
    2. **Varied Complexity:** The task complexity matches student readiness level
    3. **Appropriate Challenge:** Each tier provides the right level of stretch for the intended students
    4. **Equivalent Engagement:** All tiers offer similarly interesting and meaningful work
    5. **Common Final Assessment:** Students can be assessed on the same criteria despite different paths
    """)
    
    # Tiered assignment design activity
    st.markdown("### Design a Three-Tiered Assignment")
    
    st.markdown("""
    Select a concept from your teaching area and design a three-tiered assignment that addresses different 
    readiness levels while maintaining focus on the same essential understanding.
    """)
    
    concept_focus = st.text_input(
        "Essential concept or skill to be addressed:",
        placeholder="e.g., Character Analysis, Solving Systems of Equations, Understanding Climate Change",
        key="concept_focus"
    )
    
    if concept_focus:
        st.markdown("### Design your tiered assignment:")
        
        below_level_tier = st.text_area(
            "Tier 1 (Below Grade Level): Describe the assignment, including supports and scaffolding:",
            height=150,
            key="below_level_tier"
        )
        
        at_level_tier = st.text_area(
            "Tier 2 (At Grade Level): Describe the assignment, with moderate scaffolding:",
            height=150,
            key="at_level_tier"
        )
        
        above_level_tier = st.text_area(
            "Tier 3 (Above Grade Level): Describe the assignment, with advanced extensions:",
            height=150,
            key="above_level_tier"
        )
        
        # Elements that should be consistent across tiers
        if below_level_tier and at_level_tier and above_level_tier:
            st.markdown("### Ensuring Consistency Across Tiers")
            
            st.markdown("""
            Identify the elements that remain consistent across all three tiers to ensure 
            equivalent learning outcomes.
            """)
            
            learning_goals = st.text_area(
                "Common Learning Goals: What specific outcomes will all students achieve regardless of tier?",
                height=80,
                key="learning_goals"
            )
            
            key_content = st.text_area(
                "Essential Content: What core content will all students engage with across the tiers?",
                height=80,
                key="key_content"
            )
            
            assessment_approach = st.text_area(
                "Assessment Approach: How will you evaluate learning for all students despite different assignments?",
                height=80,
                key="assessment_approach"
            )
            
            # Check if consistency elements are addressed
            if learning_goals and key_content and assessment_approach:
                st.success("""
                Excellent work designing a comprehensive tiered assignment!
                
                Effective tiered assignments:
                - Maintain the integrity of key learning goals across all levels
                - Adjust complexity and support rather than changing essential content
                - Provide appropriate challenge for each readiness level
                - Allow all students to demonstrate mastery of the same core concepts
                
                When creating prompts for tiered assignments, be sure to explicitly request these 
                consistency elements to ensure alignment across the different versions.
                """)
    
    # Activity 3: Creating Interest-Based Choice Boards
    st.markdown("## Activity 3: Creating Interest-Based Choice Boards")
    
    st.markdown("""
    Choice boards allow students to select from multiple options based on their interests, learning 
    preferences, or strengths. This approach increases student engagement and ownership while still 
    ensuring essential learning outcomes.
    """)
    
    st.markdown("### Choice Board Structure")
    
    st.markdown("""
    Choice boards typically feature a grid of options that may be organized by:
    - Learning modality (visual, auditory, kinesthetic, etc.)
    - Multiple intelligences (linguistic, logical-mathematical, etc.)
    - Depth of knowledge levels (recall, skill/concept, strategic thinking, etc.)
    - Product type (written, visual, performance, technological, etc.)
    - Topic or subtopic within the content area
    """)
    
    # Choice board design activity
    st.markdown("### Design a Choice Board Prompt")
    
    st.markdown("""
    Create a prompt for generating an interest-based choice board for a topic in your teaching area.
    Focus on how you would structure the prompt to ensure the choice board offers meaningful options
    while maintaining consistent learning goals.
    """)
    
    choice_topic = st.text_input(
        "Topic for the choice board:",
        placeholder="e.g., Poetry Forms, States of Matter, Historical Revolutions",
        key="choice_topic"
    )
    
    if choice_topic:
        st.markdown("### Draft your prompt components:")
        
        persona_choice = st.text_area(
            "Persona: What type of educational specialist should the AI model embody?",
            height=80,
            key="persona_choice"
        )
        
        context_choice = st.text_area(
            "Context: What's the specific teaching situation and student needs?",
            height=100,
            key="context_choice"
        )
        
        task_choice = st.text_area(
            "Task: What specific type of choice board do you need?",
            height=80,
            key="task_choice"
        )
        
        format_choice = st.text_area(
            "Format: How should the choice board be structured?",
            height=120,
            key="format_choice"
        )
        
        reference_choice = st.text_area(
            "Reference Materials: What specific content, standards, or considerations should inform the board?",
            height=100,
            key="reference_choice"
        )
        
        # Assemble the prompt
        if persona_choice and context_choice and task_choice and format_choice and reference_choice:
            st.success("Here's your complete prompt for generating an interest-based choice board:")
            
            st.code(f"""
{persona_choice}

{context_choice}

{task_choice}

{format_choice}

{reference_choice}
            """)
            
            st.markdown("""
            #### Key Elements for Effective Choice Board Prompts
            
            A well-designed choice board prompt should:
            
            - Specify the organizing principle for the options (interest areas, learning modalities, etc.)
            - Request that all options address the same essential learning outcomes
            - Include clear parameters for what makes an acceptable choice
            - Maintain consistent difficulty level across different options
            - Include guidance for students on how to select appropriately challenging options
            
            Choice boards balance student agency with instructional focus, allowing personalization 
            without sacrificing alignment with learning goals.
            """)
    
    # Activity 4: Designing Adaptive Learning Pathways
    st.markdown("## Activity 4: Designing Adaptive Learning Pathways")
    
    st.markdown("""
    Adaptive learning pathways adjust content, pacing, and instructional approaches based on student 
    performance and needs. This approach to personalization is particularly powerful for skills that 
    build sequentially and for addressing gaps in prerequisite knowledge.
    """)
    
    st.markdown("### Components of Adaptive Pathways")
    
    st.markdown("""
    Effective adaptive learning pathways include:
    
    - **Pre-assessment** to determine appropriate entry points
    - **Multiple entry points** based on readiness level
    - **Branching decision points** that direct students based on performance
    - **Formative checkpoints** throughout the learning sequence
    - **Just-in-time support** for students who struggle with specific concepts
    - **Acceleration options** for students who demonstrate mastery
    - **Common end goals** despite different routes
    """)
    
    # Adaptive pathway design activity
    st.markdown("### Map an Adaptive Learning Pathway")
    
    st.markdown("""
    For a sequential skill or concept in your teaching area, create a visual map of an adaptive 
    learning pathway that accommodates different student needs.
    """)
    
    sequential_skill = st.text_input(
        "Sequential skill or concept:",
        placeholder="e.g., Fraction Operations, Paragraph Writing, Scientific Method",
        key="sequential_skill"
    )
    
    if sequential_skill:
        st.markdown("### Design your adaptive pathway components:")
        
        entry_diagnostic = st.text_area(
            "Pre-assessment: How will you determine students' starting points?",
            height=100,
            key="entry_diagnostic"
        )
        
        entry_points = st.text_area(
            "Entry Points: What are the different starting levels for students?",
            height=120,
            key="entry_points"
        )
        
        branch_points = st.text_area(
            "Branch Points: At what points will the pathway adapt based on student performance?",
            height=150,
            key="branch_points"
        )
        
        support_options = st.text_area(
            "Support Options: What interventions will be available for students who struggle?",
            height=120,
            key="support_options"
        )
        
        extension_options = st.text_area(
            "Extension Options: How will you accommodate students who demonstrate early mastery?",
            height=120,
            key="extension_options"
        )
        
        final_goal = st.text_area(
            "End Goal: What common outcome will all students reach, regardless of path?",
            height=100,
            key="final_goal"
        )
        
        # Check if pathway components are complete
        if (entry_diagnostic and entry_points and branch_points and 
            support_options and extension_options and final_goal):
            
            st.success("""
            Excellent work mapping an adaptive learning pathway!
            
            This type of detailed mapping helps you create more effective prompts for adaptive 
            learning experiences by:
            
            - Clearly identifying decision points where pathways should branch
            - Specifying the types of supports needed for different learning challenges
            - Maintaining focus on common end goals despite different routes
            - Balancing structure with responsiveness to student needs
            
            When creating prompts for adaptive pathways, include these key components to ensure 
            the generated materials provide truly responsive personalization.
            """)
            
            st.markdown("### Creating a Complete Adaptive Pathway Prompt")
            
            st.markdown("""
            Using the components you've mapped, draft a complete PCTFR prompt that would generate 
            an adaptive learning pathway for your selected skill.
            """)
            
            adaptive_prompt = st.text_area(
                "Complete Adaptive Pathway Prompt:",
                height=300,
                placeholder="Combine your pathway components into a complete PCTFR prompt...",
                key="adaptive_prompt"
            )
            
            if adaptive_prompt:
                st.success("""
                You've created a comprehensive prompt for an adaptive learning pathway!
                
                Adaptive approaches to personalization are particularly powerful because they:
                - Respond to student needs in real-time
                - Provide support exactly when and where it's needed
                - Prevent struggling students from falling further behind
                - Allow advanced students to progress without artificial constraints
                - Create efficiency by focusing instruction on actual needs
                
                This approach requires more complex prompt engineering but results in highly effective 
                personalized learning experiences.
                """)
    
    # Reflection and key takeaways
    st.markdown("## Activity Reflection")
    
    st.markdown("""
    Take a moment to reflect on what you've learned from these activities:
    
    1. **Learner profiles** provide the foundation for effective personalization by identifying the 
       specific needs, strengths, and preferences that should drive instructional decisions.
    
    2. **Tiered assignments** offer different levels of complexity and support while maintaining 
       consistent learning goals, allowing all students to engage appropriately with essential content.
    
    3. **Choice boards** provide structured options that increase student engagement and agency 
       while ensuring alignment with learning objectives.
    
    4. **Adaptive pathways** create responsive learning experiences that adjust based on student 
       performance, providing targeted support or extension exactly when needed.
    
    As you incorporate these personalization approaches into your prompt engineering, you'll create 
    more engaging, accessible, and effective learning experiences for all students.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Encourage participants to start with one approach to personalization rather than trying to implement everything at once
    * Remind participants that the PCTFR framework provides a consistent structure for different personalization approaches
    * Suggest focusing on high-impact areas where personalization will make the biggest difference for students
    * Emphasize that prompt engineering makes personalization more manageable by streamlining resource creation
    
    **Common Challenges:**
    
    * Managing the logistics of multiple versions or pathways in the classroom
    * Maintaining consistency in learning outcomes despite different routes
    * Determining which students need which level or type of personalization
    * Balancing personalization with practical classroom constraints
    
    **Extension Ideas:**
    
    * Have participants create a template for their most-used personalization approach that they can adapt for different content
    * Encourage mapping a complete unit with personalized elements from beginning to end
    * Suggest developing a protocol for determining which personalization approach is most appropriate for different learning goals
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