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
    page_title="Lesson 5: Examples",
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
    "title": "Persona Engineering: Examples",
    "lesson": "5",
    "section": "examples",
    "order": 2
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_5_examples"
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
    "lesson_5_examples",
    "examples",
    "Lesson 5: Examples of Persona Engineering",
    """
    **This section demonstrates how persona engineering transforms AI responses.**
    
    You'll see:
    - Side-by-side comparisons of prompts with and without personas
    - Examples of different personas for various educational purposes
    - How combining persona with other prompt components creates powerful results
    
    Look through these examples to understand how persona engineering 
    helps generate responses with appropriate tone, style, and perspective.
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
    st.markdown("## Persona Engineering Examples")
    
    st.markdown("""
    The following examples demonstrate how using personas in your prompts significantly 
    affects the tone, style, and approach of AI responses. Compare these examples to see
    how persona engineering can transform educational content.
    """)
    
    # Example 1: Basic Explanation with Different Personas
    st.markdown("### Example 1: Same Topic, Different Personas")
    
    st.markdown("""
    See how different personas explain the same concept in dramatically different ways:
    
    **Basic Prompt (No Persona):**
    ```
    Explain what causes seasons on Earth.
    ```
    
    **Response:** A standard, textbook-like explanation of axial tilt and Earth's orbit around the sun.
    """)
    
    # Create tabs for different personas
    persona_tabs = st.tabs([
        "Elementary Teacher Persona", 
        "High School Physicist Persona", 
        "Storyteller Persona"
    ])
    
    with persona_tabs[0]:
        st.markdown("""
        **Prompt with Elementary Teacher Persona:**
        ```
        As an enthusiastic elementary school teacher who uses simple 
        language, visual aids, and everyday examples, explain what 
        causes seasons on Earth to 2nd-grade students.
        ```
        
        **Sample Response:**
        
        # Why We Have Seasons
        
        Hello, amazing scientists! 🌞❄️
        
        Do you know why sometimes it's hot outside and sometimes it's cold? That's because of seasons!
        
        Imagine the Earth is like a big ball spinning around the sun. But here's the fun part - Earth doesn't stand up straight! It's tilted, kind of like when you lean to one side.
        
        When our part of Earth is leaning toward the sun, the sun's light hits us more directly - like shining a flashlight straight at your hand instead of at an angle. That makes it summer for us - warm and with longer days!
        
        Then, as Earth travels around the sun, our part starts leaning away from the sun. Now the sun's light hits us at an angle - like shining a flashlight sideways at your hand. That makes it winter - colder and with shorter days.
        
        Let's try something! Get an orange (that's our Earth) and a flashlight (that's our sun). If you tilt the orange and shine the light, you'll see some parts get more light than others. That's exactly how seasons work!
        
        Remember: It's not that we're closer to the sun in summer - it's all about the tilt and how directly the sunlight hits us!
        """)
        
        st.success("""
        **Persona Elements:**
        - Uses simple, child-friendly language
        - Incorporates enthusiasm and direct address ("Hello, amazing scientists!")
        - Includes a hands-on demonstration idea
        - Uses emoji and exclamation points for engagement
        - Breaks down complex concepts into relatable analogies
        """)
    
    with persona_tabs[1]:
        st.markdown("""
        **Prompt with High School Physics Teacher Persona:**
        ```
        As a high school physics teacher who emphasizes precise 
        scientific terminology while making concepts accessible 
        through clear explanations and visual models, explain 
        what causes seasons on Earth.
        ```
        
        **Sample Response:**
        
        # The Physics of Earth's Seasons
        
        Earth's seasons are a direct result of our planet's axial tilt of approximately 23.5° relative to its orbital plane around the sun. This phenomenon creates several important effects that drive seasonal changes:
        
        **1. Variation in Solar Radiation Intensity**
        
        When a hemisphere is tilted toward the sun (summer), solar radiation:
        - Strikes the surface more directly (closer to perpendicular)
        - Travels through less atmosphere
        - Concentrates energy over a smaller area
        
        Conversely, during winter, solar radiation:
        - Strikes at an oblique angle
        - Travels through more atmosphere (increasing scattering)
        - Spreads the same energy over a larger area
        
        We can calculate this intensity using the formula: Energy intensity ∝ sin(90° - |latitude - axial tilt|)
        
        **2. Duration of Daylight**
        
        The axial tilt also affects how much of each hemisphere faces the sun during each 24-hour rotation:
        - Summer: More than half of a hemisphere's rotation faces the sun, creating longer days
        - Winter: Less than half of a hemisphere's rotation faces the sun, creating shorter days
        - Equinoxes: Equal halves face the sun, creating equal day/night durations
        
        **3. Common Misconception**
        
        It's important to note that seasons are NOT caused by Earth's distance from the sun. In fact, Earth is actually closest to the sun (perihelion) in early January, during Northern Hemisphere winter. This elliptical orbit variation has minimal effect compared to the axial tilt.
        
        To visualize this concept, imagine a flashlight shining on a globe at different angles – the more direct the light, the more concentrated the energy.
        """)
        
        st.success("""
        **Persona Elements:**
        - Uses precise scientific terminology
        - Organizes information systematically
        - Includes a mathematical relationship
        - Addresses common misconceptions
        - Uses section headers for clarity
        - Maintains an educational but more formal tone
        """)
    
    with persona_tabs[2]:
        st.markdown("""
        **Prompt with Storyteller Persona:**
        ```
        As a creative storyteller who uses narrative, metaphor,
        and personification to explain scientific concepts, create
        an engaging explanation of what causes seasons on Earth.
        ```
        
        **Sample Response:**
        
        # The Earth's Dance with the Sun
        
        Long ago, Earth made a choice. Unlike her planetary siblings who stood tall and proper in their orbits, Earth decided to tilt and dance through space with a jaunty angle of 23.5 degrees. This celestial posture would forever define the rhythm of life upon her surface.
        
        And so begins our tale of seasons...
        
        Imagine Earth as a graceful dancer, perpetually circling her partner, the radiant Sun. As she waltzes through space, her tilted posture means that sometimes her northern half bows toward the Sun, while other times, her southern half takes the bow.
        
        When the Northern realms lean toward their solar partner (we call this summer), they receive the Sun's full attention – his light falls directly upon them, showering them with warmth and long, lingering days. The southern lands, turned partly away during this movement of the dance, experience the cooler embrace of winter, with the Sun's light spreading thin and days growing short.
        
        Six months later, the partners have moved halfway through their annual dance, and Earth's southern domains now bow toward the Sun, receiving his direct light and warmth. Meanwhile, the northern lands turn away slightly, entering their winter chapter.
        
        Between these movements are the transitional steps of spring and autumn, when Earth stands neither fully turned toward nor away from her partner, and his light falls equally on both hemispheres.
        
        This dance continues, year after year, an eternal waltz that brings us the blooming renewal of spring, the vibrant energy of summer, the golden reflection of autumn, and the quiet rest of winter – not because Earth moves closer or farther from the Sun, but simply because of her elegant, tilted posture as she dances.
        
        And so, the seasons are born – not from distance, but from perspective – a cosmic lesson that how we're oriented matters more than how close we stand.
        """)
        
        st.success("""
        **Persona Elements:**
        - Uses narrative structure with a beginning
        - Incorporates personification (Earth as a dancer)
        - Uses metaphors (dance, partnership) throughout
        - Employs poetic, descriptive language
        - Creates emotion and wonder around a scientific concept
        - Concludes with a broader philosophical reflection
        """)
    
    # Example 2: Feedback with Different Personas
    st.markdown("### Example 2: Student Feedback Through Different Personas")
    
    st.markdown("""
    Compare how different personas provide feedback on the same student work:
    
    **Context:** *A middle school student has written an essay on their favorite historical figure but included some factual errors and organization issues while showing enthusiasm and creativity.*
    
    **Basic Prompt (No Persona):**
    ```
    Provide feedback on a middle school student's history essay.
    ```
    
    **Response:** Standard, generic feedback that might not address the specific balance needed for a developing writer.
    """)
    
    feedback_tabs = st.tabs([
        "Growth Mindset Coach", 
        "Writing Mentor", 
        "Historical Thinking Expert"
    ])
    
    with feedback_tabs[0]:
        st.markdown("""
        **Prompt with Growth Mindset Coach Persona:**
        ```
        As a supportive teacher who emphasizes growth mindset, 
        provide feedback on a middle school student's history essay
        that celebrates their strengths, views errors as learning 
        opportunities, and encourages persistence and improvement.
        ```
        
        **Sample Response:**
        
        # Feedback on Your Historical Figure Essay
        
        I'm so impressed by the enthusiasm and creativity you brought to this essay! Your passion for this historical figure really shines through, and that's something special that can't be taught. 
        
        ## What's Working Well
        
        * Your **personal connection** to this historical figure is powerful! I can really see why they inspire you.
        * Your **creative examples** show you're thinking beyond just facts - you're considering impact and legacy.
        * Your **voice** comes through strongly - this doesn't sound like every other essay, it sounds like YOU.
        
        ## Growth Opportunities
        
        Every writer - even professional historians - continues to grow and refine their work. Here are some next steps for your writing journey:
        
        * I noticed some dates and details that need a bit more research. This is a perfect chance to strengthen your **fact-checking skills** - a super important historian tool! Try checking 2-3 different sources for key facts.
        
        * Your ideas are excellent but sometimes jump between topics. Next time, try a **quick outline** before writing to create a roadmap for your readers to follow your thinking.
        
        * You've included great information about what your historical figure did, and your next challenge is to explore **why** their actions matter in the bigger historical picture.
        
        ## Your Next Steps
        
        Remember, every draft gets better! Historical writing is a skill that grows with practice. Which of these growth areas would you like to focus on first? I'm excited to see your revision and how your understanding continues to develop!
        
        You've got this! 💪
        """)
        
        st.success("""
        **Persona Elements:**
        - Begins with celebration of strengths
        - Uses encouraging language throughout
        - Frames challenges as "growth opportunities" and "next steps"
        - Normalizes the revision process as part of learning
        - Ends with encouragement and confidence in the student
        - Includes supportive emoji
        """)
    
    with feedback_tabs[1]:
        st.markdown("""
        **Prompt with Writing Mentor Persona:**
        ```
        As an experienced writing mentor who focuses on structure, 
        clarity, and the craft of writing, provide practical feedback
        on a middle school student's history essay with specific 
        revision strategies and examples.
        ```
        
        **Sample Response:**
        
        # Writing Feedback: Historical Figure Essay
        
        Thank you for sharing your essay on this fascinating historical figure. I've focused my feedback on the writing elements that will help strengthen your work.
        
        ## Structure & Organization
        
        Your essay currently moves between different aspects of your historical figure's life without a clear organizing principle. Consider these revisions:
        
        **Current organization:**  
        Birth → Famous achievement → Early life → Another achievement → Legacy
        
        **Suggested revision:**  
        Introduction & thesis → Early life & influences → Major achievements in chronological order → Legacy & impact → Conclusion
        
        **Quick fix:** Create topic sentences for each paragraph that connect to your main thesis about why this figure matters.
        
        ## Evidence & Support
        
        I noticed several factual elements that need verification:
        
        **Example:** You wrote "Lincoln was born in 1810" - Historical records show 1809.
        
        **Revision strategy:** Create a fact-checking table with three columns:
        1. Claim made in essay
        2. Verified fact from reliable source
        3. Source citation
        
        ## Voice & Clarity
        
        Your enthusiasm comes through strongly! Some sentences are very long, which can make your points harder to follow.
        
        **Original:** "He was really amazing and did so many incredible things that changed America forever and that's why I think he's the most important person who ever lived because without him everything would be different today."
        
        **Revised example:** "Lincoln made several crucial decisions that transformed America's future. His leadership during the Civil War preserved the Union. His Emancipation Proclamation began the process of ending slavery. These actions make him, in my view, one of history's most consequential leaders."
        
        ## Next Draft Focus
        
        1. Create a simple outline before revising
        2. Verify key facts with reliable sources
        3. Break long sentences into clearer, more focused statements
        
        I look forward to seeing your next draft. Your interest in this historical figure is compelling, and strengthening these writing elements will help your readers appreciate your insights.
        """)
        
        st.success("""
        **Persona Elements:**
        - Focuses primarily on writing craft rather than content
        - Provides specific examples with "before and after" revisions
        - Uses structural analysis with clear comparisons
        - Gives concrete, actionable revision strategies
        - Maintains encouraging tone while being direct about needs
        - Closes with a narrowed focus for manageable revision
        """)
    
    with feedback_tabs[2]:
        st.markdown("""
        **Prompt with Historical Thinking Expert Persona:**
        ```
        As a history educator who specializes in developing
        historical thinking skills, provide feedback on a 
        middle school student's history essay focusing on
        source evaluation, contextual understanding, and
        causal reasoning.
        ```
        
        **Sample Response:**
        
        # Developing Historical Thinking: Essay Feedback
        
        Your essay shows genuine interest in your chosen historical figure, which is the foundation of historical inquiry. My feedback focuses on helping you develop the key historical thinking skills that professional historians use.
        
        ## Historical Accuracy & Source Evaluation
        
        I noticed several factual discrepancies that provide an opportunity to discuss how historians verify information:
        
        * Your essay states that "[historical figure] single-handedly changed the course of the war." Historians typically view historical events as resulting from multiple factors and individuals. This is an opportunity to explore **historical complexity**.
        
        * Some dates and details differ from standard historical accounts. Consider:
            - What sources did you use?
            - Are some sources more reliable than others for different types of information?
            - Why might accounts differ about the same person or event?
        
        **Historical Thinking Challenge:** Find two different sources about your historical figure and compare how they describe the same event. What might explain any differences?
        
        ## Contextual Understanding
        
        Your essay focuses on your figure's actions but less on the historical context that shaped their choices and opportunities.
        
        **Questions to enhance contextual thinking:**
        - What social, political, or economic conditions existed during your figure's time?
        - How did these conditions make their actions either possible or necessary?
        - How might this person have acted differently in another time period?
        
        ## Causation & Significance
        
        You've stated that this figure was "very important to history," which opens the door to deeper analysis of historical causation:
        
        **Historical Significance Framework:**
        1. **Immediate impact:** What changed directly because of their actions?
        2. **Long-term consequences:** How did their actions influence developments years or decades later?
        3. **Alternative scenarios:** What might have happened if they hadn't taken these actions?
        4. **Diverse perspectives:** Who benefited and who was challenged by their actions?
        
        ## Next Steps in Historical Thinking
        
        For your revision, I suggest focusing on one of these historical thinking skills:
        1. Evaluating and citing reliable sources
        2. Placing your figure in historical context
        3. Analyzing the significance and impact of their actions from multiple perspectives
        
        Your enthusiasm for history is evident, and strengthening these analytical skills will deepen your understanding and enjoyment of the subject.
        """)
        
        st.success("""
        **Persona Elements:**
        - Focuses on discipline-specific thinking skills
        - Uses questioning as a teaching strategy
        - Provides frameworks for historical analysis
        - Treats factual errors as opportunities to discuss sourcing
        - Introduces discipline-specific concepts like contextual thinking
        - Maintains academic language while remaining accessible
        """)
    
    # Example 3: Complete PCTF Examples
    st.markdown("### Example 3: Complete PCTF Prompts")
    
    st.markdown("""
    These examples show how Persona works together with Context, Task, and Format to create comprehensive, powerful prompts:
    
    **Example A: Elementary Math Lesson**
    ```
    Persona: As an enthusiastic elementary math teacher who uses concrete examples, 
             visual representations, and encourages a growth mindset
             
    Context: For a 3rd-grade class that has been introduced to basic multiplication 
             but is struggling with the concept of division as the inverse operation
             
    Task: Create a 20-minute introductory lesson on division
    
    Format: Structure the lesson with:
            1. A real-world problem as a hook (1-2 minutes)
            2. A visual demonstration using equal grouping (5 minutes)
            3. 3 guided practice problems of increasing difficulty (10 minutes)
            4. A simple formative assessment exit ticket (2-3 minutes)
            5. A list of common misconceptions and how to address them
    ```
    
    **Example B: Literature Discussion Guide**
    ```
    Persona: As a Socratic discussion facilitator who values textual evidence, 
             diverse perspectives, and student-led inquiry
             
    Context: For an 11th-grade English class that has just finished reading 
             "The Great Gatsby" and has previously analyzed themes of the American 
             Dream in other texts
             
    Task: Develop a discussion guide exploring the novel's portrayal of wealth, 
          class, and social mobility
          
    Format: Structure the guide with:
            - An essential question to frame the discussion
            - 5-7 text-dependent questions organized from literal to interpretive to evaluative
            - 3 potential student response patterns with follow-up questions for each
            - Relevant textual passages with page numbers for reference
            - A synthesis activity for conclusion
    ```
    """)
    
    # Persona Library
    st.markdown("## Educational Persona Library")
    
    st.markdown("""
    Here's a collection of carefully crafted educational personas you can use or adapt in your prompts:
    
    ### For Teaching Different Age Groups
    
    **Early Elementary Educator:**
    ```
    As an energetic early elementary educator who uses simple language, 
    concrete examples, playful analogies, frequent questions, and an 
    encouraging tone
    ```
    
    **Middle School Educator:**
    ```
    As a relatable middle school teacher who balances academic content 
    with real-world connections, uses humor appropriately, acknowledges 
    different perspectives, and provides clear step-by-step explanations
    ```
    
    **High School Academic Specialist:**
    ```
    As a knowledgeable high school [subject] specialist who emphasizes 
    analytical thinking, makes connections to contemporary issues, uses 
    precise terminology while explaining concepts clearly, and encourages 
    independent inquiry
    ```
    
    ### For Specific Pedagogical Approaches
    
    **Socratic Questioner:**
    ```
    As a Socratic educator who primarily uses thoughtful questions rather 
    than direct answers, encourages critical thinking, helps identify 
    assumptions, and guides students to their own insights through structured inquiry
    ```
    
    **Project-Based Learning Coach:**
    ```
    As a project-based learning facilitator who emphasizes real-world problem-solving, 
    interdisciplinary connections, student agency, and practical application of concepts
    ```
    
    **Universal Design for Learning (UDL) Specialist:**
    ```
    As a UDL-trained educator who presents information through multiple modalities, 
    provides various engagement options, offers flexible approaches to demonstrating 
    understanding, and anticipates potential barriers to learning
    ```
    
    ### For Student Support and Feedback
    
    **Growth Mindset Coach:**
    ```
    As a growth mindset coach who emphasizes effort over innate ability, 
    sees mistakes as learning opportunities, provides process-oriented feedback, 
    celebrates progress, and builds student confidence through supportive language
    ```
    
    **Writing Mentor:**
    ```
    As a supportive writing mentor who balances encouragement with honest critique, 
    offers specific revision strategies, focuses on the writer's goals, and uses 
    model examples to illustrate effective techniques
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
    
    * Point out how the same core information is communicated completely differently through different personas
    * Highlight that persona is about more than just simplifying or complicating language - it's about approach and perspective
    * Note how persona can create emotional resonance and engagement that might otherwise be missing
    * Show how persona choice should align with educational goals - different personas serve different purposes
    
    **Discussion Questions:**
    
    * What personas do you already adopt in your teaching for different purposes?
    * How might different students respond to different personas in AI-generated content?
    * What subject-specific personas might be valuable in your teaching area?
    
    **Extension Activity:**
    
    Have participants analyze their own teaching "personas" - what voice, tone, and approach do they use in different teaching contexts? How could they translate that into prompt engineering?
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