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
    page_title="Lesson 14: Examples",
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
    "title": "Student Feedback and Writing Prompts: Examples",
    "lesson": "14",
    "section": "examples",
    "order": 2
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_14_examples"
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
    "lesson_14_examples",
    "examples",
    "Student Feedback and Writing Prompts: Examples",
    """
    **This section provides practical examples of prompt engineering for student feedback and writing prompts.**
    
    You'll see:
    - Real-world prompts for generating effective student feedback
    - Examples of creating engaging writing prompts for various purposes
    - Approaches for differentiating feedback and writing tasks
    - Applications of the PTC-FREI framework to these essential teaching tasks
    
    These examples demonstrate how to apply prompt engineering techniques to support student growth and development.
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
    st.markdown("## Practical Examples: Student Feedback and Writing Prompts")
    
    st.markdown("""
    The following examples demonstrate how to use prompt engineering techniques to generate
    effective student feedback and create engaging writing prompts for various educational contexts.
    """)
    
    # Section 1: Student Feedback Examples
    st.markdown("# Part 1: Student Feedback Examples")
    
    # Example 1: Elementary Writing Feedback
    st.markdown("### Example 1: Elementary Writing Feedback")
    
    st.markdown("""
    **Prompt Engineering Goal:** Generate supportive, growth-oriented feedback for a young writer
    
    **Techniques Used:**
    - Role Prompting
    - Structured Format
    - Context Specification
    """)
    
    with st.expander("View the Detailed Prompt"):
        st.markdown("""
        ```
        Act as a supportive 3rd-grade teacher who emphasizes growth mindset and provides 
        encouraging feedback while also guiding students toward improvement.
        
        I need to provide feedback on a student's personal narrative about a family trip. 
        The student is developing their writing skills and needs support with paragraph 
        organization and adding descriptive details. The assignment asked students to:
        - Write about a memorable experience
        - Include a beginning, middle, and end
        - Use descriptive words to help readers picture the event
        - Include at least 3 paragraphs
        
        Here is the student's work:
        
        "My Trip to the Beach
        
        I went to the beach with my family. It was fun. We built a sand castle. 
        It was big. I found a shell. We went swimming in the water. The water 
        was cold. We had lunch. I ate a sandwich. Then we went home. It was the 
        best day."
        
        Structure your feedback in this way:
        
        1. POSITIVE ACKNOWLEDGMENT: Begin with specific praise for what the student did well
        
        2. GROWTH AREA #1: Paragraph organization
           - Explain in child-friendly language why paragraphs are important
           - Give a specific example of how to organize this writing into paragraphs
        
        3. GROWTH AREA #2: Adding descriptive details
           - Acknowledge any descriptive words they did use
           - Provide 2-3 specific questions that would help them add more details
           - Give a specific example of how to expand one of their sentences with more description
        
        4. ENCOURAGING NEXT STEPS: End with 1-2 simple, actionable steps they can take to improve,
           phrased as "Let's try..." suggestions
        
        Use language that is appropriate for a 3rd-grade student (simple words, short sentences) 
        and a warm, encouraging tone throughout. Include a specific positive comment about their 
        topic choice or an element of their story.
        ```
        """)
    
    st.markdown("""
    **What Makes This Prompt Effective:**
    
    1. **Supportive Persona**: Specifies a role that emphasizes growth mindset and encouragement
    
    2. **Clear Context**: Provides information about the student's skill level and specific needs
    
    3. **Student Work Sample**: Includes the actual writing to be assessed
    
    4. **Structured Format**: Outlines a specific feedback structure with balanced components
    
    5. **Age-Appropriate Guidance**: Requests language and tone suitable for a young student
    
    **Result:** This prompt generates balanced, constructive feedback that acknowledges strengths while providing specific guidance for improvement in a way that's accessible and encouraging for a young writer.
    """)
    
    # Example 2: Secondary Essay Feedback
    st.markdown("### Example 2: Secondary Essay Feedback")
    
    st.markdown("""
    **Prompt Engineering Goal:** Generate detailed analytical feedback on a high school argumentative essay
    
    **Techniques Used:**
    - Few-Shot Prompting
    - Multiple Feedback Perspectives
    - Rubric Integration
    """)
    
    with st.expander("View the Detailed Prompt"):
        st.markdown("""
        ```
        I need to provide comprehensive feedback on a high school student's argumentative essay 
        about climate change. The student is in 10th grade and has strong ideas but struggles with 
        organizing evidence and developing clear arguments.
        
        The essay will be evaluated using this rubric:
        
        CLAIM (20 points):
        - Clear, debatable thesis that establishes position
        - Maintains focus on the claim throughout
        
        EVIDENCE (30 points):
        - Relevant, credible evidence that supports the claim
        - Multiple types of evidence (statistics, expert opinions, examples)
        - Proper citation of sources
        
        REASONING (30 points):
        - Clear explanation of how evidence supports claims
        - Acknowledgment and refutation of counterarguments
        - Logical progression of ideas
        
        CONVENTIONS (20 points):
        - Appropriate academic tone and language
        - Correct grammar, spelling, and punctuation
        - Effective transitions between ideas
        
        [Note: The student's full essay would be included here]
        
        Please provide feedback from three perspectives:
        
        1. CONTENT SPECIALIST: Focusing on the quality of arguments, evidence, and reasoning
        
        2. WRITING COACH: Focusing on structure, organization, and clarity of expression
        
        3. PEER REVIEWER: Providing more informal feedback on overall effectiveness and engagement
        
        For each perspective, follow this structure:
        
        - Strengths (2-3 specific examples with explanations)
        - Areas for development (2-3 specific examples with explanations)
        - Actionable recommendations (3 specific, prioritized suggestions)
        
        Here's an example of effective feedback on an argument from the Content Specialist perspective:
        
        "STRENGTH: Your argument about carbon taxes effectively uses economic data to support your claim. 
        Specifically, when you cite the 12% emissions reduction in countries with carbon pricing, then 
        explain how this demonstrates market-based solutions can work, you're creating a strong 
        evidence-reasoning connection.
        
        AREA FOR DEVELOPMENT: Your counterargument section acknowledges that critics believe carbon taxes 
        burden low-income families, but you don't fully address this concern with evidence. This weakens 
        your overall argument because it leaves a significant objection inadequately refuted.
        
        RECOMMENDATION: Strengthen your counterargument by adding specific evidence about how carbon tax 
        policies can include rebates or dividends for low-income households. Consider citing examples from 
        British Columbia or Switzerland where such approaches have been implemented."
        
        Prioritize feedback that aligns with the rubric categories and will have the greatest impact 
        on improving the essay. Balance encouragement with constructive criticism.
        ```
        """)
    
    st.markdown("""
    **What Makes This Prompt Effective:**
    
    1. **Rubric Integration**: Includes the assessment criteria to ensure aligned feedback
    
    2. **Multiple Perspectives**: Requests feedback from three different viewpoints
    
    3. **Few-Shot Example**: Provides a model of effective feedback to guide the response
    
    4. **Balanced Structure**: Ensures each perspective includes strengths, growth areas, and actionable steps
    
    5. **Specific Context**: Includes details about the student's current skills and challenges
    
    **Result:** This prompt generates comprehensive, multi-faceted feedback that addresses different aspects of the writing while maintaining a consistent structure. The example feedback ensures that responses include specific references to the student's work rather than generic comments.
    """)
    
    # Example 3: Math Problem-Solving Feedback
    st.markdown("### Example 3: Math Problem-Solving Feedback")
    
    st.markdown("""
    **Prompt Engineering Goal:** Generate process-focused feedback that helps develop mathematical thinking
    
    **Techniques Used:**
    - Chain-of-Thought Analysis
    - Error Pattern Identification
    - Growth Mindset Language
    """)
    
    with st.expander("View the Detailed Prompt"):
        st.markdown("""
        ```
        Act as a middle school math teacher who emphasizes mathematical thinking and problem-solving 
        processes rather than just correct answers. Your feedback style focuses on identifying 
        patterns in student work and encouraging productive struggle.
        
        I need to provide feedback on a student's work on a multi-step word problem involving proportional 
        relationships. The student has made some errors in their solution process. The student generally 
        understands the concept of proportional relationships but struggles with setting up equations 
        and identifying which operations to use.
        
        Here is the problem and the student's work:
        
        PROBLEM:
        A recipe calls for 2 3/4 cups of flour to make 24 cookies. How much flour would be needed to make 
        60 cookies? Express your answer as a mixed number in simplest form.
        
        STUDENT'S WORK:
        24 cookies = 2 3/4 cups flour
        60 cookies = x cups flour
        
        24/60 = 2 3/4 / x
        24/60 = 2.75 / x
        0.4 = 2.75 / x
        x = 2.75 / 0.4
        x = 6.875
        x = 6 7/8 cups
        
        Analyze the student's work using these steps:
        
        1. PROCESS ANALYSIS:
           - Trace the student's problem-solving process step by step
           - Identify what mathematical concepts they applied correctly
           - Identify precisely where and how errors occurred in their reasoning
        
        2. ERROR PATTERN IDENTIFICATION:
           - Determine if this reflects a conceptual misunderstanding, procedural error, or calculation mistake
           - Connect to common misconceptions or error patterns in proportional reasoning
        
        3. STRENGTHS-BASED FEEDBACK:
           - Acknowledge specific aspects of their work that demonstrate mathematical understanding
           - Highlight effective strategies or steps they used
        
        4. GUIDED CORRECTION:
           - Do not simply provide the correct answer
           - Instead, pose guiding questions that will lead the student to discover their error
           - Provide a "hint" or "starting point" for correcting their work
        
        5. EXTENSION THINKING:
           - Suggest one way to extend their thinking about this problem
           - Connect to a real-world application of this type of proportional relationship
        
        Use a conversational, encouraging tone that emphasizes the value of the problem-solving process. 
        Use growth mindset language that frames errors as learning opportunities.
        ```
        """)
    
    st.markdown("""
    **What Makes This Prompt Effective:**
    
    1. **Process Focus**: Emphasizes analysis of mathematical thinking rather than just the answer
    
    2. **Error Analysis**: Requests identification of specific error patterns and misconceptions
    
    3. **Guided Discovery**: Asks for guiding questions rather than direct correction
    
    4. **Growth Mindset**: Specifies language that frames errors as learning opportunities
    
    5. **Complete Context**: Includes both the original problem and the student's full work
    
    **Result:** This prompt generates feedback that helps the student develop mathematical thinking and problem-solving skills rather than simply identifying right or wrong answers. The analysis of the error pattern helps address underlying misconceptions rather than just the specific mistake.
    """)
    
    # Section 2: Writing Prompt Examples
    st.markdown("# Part 2: Writing Prompt Examples")
    
    # Example 4: Elementary Narrative Writing Prompt
    st.markdown("### Example 4: Elementary Narrative Writing Prompt")
    
    st.markdown("""
    **Prompt Engineering Goal:** Create an engaging, scaffolded narrative writing prompt for young writers
    
    **Techniques Used:**
    - Creative Scenario Development
    - Embedded Scaffolding
    - Differentiation Options
    """)
    
    with st.expander("View the Detailed Prompt"):
        st.markdown("""
        ```
        Create an engaging narrative writing prompt for 2nd-grade students focused on developing 
        beginning-middle-end story structure and using descriptive language.
        
        The prompt should:
        
        1. Be centered around the theme of "unexpected discoveries" to spark imagination
        
        2. Include a creative scenario or story starter that is:
           - Age-appropriate for 7-8 year olds
           - Relatable to diverse students
           - Open-ended to allow for creativity
           - Specific enough to provide direction
        
        3. Incorporate embedded scaffolding through:
           - 3-5 "story planning" questions to help students organize their ideas
           - A simple graphic organizer concept (described in words) for beginning-middle-end
           - Prompting questions for adding sensory details (what did you see, hear, feel, etc.)
        
        4. Include differentiation options:
           - Additional support suggestion for emerging writers
           - Extension suggestion for advanced writers
        
        5. Specify success criteria in child-friendly language, such as:
           - "I included a clear beginning, middle, and end"
           - "I used describing words to help readers picture my story"
        
        6. End with 2-3 quick "getting started" tips to help hesitant writers
        
        The tone should be playful, encouraging, and exciting to motivate young writers. Avoid 
        overly complex vocabulary but do include 2-3 "stretch words" that might be new to students 
        (with simple definitions in parentheses).
        ```
        """)
    
    st.markdown("""
    **What Makes This Prompt Effective:**
    
    1. **Age-Appropriate Focus**: Specifies developmentally appropriate writing skills (beginning-middle-end structure)
    
    2. **Embedded Scaffolding**: Requests planning questions and a graphic organizer concept
    
    3. **Differentiation Options**: Includes support for both emerging and advanced writers
    
    4. **Clear Success Criteria**: Requests kid-friendly "I can" statements
    
    5. **Motivational Elements**: Specifies a playful, encouraging tone to engage young writers
    
    **Result:** This prompt generates a writing task that not only engages students with an interesting scenario but also provides the structure and support they need to be successful. The inclusion of differentiation options ensures that all students can access the writing task at an appropriate level of challenge.
    """)
    
    # Example 5: Secondary Argumentative Writing Prompt
    st.markdown("### Example 5: Secondary Argumentative Writing Prompt")
    
    st.markdown("""
    **Prompt Engineering Goal:** Create a standards-aligned argumentative writing prompt with sophisticated scaffolding
    
    **Techniques Used:**
    - Standards Integration
    - Complex Scaffolding Structures
    - PTC-FREI Framework Application
    """)
    
    with st.expander("View the Detailed Prompt"):
        st.markdown("""
        ```
        [Persona] Act as a high school English teacher who specializes in teaching argumentative writing
        with a focus on developing critical thinking and evidence-based reasoning.
        
        [Task] Create a sophisticated argumentative writing prompt for 11th-grade students on the topic
        of technology's impact on society and human interaction.
        
        [Context] These students have previously written argumentative essays and understand basic
        claim-evidence-reasoning structure. They need practice with developing nuanced claims,
        integrating and analyzing research, addressing counterarguments, and using rhetorical strategies
        effectively. This prompt will be used for a significant essay (3-4 pages) that students will
        develop over two weeks, with time for research, drafting, peer review, and revision.
        
        [Format] Structure the writing prompt with the following components:
        
        1. ENGAGING INTRODUCTION
           - Begin with a thought-provoking quote, statistic, or scenario about technology's impact
           - Briefly contextualize the ongoing debate about technology and society
        
        2. CORE PROMPT
           - Present a focused, debatable question about a specific aspect of technology's impact
           - Clarify the type of argument students should develop (causal, evaluation, proposal, etc.)
           - Specify audience and purpose for the argument
        
        3. TASK REQUIREMENTS
           - Length and format expectations
           - Required structural elements (introduction with thesis, body paragraphs, counterarguments, conclusion)
           - Research requirements (minimum number and types of sources)
           - Citation format
        
        4. SCAFFOLDING SUPPORTS
           - 3-4 guiding questions to help students develop their position
           - Suggestions for types of evidence that would strengthen different positions
           - A framework for analyzing potential counterarguments
           - A structure for evaluating the credibility and relevance of sources
        
        5. SUCCESS CRITERIA
           - Clear description of what makes an effective argument (aligned with grading expectations)
           - Examples of what different levels of achievement might look like
        
        6. TIMELINE AND PROCESS
           - Breakdown of the two-week process into specific stages
           - Checkpoints for receiving feedback
           - Peer review guidelines
        
        [Reference] Align with Common Core State Standards for Writing, grades 11-12:
        CCSS.ELA-LITERACY.W.11-12.1: Write arguments to support claims using valid reasoning and relevant evidence
        CCSS.ELA-LITERACY.W.11-12.7: Conduct research projects to answer a question or solve a problem
        CCSS.ELA-LITERACY.W.11-12.8: Gather relevant information from multiple sources, assess credibility
        
        The prompt should challenge students to think critically about nuanced aspects of technology's
        impact rather than taking simplistic pro/con positions. It should also encourage them to consider
        ethical dimensions and diverse perspectives on the issue.
        ```
        """)
    
    st.markdown("""
    **What Makes This Prompt Effective:**
    
    1. **Full PTC-FREI Application**: Uses the complete framework including Persona, Task, Context, Format, and Reference
    
    2. **Standards Alignment**: Explicitly references specific Common Core standards
    
    3. **Sophisticated Scaffolding**: Includes multiple supports appropriate for the complexity of the task
    
    4. **Process Orientation**: Addresses the full writing process including research, drafting, and revision
    
    5. **Critical Thinking Focus**: Emphasizes nuanced positions rather than simplistic arguments
    
    **Result:** This prompt generates a comprehensive writing assignment that not only presents an engaging topic but also provides the structure, supports, and timeline students need to develop sophisticated argumentative essays. The alignment with standards ensures that the assignment addresses important skills while the scaffolding helps students access challenging content.
    """)
    
    # Example 6: Cross-Curricular Project Prompt
    st.markdown("### Example 6: Cross-Curricular Project Prompt")
    
    st.markdown("""
    **Prompt Engineering Goal:** Create an interdisciplinary writing project that connects multiple subject areas
    
    **Techniques Used:**
    - Multi-Subject Integration
    - Project-Based Learning Framework
    - Role-Based Scenario
    """)
    
    with st.expander("View the Detailed Prompt"):
        st.markdown("""
        ```
        Create an engaging cross-curricular writing project prompt for 8th-grade students that 
        integrates social studies (American Revolution), science (technology and innovation), and 
        ELA (informational and argumentative writing).
        
        The project prompt should:
        
        1. ESTABLISH AN AUTHENTIC SCENARIO
           - Create a role-based situation where students act as museum exhibit designers, historical 
             documentary producers, or similar authentic role
           - Provide a clear audience, purpose, and deliverable for the writing
           - Include a compelling hook that makes the project relevant to today's world
        
        2. INTEGRATE MULTIPLE SUBJECT AREAS
           - Social Studies: Require analysis of historical events, figures, and perspectives from 
             the American Revolution
           - Science: Incorporate examination of 18th-century technologies and innovations and their 
             impact on events
           - ELA: Include both informational and argumentative writing components
        
        3. OUTLINE PROJECT REQUIREMENTS
           - Define the final product(s) students will create
           - Specify both individual and collaborative components
           - Include a research requirement with diverse source types
           - Detail any presentation or multimedia elements
        
        4. PROVIDE LEARNING SUPPORTS
           - Include a project timeline with checkpoints
           - Offer planning templates or organizational structures
           - Suggest resources for different aspects of the project
           - Include reflection questions throughout the process
        
        5. DETAIL ASSESSMENT APPROACH
           - Provide clear success criteria for each component
           - Include opportunities for peer and self-assessment
           - Explain how individual and group work will be evaluated
        
        6. OFFER DIFFERENTIATION OPTIONS
           - Include modifications for diverse learning needs
           - Provide extension opportunities for advanced students
           - Suggest alternative ways to demonstrate learning
        
        The prompt should be written in student-friendly language that creates excitement about 
        the project while clearly communicating expectations. It should emphasize authentic 
        application of skills and knowledge rather than artificial academic tasks.
        ```
        """)
    
    st.markdown("""
    **What Makes This Prompt Effective:**
    
    1. **Cross-Curricular Connections**: Integrates multiple subject areas in a meaningful way
    
    2. **Authentic Context**: Creates a role-based scenario with real-world relevance
    
    3. **Comprehensive Structure**: Addresses all aspects of project implementation
    
    4. **Support Framework**: Includes planning templates, resources, and checkpoints
    
    5. **Assessment Integration**: Clearly defines success criteria and evaluation approaches
    
    **Result:** This prompt generates a comprehensive, engaging cross-curricular project that gives students an authentic context for applying skills from multiple subject areas. The integration of scaffolding, assessment, and differentiation options ensures that the project is both challenging and accessible to diverse learners.
    """)
    
    # Summary of Strategies
    st.markdown("## Key Prompt Design Strategies for Feedback and Writing Tasks")
    
    st.markdown("""
    From these examples, we can identify several effective prompt design strategies:
    
    ### For Student Feedback:
    
    1. **Balance Strengths and Growth Areas**
       - Always include specific praise along with areas for improvement
       - Maintain a ratio that emphasizes growth while acknowledging achievement
    
    2. **Tailor to Learning Stage**
       - Adjust language, tone, and complexity based on student age and development
       - Focus on different aspects depending on the student's current skills
    
    3. **Emphasize Process Over Product**
       - Comment on the thinking and strategies, not just the final output
       - Provide forward-looking guidance for future application
    
    4. **Connect to Specific Criteria**
       - Link feedback directly to learning objectives or rubric elements
       - Make success criteria explicit and accessible
    
    ### For Writing Prompts:
    
    1. **Embed Appropriate Scaffolding**
       - Include planning questions, organizers, or structures that support the writing process
       - Scale scaffolding to match the complexity of the task and student needs
    
    2. **Create Authentic Contexts**
       - Develop scenarios that give writing real-world relevance and purpose
       - Specify audiences and outcomes that matter beyond the classroom
    
    3. **Balance Structure and Creativity**
       - Provide clear guidelines while allowing for personal expression
       - Include elements that spark imagination while developing specific skills
    
    4. **Integrate Assessment Design**
       - Build evaluation criteria directly into the prompt development
       - Make success look like something students can visualize and work toward
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Key Points to Emphasize:**
    
    * These example prompts demonstrate the importance of considering the full instructional context, not just the immediate task
    * Note how combining multiple prompt engineering techniques creates more sophisticated and effective results
    * Effective feedback and writing prompts both require a balance of structure and flexibility
    * The most powerful prompts incorporate assessment design from the beginning rather than as an afterthought
    
    **Discussion Questions:**
    
    * Which of these examples most closely aligns with your current teaching context?
    * How might you adapt these prompts for specific student populations or content areas?
    * What elements of effective feedback do you find most challenging to implement consistently?
    * How could you use these examples as templates for creating a bank of prompts for your curriculum?
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