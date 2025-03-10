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
    page_title="Lesson 18: Examples",
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
    "title": "Interdisciplinary Unit Design: Examples",
    "lesson": "18",
    "section": "examples",
    "order": 2
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_18_examples"
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
    "lesson_18_examples",
    "examples",
    "Lesson 18: Examples",
    """
    **This section provides examples of effective prompts for interdisciplinary unit design.**
    
    Each example demonstrates how to:
    - Structure prompts for different types of cross-disciplinary integration
    - Design learning experiences that maintain subject integrity while creating connections
    - Create assessments that evaluate both disciplinary and integrated learning
    - Apply the PCTFR framework to interdisciplinary contexts
    
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
    Below are examples of well-crafted prompts for creating interdisciplinary learning experiences 
    across various subject combinations and grade levels. Each example includes an analysis of the 
    prompt's key elements and what makes it effective for integrating multiple disciplines while 
    maintaining subject integrity.
    """)
    
    # Example 1: Science-ELA Integration
    st.markdown("## Example 1: Science-ELA Integration (Environmental Research Project)")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as an interdisciplinary curriculum specialist who designs integrated learning 
    experiences that connect scientific inquiry with communication skills while maintaining 
    disciplinary rigor in both areas.
    
    Context: I teach 5th grade in a self-contained classroom where I cover both science and ELA. 
    We're beginning a unit on ecosystems in science and informational writing in ELA. I want to 
    create an integrated research project where students investigate local ecosystems and create 
    informational texts about their findings, but I need to ensure that both science inquiry skills 
    and writing craft are developed with appropriate depth.
    
    Task: Create an integrated 3-week research project where students investigate a local ecosystem 
    (pond, forest, school yard, etc.), collect scientific data, and produce informational texts 
    about their findings. The project should develop both scientific practices and writing craft 
    while helping students see connections between these disciplines.
    
    Format: Design a project plan that includes:
    1. Essential questions that connect science and ELA learning
    2. Learning objectives from both science standards and ELA standards
    3. A sequence of 12-15 integrated lessons with brief descriptions
       - Science-focused lessons on ecosystem concepts and field research techniques
       - ELA-focused lessons on informational text structures and features
       - Integrated activities that connect scientific findings with writing development
    4. Formative assessment checkpoints for both science understanding and writing progress
    5. Scaffolding tools for scientific data collection and writing organization
    6. A final product specification with a rubric that evaluates both scientific accuracy and writing craft
    
    Each lesson should clearly identify which disciplinary skills are being developed while making 
    explicit connections between scientific thinking and communication skills. Include specific supports 
    for students who may struggle with either the science concepts or the writing demands.
    
    Reference Materials: The science standards address ecosystem interactions (5-LS2-1: Develop a model 
    to describe the movement of matter among plants, animals, decomposers, and the environment) and the 
    ELA standards focus on informational writing (W.5.2: Write informative/explanatory texts to examine 
    a topic and convey ideas and information clearly). Students have some experience with scientific 
    observation but need support with systematic data collection. In writing, they understand basic 
    paragraph structure but need help with organization, transitions, and domain-specific vocabulary. 
    Key ecosystem concepts include food webs, energy transfer, interdependence, and human impacts. Key 
    informational writing elements include text structures, transitions, precise language, and text features.
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Interdisciplinary Persona:**
        - Emphasizes integration expertise
        - Notes focus on maintaining rigor
        - Balances both subject areas
        
        **Detailed Classroom Context:**
        - Identifies specific grade and setup
        - Names concurrent content areas
        - Notes student experience level
        
        **Clear Integration Task:**
        - Specifies project-based approach
        - Focuses on local, accessible context
        - Balances science inquiry and writing
        """)
    
    with col2:
        st.markdown("""
        **Comprehensive Format Structure:**
        - Includes essential questions as organizers
        - Balances subject-specific and integrated lessons
        - Incorporates assessment for both areas
        - Includes scaffolding and differentiation
        
        **Detailed Reference Materials:**
        - Cites specific standards from both subjects
        - Notes student background in each area
        - Identifies key concepts in both disciplines
        - Highlights potential challenges
        """)
    
    # Example 2: Math-Social Studies Integration
    st.markdown("## Example 2: Math-Social Studies Integration (Data Analysis Unit)")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as a secondary curriculum designer who specializes in creating authentic 
    connections between mathematics and social studies that maintain the methodological 
    integrity of both disciplines.
    
    Context: I co-teach an 8th grade math and social studies block with a colleague. We're 
    planning a unit that integrates statistical analysis with the study of immigration patterns 
    and demographic change. Many of our students struggle to see the relevance of statistics 
    and need support connecting data analysis skills to meaningful social contexts.
    
    Task: Create a 3-week integrated unit that helps students develop statistical literacy while 
    examining immigration patterns in the United States from 1880-1920. The unit should help 
    students understand how mathematical tools can illuminate historical trends while also 
    appreciating the human stories behind the numbers.
    
    Format: Design an integrated unit plan that includes:
    1. Overarching essential questions that connect mathematical and historical inquiry
    2. Learning objectives from both math standards and social studies standards
    3. A sequence of 15 daily lessons with clear descriptions of:
       - Math-focused lessons on statistical concepts and data analysis techniques
       - History-focused lessons on immigration causes, patterns, and impacts
       - Integrated activities that apply statistical analysis to historical data
    4. Primary source documents and data sets at varied complexity levels
    5. Graphic organizers that help students connect quantitative and qualitative analysis
    6. Formative assessments that check understanding in both disciplines
    7. A culminating project where students analyze immigration data and present evidence-based conclusions
    
    Each lesson should clearly identify which disciplinary skills are being developed while making 
    explicit connections between mathematical thinking and historical understanding. The unit should 
    maintain appropriate mathematical rigor while ensuring the human context of immigration is not 
    reduced to just numbers.
    
    Reference Materials: Math standards include 8.SP.A.1 (Construct and interpret scatter plots), 
    8.SP.A.2 (Use the equation of a linear model to solve problems), and 8.SP.A.4 (Understand patterns 
    of association in bivariate categorical data). Social studies standards address the causes and 
    impacts of the "new immigration" from Southern and Eastern Europe, Ellis Island, settlement patterns, 
    and nativism. Students have prior knowledge of mean, median, and mode, but need support with 
    statistical displays, correlation, and drawing evidence-based conclusions. Historical context 
    should include push and pull factors for immigration, immigration legislation, and the social 
    impacts of demographic change. Key immigration groups include Italians, Jews, Poles, and Greeks.
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Specialized Integration Persona:**
        - Emphasizes secondary curriculum expertise
        - Notes focus on authentic connections
        - Stresses methodological integrity
        
        **Co-Teaching Context:**
        - Identifies block scheduling arrangement
        - Notes specific grade level and subjects
        - Addresses student engagement challenges
        
        **Balanced Integration Task:**
        - Specifies historical time period
        - Connects statistical skills to human context
        - Balances quantitative and qualitative elements
        """)
    
    with col2:
        st.markdown("""
        **Detailed Unit Structure:**
        - Includes essential questions as organizing framework
        - Balances discipline-specific and integrated lessons
        - Incorporates varied resource complexity
        - Connects assessment to both subject areas
        
        **Specific Content References:**
        - Cites exact standards from both disciplines
        - Notes prior knowledge and learning needs
        - Identifies key historical context elements
        - Specifies mathematical concepts to address
        """)
    
    # Example 3: Arts-Science Integration
    st.markdown("## Example 3: Arts-Science Integration (Light and Color Unit)")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as a STEAM education specialist who designs learning experiences that meaningfully 
    connect artistic and scientific practices while honoring the unique methodologies and ways of 
    knowing in each discipline.
    
    Context: I collaborate with the art teacher at my elementary school to create integrated units. 
    We're planning a 4-week exploration of light and color for 4th graders that will bridge their 
    science unit on the properties of light with visual arts instruction on color theory and technique. 
    We want students to understand both the scientific properties of light and color as well as their 
    artistic applications.
    
    Task: Create an integrated unit plan that helps students understand the science of light and color 
    while developing artistic skills in color mixing, application, and composition. The unit should 
    help students see connections between scientific understanding and artistic expression while 
    developing skills and knowledge in both areas.
    
    Format: Design a 4-week integrated unit plan with:
    1. Big ideas and essential questions that connect scientific and artistic concepts of light and color
    2. Learning objectives from both science standards and visual arts standards
    3. A sequence of 16 lessons (4 per week) that include:
       - Science investigations of light properties (reflection, refraction, spectrum)
       - Art studio experiences with color mixing, application techniques, and composition
       - Integrated activities that connect scientific principles with artistic practice
    4. Materials list and preparation guidelines for hands-on activities
    5. Visual resources showing both scientific diagrams and artistic examples
    6. Formative assessments for both scientific understanding and artistic development
    7. A culminating project where students create artwork that demonstrates understanding of both 
       color science and artistic principles
    
    The unit should maintain the integrity of both scientific inquiry and artistic processes, making 
    explicit connections between them without subordinating either discipline to the other. Include 
    differentiation strategies for students who may excel in one area but struggle in the other.
    
    Reference Materials: Science standards address the properties of light (4-PS4-2: Develop a model 
    to describe how light reflecting from objects and entering the eye allows objects to be seen) and 
    properties of color (4-PS4-1: Develop a model of waves to describe patterns in terms of amplitude 
    and wavelength). Art standards focus on color theory (primary/secondary/tertiary colors, color 
    mixing, warm/cool colors, tints, and shades) and composition principles. Key science concepts 
    include the visible spectrum, reflection, refraction, absorption, and how the eye perceives color. 
    Key art concepts include color wheel relationships, color mixing techniques, expressive properties 
    of color, and compositional use of color to create harmony, contrast, emphasis, and mood.
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **STEAM Integration Persona:**
        - Emphasizes STEAM education expertise
        - Notes focus on meaningful connections
        - Respects methodologies of both disciplines
        
        **Collaborative Teaching Context:**
        - Identifies teacher collaboration approach
        - Notes specific grade level
        - Establishes concurrent content areas
        
        **Balanced Integration Task:**
        - Connects scientific principles with artistic expression
        - Maintains dual focus on skills and concepts
        - Respects both disciplinary approaches
        """)
    
    with col2:
        st.markdown("""
        **Clear Unit Structure:**
        - Organizes with big ideas and essential questions
        - Balances science investigations and art studios
        - Includes visual resources for both areas
        - Maintains assessment in both disciplines
        
        **Specific Content References:**
        - Cites standards from both science and art
        - Details key scientific principles
        - Outlines essential art concepts
        - Connects complementary content areas
        """)
    
    # Example 4: Physical Education-Math Integration
    st.markdown("## Example 4: Physical Education-Math Integration (Sports Analytics Unit)")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as a physical education and mathematics integration specialist who designs active 
    learning experiences that develop mathematical thinking through authentic movement contexts.
    
    Context: I'm a middle school PE teacher working with a math teacher to create a cross-curricular 
    unit on sports analytics for our 7th graders. We want to help students see real-world applications 
    of statistics while also developing physical skills and sports understanding. Many of our students 
    are engaged in sports but don't see connections to mathematics, while others who enjoy math don't 
    always participate enthusiastically in physical activities.
    
    Task: Create a 2-week integrated unit that connects statistical concepts with physical education 
    through a sports analytics approach. Students should collect, analyze, and interpret data from 
    their own physical performances while developing both mathematical understanding and movement skills.
    
    Format: Design a 10-lesson unit plan (5 lessons per week) that includes:
    1. Learning objectives that address both PE standards and math standards
    2. A progression of physical activities where students generate performance data
    3. Connected mathematical lessons where students analyze their performance data
    4. Data collection tools appropriate for PE settings (simple, durable, efficient)
    5. Statistical analysis activities that increase in complexity
    6. Reflection questions that connect physical performance with data insights
    7. A culminating project where students use data to create improvement plans
    
    Each lesson should include both physical activity and mathematical thinking, with clear connections 
    between them. The physical activities should be accessible to students of varying athletic abilities, 
    and the data analysis should be scaffolded for different levels of mathematical readiness. Include 
    modifications for students with physical limitations.
    
    Reference Materials: PE standards address motor skill development, fitness concepts, and game strategy. 
    Math standards include 7.SP.A.1 (Understand that statistics can be used to gain information about a 
    population by examining a sample), 7.SP.A.2 (Use data from a random sample to draw inferences about 
    a population), and 7.SP.B.4 (Use measures of center and measures of variability for numerical data 
    from random samples to draw informal comparative inferences about two populations). Physical activities 
    could include basketball shooting, fitness testing, heart rate monitoring, running/jumping measurements, 
    or team sport performance. Students have prior knowledge of basic statistics (mean, median, mode, range) 
    but need support with sampling, variability, and drawing evidence-based conclusions.
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Specialized Integration Persona:**
        - Emphasizes PE-Math integration expertise
        - Focuses on active learning approaches
        - Connects movement contexts to math concepts
        
        **Teacher Collaboration Context:**
        - Identifies cross-curricular partnership
        - Notes student engagement patterns
        - Addresses diverse student interests
        
        **Authentic Integration Task:**
        - Uses sports analytics as relevant framework
        - Connects personal physical data to math
        - Balances skill development in both areas
        """)
    
    with col2:
        st.markdown("""
        **Practical Lesson Structure:**
        - Includes realistic PE data collection methods
        - Provides progressive complexity in analysis
        - Connects performance to improvement planning
        - Addresses physical activity and math in each lesson
        
        **Detailed Content Specifications:**
        - Cites specific math standards on statistics
        - Identifies potential physical activities
        - Notes prior knowledge and learning needs
        - Addresses physical modifications needs
        """)
    
    # Example 5: Humanities Integration (History-Literature)
    st.markdown("## Example 5: Humanities Integration (History-Literature)")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as a humanities curriculum specialist who designs integrated experiences that connect 
    historical context with literary analysis while maintaining disciplinary depth in both areas.
    
    Context: I teach a 10th grade humanities block that combines English and history instruction. 
    We're beginning a unit on the Harlem Renaissance, exploring both the historical context and literary/
    artistic movements. Students often struggle to make meaningful connections between historical events 
    and artistic/literary developments, seeing them as separate rather than interconnected.
    
    Task: Create a 4-week integrated humanities unit on the Harlem Renaissance that helps students 
    understand how historical forces shaped artistic expression and how literature and art provide 
    insight into historical experiences. The unit should develop students' skills in both historical 
    analysis and literary interpretation.
    
    Format: Design a comprehensive unit plan that includes:
    1. Essential questions that bridge historical understanding and literary analysis
    2. Learning objectives from both history standards and English/literature standards
    3. A sequence of 20 lessons (5 per week) that include:
       - Historical context lessons on Great Migration, urban life, and racial dynamics
       - Literary analysis lessons focusing on poetry, fiction, and essays
       - Visual and performing arts connections including music, dance, and visual art
       - Integrated activities that explicitly connect historical factors with artistic expression
    4. Primary and secondary sources at varied complexity levels
    5. Discussion protocols that integrate historical and literary perspectives
    6. Formative assessments for both historical understanding and literary analysis
    7. A culminating project where students analyze a Harlem Renaissance work in its historical context
    
    Each lesson should clearly identify which disciplinary skills are being developed while making 
    explicit connections between historical factors and artistic responses. The unit should maintain 
    appropriate depth in both disciplines while helping students see their interconnections.
    
    Reference Materials: History standards address the Great Migration, urbanization, segregation, 
    and the social/cultural developments of the 1920s. English standards focus on analyzing how authors' 
    choices reflect historical and cultural contexts (RL.9-10.6), analyzing thematic development (RL.9-10.2), 
    and evaluating authors' perspectives and purposes. Key historical concepts include push/pull factors 
    of migration, discrimination and segregation, economic opportunity, and community development. Key 
    literary figures include Langston Hughes, Zora Neale Hurston, Claude McKay, Countee Cullen, and Nella 
    Larsen. Visual arts connections include Aaron Douglas, Jacob Lawrence, and Augusta Savage. Musical 
    connections include jazz, blues, and spirituals. Students have prior knowledge of WWI and basic literary 
    analysis skills but need support with contextual analysis.
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Humanities Specialist Persona:**
        - Emphasizes integrated humanities approach
        - Notes focus on maintaining disciplinary depth
        - Balances historical and literary expertise
        
        **Block Scheduling Context:**
        - Identifies humanities block arrangement
        - Notes specific integration challenges
        - Establishes grade level and content focus
        
        **Balanced Integration Task:**
        - Focuses on historical-literary connections
        - Examines influence in both directions
        - Maintains dual skill development focus
        """)
    
    with col2:
        st.markdown("""
        **Comprehensive Unit Structure:**
        - Uses essential questions as organizing framework
        - Balances historical and literary content
        - Includes multimodal artistic connections
        - Maintains assessment in both disciplines
        
        **Rich Content References:**
        - Names specific historical developments
        - Lists key literary and artistic figures
        - Identifies relevant standards
        - Notes prior knowledge and learning needs
        """)
    
    # Example 6: Elementary Integration Across Multiple Subjects
    st.markdown("## Example 6: Elementary Integration Across Multiple Subjects")
    
    st.markdown("#### Prompt:")
    
    st.markdown("""
    ```
    Persona: Act as an elementary education specialist who designs thematic units that meaningfully 
    integrate multiple subject areas while ensuring appropriate skill development in each discipline.
    
    Context: I teach 3rd grade in a self-contained classroom and am planning our 6-week ocean unit. 
    I want to integrate science, ELA, math, and social studies around this theme, but I need help 
    designing meaningful connections that don't sacrifice learning in any area. My students have diverse 
    learning needs and interests.
    
    Task: Create a 6-week integrated thematic unit on oceans that develops grade-appropriate skills 
    and knowledge across multiple subject areas. The unit should help students see connections between 
    disciplines while ensuring they develop the specific skills required in each subject area.
    
    Format: Design a comprehensive unit plan that includes:
    1. Overarching essential questions that connect all subject areas
    2. Learning objectives from science, ELA, math, and social studies standards
    3. A weekly overview showing integration points (30 lessons total):
       - Science: Ocean habitats, marine life, conservation, and water properties
       - ELA: Ocean-themed literature, informational reading, and writing
       - Math: Data collection, measurement, graphing, and problem-solving
       - Social Studies: Ocean industries, maritime history, and geography
    4. Daily lesson plans with clear subject focus and cross-curricular connections
    5. Differentiated learning activities for varied readiness levels
    6. Formative assessments for each subject area
    7. A culminating project that synthesizes learning across disciplines
    
    The unit should maintain appropriate content depth and skill development in each subject area while 
    helping students see meaningful connections. Include strategies for balancing focused skill instruction 
    with integrated thematic exploration.
    
    Reference Materials: Science standards address ocean habitats, marine organisms, and conservation 
    (3-LS4-3, 3-LS4-4). ELA standards focus on informational text features (RI.3.5), writing informative 
    texts (W.3.2), and comparing themes in stories (RL.3.9). Math standards include representing and 
    interpreting data (3.MD.B.3, 3.MD.B.4) and measurement (3.MD.A.2). Social studies standards address 
    geography, natural resources, and human impact on environments. Students have varied reading levels 
    (1st-4th grade equivalent) and different background knowledge about oceans. Key science concepts 
    include food webs, adaptations, habitats, and conservation. Integration opportunities include marine 
    life data collection and graphing, ocean narrative and informational writing, map skills, and research 
    projects.
    ```
    """)
    
    st.markdown("#### What Makes This Prompt Effective:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Elementary Integration Persona:**
        - Emphasizes thematic approach expertise
        - Notes focus on meaningful integration
        - Stresses skill development across subjects
        
        **Self-Contained Classroom Context:**
        - Identifies elementary grade level
        - Notes specific timeframe and theme
        - Acknowledges diverse learning needs
        
        **Multi-Subject Integration Task:**
        - Balances four core subject areas
        - Focuses on ocean theme across disciplines
        - Emphasizes both connections and subject integrity
        """)
    
    with col2:
        st.markdown("""
        **Comprehensive Unit Structure:**
        - Uses weekly organization with subject breakdown
        - Balances subject-specific and integrated elements
        - Includes differentiation across subjects
        - Maintains assessment in each discipline
        
        **Specific Standard References:**
        - Cites exact standards from multiple subjects
        - Notes reading level variations
        - Identifies key concepts in each area
        - Suggests specific integration opportunities
        """)
    
    # Key Takeaways Section
    st.markdown("## Key Takeaways from Examples")
    
    st.markdown("""
    ### Effective Prompts for Interdisciplinary Unit Design:
    
    * **Specify the integration approach** (multidisciplinary, interdisciplinary, transdisciplinary)
    * **Identify the organizational framework** (essential questions, themes, problems, etc.)
    * **Balance disciplinary integrity with meaningful connections**
    * **Address standards and learning objectives from each discipline**
    * **Include assessment strategies for both disciplinary and integrated learning**
    * **Request explicit connection points** between subject areas
    * **Provide specific content references** from each discipline
    
    ### The Power of the PCTFR Framework for Interdisciplinary Design:
    
    * **Persona:** Defines the integration approach and disciplinary expertise lens
    * **Context:** Establishes teaching arrangement, student needs, and logistical constraints
    * **Task:** Specifies the type of integration and its learning goals
    * **Format:** Provides detailed structure for the unit and its components
    * **Reference Materials:** Ensures content accuracy and standards alignment across multiple disciplines
    
    In the next section, you'll have the opportunity to practice creating your own prompts for
    interdisciplinary learning experiences that address your specific teaching context.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Encourage participants to note which integration approaches might work best in their teaching context
    * Point out how each example maintains disciplinary integrity while creating meaningful connections
    * Emphasize that the degree of integration can vary based on logistical constraints and learning goals
    * Highlight how these prompts create starting points that teachers should always review and adapt
    
    **Common Questions:**
    
    * "How do I find time for interdisciplinary teaching?" — Start with small integration points in existing units
    * "What if I don't have the content knowledge for all disciplines?" — Consider collaborative planning with colleagues
    * "How do I balance breadth and depth?" — Focus on authentic connection points rather than forcing integration
    
    **Extension Activity:**
    
    Have participants identify one example that most closely aligns with their teaching context, then modify it by:
    1. Changing the disciplines to match their teaching situation
    2. Adjusting the integration approach to suit their students' needs
    3. Adding specific content references relevant to their curriculum
    
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