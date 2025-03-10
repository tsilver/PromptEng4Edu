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
    page_title="Lesson 15: Introduction",
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
    "title": "Discussion Questions and Content Creation: Introduction",
    "lesson": "15",
    "section": "introduction",
    "order": 1
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_15_introduction"
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
    "lesson_15_introduction",
    "introduction",
    "Lesson 15: Discussion Questions and Content Creation",
    """
    **Welcome to Lesson 15: Discussion Questions and Content Creation!**
    
    In this lesson, you'll learn how to:
    - Craft thought-provoking discussion questions that promote critical thinking
    - Generate engaging instructional content across different formats
    - Apply prompt engineering techniques to enhance student engagement and learning
    - Design differentiated learning materials for diverse classrooms
    
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
    ## Creating Effective Learning Experiences Through Discussion and Content
    
    Thoughtful discussion questions and well-designed instructional content are fundamental to
    effective teaching and learning. They facilitate deeper understanding, critical thinking,
    and student engagement. In this lesson, we'll explore how prompt engineering can help you
    create high-quality discussion questions and instructional content efficiently.
    """)
    
    # Why This Matters
    st.markdown("""
    ## Why This Matters
    
    Quality discussion questions and instructional content are essential because they:
    
    * **Promote deeper thinking** beyond surface-level facts and concepts
    * **Engage diverse learners** through multiple entry points and perspectives
    * **Create meaningful learning experiences** that connect to students' lives and interests
    * **Support differentiation** by providing varied ways for students to access content
    * **Develop critical thinking skills** through analytical and evaluative prompts
    * **Encourage student agency** by inviting multiple interpretations and approaches
    """)
    
    # Key Concepts About Discussion Questions
    st.markdown("""
    ## Creating Effective Discussion Questions
    
    ### Types of Discussion Questions
    
    Different types of questions serve different purposes in the learning process:
    
    | Question Type | Purpose | Example |
    | --- | --- | --- |
    | **Factual** | Check comprehension and recall | "What are the three branches of government?" |
    | **Analytical** | Examine relationships and causality | "How did westward expansion affect Native American nations?" |
    | **Evaluative** | Assess using criteria and make judgments | "Which character's actions were most justified? Why?" |
    | **Creative** | Generate new ideas or perspectives | "How might the story end differently if...?" |
    | **Connective** | Link to prior knowledge or experiences | "How does this compare to what we learned about...?" |
    | **Metacognitive** | Reflect on one's own thinking | "What was most challenging about understanding...?" |
    
    ### Bloom's Taxonomy and Question Design
    
    Bloom's Taxonomy provides a framework for designing questions at various cognitive levels:
    
    **Lower-Order Questions:**
    - **Remember**: Questions about recalling facts, terms, concepts, or answers
    - **Understand**: Questions about explaining ideas or concepts
    - **Apply**: Questions about using information in new situations
    
    **Higher-Order Questions:**
    - **Analyze**: Questions about drawing connections among ideas
    - **Evaluate**: Questions about justifying a stand or decision
    - **Create**: Questions about producing new or original work
    
    A balanced approach includes questions at multiple levels to support all learners while
    promoting higher-order thinking.
    """)
    
    # Key Concepts About Content Creation
    st.markdown("""
    ## Designing Effective Instructional Content
    
    ### Content Formats
    
    Instructional content can take many forms, each with unique advantages:
    
    - **Direct Instruction Materials**: Clear explanations, definitions, processes
    - **Guided Notes**: Structured templates with key information and space for student input
    - **Case Studies**: Real-world scenarios that illustrate concepts and principles
    - **Simulations and Scenarios**: Immersive contexts for applying knowledge
    - **Multimedia Resources**: Videos, infographics, interactive presentations
    - **Inquiry-Based Activities**: Exploration guides, investigation prompts
    - **Assessment Materials**: Formative checks, practice problems, authentic tasks
    
    ### Principles of Effective Content Design
    
    Regardless of format, effective instructional content should:
    
    1. **Be clearly aligned with learning objectives**
    2. **Present information in meaningful chunks**
    3. **Use accessible language appropriate for the audience**
    4. **Incorporate multiple representations of concepts**
    5. **Include varied examples and non-examples**
    6. **Anticipate misconceptions and address them directly**
    7. **Provide opportunities for application and practice**
    8. **Support differentiation for diverse learners**
    """)
    
    # Prompt Engineering for Discussion Questions and Content
    st.markdown("""
    ## Prompt Engineering for Discussion Questions and Content
    
    ### Prompt Engineering for Discussion Questions
    
    When creating AI prompts to generate discussion questions, consider:
    
    * **Specifying cognitive levels** (e.g., "Generate 3 analysis-level questions and 2 evaluation-level questions")
    * **Targeting specific skills** (e.g., "Create questions that require textual evidence")
    * **Focusing on key concepts** (e.g., "Design questions centered on the concept of energy transfer")
    * **Identifying misconceptions** (e.g., "Include a question that addresses the common misconception that...")
    * **Incorporating diverse perspectives** (e.g., "Generate questions that explore multiple perspectives on...")
    
    ### Prompt Engineering for Content Creation
    
    When creating AI prompts to generate instructional content, consider:
    
    * **Defining the format clearly** (e.g., "Create a guided notes template" or "Design a case study")
    * **Specifying the learning objectives** (e.g., "Content should support students in mastering...")
    * **Indicating the audience** (e.g., "For 7th-grade students with varied reading levels")
    * **Requesting scaffolding elements** (e.g., "Include vocabulary supports and visual organizers")
    * **Providing examples of your teaching style** (e.g., "Content should use an inquiry approach similar to...")
    """)
    
    # Application in the PCTFR Framework
    st.markdown("""
    ## Applying the PCTFR Framework
    
    The PCTFR framework (Persona, Context, Task, Format, Reference Materials) can be applied to
    create effective prompts for discussion questions and content creation:
    
    ### Example for Discussion Questions:
    
    ```
    Persona: Act as an experienced humanities teacher who specializes in Socratic seminar facilitation
    
    Context: I'm teaching To Kill a Mockingbird to 9th graders who have just completed reading through Chapter 15
    
    Task: Create a set of discussion questions that will help students explore themes of justice, courage, and prejudice
    
    Format: Provide 8-10 questions organized into categories: Opening Questions, Core Analysis Questions, and Reflective Closing Questions. Include possible student responses and follow-up questions.
    
    Reference Materials: The key scenes from Chapters 1-15 include Scout's first day at school, the discovery of gifts in the tree, Atticus taking the case, and the confrontation at the jail. Key themes established include innocence, prejudice, moral education, and courage.
    ```
    
    ### Example for Content Creation:
    
    ```
    Persona: Act as a STEM curriculum developer who specializes in inquiry-based science instruction
    
    Context: I'm developing materials for an 8th-grade unit on forces and motion
    
    Task: Create a lab investigation guide that allows students to explore Newton's Third Law of Motion
    
    Format: Design a structured inquiry lab with clearly defined sections: Background, Question, Hypothesis, Materials, Procedure, Data Collection, Analysis Questions, and Extension. Include safety considerations and differentiation options.
    
    Reference Materials: The lab should align with NGSS MS-PS2-1: "Apply Newton's Third Law to design a solution to a problem involving the motion of two colliding objects." Students have already completed labs on Newton's First and Second Laws.
    ```
    """)
    
    # Strategic Considerations
    st.markdown("""
    ## Strategic Considerations
    
    When using prompt engineering for discussion questions and content creation:
    
    ### For Discussion Questions:
    
    * **Balance breadth and depth**: Mix questions that cover essential content with those that explore fewer topics deeply
    * **Consider sequencing**: Design questions that build on each other in complexity and focus
    * **Plan for flexibility**: Create more questions than you need so you can adapt to student responses
    * **Integrate different perspectives**: Ensure questions invite multiple viewpoints and interpretations
    * **Anticipate responses**: Have follow-up questions ready to deepen thinking
    
    ### For Content Creation:
    
    * **Start with clear learning objectives**: Know exactly what you want students to learn
    * **Request variations**: Generate multiple versions for differentiation
    * **Maintain consistency**: Ensure new content aligns with your teaching approach and previous materials
    * **Review critically**: Evaluate generated content for accuracy, clarity, and alignment
    * **Remix and adapt**: Combine elements from multiple generated options for optimal results
    """)
    
    # Connection to Previous and Next Lessons
    st.markdown("""
    ## Connections to Other Lessons
    
    This lesson builds on concepts from previous lessons:
    
    * **Lesson 14 (Student Feedback and Writing Prompts)**: Just as you created scaffolded writing prompts, you'll now create structured discussion questions and learning materials
    
    * **Earlier Lessons on Prompt Engineering Techniques**: You'll apply the PCTFR framework and other techniques to a new set of educational tasks
    
    In the next section, you'll see examples of effective prompts for generating discussion questions and instructional content across various subject areas and grade levels.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Connect this lesson to teachers' current instructional planning processes
    * Acknowledge the time investment in creating quality discussion questions and content, and how prompt engineering can help
    * Emphasize that AI-generated content should always be evaluated and refined based on professional judgment
    * Encourage teachers to start with small, focused tasks before attempting to generate complete lessons
    
    **Discussion Prompts:**
    
    * What types of discussion questions do you find most challenging to create? Why?
    * How do you currently approach creating differentiated instructional materials?
    * Where in your planning process could prompt engineering be most helpful?
    
    **Extension Opportunities:**
    
    * Invite teachers to bring existing discussion guides or content for revision using these techniques
    * Suggest creating a department-wide repository of effective content prompts organized by standard or unit
    * Explore how these techniques might support collaborative planning among teaching teams
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