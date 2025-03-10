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
    page_title="Lesson 2: Activities",
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
    "title": "The Power of Context: Activities",
    "lesson": "2",
    "section": "activities",
    "order": 3
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_2_activities"
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
    "lesson_2_activities",
    "activities",
    "Lesson 2 Activities",
    """
    **This section provides hands-on practice with context in prompting.**
    
    You'll:
    - Analyze the impact of context on AI responses
    - Create prompts with varying levels of context
    - See how context shapes educational content
    
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
    
    Complete the activities below to practice adding context to your prompts.
    After finishing these activities, proceed to the Reflection section to solidify your learning 
    and unlock the next lesson.
    """)
    
    # Activity 1
    st.markdown("## Activity 1: Compare Responses with Different Contexts")
    
    st.markdown("""
    Let's explore how changing the context affects the AI's response to the same basic prompt.
    
    **Base prompt:** "Explain the concept of fractions."
    
    Add different contexts below and observe how the responses change:
    """)
    
    # Context options
    context_option = st.radio(
        "Select a context to add:",
        [
            "For 2nd grade students who are just learning about fractions.",
            "For middle school algebra students who need to solve equations with fractions.",
            "For a culinary class learning about measurement conversions in recipes."
        ],
        key="context_option"
    )
    
    # Display the complete prompt
    st.markdown("### Complete Prompt:")
    st.code(f"Explain the concept of fractions. {context_option}")
    
    # Compare button (in a real implementation, this would call the AI)
    if st.button("See How Context Changes the Response", key="compare_responses"):
        if "For 2nd grade" in context_option:
            st.success("Response tailored for young learners:")
            st.markdown("""
            Fractions are like slices of pizza! 🍕
            
            Imagine you have a whole pizza. If you cut it into 4 equal pieces and take 1 piece, you have 1/4 (one-fourth) of the pizza.
            
            The bottom number (4) tells us how many equal pieces the whole thing is divided into.
            The top number (1) tells us how many pieces we're talking about.
            
            You can see fractions everywhere:
            - Half an apple (1/2)
            - Quarter of a cookie (1/4)
            - Three-quarters of a glass of milk (3/4)
            
            Let's practice: If you eat 2 slices of a pizza that has 8 equal slices, what fraction of the pizza did you eat? That's right, 2/8 (which can also be called 1/4)!
            """)
        
        elif "middle school" in context_option:
            st.success("Response tailored for algebra students:")
            st.markdown("""
            # Fractions in Algebraic Equations
            
            Fractions represent division and are essential in algebraic operations. When working with equations containing fractions, remember these key principles:
            
            ## Basic Operations with Fractions in Equations
            
            1. **Addition/Subtraction**: Find a common denominator first
               - Example: Solving $\\frac{x}{3} + \\frac{x}{4} = 7$
               - Convert to $\\frac{4x}{12} + \\frac{3x}{12} = 7$
               - Simplify to $\\frac{7x}{12} = 7$
            
            2. **Multiplication**: Multiply across numerators and denominators
               - Example: $\\frac{2}{3} \\cdot \\frac{x}{5} = \\frac{2x}{15}$
            
            3. **Division**: Multiply by the reciprocal
               - Example: $\\frac{x}{4} ÷ \\frac{2}{3} = \\frac{x}{4} \\cdot \\frac{3}{2} = \\frac{3x}{8}$
            
            4. **Clearing Fractions**: Multiply both sides by the LCD (Least Common Denominator)
               - Example: To solve $\\frac{x}{3} - \\frac{1}{6} = \\frac{5}{6}$
               - Multiply all terms by 6: $2x - 1 = 5$
               - Solve: $2x = 6$, so $x = 3$
            
            Remember that fractions in algebra follow the same rules as numeric fractions, but variables can be in the numerator, denominator, or both.
            """)
        
        else:
            st.success("Response tailored for culinary students:")
            st.markdown("""
            # Understanding Fractions in Culinary Measurements
            
            Fractions are essential in the kitchen and appear throughout recipes and measurement systems.
            
            ## Practical Applications in Cooking
            
            ### Recipe Scaling
            When you need to halve a recipe that calls for 3/4 cup of flour, you'll need 3/8 cup (3/4 ÷ 2 = 3/8).
            
            ### Measurement Conversions
            - 1/4 cup = 4 tablespoons
            - 1/3 cup = 5 tablespoons + 1 teaspoon
            - 1/2 cup = 8 tablespoons
            
            ### Working with Mixed Measurements
            When a recipe calls for 1 1/2 cups of milk, you're using a mixed number (1 + 1/2).
            
            ### Precise Portioning
            Professional bakers often use weight instead of volume, but fractions remain important:
            - 1/4 pound = 4 ounces
            - 1/3 pound ≈ 5.3 ounces
            
            ### Practical Equivalents
            - 1/16 tsp = a pinch
            - 1/8 tsp = a dash
            - 1/4 tsp = a quarter teaspoon
            
            Understanding fractions allows you to accurately adjust recipes, portion ingredients, and convert between measurement systems - all crucial skills in professional cooking.
            """)
        
        st.markdown("""
        **Notice how:**
        - The language complexity adjusts to the audience
        - The examples become relevant to the specific context
        - The information focuses on different aspects based on the context
        - The organization and format changes to suit the purpose
        """)
    
    # Activity 2
    st.markdown("## Activity 2: Add Contextual Details")
    
    st.markdown("""
    Improve these basic prompts by adding contextual details.
    For each prompt, think about what additional information would help the AI generate a more useful response.
    """)
    
    # Prompt 1
    st.markdown("### Basic Prompt 1: 'Create a quiz about animals.'")
    
    context1 = st.text_area(
        "Add context:", 
        placeholder="Example: The quiz is for 3rd grade students learning about animal habitats. Include questions about forests, oceans, and deserts.",
        key="context1"
    )
    
    if context1:
        st.markdown("**Your improved prompt:**")
        st.code(f"Create a quiz about animals. {context1}")
    
    # Prompt 2
    st.markdown("### Basic Prompt 2: 'Write a lesson plan about renewable energy.'")
    
    context2 = st.text_area(
        "Add context:", 
        placeholder="Example: This is for a high school environmental science class that has already covered fossil fuels. The lesson should be 45 minutes long and include a hands-on activity.",
        key="context2"
    )
    
    if context2:
        st.markdown("**Your improved prompt:**")
        st.code(f"Write a lesson plan about renewable energy. {context2}")
    
    # Activity 3
    st.markdown("## Activity 3: Create a Context-Rich Educational Prompt")
    
    st.markdown("""
    Create a prompt for an educational task that includes rich contextual information.
    Choose one of the educational scenarios below:
    """)
    
    scenario = st.selectbox(
        "Select a scenario:",
        [
            "Creating a rubric for student presentations",
            "Developing a case study for a business class",
            "Designing a science experiment for remote learning",
            "Writing a creative writing prompt for an English class"
        ],
        key="context_scenario"
    )
    
    task = st.text_area("Basic task:", placeholder="What you want the AI to create", key="context_task")
    
    st.markdown("### Add Rich Context")
    st.markdown("Include information about:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        audience = st.text_area("Audience:", placeholder="Grade level, prior knowledge, etc.", key="context_audience")
        purpose = st.text_area("Purpose:", placeholder="Learning objectives, outcomes, etc.", key="context_purpose")
    
    with col2:
        constraints = st.text_area("Constraints:", placeholder="Time, resources, special needs, etc.", key="context_constraints")
        format_pref = st.text_area("Format preferences:", placeholder="Structure, length, style, etc.", key="context_format")
    
    # Show the complete prompt
    if task:
        st.markdown("### Your Complete Context-Rich Prompt:")
        
        complete_prompt = task
        
        additional_context = []
        if audience:
            additional_context.append(f"The audience is {audience}")
        if purpose:
            additional_context.append(f"The purpose is {purpose}")
        if constraints:
            additional_context.append(f"Working within these constraints: {constraints}")
        if format_pref:
            additional_context.append(f"The format should be {format_pref}")
        
        if additional_context:
            complete_prompt += " " + " ".join(additional_context)
        
        st.code(complete_prompt)
        
        st.markdown("""
        **Reflection Questions:**
        - How did adding context change your prompt?
        - Which contextual elements do you think will have the biggest impact on the AI's response?
        - How might your prompt help produce a more targeted and useful output for education?
        """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * For Activity 1, highlight how dramatically the content, examples, and language change based on audience context
    * For Activity 2, encourage participants to be specific about grade levels, prior knowledge, and learning objectives
    * For Activity 3, discuss how real-world educational tasks almost always require rich context
    
    **Discussion Prompts:**
    - "What contextual elements are most important when creating content for your specific subject area?"
    - "How does adding educational context mirror what you already do when differentiating instruction?"
    - "How might adding precise context save you time when using AI tools?"
    
    **Common Pitfalls:**
    - Too vague about audience (e.g., just saying "students" instead of specifics about age/grade/level)
    - Not mentioning prior knowledge or sequencing in the curriculum
    - Forgetting to specify format preferences or length constraints
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