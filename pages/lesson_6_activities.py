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
    page_title="Lesson 6: Activities",
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
    "title": "Reference Materials: Activities",
    "lesson": "6",
    "section": "activities",
    "order": 3
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_6_activities"
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
    "lesson_6_activities",
    "activities",
    "Lesson 6 Activities",
    """
    **This section provides hands-on practice with reference materials in prompting.**
    
    You'll:
    - Identify suitable reference materials for different prompt purposes
    - Practice incorporating reference materials effectively
    - Create complete prompts that use reference materials with other prompt components
    
    Complete these activities to strengthen your understanding before 
    moving to the reflection.
    """
)

# Render the improved teacher controls in the sidebar
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
    
    Complete the activities below to practice incorporating reference materials in your prompts.
    After finishing these activities, proceed to the Reflection section to solidify your learning 
    and unlock the next lesson.
    """)
    
    # Activity 1
    st.markdown("## Activity 1: Identify Useful Reference Materials")
    
    st.markdown("""
    For each educational purpose, identify what specific reference materials would be most helpful
    to include in a prompt. Consider what sources would ensure your AI-generated content aligns with
    your curriculum and teaching needs.
    """)
    
    # Educational purpose 1
    st.markdown("### Educational Purpose 1: Creating a lesson on a key historical event")
    
    reference_materials1 = st.text_area(
        "List specific reference materials you would include:", 
        height=100,
        placeholder="Example: 1. State/district social studies standards for the grade level\n2. Specific textbook passages about the event\n3. Primary source documents relevant to the event\n4. Timeline of related historical developments\n5. Existing assessment rubric for historical analysis",
        key="reference_materials1"
    )
    
    if reference_materials1:
        st.success("You've identified potential reference materials! Let's analyze your choices:")
        
        st.markdown("""
        **Effective Reference Materials Checklist:**
        - Did you include curriculum standards to ensure alignment?
        - Did you consider both content sources (what to teach) and pedagogical sources (how to teach it)?
        - Are your selected materials specific and directly relevant to the purpose?
        - Would these materials help the AI understand the expected scope and sequence?
        - Are there any additional materials that might help with differentiation or assessment?
        """)
    
    # Educational purpose 2
    st.markdown("### Educational Purpose 2: Providing feedback on student lab reports")
    
    reference_materials2 = st.text_area(
        "List specific reference materials you would include:", 
        height=100,
        placeholder="Example: 1. Grading rubric for lab reports with detailed criteria\n2. Example of a high-quality lab report (anonymized)\n3. Common misconceptions or errors related to the lab topic\n4. Science vocabulary list relevant to the lab\n5. Learning objectives for the lab activity",
        key="reference_materials2"
    )
    
    if reference_materials2:
        st.success("You've identified potential reference materials! Let's analyze your choices:")
        
        st.markdown("""
        **Effective Reference Materials Checklist:**
        - Did you include assessment criteria to ensure clear evaluation standards?
        - Did you consider exemplars to guide the feedback quality and approach?
        - Are your selected materials specific enough to focus the feedback?
        - Would these materials help provide consistent feedback across students?
        - Have you included both content and format considerations?
        """)
    
    # Activity 2
    st.markdown("## Activity 2: Incorporate Reference Materials")
    
    st.markdown("""
    Practice incorporating reference materials into prompts. For the given educational scenario,
    enhance the basic prompt by effectively integrating the provided reference material.
    """)
    
    # Scenario with references
    st.markdown("""
    ### Scenario: Creating a math worksheet on fractions
    
    **Basic Prompt:**
    ```
    Create a math worksheet on fractions for 4th grade.
    ```
    
    **Available Reference Material:**
    ```
    4.NF.A.1 - Explain why a fraction a/b is equivalent to a fraction 
    (n × a)/(n × b) by using visual fraction models, with attention to how 
    the number and size of the parts differ even though the two fractions 
    themselves are the same size. Use this principle to recognize and 
    generate equivalent fractions.
    
    4.NF.A.2 - Compare two fractions with different numerators and different 
    denominators, e.g., by creating common denominators or numerators, or by 
    comparing to a benchmark fraction such as 1/2. Recognize that comparisons 
    are valid only when the two fractions refer to the same whole. Record the 
    results of comparisons with symbols >, =, or <, and justify the conclusions, 
    e.g., by using a visual fraction model.
    ```
    """)
    
    # User's enhanced prompt
    enhanced_prompt = st.text_area(
        "Your enhanced prompt with reference material:", 
        height=150,
        placeholder="Example: Create a math worksheet on fractions for 4th grade students that focuses on the following standards:\n\n[Insert standards here]\n\nThe worksheet should include problems that help students understand equivalent fractions through visual models and compare fractions with different numerators and denominators. Include examples that require students to record comparisons using >, =, and < symbols and justify their reasoning.",
        key="enhanced_prompt"
    )
    
    if enhanced_prompt:
        st.success("You've enhanced the prompt with reference materials! Let's analyze your approach:")
        
        st.markdown("""
        **Reference Integration Checklist:**
        - Did you clearly incorporate the standards language into your prompt?
        - Did you maintain the focus on both equivalent fractions and comparing fractions?
        - Did you include the requirement for visual models as specified in the standards?
        - Did you keep the mathematical symbols (>, =, <) and justification requirements?
        - Does your enhanced prompt align with the grade-level expectations in the standards?
        """)
    
    # Activity 3
    st.markdown("## Activity 3: Complete PCTFR Prompt Builder")
    
    st.markdown("""
    Create a complete prompt that includes Persona, Context, Task, Format, and Reference Materials.
    This activity brings together what you've learned through the first six lessons.
    """)
    
    # Educational purpose selection
    ed_purpose = st.selectbox(
        "Select an educational purpose:",
        [
            "Creating a lesson plan",
            "Developing an assessment",
            "Providing student feedback",
            "Designing learning materials",
            "Creating a rubric"
        ],
        key="ed_purpose"
    )
    
    # PCTFR components
    persona = st.text_area("Persona (role, communication style, perspective):", 
                         placeholder="Example: As an experienced science educator who emphasizes inquiry-based learning, uses clear explanations with supporting visuals, and encourages students to make real-world connections",
                         height=80,
                         key="persona")
    
    context = st.text_area("Context (background, audience, situation):", 
                          placeholder="Example: For a 7th-grade life science class studying cell structures and functions. Students have previously learned about the scientific method and basic microscope use but have limited prior knowledge about cells.",
                          height=80,
                          key="context")
    
    task = st.text_area("Task (what you want the AI to do):", 
                       placeholder="Example: Create a laboratory investigation guide for observing and identifying cellular structures",
                       height=80,
                       key="task")
    
    format_spec = st.text_area("Format (how you want it structured):", 
                             placeholder="Example: Structure the guide with: 1) A central driving question, 2) Background information (200-250 words), 3) A materials list with safety precautions, 4) Step-by-step procedures with estimated timing, 5) Observation tables for data collection, 6) Analysis questions of increasing complexity, and 7) A conclusion section connecting to the driving question",
                             height=100,
                             key="format_spec")
    
    reference = st.text_area("Reference Materials (specific content to incorporate):",
                           placeholder="Example: Base the content on these Next Generation Science Standards and our textbook excerpt:\n\nMS-LS1-1: Conduct an investigation to provide evidence that living things are made of cells; either one cell or many different numbers and types of cells.\n\nMS-LS1-2: Develop and use a model to describe the function of a cell as a whole and ways the parts of cells contribute to the function.\n\nTextbook excerpt: 'Plant cells can be distinguished from animal cells by the presence of cell walls and chloroplasts. The cell wall provides structural support while chloroplasts contain chlorophyll, which captures light energy for photosynthesis. Both plant and animal cells contain a nucleus, cell membrane, cytoplasm, mitochondria, and other organelles. The nucleus contains genetic material and directs cellular activities. Mitochondria are known as the powerhouse of the cell because they convert energy from food into a usable form called ATP.'",
                           height=150,
                           key="reference")
    
    # Show the complete prompt
    if persona and context and task and format_spec and reference:
        st.markdown("### Your Complete PCTFR Prompt:")
        
        complete_prompt = f"""Persona: {persona}

Context: {context}

Task: {task}

Format: {format_spec}

Reference: {reference}"""
        
        st.code(complete_prompt)
        
        st.markdown("""
        **Prompt Effectiveness Analysis:**
        
        Your prompt now combines all five essential elements:
        - **Persona** establishes who is communicating and how
        - **Context** provides the background information that shapes understanding
        - **Task** specifies what you want the AI to create
        - **Format** details exactly how you want the output structured
        - **Reference** ensures the content aligns with specific standards and materials
        
        This comprehensive approach creates highly tailored, appropriate content that communicates in the right voice and aligns perfectly with your curriculum.
        """)
    
    # Activity 4
    st.markdown("## Activity 4: Extract Key References")
    
    st.markdown("""
    An important skill in using reference materials is identifying and extracting the most relevant portions from longer documents.
    Practice selecting the most important elements from this curriculum document excerpt to include in a prompt.
    """)
    
    # Sample curriculum document
    st.markdown("""
    ### Sample Curriculum Guide Excerpt: Middle School Writing Program
    
    #### Section 3.2: Argumentative Writing - Grade 8
    
    **Learning Objectives:**
    By the end of the unit, students will be able to:
    * Write arguments to support claims with clear reasons and relevant evidence.
    * Introduce claim(s), acknowledge and distinguish the claim(s) from alternate or opposing claims, and organize the reasons and evidence logically.
    * Support claim(s) with logical reasoning and relevant evidence, using accurate, credible sources.
    * Use words, phrases, and clauses to create cohesion and clarify the relationships among claim(s), counterclaims, reasons, and evidence.
    * Establish and maintain a formal style.
    * Provide a concluding statement or section that follows from and supports the argument presented.
    
    **Key Vocabulary:**
    Claim, counterclaim, rebuttal, evidence, credibility, logical fallacy, ethos, pathos, logos, transition, coherence, formal style
    
    **Assessment Criteria:**
    * Clear thesis statement that makes a debatable claim (15%)
    * Logical organization of ideas with effective transitions (20%)
    * Quality and relevance of evidence to support claims (25%)
    * Recognition and response to counterclaims (15%)
    * Use of formal academic language and proper citations (15%)
    * Effective conclusion that addresses the significance of the argument (10%)
    
    **Common Student Challenges:**
    * Difficulty distinguishing between facts and opinions
    * Overreliance on personal anecdotes rather than authoritative sources
    * Weak or absent counterclaim section
    * Informal tone or inappropriate voice
    * Insufficient development of reasoning to connect evidence to claims
    
    **Suggested Teaching Sequence:**
    Week 1: Analyzing argumentative texts and identifying their components
    Week 2: Developing claims and gathering evidence
    Week 3: Organizing arguments and addressing counterclaims
    Week 4: Drafting, peer review, and revision
    Week 5: Final editing and publication
    """)
    
    # User's extracted references
    extracted_references = st.text_area(
        "Extract the most relevant sections to include in a prompt for creating an argumentative writing lesson:", 
        height=150,
        placeholder="Copy and paste the most important sections from the curriculum guide that would be essential for creating an aligned argumentative writing lesson.",
        key="extracted_references"
    )
    
    if extracted_references:
        st.success("You've extracted reference materials! Let's analyze your selections:")
        
        st.markdown("""
        **Effective Extraction Checklist:**
        - Did you include the core learning objectives to ensure alignment?
        - Did you select the assessment criteria to guide the lesson's focus?
        - Did you include common student challenges to address in the lesson?
        - Did you consider the key vocabulary that should be incorporated?
        - Did you maintain the appropriate grade level and curricular context?
        
        Selecting just the most relevant portions of a longer document helps create focused prompts without overwhelming the AI with unnecessary information.
        """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * For Activity 1, encourage participants to think about the actual curriculum documents, rubrics, and resources they use regularly
    * For Activity 2, discuss how reference materials can be incorporated without making prompts overly long or complex
    * For Activity 3, have participants share their PCTFR prompts and analyze how the reference materials enhance alignment
    * For Activity 4, emphasize the importance of selecting only the most relevant sections from longer documents
    
    **Common Challenges:**
    
    * Including too much reference material, which can overwhelm the AI
    * Not clearly indicating how the reference materials should be used in generating the response
    * Copying full documents rather than selecting the most relevant portions
    * Expecting the AI to perfectly understand complex curriculum documents without additional guidance
    
    **Extension Ideas:**
    
    * Have participants bring in their own curriculum documents or standards to practice extracting key elements
    * Create a shared resource library of effective reference materials for common educational tasks
    * Practice creating prompts that use reference materials to ensure differentiation for diverse learners
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

# Debug section at the bottom (now controlled by the teacher controls sidebar)
if st.session_state.get("show_debug", False):
    with st.expander("Debug Information", expanded=True):
        st.write("### Debug Info")
        st.write(f"Current Page: {current_page}")
        st.write(f"Current Directory: {current_dir}")
        st.write(f"Pages Directory: {os.path.join(current_dir, 'pages')}")
        st.write(f"sys.path: {sys.path}")
        st.write(f"All Pages: {all_pages}")
        st.write(f"Session State: {dict(st.session_state)}") 