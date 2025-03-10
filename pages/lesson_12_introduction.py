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
    page_title="Lesson 12: Role Prompting",
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
    "title": "Role Prompting",
    "lesson": "12",
    "section": "introduction",
    "order": 1
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_12_introduction"
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
    "lesson_12_introduction",
    "introduction",
    "Lesson 12: Role Prompting",
    """
    **Welcome to Lesson 12 on Role Prompting!**
    
    In this lesson, you'll learn:
    - How to use persona instructions to shape AI responses
    - Techniques for creating effective role-based prompts
    - When and why to use different personas for educational content
    - How to combine role prompting with other techniques
    
    This approach can significantly enhance the relevance and engagement of AI-generated content.
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
    st.markdown(f"# Lesson 12: {PAGE_INFO['title']}")
    
    # Objective
    st.markdown("## Objective")
    st.markdown("""
    To understand and apply role prompting techniques that guide AI to adopt specific personas,
    voices, and perspectives when generating educational content, making the content more engaging,
    appropriate, and effective for different learning contexts.
    """)
    
    # Real-world hook
    st.info("""
    ### Real-World Hook
    
    Think about how differently a kindergarten teacher, a university professor, and a peer tutor would 
    explain the same concept. Each would adjust their language, examples, and approach to match their role 
    and audience. Role prompting does exactly this with AI - it instructs the AI to adopt a specific persona 
    to make its responses more appropriate and effective for your particular educational needs.
    """)
    
    # Jargon-Free Explanation
    st.markdown("## Understanding Role Prompting")
    
    st.markdown("""
    **Role Prompting** (also called Persona Prompting) is a technique where you explicitly instruct the AI 
    to adopt a specific character, role, or voice when generating responses. It's the "P" (Persona) in our 
    PTC-FREI framework.

    When using role prompting, you're essentially saying:
    
    > "Act as [specific role/persona] while answering this question or completing this task."
    
    This approach shapes:
    - The **language and tone** of the response
    - The **examples and references** used
    - The **level of detail and complexity**
    - The **perspective** from which information is presented
    
    Role prompting is particularly powerful when combined with other techniques we've learned, such as 
    contextual prompting, format specification, and chain-of-thought reasoning.
    """)
    
    # Why it matters in education
    st.markdown("## Benefits for Education")
    
    st.markdown("""
    Role prompting offers several key benefits for educators:
    
    ### 1. Audience-Appropriate Content
    
    By specifying personas like "elementary science teacher" or "high school math coach," you can 
    generate content that uses age-appropriate language, examples, and complexity levels.
    
    ### 2. Engaging and Relatable Voice
    
    Content created in the voice of a "patient tutor," "enthusiastic science guide," or even 
    "historical figure" can be more engaging and memorable for students.
    
    ### 3. Multiple Perspectives
    
    You can generate explanations from different viewpoints, such as "explain this historical 
    event as a local citizen" versus "as a foreign diplomat" to promote critical thinking.
    
    ### 4. Modeling Expert Thinking
    
    Having the AI assume the role of an expert in a field can model how specialists approach 
    problems and communicate about their areas of expertise.
    
    ### 5. Cultural and Contextual Sensitivity
    
    Role prompting can help ensure content respects specific cultural contexts or educational 
    traditions when needed.
    """)
    
    # Key concepts
    st.markdown("## Key Elements of Effective Role Prompts")
    
    st.markdown("""
    ### 1. Specific Role Definition
    
    Be clear and specific about the role you want the AI to adopt. "Act as a biology teacher" 
    is good, but "Act as a high school AP Biology teacher with 15 years of experience" provides 
    even more guidance.
    
    ### 2. Audience Awareness
    
    Include information about who the content is for. "Explain this to 3rd-grade students" 
    helps the AI adjust its language and examples appropriately.
    
    ### 3. Behavioral Characteristics
    
    Specify how the persona should behave. "Be patient and encouraging" or "Use a Socratic 
    questioning approach" shapes the tone and teaching style.
    
    ### 4. Knowledge Parameters
    
    Define what knowledge base the persona has access to. "As a science historian specializing 
    in the 20th century" helps focus the content appropriately.
    
    ### 5. Communication Style
    
    Indicate the desired communication style. "Use simple analogies," "incorporate humor," or 
    "be concise and direct" shapes how information is presented.
    """)
    
    # Simple comparison
    st.markdown("## Basic vs. Role-Based Approach")
    
    basic_prompt = """
    Explain the water cycle.
    """
    
    role_prompt = """
    Act as an enthusiastic elementary science teacher explaining 
    the water cycle to 2nd-grade students. Use simple language, 
    relatable examples, and an engaging tone that would capture 
    young children's attention and make them excited about science.
    """
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Basic Prompt:")
        st.code(basic_prompt, language="text")
        st.markdown("""
        **Typical response:**
        
        The water cycle, also known as the hydrologic cycle, is a continuous process by which water circulates between the Earth's oceans, atmosphere, and land. It involves the following major processes: evaporation, transpiration, condensation, precipitation, and runoff.
        
        Evaporation occurs when the sun heats up water in rivers, lakes, and oceans, turning it into water vapor that rises into the air. Transpiration is the process by which plants release water vapor into the atmosphere. Together, these processes are called evapotranspiration.
        
        As water vapor rises into the cooler atmosphere, it condenses to form clouds. When the water droplets in clouds become too heavy, they fall back to Earth as precipitation in the form of rain, snow, sleet, or hail. The precipitation that falls on land may then flow across the surface as runoff, eventually returning to bodies of water, or it may infiltrate the ground, becoming groundwater.
        
        Groundwater can be stored in aquifers for long periods or eventually seep into streams, lakes, and oceans, where the cycle begins again. This continuous movement of water is essential for maintaining Earth's ecosystems and weather patterns.
        """)
        
    with col2:
        st.markdown("### Role-Based Prompt:")
        st.code(role_prompt, language="text")
        st.markdown("""
        **Improved response:**
        
        # The Magical Water Cycle Adventure!
        
        Hello, my amazing scientists! Today we're going to learn about something SUPER COOL - the water cycle! It's like a never-ending water ride that happens all around us every day!
        
        🌊 First, imagine you're at the beach, and the sun is shining down on the ocean. The sun is like a giant hairdryer, warming up the water! But instead of staying in the ocean, some water turns into a gas called water vapor that we can't see. This is called EVAPORATION! It's like the water is playing hide-and-seek!
        
        ☁️ The invisible water vapor floats up, up, UP into the sky! As it goes higher, it gets colder (just like how it's colder at the top of a slide than at the bottom). When it gets cold enough, the water vapor turns back into tiny water droplets that we CAN see - and that's how CLOUDS are made! This is called CONDENSATION! It's like the water is putting on its cloud costume!
        
        🌧️ When the clouds get really full of water - kind of like a sponge that can't hold any more - the water falls back down to Earth as rain, snow, or hail. This is called PRECIPITATION! It's like the sky is giving Earth a big drink of water!
        
        🏞️ Where does the water go next? Some soaks into the ground to help plants grow. Some flows into rivers and streams in a big race back to the ocean! And once it reaches the ocean...guess what? The whole amazing cycle starts all over again!
        
        Let's try a fun activity: Stand up and let's act out the water cycle together! First, squat down low - you're water in the ocean. Now, as the sun shines, slowly rise up with your arms waving - you're evaporating! Gather together with friends and hold hands - you're forming a cloud! Then drop back down to the ground - you're precipitation! And finally, wiggle your way across the floor back to where you started - you're flowing back to the ocean!
        
        Isn't it AMAZING how water keeps going around and around in this fantastic cycle? Water is such a superhero - the same water dinosaurs splashed in millions of years ago might be in your water bottle today! WOW!
        
        What questions do you have about our water cycle adventure?
        """)
    
    # Connection to Persona component
    st.markdown("## Role Prompting and the Persona Component")
    
    st.markdown("""
    Role prompting is the practical application of the "P" (Persona) component in our PTC-FREI framework. 
    While we briefly covered the Persona component in Lesson 5, this lesson explores advanced techniques 
    and applications specifically for educational contexts.
    
    When using the full PTC-FREI framework, your role prompting would be combined with:
    - **Task**: The specific output you want
    - **Context**: Background information and situational details
    - **Format**: The structure and organization of the response
    - **Reference**: Source materials or standards to incorporate
    
    For example:
    
    ```
    [Persona] Acting as a patient high school math tutor
    [Task] Explain how to solve quadratic equations
    [Context] For students who understand basic algebra but struggle with factoring
    [Format] Using a step-by-step guide with examples
    [Reference] Aligned with Common Core Math Standards
    ```
    
    This comprehensive approach creates highly tailored educational content that's both pedagogically 
    effective and engaging for students.
    """)
    
    # Role Selection Guidance
    st.markdown("## Choosing the Right Role for Your Purpose")
    
    st.markdown("""
    Different educational needs call for different personas. Here are some guidelines for selecting effective roles:
    
    | Educational Purpose | Useful Personas |
    |---------------------|-----------------|
    | Initial introduction to concepts | Enthusiastic guides, storytellers, relatable figures |
    | Detailed explanations | Patient tutors, subject matter experts, mentors |
    | Critical thinking development | Devil's advocates, Socratic questioners, diverse viewpoints |
    | Skill practice and feedback | Coaches, supportive peers, master practitioners |
    | Motivation and engagement | Inspirational figures, relatable role models, characters from literature |
    | Addressing misconceptions | Myth busters, detectives, "common mistake" spotters |
    
    When choosing a role, consider:
    - The age and background of your students
    - The subject matter and its challenges
    - The specific learning objectives
    - Cultural relevance and appropriateness
    - The emotional tone you want to establish
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Connect role prompting to the educational concept of "voice and tone" in writing and communication
    * Emphasize that different personas work better for different students - differentiation opportunity
    * Point out how role prompting can help address issues of representation and inclusivity
    * Discuss how combining role prompting with chain-of-thought (from previous lesson) can be particularly powerful
    
    **Implementation Ideas:**
    
    * Create content in the voice of historical figures to bring primary sources to life
    * Generate explanations of the same concept using different personas to support diverse learning styles
    * Use role prompting to create more engaging and age-appropriate instructions for assignments
    * Develop discipline-specific academic language by using expert personas
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