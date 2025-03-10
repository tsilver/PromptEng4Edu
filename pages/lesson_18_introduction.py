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
    page_title="Lesson 18: Introduction",
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
    "title": "Interdisciplinary Unit Design: Introduction",
    "lesson": "18",
    "section": "introduction",
    "order": 1
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_18_introduction"
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
    "lesson_18_introduction",
    "introduction",
    "Lesson 18: Interdisciplinary Unit Design",
    """
    **Welcome to Lesson 18: Interdisciplinary Unit Design!**
    
    In this lesson, you'll learn how to:
    - Use prompt engineering to create meaningful cross-disciplinary connections
    - Design integrated learning experiences that maintain subject integrity
    - Develop prompts that generate materials for interdisciplinary units
    - Create assessments that evaluate learning across multiple disciplines
    
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
    ## Designing Effective Interdisciplinary Learning Experiences
    
    Interdisciplinary learning integrates knowledge and methods from different disciplines to explore 
    complex topics, solve problems, and develop deeper understanding. When designed effectively, 
    interdisciplinary units help students make meaningful connections, apply knowledge in authentic contexts, 
    and develop transferable skills. In this lesson, we'll explore how prompt engineering can help you 
    create high-quality interdisciplinary learning experiences efficiently.
    """)
    
    # Why This Matters
    st.markdown("""
    ## Why This Matters
    
    Effective interdisciplinary learning offers numerous benefits:
    
    * **Reflects real-world complexity** by showing how knowledge areas connect and intersect
    * **Develops transferable skills** that apply across multiple domains
    * **Increases student engagement** through authentic problems and contexts
    * **Promotes deeper understanding** by examining topics from multiple perspectives
    * **Builds cognitive flexibility** through integration of different disciplinary approaches
    * **Prepares students for future challenges** that don't fit neatly into subject categories
    
    However, designing high-quality interdisciplinary units can be challenging due to the need to 
    maintain disciplinary integrity while creating meaningful connections. Prompt engineering helps 
    address this challenge by enabling you to efficiently generate materials that integrate multiple 
    subject areas effectively.
    """)
    
    # Key Concepts of Interdisciplinary Learning
    st.markdown("""
    ## Key Concepts of Interdisciplinary Learning
    
    ### Types of Disciplinary Integration
    
    Interdisciplinary learning exists on a spectrum of integration:
    
    | Type | Description | Example |
    | --- | --- | --- |
    | **Multidisciplinary** | Different disciplines address the same topic with limited integration | Studying the Renaissance in history, art, and literature classes simultaneously |
    | **Interdisciplinary** | Concepts and skills from different disciplines are intentionally integrated | Analyzing environmental issues through scientific, economic, and ethical lenses |
    | **Transdisciplinary** | Problem-centered approach that transcends individual disciplines | Designing solutions for community challenges using knowledge and skills from multiple areas |
    
    Each type serves different purposes and can be appropriate depending on your learning goals,
    student readiness, and logistical constraints.
    
    ### Organizing Frameworks for Interdisciplinary Units
    
    Effective interdisciplinary units need organizing structures to create coherence across subjects:
    
    - **Essential Questions** that transcend individual disciplines
    - **Themes or Concepts** that appear in multiple subject areas
    - **Problems or Issues** that require multiple disciplinary perspectives
    - **Processes or Skills** that apply across disciplines
    - **Products or Performances** that integrate knowledge from different areas
    
    These frameworks help maintain focus and ensure that connections aren't superficial or forced.
    """)
    
    # Principles of Effective Interdisciplinary Design
    st.markdown("""
    ## Principles of Effective Interdisciplinary Design
    
    Research and best practices suggest several key principles for designing high-quality 
    interdisciplinary learning experiences:
    
    ### 1. Maintain Disciplinary Integrity
    
    Effective interdisciplinary learning doesn't water down individual subjects but rather 
    strengthens them through meaningful connections. Each discipline should be represented 
    through its:
    
    - Core concepts and big ideas
    - Key skills and practices
    - Essential standards and learning outcomes
    - Authentic methodologies and approaches
    
    ### 2. Create Authentic Connections
    
    Connections between disciplines should be meaningful and natural rather than forced or superficial:
    
    - Focus on conceptual connections rather than just thematic links
    - Identify complementary processes and methodologies
    - Explore how different disciplines approach similar questions
    - Look for ways disciplines can enhance and inform each other
    
    ### 3. Design Clear Learning Progressions
    
    Students need structured guidance to integrate knowledge across disciplines:
    
    - Sequence learning to build necessary disciplinary foundations
    - Provide explicit instruction in making connections
    - Scaffold the complexity of integration
    - Include reflection on how disciplines interact
    
    ### 4. Balance Breadth and Depth
    
    Interdisciplinary units should deepen understanding rather than just covering more content:
    
    - Prioritize depth of understanding over breadth of coverage
    - Focus on transferable concepts and skills
    - Allow time for exploration and application
    - Create opportunities for sustained inquiry
    """)
    
    # Challenges in Interdisciplinary Design
    st.markdown("""
    ## Common Challenges in Interdisciplinary Design
    
    Despite its benefits, designing effective interdisciplinary learning experiences presents 
    several challenges:
    
    ### 1. Maintaining Disciplinary Rigor
    
    There's a risk of sacrificing depth for breadth or creating "holiday curriculum" that's 
    engaging but lacks substantive learning. Effective interdisciplinary design requires ensuring 
    that disciplinary standards and skills remain central.
    
    ### 2. Creating Meaningful (Not Forced) Connections
    
    Not all disciplines connect in equally meaningful ways around all topics. Finding authentic 
    points of integration requires careful analysis of curricula and standards across subjects.
    
    ### 3. Managing Logistical Complexity
    
    Interdisciplinary units often involve coordination across teachers, schedules, and resources, 
    creating logistical challenges that can undermine implementation.
    
    ### 4. Designing Appropriate Assessment
    
    Traditional assessments may not adequately capture interdisciplinary understanding. New 
    approaches are needed to evaluate both disciplinary mastery and integrated learning.
    
    ### 5. Supporting Teacher Collaboration
    
    Many teachers lack experience designing interdisciplinary curricula or collaborating across 
    subject boundaries, creating professional learning challenges.
    """)
    
    # Prompt Engineering for Interdisciplinary Learning
    st.markdown("""
    ## Prompt Engineering for Interdisciplinary Learning
    
    Prompt engineering can help address these challenges by generating well-designed interdisciplinary 
    materials, activities, and assessments. When creating AI prompts for interdisciplinary learning, 
    consider:
    
    ### For Unit Planning:
    
    * **Identifying cross-disciplinary standards** with natural connections
    * **Highlighting essential questions** that bridge multiple subjects
    * **Developing conceptual frameworks** that organize learning across disciplines
    * **Creating learning progressions** that build both disciplinary and integrated understanding
    * **Designing culminating projects** that require synthesis across subjects
    
    ### For Instructional Materials:
    
    * **Generating resources that maintain disciplinary integrity** while creating connections
    * **Developing scaffolds** for students to make cross-disciplinary connections
    * **Creating content that illustrates concepts from multiple perspectives**
    * **Designing learning activities that integrate skills from different areas**
    * **Producing materials at varied levels for differentiation**
    
    ### For Assessment:
    
    * **Creating rubrics that evaluate both disciplinary and integrated learning**
    * **Designing performance tasks that require synthesis across subjects**
    * **Developing formative assessments that check for conceptual connections**
    * **Generating reflection prompts that help students process integrated learning**
    * **Creating exemplars that model effective interdisciplinary thinking**
    """)
    
    # Application in the PCTFR Framework
    st.markdown("""
    ## Applying the PCTFR Framework
    
    The PCTFR framework (Persona, Context, Task, Format, Reference Materials) can be applied to
    create effective prompts for interdisciplinary learning materials:
    
    ### Example for a Humanities-Science Integration:
    
    ```
    Persona: Act as an interdisciplinary curriculum specialist who designs integrated learning experiences 
    that maintain disciplinary integrity while creating meaningful connections across subjects
    
    Context: I teach both 10th grade environmental science and English language arts, and I'm designing a 
    unit that integrates climate change science with persuasive writing. Many students struggle to see 
    connections between scientific evidence and effective argumentation. I want to help them understand 
    how scientific concepts and rhetorical techniques can work together to create evidence-based arguments.
    
    Task: Create a two-week integrated unit plan that helps students understand climate change science 
    while developing their persuasive writing skills. The unit should culminate in students writing 
    evidence-based argumentative essays about climate policy that incorporate scientific data and 
    rhetorical strategies.
    
    Format: Design a unit plan that includes:
    1. Essential questions that bridge science and ELA
    2. Learning objectives from both disciplines (science content and writing skills)
    3. A sequence of 8-10 integrated lessons with brief descriptions
    4. 2-3 formative assessments that check understanding in both areas
    5. A final performance task with a rubric that evaluates both scientific accuracy and persuasive writing
    6. Resources needed for implementation
    
    The unit should maintain the integrity of both disciplines while helping students see how scientific 
    understanding enhances persuasive writing and how rhetorical skills can effectively communicate 
    scientific concepts. Include specific strategies for helping students connect scientific evidence to 
    persuasive techniques.
    
    Reference Materials: Science standards include HS-ESS3-5 (Analyze geoscience data and the results from 
    global climate models to make an evidence-based forecast of the current rate of global or regional 
    climate change and associated future impacts to Earth systems) and HS-ESS3-4 (Evaluate or refine a 
    technological solution that reduces impacts of human activities on natural systems). ELA standards 
    include W.9-10.1 (Write arguments to support claims in an analysis of substantive topics or texts, 
    using valid reasoning and relevant and sufficient evidence) and W.9-10.7 (Conduct short as well as more 
    sustained research projects to answer a question or solve a problem). Key climate science concepts 
    include greenhouse effect, carbon cycle, feedback loops, and mitigation strategies. Key rhetorical 
    concepts include ethos/pathos/logos, counterargument, evidence integration, and rhetorical devices.
    ```
    
    ### Example for a Math-Social Studies Integration:
    
    ```
    Persona: Act as a middle school curriculum designer who specializes in creating integrated learning 
    experiences that connect mathematical thinking with social studies concepts
    
    Context: I'm collaborating with 7th grade math and social studies teachers to create an integrated 
    unit on data analysis and social inequality. Students will analyze demographic and economic data to 
    better understand patterns of inequality in their community and beyond. Many students struggle to see 
    the relevance of statistics and need support connecting abstract mathematical concepts to real-world 
    social issues.
    
    Task: Create an integrated two-week unit that helps students develop statistical reasoning skills 
    while exploring concepts of economic inequality and social justice. The unit should help students 
    understand how mathematical tools can illuminate important social issues and how social contexts 
    can make mathematics more meaningful.
    
    Format: Design a unit plan that includes:
    1. Integrated learning objectives addressing both statistical concepts and social studies understanding
    2. A sequence of 8 lessons that build both mathematical skills and social awareness
    3. Data sets and analysis activities appropriate for 7th graders
    4. Discussion questions that connect mathematical findings to social implications
    5. Scaffolding for students who struggle with either the math concepts or the social complexities
    6. A final project where students create and present data visualizations that tell a story about 
       inequality in their community
    
    Each lesson should include both mathematical skill development and social studies concepts, with 
    clear connections between them. The unit should maintain appropriate mathematical rigor while making 
    the content accessible and relevant through social applications.
    
    Reference Materials: Math standards include 7.SP.A.1 (Understand that statistics can be used to gain 
    information about a population by examining a sample of the population), 7.SP.A.2 (Use data from a 
    random sample to draw inferences about a population), and 7.SP.B.4 (Use measures of center and measures 
    of variability for numerical data from random samples to draw informal comparative inferences about two 
    populations). Social studies standards focus on economic systems, social stratification, and civic 
    action. Students have prior knowledge of basic graphing, mean, median, and mode, but need support with 
    sampling, statistical significance, and data visualization techniques. They have explored concepts of 
    fairness and equity but need to develop more nuanced understanding of systemic inequality.
    ```
    """)
    
    # Strategic Considerations
    st.markdown("""
    ## Strategic Considerations
    
    When using prompt engineering for interdisciplinary design:
    
    ### 1. Start with Strong Disciplinary Foundations
    
    * **Identify key standards** from each discipline to serve as anchors
    * **Analyze disciplinary practices** to find complementary processes
    * **Consider progression of skills** within each subject area
    * **Maintain disciplinary vocabulary and methods** while creating connections
    
    ### 2. Focus on Authentic Integration Points
    
    * **Look for natural conceptual overlaps** rather than forced connections
    * **Consider how disciplines can enhance each other**
    * **Identify problems that genuinely require multiple perspectives**
    * **Build on existing curriculum rather than creating everything from scratch**
    
    ### 3. Design for Appropriate Balance
    
    * **Determine the integration level** that best serves your learning goals
    * **Consider logistical constraints** when planning complexity
    * **Balance structure with flexibility** to accommodate different paces
    * **Plan for appropriate assessment** of both disciplinary and integrated learning
    
    ### 4. Support Implementation Success
    
    * **Create clear guidance** for navigating integrated materials
    * **Develop supports for teachers** less familiar with some content areas
    * **Anticipate potential challenges** and design mitigation strategies
    * **Include reflection opportunities** to help students process connections
    """)
    
    # Connection to Previous and Next Lessons
    st.markdown("""
    ## Connections to Other Lessons
    
    This lesson builds on concepts from previous lessons:
    
    * **Lesson 17 (Personalized Learning Pathways)**: Just as personalized learning creates tailored paths 
      for individual students, interdisciplinary design creates connections across different content areas. 
      Both approaches require thoughtful design that balances structure with flexibility.
    
    * **Earlier Lessons on Prompt Engineering Techniques**: The PCTFR framework continues to provide 
      structure for creating complex, multi-faceted prompts that address both disciplinary integrity 
      and cross-curricular connections.
    
    In the next section, you'll see examples of effective prompts for generating various types of
    interdisciplinary materials and units across different subject areas and grade levels.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Connect this lesson to participants' existing curriculum integration efforts
    * Acknowledge the challenges of implementing interdisciplinary learning within traditional school structures
    * Emphasize that interdisciplinary design exists on a spectrum—even small cross-curricular connections can benefit students
    * Encourage teachers to start with natural connection points between their subject and one other area
    
    **Discussion Prompts:**
    
    * What natural connections exist between your subject area and other disciplines?
    * How might prompt engineering help address common barriers to interdisciplinary teaching?
    * What organizing frameworks (essential questions, themes, etc.) have you found most effective for integrated units?
    
    **Extension Opportunities:**
    
    * Invite teachers to identify a standard from their discipline and find complementary standards from other subjects
    * Suggest creating an interdisciplinary prompt template that could be applied across multiple units
    * Explore how prompt engineering might support teacher collaboration across departments
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