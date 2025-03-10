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
    page_title="Lesson 7: Activities",
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
    "title": "Evaluation: Activities",
    "lesson": "7",
    "section": "activities",
    "order": 3
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_7_activities"
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
    "lesson_7_activities",
    "activities",
    "Lesson 7 Activities",
    """
    **This section provides hands-on practice with evaluation techniques.**
    
    You'll:
    - Apply different evaluation approaches to AI-generated content
    - Create custom rubrics for your educational context
    - Learn to translate evaluations into prompt improvements
    
    Complete these activities to strengthen your evaluation skills before
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
    
    Complete the activities below to practice evaluating AI outputs and creating effective evaluation criteria.
    After finishing these activities, proceed to the Reflection section to solidify your learning 
    and unlock the next lesson.
    """)
    
    # Activity 1
    st.markdown("## Activity 1: Apply the ACRE Framework")
    
    st.markdown("""
    In this activity, you'll apply the ACRE framework (Accuracy, Curriculum Alignment, Readability, Engagement)
    to evaluate an AI-generated response.
    """)
    
    # Sample AI response to evaluate
    st.markdown("""
    ### AI-Generated Response to Evaluate
    
    **Original Prompt:** *Create an explanation of the water cycle for 3rd-grade students.*
    
    **AI Response:**
    
    # The Water Cycle
    
    The water cycle is the continuous movement of water on, above, and below Earth's surface. It's like a big recycling system for water!
    
    Here's how it works:
    
    1. **Evaporation:** The sun heats up water in oceans, lakes, and rivers, turning it into water vapor that rises into the air. Plants also release water vapor through a process called transpiration.
    
    2. **Condensation:** As the water vapor rises, it cools and forms clouds.
    
    3. **Precipitation:** When the clouds get heavy with water droplets, the water falls back to Earth as rain, snow, sleet, or hail.
    
    4. **Collection:** The water that falls collects in oceans, lakes, and rivers, or soaks into the ground to become groundwater.
    
    And then the cycle begins again! The water we use today has been cycling around our planet for millions of years.
    
    **Fun Fact:** The water you drink might have once been drunk by a dinosaur!
    """)
    
    # ACRE evaluation form
    st.markdown("### Your ACRE Evaluation")
    
    accuracy = st.slider("Accuracy (1-5):", 1, 5, 3, help="How factually correct and comprehensive is the content?")
    
    curriculum_alignment = st.slider("Curriculum Alignment (1-5):", 1, 5, 3, help="How well does it align with typical 3rd-grade science standards?")
    
    readability = st.slider("Readability (1-5):", 1, 5, 3, help="How appropriate is the language and complexity for 3rd-grade students?")
    
    engagement = st.slider("Engagement (1-5):", 1, 5, 3, help="How likely is this content to capture and maintain student interest?")
    
    evaluation_notes = st.text_area(
        "Evaluation Notes:",
        height=150,
        placeholder="Provide specific feedback on each dimension of the ACRE framework. What are the strengths and weaknesses? What would you suggest to improve this response?",
        key="acre_notes"
    )
    
    # Calculate overall score
    if st.button("Calculate Overall Score", key="calculate_score"):
        total_score = accuracy + curriculum_alignment + readability + engagement
        percentage = (total_score / 20) * 100
        st.success(f"Overall ACRE Score: {total_score}/20 ({percentage:.1f}%)")
        
        # Provide automated feedback based on scores
        feedback = []
        
        if accuracy < 3:
            feedback.append("⚠️ **Accuracy needs improvement**: Consider checking for factual errors or missing key concepts.")
        elif accuracy >= 4:
            feedback.append("✅ **Strong accuracy**: The content contains correct scientific information.")
            
        if curriculum_alignment < 3:
            feedback.append("⚠️ **Better curriculum alignment needed**: The content may not fully align with grade-level standards.")
        elif curriculum_alignment >= 4:
            feedback.append("✅ **Well-aligned with curriculum**: The content appropriately addresses grade-level expectations.")
            
        if readability < 3:
            feedback.append("⚠️ **Readability could be improved**: The language may be too complex or simple for the target grade level.")
        elif readability >= 4:
            feedback.append("✅ **Appropriate readability**: The language and complexity level are well-suited for 3rd-grade students.")
            
        if engagement < 3:
            feedback.append("⚠️ **More engaging elements needed**: Consider adding interactive elements, questions, or interesting facts.")
        elif engagement >= 4:
            feedback.append("✅ **Engaging content**: The content includes elements that would likely capture student interest.")
        
        st.write("### Automated Feedback Summary")
        for item in feedback:
            st.markdown(item)
            
        st.markdown("### Suggested Prompt Revision")
        st.markdown("""
        Based on typical evaluation results, here's how you might revise the original prompt to improve the response:
        
        ```
        Create an explanation of the water cycle for 3rd-grade students that:
        1. Includes all key stages (evaporation, condensation, precipitation, collection)
        2. Uses simple, age-appropriate language
        3. Includes a visual description that could be drawn
        4. Connects to students' everyday experiences with water
        5. Incorporates 2-3 interactive questions to check understanding
        ```
        
        This revised prompt addresses specific evaluation criteria from the ACRE framework.
        """)
    
    # Activity 2
    st.markdown("## Activity 2: Create a Custom Evaluation Rubric")
    
    st.markdown("""
    In this activity, you'll create a custom evaluation rubric for a specific type of educational content
    you commonly use or create. This will help you systematically assess AI-generated content for your
    particular teaching needs.
    """)
    
    # Content type selection
    content_type = st.selectbox(
        "Select a content type to create a rubric for:",
        [
            "Lesson Plan",
            "Student Assignment",
            "Assessment/Quiz",
            "Reading/Discussion Questions",
            "Lab Activity",
            "Presentation Materials",
            "Student Feedback",
            "Other (specify in notes)"
        ],
        key="content_type"
    )
    
    st.markdown(f"### Custom Rubric for: {content_type}")
    
    # Template for adding criteria
    st.markdown("""
    Add 3-5 evaluation criteria that are most important for this type of content in your teaching context.
    For each criterion, provide:
    - A clear name
    - A description of what you're evaluating
    - How you would rate it (scale, yes/no, etc.)
    """)
    
    # First criterion
    criterion1_name = st.text_input("Criterion 1 Name:", placeholder="e.g., Content Accuracy", key="crit1_name")
    criterion1_desc = st.text_area("Description:", placeholder="What specifically are you looking for? What makes this criterion important?", height=80, key="crit1_desc")
    criterion1_scale = st.text_input("Rating Scale:", placeholder="e.g., 1-5 where 1=Poor and 5=Excellent", key="crit1_scale")
    
    # Second criterion
    criterion2_name = st.text_input("Criterion 2 Name:", placeholder="e.g., Instructional Clarity", key="crit2_name")
    criterion2_desc = st.text_area("Description:", placeholder="What specifically are you looking for? What makes this criterion important?", height=80, key="crit2_desc")
    criterion2_scale = st.text_input("Rating Scale:", placeholder="e.g., 1-5 where 1=Poor and 5=Excellent", key="crit2_scale")
    
    # Third criterion
    criterion3_name = st.text_input("Criterion 3 Name:", placeholder="e.g., Student Engagement", key="crit3_name")
    criterion3_desc = st.text_area("Description:", placeholder="What specifically are you looking for? What makes this criterion important?", height=80, key="crit3_desc")
    criterion3_scale = st.text_input("Rating Scale:", placeholder="e.g., 1-5 where 1=Poor and 5=Excellent", key="crit3_scale")
    
    # Optional additional criteria
    if st.checkbox("Add more criteria"):
        # Fourth criterion
        criterion4_name = st.text_input("Criterion 4 Name:", placeholder="e.g., Differentiation", key="crit4_name")
        criterion4_desc = st.text_area("Description:", placeholder="What specifically are you looking for? What makes this criterion important?", height=80, key="crit4_desc")
        criterion4_scale = st.text_input("Rating Scale:", placeholder="e.g., 1-5 where 1=Poor and 5=Excellent", key="crit4_scale")
        
        # Fifth criterion
        criterion5_name = st.text_input("Criterion 5 Name:", placeholder="e.g., Assessment Alignment", key="crit5_name")
        criterion5_desc = st.text_area("Description:", placeholder="What specifically are you looking for? What makes this criterion important?", height=80, key="crit5_desc")
        criterion5_scale = st.text_input("Rating Scale:", placeholder="e.g., 1-5 where 1=Poor and 5=Excellent", key="crit5_scale")
    
    # Notes on using the rubric
    rubric_notes = st.text_area(
        "Notes on Using This Rubric:",
        height=100,
        placeholder="Add any additional information about how to use this rubric effectively, or specific considerations for your teaching context.",
        key="rubric_notes"
    )
    
    # Generate the rubric
    if st.button("Generate My Rubric", key="generate_rubric"):
        st.success("Your custom evaluation rubric has been created!")
        
        st.markdown(f"## Evaluation Rubric for {content_type}")
        
        # Create the rubric table
        rubric_data = []
        
        if criterion1_name and criterion1_desc:
            rubric_data.append([criterion1_name, criterion1_desc, criterion1_scale])
        
        if criterion2_name and criterion2_desc:
            rubric_data.append([criterion2_name, criterion2_desc, criterion2_scale])
            
        if criterion3_name and criterion3_desc:
            rubric_data.append([criterion3_name, criterion3_desc, criterion3_scale])
            
        if st.session_state.get("crit4_name") and st.session_state.get("crit4_desc"):
            rubric_data.append([st.session_state.crit4_name, st.session_state.crit4_desc, st.session_state.get("crit4_scale", "")])
            
        if st.session_state.get("crit5_name") and st.session_state.get("crit5_desc"):
            rubric_data.append([st.session_state.crit5_name, st.session_state.crit5_desc, st.session_state.get("crit5_scale", "")])
        
        # Display the rubric as a table
        if rubric_data:
            table_html = "<table style='width:100%; border-collapse: collapse;'>"
            table_html += "<tr style='background-color:#f2f2f2'><th style='padding:10px; border:1px solid #ddd;'>Criterion</th><th style='padding:10px; border:1px solid #ddd;'>Description</th><th style='padding:10px; border:1px solid #ddd;'>Rating Scale</th></tr>"
            
            for i, row in enumerate(rubric_data):
                bg_color = "#f9f9f9" if i % 2 == 0 else "white"
                table_html += f"<tr style='background-color:{bg_color}'>"
                for cell in row:
                    table_html += f"<td style='padding:10px; border:1px solid #ddd;'>{cell}</td>"
                table_html += "</tr>"
            
            table_html += "</table>"
            st.markdown(table_html, unsafe_allow_html=True)
            
            if rubric_notes:
                st.markdown("### Usage Notes")
                st.markdown(rubric_notes)
                
            st.markdown("""
            **Next Steps:**
            1. Use this rubric to evaluate AI-generated content in your teaching practice
            2. Refine the criteria based on what you learn from using it
            3. Share the rubric with colleagues to establish consistent evaluation standards
            """)
        else:
            st.warning("Please fill in at least one criterion to generate a rubric.")
    
    # Activity 3
    st.markdown("## Activity 3: From Evaluation to Prompt Improvement")
    
    st.markdown("""
    This activity focuses on using evaluation results to improve prompts. You'll analyze an evaluated
    AI response and develop a better prompt based on the feedback.
    """)
    
    st.markdown("""
    ### Sample Evaluation Results
    
    **Original Prompt:**
    ```
    Create a middle school science lab on density.
    ```
    
    **AI Response:** *(summarized)*
    A basic lab activity where students measure the mass and volume of different objects and calculate density.
    
    **Evaluation Results:**
    
    | Criterion | Score | Feedback |
    |---|---|---|
    | Scientific Accuracy | 4/5 | Correctly presents density formula and measurement methods |
    | Safety Considerations | 2/5 | Missing important safety guidelines for handling materials |
    | Inquiry-Based Approach | 1/5 | Lacks questions that promote scientific inquiry; too procedural |
    | Student Engagement | 2/5 | Basic procedure without real-world connections or interesting context |
    | Differentiation | 1/5 | No adaptations for different learning needs or extension activities |
    
    **Overall Assessment:**
    The lab is scientifically accurate but lacks inquiry elements, safety guidelines, engagement factors, and differentiation options.
    """)
    
    # Prompt improvement task
    st.markdown("### Your Task: Revise the Prompt")
    
    revised_prompt = st.text_area(
        "Write an improved prompt that addresses the evaluation feedback:",
        height=200,
        placeholder="Example: Create a middle school science lab on density that includes: 1) Clear safety guidelines for all materials and procedures, 2) An inquiry-based approach with testable questions, 3) Real-world applications that engage students, 4) Differentiation options for various learning needs, 5) Extensions for advanced students...",
        key="revised_prompt"
    )
    
    prompt_explanation = st.text_area(
        "Explain how your revised prompt addresses each evaluation criterion:",
        height=150,
        placeholder="Explain how each change in your prompt addresses specific issues identified in the evaluation. For example: 'I added safety requirements to address the low score on Safety Considerations...'",
        key="prompt_explanation"
    )
    
    if revised_prompt and prompt_explanation:
        st.success("You've completed the prompt improvement task!")
        
        st.markdown("""
        ### From Evaluation to Improvement: Key Principles
        
        Based on this activity, remember these key principles:
        
        1. **Be specific about deficiencies** - Clearly identify what's missing or inadequate
        
        2. **Add explicit requirements** - Don't hint at what you want; state it directly
        
        3. **Address all dimensions** - Ensure your prompt covers all important evaluation criteria
        
        4. **Provide examples when needed** - If a concept like "inquiry-based" might be ambiguous, provide an example
        
        5. **Test and iterate** - The evaluation-improvement cycle is ongoing
        """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * For Activity 1, encourage participants to be specific in their evaluation notes with concrete examples
    * For Activity 2, suggest that participants save their custom rubrics for future use in their teaching
    * For Activity 3, emphasize that prompt improvement based on evaluation is an iterative process
    
    **Common Challenges:**
    
    * Participants may find it difficult to balance detailed evaluation criteria with practical usability
    * Some may struggle to convert evaluation feedback into specific prompt improvements
    * The subjective nature of some criteria (like engagement) can make consistent evaluation difficult
    
    **Extension Ideas:**
    
    * Have participants exchange custom rubrics and use them to evaluate the same AI output to see how different criteria affect assessment
    * Create a shared repository of evaluation rubrics for different content types and grade levels
    * Apply evaluation techniques to actual AI-generated content used in classrooms, identifying specific improvements
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