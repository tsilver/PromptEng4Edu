import streamlit as st
import os
import sys
from utils.navigation import scroll_to_top, get_all_pages
from utils.state_management import initialize_session_state, mark_page_completed
from utils.teacher_client import TeacherClient
from components.teacher_notes import render_teacher_notes
from components.bottom_navigator import render_bottom_navigator
from components.breadcrumb_navigator import render_breadcrumb
from components.course_navigation import render_course_navigation
from components.top_navigator import render_top_navigator
from components.first_visit_dialog import show_first_visit_dialog
from components.progress_manager import render_teacher_controls_sidebar

# Initialize the TeacherClient
client = TeacherClient()

# Configure page
st.set_page_config(
    page_title="Lesson 6: Examples",
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
    "title": "Reference Materials: Examples",
    "lesson": "6",
    "section": "examples",
    "order": 2
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_6_examples"
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
    "lesson_6_examples",
    "examples",
    "Lesson 6: Examples of Reference Materials",
    """
    **This section demonstrates how incorporating reference materials enhances AI responses.**
    
    You'll see:
    - Side-by-side comparisons of prompts with and without reference materials
    - Examples of different types of references for various educational purposes
    - How combining reference materials with other prompt components creates powerful results
    
    Look through these examples to understand how reference materials 
    help generate responses that align with specific curriculum and resources.
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
    st.markdown("## Reference Materials Examples")
    
    st.markdown("""
    The following examples demonstrate how incorporating reference materials in your prompts significantly 
    improves the relevance and alignment of AI responses. Compare these examples to see
    how reference materials can transform educational content.
    """)
    
    # Example 1: Standards-Based Lesson Planning
    st.markdown("### Example 1: Standards-Based Lesson Planning")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Basic Prompt (No References):**
        ```
        Create a 3rd-grade math lesson plan about telling time.
        ```
        
        **Potential Issues:**
        - May not align with specific grade-level standards
        - Could cover content already taught or not yet introduced
        - Might use different terminology than your curriculum
        - May not match your instructional approach
        """)
    
    with col2:
        st.markdown("""
        **Prompt with Reference Materials:**
        ```
        Create a 3rd-grade math lesson plan about telling time
        based on these specific standards:
        
        CCSS.MATH.CONTENT.3.MD.A.1:
        Tell and write time to the nearest minute and measure 
        time intervals in minutes. Solve word problems involving 
        addition and subtraction of time intervals in minutes, 
        e.g., by representing the problem on a number line diagram.
        
        Our district curriculum map indicates students should 
        already be familiar with:
        - Telling time to the nearest hour and half hour
        - Understanding the concept of minutes and hours
        - Basic addition and subtraction within 100
        ```
        
        **Improvements:**
        - Ensures alignment with exact standard language
        - Establishes appropriate prior knowledge
        - Creates progression appropriate to curriculum sequence
        - Focuses content on specific learning objectives
        """)
    
    # Example 2: Text Analysis with Reference
    st.markdown("### Example 2: Text Analysis with Reference")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Basic Prompt (No References):**
        ```
        Create discussion questions about "The Giver" for 8th grade.
        ```
        
        **Potential Issues:**
        - Questions may not relate to specific passages in the book
        - Content might not match your teaching focus
        - May be too general without textual anchoring
        - Could miss key themes or moments from the text
        """)
    
    with col2:
        st.markdown("""
        **Prompt with Reference Materials:**
        ```
        Create five discussion questions about "The Giver" for 8th grade, 
        focusing specifically on the theme of individuality versus 
        conformity. Base the questions on these key passages:
        
        Passage 1: "The community of the Giver had achieved at great 
        price. They had eliminated all the dangers: pain, poverty, 
        hunger, war. They had eliminated fear of pain, of hunger, of 
        war. And they had eliminated hatred. The community was successful, 
        unlike previous ones they had studied in history. Jonas could see 
        that their lives had changed; but it was the same community in 
        which they had always lived."
        
        Passage 2: "The worst part of holding the memories is not the 
        pain. It's the loneliness of it. Memories need to be shared."
        
        Passage 3: "If you were to be released, you would be sent 
        Elsewhere and never return. It's the same as in your dream. 
        Just a different way of saying the same thing."
        ```
        
        **Improvements:**
        - Questions will directly relate to specific text passages
        - Focus is narrowed to a specific theme
        - Ensures students can point to textual evidence
        - Creates analytical depth through targeted examination
        """)
    
    # Example 3: Reference-Based Assessment Creation
    st.markdown("### Example 3: Reference-Based Assessment Creation")
    
    st.markdown("""
    **Prompt with Reference Materials:**
    ```
    Create a 10-question assessment on photosynthesis for high school biology 
    that aligns with our textbook's explanation. Base the questions on this 
    excerpt from our textbook:
    
    "Photosynthesis is the process by which plants, some bacteria, and some 
    protistans use the energy from sunlight to produce sugar, which cellular 
    respiration converts into ATP, the "fuel" used by all living things. The 
    conversion of unusable sunlight energy into usable chemical energy is 
    associated with the actions of the green pigment chlorophyll.
    
    The process is divided into two parts: the light-dependent reactions and 
    the light-independent reactions (Calvin cycle). In the light-dependent 
    reactions, energy from sunlight is absorbed by chlorophyll and converted 
    into stored chemical energy. In the Calvin cycle, the stored chemical 
    energy is used to synthesize glucose from carbon dioxide.
    
    During photosynthesis in plants, water (H₂O) and carbon dioxide (CO₂) are 
    used to produce glucose (C₆H₁₂O₆) and oxygen (O₂). The chemical equation is:
    6CO₂ + 6H₂O + light energy → C₆H₁₂O₆ + 6O₂"
    
    Include 6 multiple-choice questions and 4 short-answer questions, covering 
    all key concepts in the text. Questions should vary in difficulty from recall 
    to application and analysis.
    ```
    
    **Sample Output (Excerpt):**
    
    # Photosynthesis Assessment
    
    ## Multiple Choice Questions
    
    1. What is the primary purpose of photosynthesis?
       A. To convert water into oxygen
       B. To convert sunlight energy into usable chemical energy
       C. To break down glucose for energy
       D. To remove carbon dioxide from the atmosphere
    
    2. Which of the following is directly associated with capturing energy from sunlight?
       A. The Calvin cycle
       B. Cellular respiration
       C. Chlorophyll
       D. Glucose production
    
    3. The light-independent reactions of photosynthesis are also known as:
       A. The Krebs cycle
       B. The Calvin cycle
       C. The electron transport chain
       D. The glycolysis process
    
    ## Short Answer Questions
    
    7. Explain the relationship between light-dependent reactions and the Calvin cycle in photosynthesis. What does each process contribute to the overall outcome?
    
    8. Using the chemical equation from the text, explain what happens to water molecules during photosynthesis. Where do the hydrogen and oxygen atoms end up?
    
    **Key Benefits:**
    - The assessment directly aligns with the textbook's terminology and explanation
    - Questions cover exactly what students have learned from their course materials
    - The assessment follows the same conceptual organization as the textbook
    - The questions reflect the level of detail in the source material
    """)
    
    # Example 4: Student Work Analysis
    st.markdown("### Example 4: Student Work Analysis")
    
    st.markdown("""
    **Prompt with Reference Materials:**
    ```
    As a supportive writing instructor, analyze this 6th-grade student's 
    narrative essay according to our class rubric. Provide specific, 
    constructive feedback that acknowledges strengths and offers actionable 
    suggestions for improvement.
    
    STUDENT ESSAY:
    "The Big Game"
    
    I was nervus the day of the big game. Me and my team had practiced 
    for weeks and weeks. We really wanted to win the championship! 
    
    When I got to the field, I saw so many people in the stands. My 
    heart was beating fast and my hands were shaking. My couch told us 
    to remember all the things we practiced. He said "Just do your best 
    and have fun." That made me feel a little better.
    
    The game started and the other team was really good. They scored a 
    goal in the first ten minutes and everyone on my team looked sad. 
    But I remembered what my mom always says about not giving up.
    
    In the second half I got the ball and passed it to my friend Tyler. 
    He kicked it to Jamie and she scored! Everyone cheered so loud! 
    The game was tied 1-1.
    
    With only five minutes left, I got the ball again. I saw an opening 
    and started running. I kicked the ball as hard as I could and it went 
    in the goal! We won the game 2-1 and everyone was jumping and screaming. 
    It was the best day ever and I learned that hard work pays off and 
    to never give up.
    
    RUBRIC:
    1. Organization (20 points)
       - Clear beginning, middle, and end
       - Logical sequence of events
       - Coherent paragraphing
    
    2. Development (20 points)
       - Descriptive details and sensory language
       - Character thoughts and feelings included
       - Dialogue used effectively
    
    3. Voice (20 points)
       - Distinctive, engaging voice
       - Appropriate to narrative purpose
       - Consistent throughout
    
    4. Conventions (20 points)
       - Grade-appropriate spelling
       - Correct grammar and punctuation
       - Varied sentence structure
    
    5. Theme/Message (20 points)
       - Clear theme or message
       - Theme developed through events
       - Thoughtful conclusion
    
    Please provide specific examples from the text in your feedback and 
    suggest 2-3 priority areas for improvement.
    ```
    
    **Sample Output (Excerpt):**
    
    # Feedback on "The Big Game"
    
    Dear Writer,
    
    I enjoyed reading your narrative about the championship game! You've created an exciting story with a clear message about perseverance. Here's my feedback based on our class rubric:
    
    ## Strengths
    
    **Organization (17/20)**: Your story has a clear beginning that sets up your nervousness, a middle that shows the challenge of the opposing team scoring, and a satisfying end with your winning goal. Your paragraphing helps the reader follow the sequence of events nicely.
    
    **Voice (18/20)**: You have a genuine, authentic voice that sounds like a real 6th-grade student experiencing an important moment. Phrases like "my heart was beating fast and my hands were shaking" help readers connect with your feelings.
    
    **Theme/Message (19/20)**: Your conclusion about how "hard work pays off and to never give up" comes through clearly in your story. You showed this theme through both the team's comeback and your personal triumph.
    
    ## Areas for Growth
    
    **Conventions (14/20)**: I noticed a few spelling and grammar errors that could be fixed with careful proofreading:
    - "nervus" → "nervous"
    - "couch" → "coach"
    - Several missing commas in dialogue
    
    **Development (15/20)**: While you included some great details about how you felt, you could make the story even more vivid by adding:
    1. More sensory details - What did the field smell like? What sounds did you hear besides cheering?
    2. Expanded dialogue - Instead of only quoting your coach briefly, consider adding more conversation between teammates
    
    ## Revision Suggestions
    
    1. **First Priority**: Proofread carefully for spelling and grammar. Try reading your story aloud to catch errors.
    
    2. **Second Priority**: Add 3-5 more descriptive details that use different senses (sight, sound, smell, touch).
    
    3. **Third Priority**: Expand one moment in more detail - perhaps the moment you scored the winning goal. How exactly did it feel? What exactly did your teammates do?
    
    I can see your hard work in this story, and your excitement about the game comes through clearly. With some careful editing and added details, this will be an even more engaging narrative!
    
    **Key Benefits:**
    - The feedback directly applies the specific class rubric to the student's work
    - Comments reference actual examples from the student's writing
    - Suggestions are age-appropriate and focused on the most important improvements
    - The analysis creates a fair, balanced assessment based on established criteria
    """)
    
    # Example 5: Complete PCTFR Example
    st.markdown("### Example 5: Complete PCTFR Prompt")
    
    st.markdown("""
    This example shows how Reference Materials work together with Persona, Context, Task, and Format to create a comprehensive, powerful prompt:
    
    ```
    Persona: As an experienced high school physics teacher who explains complex concepts 
            through real-world applications and uses scaffolded instruction
    
    Context: For an 11th-grade physics class studying circular motion and centripetal force. 
            Most students have strong math skills (through Algebra 2) but struggle with 
            applying formulas to real-world scenarios.
    
    Task: Create a guided problem-solving worksheet
    
    Format: Structure the worksheet with:
           1. A brief review of key concepts and formulas (1 paragraph)
           2. A worked example with step-by-step reasoning
           3. 4 practice problems of increasing difficulty with hints
           4. A real-world application question as a challenge
    
    Reference: Base the content on our textbook's explanation of centripetal force:
              "Centripetal force is defined as the force that is necessary to keep an
              object moving in a curved path and that is directed inward toward the center
              of rotation. The magnitude of centripetal force on an object of mass m moving
              at speed v in a circle of radius r is given by: F = mv²/r
              
              Examples of centripetal force include:
              - The tension in a string when swinging an object in a horizontal circle
              - The gravitational force on a satellite in circular orbit
              - The force of friction on a car making a flat turn
              - The normal force on a roller coaster at the bottom of a loop
              
              For an object to remain in circular motion, this force must be continuously
              applied. If the force ceases, the object will continue in a straight-line path
              tangent to the circle at the point where the force was removed (Newton's First Law)."
    ```
    
    **Benefits of Including References:**
    - The worksheet will use the exact terminology and formula notation from the textbook
    - Examples will be consistent with those students have already seen
    - Practice problems will match the textbook's approach to applying the formula
    - The physics concepts will be explained using the same framework students are learning from
    """)
    
    # Reference Techniques Library
    st.markdown("## Reference Materials Techniques Library")
    
    st.markdown("""
    Here's a collection of techniques for effectively incorporating different types of reference materials:
    
    ### For Curriculum Standards
    
    **Standards-Based Lesson Design:**
    ```
    Create a lesson plan addressing these specific Next Generation Science Standards:
    [paste exact standards]
    
    Include learning objectives that directly use the language of these standards.
    ```
    
    **Cross-Standard Integration:**
    ```
    Design an interdisciplinary activity that addresses both these ELA standards:
    [paste ELA standards]
    
    AND these Social Studies standards:
    [paste Social Studies standards]
    ```
    
    ### For Textbook/Reading Materials
    
    **Text-Based Questions:**
    ```
    Based on this excerpt from [book title/chapter]:
    [paste excerpt]
    
    Create 5 text-dependent questions that require students to analyze the author's use of [literary element].
    ```
    
    **Vocabulary Extraction:**
    ```
    From this passage in our science textbook:
    [paste passage]
    
    Identify the 10 most important content-specific vocabulary terms and create a student-friendly
    definition and example sentence for each.
    ```
    
    ### For Student Work
    
    **Analytical Feedback:**
    ```
    Review this student essay:
    [paste student work]
    
    Using our class writing rubric:
    [paste rubric]
    
    Provide constructive feedback that identifies 3 strengths and 2 areas for improvement.
    ```
    
    **Progression Analysis:**
    ```
    Here are samples of a student's writing from September, December, and March:
    [paste three writing samples]
    
    Analyze the student's growth in these specific skills: [list skills]
    Recommend two focus areas for continued development.
    ```
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific guidance
    render_teacher_notes("""
    **Key Points to Emphasize:**
    
    * The examples demonstrate how reference materials create highly targeted, aligned content
    * Using references doesn't mean the AI just copies them - it uses them as guidance for its output
    * References can be combined with other prompt elements (PCTF) for even more targeted results
    * Different types of references serve different educational purposes
    
    **Discussion Questions:**
    
    * What curriculum documents, standards, or textbooks do you regularly reference that could be included in prompts?
    * How might including reference materials help ensure AI-generated content is appropriate for your specific teaching context?
    * What types of student work might benefit from AI analysis using your established rubrics or criteria?
    
    **Extension Activity:**
    
    Have participants identify one course-specific document they use regularly and create a prompt that incorporates it as a reference material.
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