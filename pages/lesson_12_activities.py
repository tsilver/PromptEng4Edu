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
    page_title="Lesson 12: Activities",
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
    "title": "Role Prompting: Activities",
    "lesson": "12",
    "section": "activities",
    "order": 3
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_12_activities"
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
    "lesson_12_activities",
    "activities",
    "Role Prompting: Activities",
    """
    **This section provides hands-on practice with role prompting.**
    
    You'll:
    - Create your own role-based prompts for different educational purposes
    - Transform basic prompts into more effective role-based versions
    - Identify ideal personas for various educational contexts
    - Practice combining role prompting with other techniques
    
    Complete these activities to strengthen your role prompting skills before
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
    
    Complete the activities below to practice creating effective role-based prompts.
    After finishing these activities, proceed to the Reflection section to consolidate your learning 
    and unlock the next lesson.
    """)
    
    # Activity 1
    st.markdown("## Activity 1: Persona Selection for Different Purposes")
    
    st.markdown("""
    Different educational goals call for different types of personas. In this activity, you'll practice 
    selecting the most appropriate personas for specific educational needs.
    """)
    
    st.markdown("### Match the educational purpose with the most appropriate persona:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**1. Making abstract concepts concrete for young learners**")
        persona1 = st.selectbox(
            "Choose the most appropriate persona:",
            [
                "Choose a persona...",
                "A university professor with expertise in the field",
                "A magical character who can transform concepts into stories",
                "A technical expert who values precision",
                "A debate moderator presenting multiple viewpoints"
            ],
            key="persona_match1"
        )
        
        if persona1 == "A magical character who can transform concepts into stories":
            st.success("Great choice! Magical characters can make abstract ideas tangible through metaphors and stories, which works well for young learners.")
        elif persona1 != "Choose a persona...":
            st.info("Consider which persona would naturally use concrete examples, metaphors, and visuals that young children can relate to.")
    
    with col2:
        st.markdown("**2. Teaching a complex scientific process to high school students**")
        persona2 = st.selectbox(
            "Choose the most appropriate persona:",
            [
                "Choose a persona...",
                "A friendly kindergarten teacher",
                "A drill sergeant focused on memorization",
                "A passionate scientist who breaks down complex ideas step-by-step",
                "A poet who speaks in metaphors"
            ],
            key="persona_match2"
        )
        
        if persona2 == "A passionate scientist who breaks down complex ideas step-by-step":
            st.success("Excellent! A passionate scientist persona naturally combines technical accuracy with the ability to explain complex ideas in accessible ways.")
        elif persona2 != "Choose a persona...":
            st.info("Consider which persona would maintain scientific accuracy while making the content engaging and accessible to high school students.")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("**3. Encouraging critical thinking about a historical event**")
        persona3 = st.selectbox(
            "Choose the most appropriate persona:",
            [
                "Choose a persona...",
                "A biased news reporter giving only one perspective",
                "A time-traveling journalist interviewing people from different sides",
                "A cheerful entertainer focused on fun facts",
                "A drill sergeant demanding memorization of dates"
            ],
            key="persona_match3"
        )
        
        if persona3 == "A time-traveling journalist interviewing people from different sides":
            st.success("Great choice! A time-traveling journalist naturally presents multiple perspectives and primary sources, encouraging critical analysis.")
        elif persona3 != "Choose a persona...":
            st.info("Consider which persona would naturally present multiple perspectives and encourage analysis rather than simple memorization.")
    
    with col4:
        st.markdown("**4. Providing encouraging feedback on student writing**")
        persona4 = st.selectbox(
            "Choose the most appropriate persona:",
            [
                "Choose a persona...",
                "A harsh literary critic focused only on flaws",
                "A supportive writing coach who balances encouragement with constructive feedback",
                "A grammar police officer concerned only with rules",
                "A fellow student with limited expertise"
            ],
            key="persona_match4"
        )
        
        if persona4 == "A supportive writing coach who balances encouragement with constructive feedback":
            st.success("Perfect! A supportive writing coach naturally balances positive reinforcement with specific suggestions for improvement.")
        elif persona4 != "Choose a persona...":
            st.info("Consider which persona would provide feedback in a way that motivates continued effort while still helping students improve.")
    
    # Activity 2
    st.markdown("## Activity 2: Creating Rich Persona Descriptions")
    
    st.markdown("""
    Effective role prompting requires rich, specific persona descriptions. In this activity, you'll practice 
    creating detailed persona specifications for educational contexts.
    """)
    
    st.markdown("""
    ### Select an educational context and create a detailed persona description:
    
    For your chosen context, develop a persona description that includes:
    1. **The basic role** (who they are)
    2. **Relevant expertise** (what they know)
    3. **Personality traits** (how they communicate)
    4. **Teaching approach** (how they explain concepts)
    5. **Relationship with audience** (how they relate to students)
    """)
    
    educational_context = st.selectbox(
        "Choose an educational context:",
        [
            "Elementary Math: Teaching fractions",
            "Middle School Science: Introducing the scientific method",
            "High School Literature: Analyzing Shakespeare",
            "College Economics: Explaining supply and demand",
            "Teacher Professional Development: Classroom management strategies"
        ],
        key="ed_context"
    )
    
    st.markdown("### Now create your detailed persona description:")
    
    persona_description = st.text_area(
        "Write a rich, detailed persona description for your chosen educational context:",
        height=150,
        placeholder="Act as a...",
        key="persona_description"
    )
    
    if persona_description:
        st.success("You've created a persona description! Let's analyze its components:")
        
        # Simple analysis of the persona description
        components = {
            "Basic role": "✓" if len(persona_description.split()) >= 5 else "❌",
            "Expertise": "✓" if "experience" in persona_description.lower() or "expert" in persona_description.lower() or "specialist" in persona_description.lower() or "knowledge" in persona_description.lower() else "❌",
            "Personality": "✓" if "friendly" in persona_description.lower() or "patient" in persona_description.lower() or "enthusiastic" in persona_description.lower() or "passionate" in persona_description.lower() or "kind" in persona_description.lower() else "❌",
            "Teaching approach": "✓" if "explain" in persona_description.lower() or "teach" in persona_description.lower() or "guide" in persona_description.lower() or "show" in persona_description.lower() or "approach" in persona_description.lower() else "❌",
            "Audience relationship": "✓" if "student" in persona_description.lower() or "learner" in persona_description.lower() or "audience" in persona_description.lower() or "children" in persona_description.lower() or "class" in persona_description.lower() else "❌"
        }
        
        for component, status in components.items():
            st.write(f"{component}: {status}")
        
        if all(status == "✓" for status in components.values()):
            st.success("Excellent! Your persona description includes all key components for effective role prompting.")
        else:
            missing = [component for component, status in components.items() if status == "❌"]
            if missing:
                st.info(f"Consider adding more details about: {', '.join(missing)}")
        
        st.markdown("""
        ### Tips for Refining Your Persona:
        
        1. **Be Specific:** Instead of "a science teacher," try "a marine biologist who has spent 15 years studying ocean ecosystems and loves using hands-on demonstrations"
        
        2. **Add Personality:** Include traits that shape communication style, like "patient," "enthusiastic," or "methodical"
        
        3. **Specify Teaching Methods:** Mention how they teach, such as "uses everyday analogies" or "asks Socratic questions"
        
        4. **Define Expertise Level:** Clarify their knowledge base with details like "specializes in Renaissance literature" or "has practical experience in elementary classrooms"
        
        5. **Include Audience Awareness:** Mention how they relate to students, such as "speaks in a supportive, encouraging tone for beginners"
        """)
    
    # Activity 3
    st.markdown("## Activity 3: Transforming Basic Prompts with Role Prompting")
    
    st.markdown("""
    In this activity, you'll practice transforming basic prompts into more effective role-based prompts
    for specific educational purposes.
    """)
    
    # Create tabs for different transformation exercises
    prompt_tabs = st.tabs(["Elementary", "Middle School", "High School"])
    
    with prompt_tabs[0]:
        st.markdown("""
        ### Transform this elementary education prompt:
        
        **Basic Prompt:**
        ```
        Explain the life cycle of a butterfly.
        ```
        
        **Your Task:** Transform this into a role-based prompt that would create an engaging, 
        age-appropriate explanation for 2nd-grade students.
        """)
        
        elementary_transform = st.text_area(
            "Your transformed role-based prompt:",
            height=150,
            placeholder="Act as a...",
            key="elementary_transform"
        )
        
        if elementary_transform:
            st.success("You've transformed the elementary prompt! Let's analyze its effectiveness:")
            
            # Check for key elements
            has_role = "act as" in elementary_transform.lower() or "as a" in elementary_transform.lower() or "role of" in elementary_transform.lower()
            has_age = "2nd" in elementary_transform.lower() or "second" in elementary_transform.lower() or "grade" in elementary_transform.lower() or "elementary" in elementary_transform.lower() or "young" in elementary_transform.lower() or "child" in elementary_transform.lower()
            has_engagement = "engaging" in elementary_transform.lower() or "fun" in elementary_transform.lower() or "exciting" in elementary_transform.lower() or "interesting" in elementary_transform.lower() or "story" in elementary_transform.lower()
            
            if has_role and has_age and has_engagement:
                st.success("Excellent transformation! Your prompt includes a clear role, age-appropriate considerations, and elements to increase engagement.")
            else:
                if not has_role:
                    st.info("Consider specifying a clear role or persona at the beginning of your prompt (e.g., 'Act as a...')")
                if not has_age:
                    st.info("Consider mentioning the audience age or grade level to ensure age-appropriate content")
                if not has_engagement:
                    st.info("Consider adding elements to make the explanation more engaging for young learners")
            
            st.markdown("""
            ### Example of an Effective Transformation:
            
            ```
            Act as a friendly butterfly expert visiting a 2nd-grade classroom. 
            Explain the life cycle of a butterfly using simple language, colorful 
            descriptions, and an enthusiastic tone. Compare the butterfly's changes 
            to things children might be familiar with, and include an interactive 
            element where students can pretend to go through the butterfly life 
            cycle themselves.
            ```
            """)
    
    with prompt_tabs[1]:
        st.markdown("""
        ### Transform this middle school prompt:
        
        **Basic Prompt:**
        ```
        Explain how to solve two-step equations.
        ```
        
        **Your Task:** Transform this into a role-based prompt that would create a clear, 
        engaging explanation for middle school math students who find equations challenging.
        """)
        
        middle_transform = st.text_area(
            "Your transformed role-based prompt:",
            height=150,
            placeholder="Act as a...",
            key="middle_transform"
        )
        
        if middle_transform:
            st.success("You've transformed the middle school prompt! Let's analyze its effectiveness:")
            
            # Check for key elements
            has_role = "act as" in middle_transform.lower() or "as a" in middle_transform.lower() or "role of" in middle_transform.lower()
            has_audience = "middle" in middle_transform.lower() or "student" in middle_transform.lower() or "grade" in middle_transform.lower() or "challenging" in middle_transform.lower() or "struggle" in middle_transform.lower()
            has_approach = "step" in middle_transform.lower() or "clear" in middle_transform.lower() or "simple" in middle_transform.lower() or "example" in middle_transform.lower() or "method" in middle_transform.lower()
            
            if has_role and has_audience and has_approach:
                st.success("Excellent transformation! Your prompt includes a clear role, audience understanding, and an effective teaching approach.")
            else:
                if not has_role:
                    st.info("Consider specifying a clear role or persona at the beginning of your prompt (e.g., 'Act as a...')")
                if not has_audience:
                    st.info("Consider describing the audience and their needs to ensure relevant content")
                if not has_approach:
                    st.info("Consider specifying a teaching approach that would work well for this challenging topic")
            
            st.markdown("""
            ### Example of an Effective Transformation:
            
            ```
            Act as a patient, encouraging math coach who specializes in helping 
            students who find algebra challenging. Explain how to solve two-step 
            equations using clear, simple language and real-world examples that 
            middle school students would relate to. Include a step-by-step method 
            with visual cues, address common mistakes students make, and provide 
            a simple memory trick to help them remember the correct order of operations.
            ```
            """)
    
    with prompt_tabs[2]:
        st.markdown("""
        ### Transform this high school prompt:
        
        **Basic Prompt:**
        ```
        Analyze the causes of the Civil War.
        ```
        
        **Your Task:** Transform this into a role-based prompt that would create a nuanced, 
        thought-provoking analysis for high school history students.
        """)
        
        high_transform = st.text_area(
            "Your transformed role-based prompt:",
            height=150,
            placeholder="Act as a...",
            key="high_transform"
        )
        
        if high_transform:
            st.success("You've transformed the high school prompt! Let's analyze its effectiveness:")
            
            # Check for key elements
            has_role = "act as" in high_transform.lower() or "as a" in high_transform.lower() or "role of" in high_transform.lower()
            has_nuance = "perspective" in high_transform.lower() or "viewpoint" in high_transform.lower() or "multiple" in high_transform.lower() or "different" in high_transform.lower() or "complex" in high_transform.lower()
            has_critical = "critical" in high_transform.lower() or "analyze" in high_transform.lower() or "evaluate" in high_transform.lower() or "evidence" in high_transform.lower() or "question" in high_transform.lower()
            
            if has_role and has_nuance and has_critical:
                st.success("Excellent transformation! Your prompt includes a clear role, encourages nuanced analysis, and promotes critical thinking.")
            else:
                if not has_role:
                    st.info("Consider specifying a clear role or persona at the beginning of your prompt (e.g., 'Act as a...')")
                if not has_nuance:
                    st.info("Consider adding elements that encourage examination of multiple perspectives or complexities")
                if not has_critical:
                    st.info("Consider adding elements that promote critical thinking and evidence-based analysis")
            
            st.markdown("""
            ### Example of an Effective Transformation:
            
            ```
            Act as a panel of three different historians from different eras and 
            regions (Northern, Southern, and modern) discussing the causes of the 
            Civil War for an advanced high school history class. Present each 
            historian's perspective with appropriate evidence and reasoning, highlighting 
            areas of agreement and disagreement. Conclude with thought-provoking 
            questions that would help students evaluate the relative importance of 
            different factors and develop their own evidence-based interpretation.
            ```
            """)
    
    # Activity 4
    st.markdown("## Activity 4: Combining Role Prompting with Other Techniques")
    
    st.markdown("""
    In this activity, you'll practice combining role prompting with other techniques you've 
    learned in this course, such as chain-of-thought prompting or few-shot examples.
    """)
    
    st.markdown("""
    ### Choose a combination to explore:
    
    Select one of the following combinations, then create a prompt that effectively combines 
    role prompting with the selected technique.
    """)
    
    combination = st.radio(
        "Which combination would you like to explore?",
        [
            "Role Prompting + Chain-of-Thought Prompting",
            "Role Prompting + Few-Shot Examples",
            "Role Prompting + Context Specification",
            "Role Prompting + Format Requirements"
        ],
        key="combination"
    )
    
    if combination == "Role Prompting + Chain-of-Thought Prompting":
        st.markdown("""
        ### Combining Role Prompting with Chain-of-Thought Prompting
        
        This powerful combination not only specifies who is explaining, but also how they should 
        think through the problem or concept step-by-step.
        
        **Example Structure:**
        ```
        Act as [specific role with relevant traits].
        
        Explain [concept/process/problem] by thinking step-by-step through 
        your reasoning process. As you explain, make sure to:
        
        1. Start with [specific first step in reasoning]
        2. Then consider [specific second step]
        3. Next, analyze [specific third step]
        4. Finally, conclude with [specific final step]
        
        Throughout your explanation, maintain the [specific characteristics] 
        of your role while making your thinking process explicit.
        ```
        """)
    
    elif combination == "Role Prompting + Few-Shot Examples":
        st.markdown("""
        ### Combining Role Prompting with Few-Shot Examples
        
        This combination defines a persona that should generate content and provides examples 
        of the desired output in that persona's voice.
        
        **Example Structure:**
        ```
        Act as [specific role with relevant traits].
        
        I need you to create [type of content] in your role. Here are two examples 
        of the kind of [content type] I'm looking for:
        
        Example 1:
        "[Sample content in the persona's voice]"
        
        Example 2:
        "[Another sample in the persona's voice]"
        
        Using these examples as a guide for tone and style, create [number] 
        original [content type] about [topic] while maintaining your role.
        ```
        """)
    
    elif combination == "Role Prompting + Context Specification":
        st.markdown("""
        ### Combining Role Prompting with Context Specification
        
        This combination defines both who is speaking and the specific context or background 
        information they should incorporate.
        
        **Example Structure:**
        ```
        Act as [specific role with relevant traits].
        
        Context:
        - [Specific background information]
        - [Student characteristics or needs]
        - [Previous learning or prerequisites]
        - [Curricular context or standards]
        
        Based on this context, [explain/create/analyze] [topic] in a way that 
        is appropriate for [specific audience] while maintaining your role.
        ```
        """)
    
    elif combination == "Role Prompting + Format Requirements":
        st.markdown("""
        ### Combining Role Prompting with Format Requirements
        
        This combination defines both who is speaking and the specific format or structure 
        the response should follow.
        
        **Example Structure:**
        ```
        Act as [specific role with relevant traits].
        
        Create [content type] about [topic] following this specific format:
        
        1. [First section heading]
           - [Requirements for this section]
           
        2. [Second section heading]
           - [Requirements for this section]
           
        3. [Third section heading]
           - [Requirements for this section]
           
        While following this format, maintain the [specific characteristics] 
        of your role throughout.
        ```
        """)
    
    # Combined prompt creation
    st.markdown("### Create Your Combined Prompt")
    
    topic = st.text_input(
        "Choose a topic or concept to focus on:",
        placeholder="e.g., 'photosynthesis' or 'solving quadratic equations'",
        key="combined_topic"
    )
    
    combined_prompt = st.text_area(
        f"Write a prompt that combines Role Prompting with {combination.split('+')[1].strip()}:",
        height=200,
        key="combined_prompt"
    )
    
    if topic and combined_prompt:
        st.success(f"You've created a combined prompt about {topic}!")
        
        # General feedback about combined approaches
        st.markdown("""
        ### Benefits of Combined Approaches
        
        Combining role prompting with other techniques creates more powerful prompts that:
        
        1. **Provide more structure** - The combination gives more specific guidance about both voice and content
        
        2. **Create consistent outputs** - Multiple techniques help ensure the AI follows all aspects of your requirements
        
        3. **Enhance educational value** - Each technique addresses different aspects of effective educational content
        
        4. **Enable creative solutions** - The combination often produces more innovative and engaging responses
        
        As you develop your prompting skills, experimenting with these combinations will help you generate 
        increasingly effective educational content tailored to your specific needs.
        """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * For Activity 1, emphasize that different educational purposes may require different personas - there's no one-size-fits-all approach
    * For Activity 2, encourage participants to think about actual teachers they admire and what makes their teaching style effective
    * For Activity 3, remind participants that effective role prompts are specific and detailed, not just generic labels
    * For Activity 4, highlight how combining techniques addresses different aspects of prompt engineering for maximum effectiveness
    
    **Common Challenges:**
    
    * Some participants may create overly simplistic roles (e.g., "Act as a teacher") without enough specificity
    * Others may focus too much on the persona and not enough on the educational purpose
    * Participants might need encouragement to be creative with personas beyond obvious educational roles
    
    **Extension Ideas:**
    
    * Prompt library creation: Have participants develop a "persona library" for different educational purposes
    * Persona profile cards: Create detailed persona cards that can be quickly referenced for common educational needs
    * Role comparison: Generate content using different personas and analyze the differences in effectiveness
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