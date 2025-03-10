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
    page_title="Lesson 13: Activities",
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
    "title": "Lesson Planning and Assessment Creation: Activities",
    "lesson": "13",
    "section": "activities",
    "order": 3
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_13_activities"
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
    "lesson_13_activities",
    "activities",
    "Lesson Planning and Assessment Creation: Activities",
    """
    **This section provides hands-on practice with prompt engineering for curriculum development.**
    
    You'll:
    - Create effective prompts for lesson plans and assessments
    - Practice applying different techniques for specific educational needs
    - Develop a personal prompt template library for your teaching context
    - Evaluate and improve prompt designs for better results
    
    Complete these activities to strengthen your curriculum development skills before
    moving to the reflection section.
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
    
    Complete the activities below to practice creating effective prompts for lesson plans and assessments.
    After finishing these activities, proceed to the Reflection section to consolidate your learning 
    and unlock the next lesson.
    """)
    
    # Activity 1: Prompt Analysis and Improvement
    st.markdown("## Activity 1: Prompt Analysis and Improvement")
    
    st.markdown("""
    In this activity, you'll analyze a basic prompt for lesson planning and improve it using the 
    techniques we've covered. This exercise will help you understand how to transform general prompts
    into highly effective ones.
    """)
    
    st.markdown("### Basic Prompt for Analysis:")
    
    st.code("""
    Create a lesson plan about fractions for elementary students.
    """, language="text")
    
    st.markdown("""
    ### Analyze the Basic Prompt:
    
    Identify what's missing or could be improved in the basic prompt above:
    """)
    
    st.checkbox("Lacks specific grade level", key="missing1")
    st.checkbox("No mention of standards alignment", key="missing2")
    st.checkbox("Doesn't specify lesson duration or format", key="missing3")
    st.checkbox("No context about student characteristics or needs", key="missing4")
    st.checkbox("Doesn't indicate which aspect of fractions to focus on", key="missing5")
    st.checkbox("No information about available resources", key="missing6")
    st.checkbox("No persona or role specification", key="missing7")
    
    st.markdown("### Now, Transform the Prompt:")
    
    st.markdown("""
    Rewrite the basic prompt by adding PTC-FREI elements, specific details, and structure to make it 
    more effective. Use the sections below to build your improved prompt.
    """)
    
    # Persona component
    persona = st.text_area(
        "**Persona:** (Specify the role/expertise the AI should adopt)",
        placeholder="Act as an experienced elementary math teacher who...",
        height=80,
        key="persona_component"
    )
    
    # Task component
    task = st.text_area(
        "**Task:** (Clearly define what you want the AI to create)",
        placeholder="Create a detailed lesson plan about comparing fractions with...",
        height=80,
        key="task_component"
    )
    
    # Context component
    context = st.text_area(
        "**Context:** (Provide relevant background information)",
        placeholder="This is for a 3rd-grade class with 25 students, including...",
        height=80,
        key="context_component"
    )
    
    # Format component
    format = st.text_area(
        "**Format:** (Specify the structure and organization)",
        placeholder="Organize the lesson plan with the following sections: 1. Lesson Overview...",
        height=120,
        key="format_component"
    )
    
    # Reference component
    reference = st.text_area(
        "**Reference:** (Include standards or resources to incorporate)",
        placeholder="Align with Common Core Standard 3.NF.A.3: Explain equivalence of fractions...",
        height=80,
        key="reference_component"
    )
    
    # Display complete improved prompt
    if persona and task and context and format:
        st.success("You've built a more effective prompt! Here's your complete prompt:")
        
        improved_prompt = f"""
        [{persona.strip()}]
        
        [{task.strip()}]
        
        [{context.strip()}]
        
        [{format.strip()}]
        """
        
        if reference:
            improved_prompt += f"\n\n[{reference.strip()}]"
        
        st.code(improved_prompt, language="text")
        
        st.markdown("""
        ### Improvements in Your Prompt:
        
        Your enhanced prompt is much more likely to generate a useful, tailored lesson plan because:
        
        1. **Specificity:** You've defined exactly what aspect of fractions to focus on and for which grade level
        
        2. **Context Awareness:** You've provided information about student characteristics and classroom environment
        
        3. **Clear Structure:** You've outlined the specific format and sections you want in the lesson plan
        
        4. **Standards Alignment:** You've included curriculum standards to ensure relevance
        
        5. **Expert Voice:** You've specified a persona with relevant expertise to enhance the quality
        """)
    
    # Activity 2: Assessment Prompt Builder
    st.markdown("## Activity 2: Assessment Prompt Builder")
    
    st.markdown("""
    In this activity, you'll build a prompt specifically designed to create a high-quality assessment.
    Different assessment types and purposes require different prompt approaches.
    """)
    
    # Assessment context selection
    assessment_context = st.selectbox(
        "Choose an assessment context to work with:",
        [
            "Select a context...",
            "Formative quiz for checking understanding mid-unit",
            "Summative test for end-of-unit evaluation",
            "Performance task for project-based assessment",
            "Exit ticket for quick daily check-in",
            "Pre-assessment for gauging prior knowledge"
        ],
        key="assessment_context"
    )
    
    if assessment_context and assessment_context != "Select a context...":
        st.markdown(f"### Building an Assessment Prompt for: {assessment_context}")
        
        # Subject area and grade level
        col1, col2 = st.columns(2)
        
        with col1:
            subject = st.selectbox(
                "Subject Area:",
                ["Mathematics", "Science", "English/Language Arts", "Social Studies", "Foreign Language", "Arts", "Physical Education"],
                key="subject_area"
            )
        
        with col2:
            grade = st.selectbox(
                "Grade Level:",
                ["Elementary (K-2)", "Elementary (3-5)", "Middle School (6-8)", "High School (9-12)"],
                key="grade_level"
            )
        
        # Assessment characteristics
        st.markdown("### Assessment Characteristics:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Question Types to Include:**")
            mc = st.checkbox("Multiple Choice", key="mc")
            sa = st.checkbox("Short Answer", key="sa")
            essay = st.checkbox("Extended Response/Essay", key="essay")
            matching = st.checkbox("Matching", key="matching")
            performance = st.checkbox("Performance Task", key="performance")
        
        with col2:
            st.markdown("**Cognitive Levels to Target:**")
            remember = st.checkbox("Remember/Recall", key="remember")
            understand = st.checkbox("Understand/Comprehend", key="understand")
            apply = st.checkbox("Apply", key="apply")
            analyze = st.checkbox("Analyze", key="analyze")
            evaluate = st.checkbox("Evaluate", key="evaluate")
            create = st.checkbox("Create", key="create")
        
        # Assessment details and techniques
        st.markdown("### Additional Details and Techniques:")
        
        include_rubric = st.checkbox("Include scoring rubrics or answer keys", key="include_rubric")
        include_examples = st.checkbox("Include few-shot examples of questions", key="include_examples")
        differentiation = st.checkbox("Request differentiation options", key="differentiation")
        tech_integration = st.checkbox("Incorporate digital tools or technology", key="tech_integration")
        
        # Learning objectives
        learning_objectives = st.text_area(
            "Specific Learning Objectives:",
            placeholder="Students will be able to...",
            height=100,
            key="learning_objectives"
        )
        
        # Generate prompt button
        if st.button("Generate Assessment Prompt", key="generate_assessment"):
            # Check if learning objectives are provided
            if not learning_objectives:
                st.warning("Please specify at least one learning objective to generate a meaningful prompt.")
            else:
                # Begin building the prompt
                assessment_prompt = "Create a"
                
                # Add assessment type
                if "formative" in assessment_context.lower():
                    assessment_prompt += " formative assessment"
                elif "summative" in assessment_context.lower():
                    assessment_prompt += " summative assessment"
                elif "performance" in assessment_context.lower():
                    assessment_prompt += " performance-based assessment"
                elif "exit" in assessment_context.lower():
                    assessment_prompt += "n exit ticket"
                elif "pre-assessment" in assessment_context.lower():
                    assessment_prompt += " pre-assessment"
                else:
                    assessment_prompt += "n assessment"
                
                # Add subject and grade level
                assessment_prompt += f" for {grade} {subject}"
                
                # Add learning objectives
                assessment_prompt += f" aligned with the following learning objectives:\n{learning_objectives}\n\n"
                
                # Add question types
                question_types = []
                if mc:
                    question_types.append("multiple-choice questions")
                if sa:
                    question_types.append("short-answer questions")
                if essay:
                    question_types.append("extended response/essay questions")
                if matching:
                    question_types.append("matching questions")
                if performance:
                    question_types.append("performance tasks")
                
                if question_types:
                    assessment_prompt += "Include the following question types:\n"
                    for qt in question_types:
                        assessment_prompt += f"- {qt}\n"
                    assessment_prompt += "\n"
                
                # Add cognitive levels
                cognitive_levels = []
                if remember:
                    cognitive_levels.append("Remember/Recall")
                if understand:
                    cognitive_levels.append("Understand/Comprehend")
                if apply:
                    cognitive_levels.append("Apply")
                if analyze:
                    cognitive_levels.append("Analyze")
                if evaluate:
                    cognitive_levels.append("Evaluate")
                if create:
                    cognitive_levels.append("Create")
                
                if cognitive_levels:
                    assessment_prompt += "Ensure questions target the following cognitive levels:\n"
                    for cl in cognitive_levels:
                        assessment_prompt += f"- {cl}\n"
                    assessment_prompt += "\n"
                
                # Add additional requirements
                additional_reqs = []
                if include_rubric:
                    additional_reqs.append("Include detailed scoring rubrics or answer keys for each question type")
                if include_examples:
                    additional_reqs.append("Provide example questions with ideal responses to illustrate quality expectations")
                if differentiation:
                    additional_reqs.append("Include modifications for diverse learners (e.g., ELLs, students with IEPs)")
                if tech_integration:
                    additional_reqs.append("Suggest digital tools or platforms that could be used to deliver this assessment")
                
                if additional_reqs:
                    assessment_prompt += "Additional requirements:\n"
                    for req in additional_reqs:
                        assessment_prompt += f"- {req}\n"
                
                # Display the generated prompt
                st.success("Your assessment prompt is ready!")
                st.code(assessment_prompt, language="text")
                
                st.markdown("""
                ### Next Steps:
                
                1. **Review the prompt** for any missing details or specifications
                2. **Consider adding a specific persona** (e.g., "Act as an experienced assessment specialist...")
                3. **Add format requirements** if you have preferences for how the assessment should be structured
                4. **Copy and use this prompt** with your preferred AI tool to generate the assessment
                """)
    
    # Activity 3: Differentiation and Modification Prompt Template
    st.markdown("## Activity 3: Differentiation and Modification Prompt Template")
    
    st.markdown("""
    Creating materials that support diverse learners is a critical teaching skill. In this activity,
    you'll develop a prompt template specifically designed to generate differentiated versions of
    a lesson or activity.
    """)
    
    st.markdown("""
    ### Scenario:
    
    You have a standard lesson or activity that you want to modify for diverse learners.
    Create a prompt template that will help you generate differentiated versions of this material.
    """)
    
    # Original material description
    original_material = st.text_area(
        "Briefly describe the original material you want to differentiate:",
        placeholder="e.g., A reading comprehension activity on a 7th-grade level text about photosynthesis with 5 analysis questions...",
        height=80,
        key="original_material"
    )
    
    # Student needs selection
    st.markdown("### Select the student needs you want to address:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Learning Profiles:**")
        english_learners = st.checkbox("English Language Learners", key="ell")
        reading_support = st.checkbox("Reading Support Needs", key="reading")
        advanced_learners = st.checkbox("Advanced/Gifted Learners", key="advanced")
        attention_needs = st.checkbox("Attention/Focus Needs", key="attention")
    
    with col2:
        st.markdown("**Other Considerations:**")
        visual_learners = st.checkbox("Visual Learners", key="visual")
        auditory_learners = st.checkbox("Auditory Learners", key="auditory")
        kinesthetic_learners = st.checkbox("Kinesthetic Learners", key="kinesthetic")
        executive_function = st.checkbox("Executive Function Support", key="executive")
    
    # Differentiation approach
    diff_approach = st.radio(
        "Preferred differentiation approach:",
        ["Tiered Activities (same goal, different levels)", "Multiple Means of Representation", "Multiple Means of Expression", "Scaffolded Support"],
        key="diff_approach"
    )
    
    # Generate template button
    if st.button("Generate Differentiation Prompt Template", key="generate_diff"):
        if not original_material:
            st.warning("Please describe the original material you want to differentiate.")
        else:
            # Build the persona component based on selections
            persona = "Act as an educational specialist with expertise in differentiated instruction"
            
            if english_learners or reading_support or advanced_learners or attention_needs:
                persona += " who specializes in supporting"
                needs = []
                if english_learners:
                    needs.append("English Language Learners")
                if reading_support:
                    needs.append("students with reading challenges")
                if advanced_learners:
                    needs.append("advanced/gifted learners")
                if attention_needs:
                    needs.append("students with attention/focus needs")
                persona += " " + ", ".join(needs)
            
            persona += "."
            
            # Build the task component
            task = f"Create differentiated versions of the following material: {original_material}"
            
            # Build the context component
            context = "I need to support diverse learners in my classroom, including"
            learning_profiles = []
            if english_learners:
                learning_profiles.append("English Language Learners")
            if reading_support:
                learning_profiles.append("students who need reading support")
            if advanced_learners:
                learning_profiles.append("students who need additional challenge")
            if attention_needs:
                learning_profiles.append("students with attention/focus needs")
            if visual_learners:
                learning_profiles.append("visual learners")
            if auditory_learners:
                learning_profiles.append("auditory learners")
            if kinesthetic_learners:
                learning_profiles.append("kinesthetic learners")
            if executive_function:
                learning_profiles.append("students who need executive function support")
            
            if learning_profiles:
                context += " " + ", ".join(learning_profiles) + "."
            else:
                context += " diverse learners with different needs and strengths."
            
            # Build the format component based on differentiation approach
            format = "Provide the following differentiated versions of the material:\n\n"
            
            if diff_approach == "Tiered Activities (same goal, different levels)":
                format += """1. TIER 1 (FOUNDATIONAL LEVEL):
   - Modified version for students who need additional support
   - Key scaffolds or accommodations included
   - Essential learning preserved
   - Visual or organizational supports

2. TIER 2 (GRADE LEVEL):
   - Standard version of the material
   - Moderate supports built in
   - Options for multiple means of engagement

3. TIER 3 (ADVANCED LEVEL):
   - Extended version for students who need additional challenge
   - Higher-order thinking requirements
   - Opportunities for deeper application or creativity
   - Increased complexity or abstraction"""

            elif diff_approach == "Multiple Means of Representation":
                format += """1. VISUAL REPRESENTATION:
   - Present the key content using visual formats (diagrams, charts, etc.)
   - Include color-coding or visual organization strategies
   - Provide graphic organizers or visual supports

2. AUDITORY REPRESENTATION:
   - Structure the content for auditory learners
   - Include discussion prompts or audio-based activities
   - Suggest read-aloud approaches or verbal processing

3. KINESTHETIC/TACTILE REPRESENTATION:
   - Transform the content into hands-on activities
   - Include movement-based learning options
   - Provide manipulatives or physical models to represent concepts"""

            elif diff_approach == "Multiple Means of Expression":
                format += """1. WRITTEN EXPRESSION OPTION:
   - How students can demonstrate learning through writing
   - Modifications for different writing levels
   - Templates or organizers for written responses

2. VERBAL EXPRESSION OPTION:
   - How students can demonstrate learning through speaking
   - Discussion or presentation formats
   - Supporting structures for verbal sharing

3. CREATIVE/MULTIMEDIA EXPRESSION OPTION:
   - How students can demonstrate learning through creative projects
   - Digital or artistic expression options
   - Alternative assessment approaches"""

            elif diff_approach == "Scaffolded Support":
                format += """1. SUBSTANTIAL SUPPORT VERSION:
   - Step-by-step breakdown of processes
   - Simplified language and reduced cognitive load
   - Essential content preserved but streamlined
   - Visual supports and clear structure

2. MODERATE SUPPORT VERSION:
   - Guided approach with some scaffolding
   - Prompts and hints for challenging aspects
   - Models or examples to follow
   - Check-in points for understanding

3. MINIMAL SUPPORT/EXTENSION VERSION:
   - Limited guidance for independent learners
   - Extension opportunities for deeper thinking
   - Open-ended exploration options
   - Complexity preserved or enhanced"""
            
            format += "\n\nFor EACH version, include:\n- Specific modifications made and why\n- Implementation suggestions\n- Materials or resources needed\n- Success criteria appropriate for that level"
            
            # Assemble the full template
            diff_template = f"{persona}\n\n{task}\n\n{context}\n\n{format}"
            
            # Display the template
            st.success("Your differentiation prompt template is ready!")
            st.code(diff_template, language="text")
            
            st.markdown("""
            ### Using Your Template:
            
            1. **Copy this template** and customize it further for your specific needs
            2. **Be specific** about the original material and learning objectives
            3. **Adjust the student profiles** as needed for your particular class
            4. **Review and refine** the generated differentiated materials
            5. **Save effective prompts** in your personal prompt library for future use
            """)
    
    # Activity 4: Personal Prompt Library Builder
    st.markdown("## Activity 4: Personal Prompt Library Builder")
    
    st.markdown("""
    In this activity, you'll start building a personal library of effective prompts for curriculum development
    that you can reuse and adapt for different contexts.
    """)
    
    st.markdown("""
    ### Select a curriculum development task you frequently perform:
    """)
    
    curriculum_task = st.selectbox(
        "Common curriculum task:",
        [
            "Daily lesson planning",
            "Unit planning",
            "Creating formative assessments",
            "Developing summative assessments",
            "Creating differentiated materials",
            "Designing project-based learning activities",
            "Building rubrics and scoring guides",
            "Creating student worksheets and handouts",
            "Developing discussion questions",
            "Creating digital learning materials"
        ],
        key="curriculum_task"
    )
    
    if curriculum_task:
        st.markdown(f"### Creating a Reusable Prompt Template for: {curriculum_task}")
        
        st.markdown("""
        To create an effective reusable template, focus on creating a general structure with placeholders
        that you can quickly customize for different topics or contexts.
        """)
        
        # Template approach
        template_approach = st.radio(
            "Template approach:",
            ["Full PTC-FREI Framework", "Task and Format Focus", "Simple Fill-in-the-Blank"],
            key="template_approach"
        )
        
        if template_approach == "Full PTC-FREI Framework":
            # Display a PTC-FREI template with placeholders
            template = f"""
            [Persona] Act as an experienced educator with expertise in [SUBJECT AREA] and [SPECIFIC EXPERTISE].
            
            [Task] Create a {curriculum_task.lower()} about [SPECIFIC TOPIC] for [GRADE LEVEL] students.
            
            [Context] This is for a class with [CLASS DESCRIPTION] students. They have prior knowledge of [PRIOR KNOWLEDGE], but need support with [LEARNING NEEDS]. Available resources include [AVAILABLE RESOURCES].
            
            [Format] Structure the {curriculum_task.lower().replace("creating ", "").replace("developing ", "")} as follows:
            
            1. [SECTION 1 NAME]
               - [SECTION 1 COMPONENT 1]
               - [SECTION 1 COMPONENT 2]
            
            2. [SECTION 2 NAME]
               - [SECTION 2 COMPONENT 1]
               - [SECTION 2 COMPONENT 2]
            
            [Additional sections as needed...]
            
            [Reference] Align with the following standards or resources:
            - [STANDARD/RESOURCE 1]
            - [STANDARD/RESOURCE 2]
            """
            
        elif template_approach == "Task and Format Focus":
            # Display a simplified template focusing on task and format
            template = f"""
            Create a {curriculum_task.lower()} about [TOPIC] for [GRADE LEVEL] students.
            
            The {curriculum_task.lower().replace("creating ", "").replace("developing ", "")} should:
            - Be appropriate for [STUDENT DESCRIPTION]
            - Focus on [SPECIFIC LEARNING OBJECTIVES]
            - Include [KEY COMPONENTS]
            - Align with [STANDARDS]
            
            Structure the {curriculum_task.lower().replace("creating ", "").replace("developing ", "")} with the following sections:
            
            1. [SECTION 1 NAME]
            2. [SECTION 2 NAME]
            3. [SECTION 3 NAME]
            
            Include [SPECIFIC REQUIREMENTS] for each section.
            """
            
        else:  # Simple Fill-in-the-Blank
            # Display a very simple template
            template = f"""
            Create a {curriculum_task.lower()} on _____ for _____ grade students.
            
            The {curriculum_task.lower().replace("creating ", "").replace("developing ", "")} should cover:
            1. _____
            2. _____
            3. _____
            
            Make sure to include _____ and align with _____ standards.
            """
        
        # Display the template with an editable text area
        st.markdown("### Your Customizable Template:")
        
        custom_template = st.text_area(
            "Edit this template to suit your specific needs:",
            template,
            height=300,
            key="custom_template"
        )
        
        # Template usage guidance
        st.markdown("""
        ### Using Your Template Library:
        
        1. **Save these templates** in a document or note-taking system for quick access
        
        2. **Create subject-specific versions** for different courses you teach
        
        3. **Update them periodically** as you discover more effective prompting strategies
        
        4. **Share effective templates** with colleagues to save them time
        
        5. **Create a system** for categorizing and retrieving templates when needed
        
        Building a personal prompt library will make you increasingly efficient at generating
        high-quality educational materials with AI assistance.
        """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Encourage participants to focus on creating prompts that align with their specific curriculum and teaching style
    * Emphasize the importance of starting with clear learning objectives when creating any prompt for curriculum materials
    * Suggest collaborative prompt development among grade-level or subject-area teams for consistency
    * Point out that saved prompts can be incrementally improved over time based on the quality of results
    
    **Common Challenges:**
    
    * Some participants may struggle with the technical language of prompt components - encourage them to focus on simply being clear and specific
    * Others may have difficulty creating reusable templates - suggest focusing on common elements across lessons
    * Participants might need help balancing structure and flexibility in their prompts
    
    **Extension Ideas:**
    
    * Challenge participants to create prompts for a complete unit or sequence of lessons rather than just individual components
    * Suggest developing prompts for interdisciplinary or cross-curricular materials
    * Encourage experimentation with different personas to see which produce the most effective results for their context
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