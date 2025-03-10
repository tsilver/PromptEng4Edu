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
    page_title="Lesson 15: Activities",
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
    "title": "Discussion Questions and Content Creation: Activities",
    "lesson": "15",
    "section": "activities",
    "order": 3
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_15_activities"
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
    "lesson_15_activities",
    "activities",
    "Discussion Questions and Content Creation: Activities",
    """
    **This section provides hands-on practice with creating prompts for discussion questions and instructional content.**
    
    You'll practice:
    - Crafting discussion questions for different cognitive levels
    - Creating prompts for various types of instructional content
    - Applying the PCTFR framework to your specific teaching context
    - Differentiating materials for diverse learners
    
    Complete these activities to strengthen your skills before moving to the reflection section.
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
    
    Complete the activities below to practice creating effective prompts for discussion questions and instructional content.
    After finishing these activities, proceed to the Reflection section to consolidate your learning 
    and unlock the next lesson.
    """)
    
    # Activity 1: Discussion Question Design
    st.markdown("## Activity 1: Discussion Question Design")
    
    st.markdown("""
    In this activity, you'll practice creating discussion questions at different cognitive levels 
    using Bloom's Taxonomy as a framework.
    """)
    
    # Topic selection
    st.markdown("### Select a topic from your teaching area:")
    
    topic = st.text_input(
        "Enter a specific topic you teach (e.g., 'Photosynthesis', 'American Revolution', 'To Kill a Mockingbird', etc.)",
        key="discussion_topic"
    )
    
    if topic:
        st.markdown(f"### Creating Questions for: {topic}")
        
        st.markdown("""
        For your selected topic, create one discussion question at each of the following cognitive levels.
        Remember that higher-level questions typically lead to deeper thinking and more engaging discussions.
        """)
        
        # Question development at different levels
        st.markdown("#### Remembering/Understanding Level (Factual/Basic Comprehension)")
        st.markdown("""
        These questions focus on recall of information or basic understanding of concepts.
        Example: "What are the three branches of government?"
        """)
        
        remember_question = st.text_area(
            "Your remembering/understanding level question:",
            height=80,
            key="remember_question"
        )
        
        st.markdown("#### Applying/Analyzing Level (Application/Analysis)")
        st.markdown("""
        These questions ask students to use information in new situations or examine relationships.
        Example: "How does the character's decision in chapter 3 influence the later events in chapter 7?"
        """)
        
        analyze_question = st.text_area(
            "Your applying/analyzing level question:",
            height=80,
            key="analyze_question"
        )
        
        st.markdown("#### Evaluating Level (Judgment/Assessment)")
        st.markdown("""
        These questions require students to make judgments based on criteria.
        Example: "Which solution to the problem is most effective and why?"
        """)
        
        evaluate_question = st.text_area(
            "Your evaluating level question:",
            height=80,
            key="evaluate_question"
        )
        
        st.markdown("#### Creating Level (Synthesis/Generation)")
        st.markdown("""
        These questions ask students to create something new or alternative.
        Example: "How might the story end differently if the main character had made a different choice?"
        """)
        
        create_question = st.text_area(
            "Your creating level question:",
            height=80,
            key="create_question"
        )
        
        # Question sequence planning
        if remember_question and analyze_question and evaluate_question and create_question:
            st.success("You've created questions at multiple cognitive levels! Now, consider how you would sequence these questions.")
            
            st.markdown("### Question Sequencing")
            
            st.markdown("""
            Effective discussions often follow a sequence that builds from lower to higher cognitive levels.
            Arrange your questions in the order you would use them in a discussion by numbering them 1-4.
            """)
            
            col1, col2 = st.columns(2)
            
            with col1:
                seq_remember = st.selectbox(
                    "Remembering/Understanding Question:",
                    ["Select position...", "1 (First)", "2 (Second)", "3 (Third)", "4 (Fourth)"],
                    key="seq_remember"
                )
                
                seq_analyze = st.selectbox(
                    "Applying/Analyzing Question:",
                    ["Select position...", "1 (First)", "2 (Second)", "3 (Third)", "4 (Fourth)"],
                    key="seq_analyze"
                )
                
            with col2:
                seq_evaluate = st.selectbox(
                    "Evaluating Question:",
                    ["Select position...", "1 (First)", "2 (Second)", "3 (Third)", "4 (Fourth)"],
                    key="seq_evaluate"
                )
                
                seq_create = st.selectbox(
                    "Creating Question:",
                    ["Select position...", "1 (First)", "2 (Second)", "3 (Third)", "4 (Fourth)"],
                    key="seq_create"
                )
            
            # Follow-up questions
            st.markdown("### Planning for Follow-up")
            
            st.markdown("""
            For one of your higher-level questions (analyzing, evaluating, or creating), 
            write a follow-up question you might ask if:
            """)
            
            followup_stuck = st.text_area(
                "Students seem stuck or confused by the question:",
                height=80,
                key="followup_stuck"
            )
            
            followup_surface = st.text_area(
                "Students are giving only surface-level responses:",
                height=80,
                key="followup_surface"
            )
            
            if followup_stuck and followup_surface:
                st.success("""
                Excellent work planning for differentiated questioning!
                
                Creating a sequence of questions that builds from lower to higher cognitive levels helps:
                - Establish a shared understanding of foundational concepts
                - Build confidence through early success with easier questions
                - Scaffold students toward more complex thinking
                - Create a natural flow that deepens discussion over time
                
                Having follow-up questions prepared helps you maintain momentum and deeper thinking, even when 
                students struggle or give limited responses.
                """)
    
    # Activity 2: PCTFR Framework for Discussion Questions
    st.markdown("## Activity 2: PCTFR Framework for Discussion Questions")
    
    st.markdown("""
    In this activity, you'll practice using the PCTFR framework to create a comprehensive prompt for 
    generating discussion questions on a topic of your choice.
    """)
    
    # PCTFR components for discussion questions
    st.markdown("### Complete each component of the PCTFR framework:")
    
    persona_disc = st.text_area(
        "**Persona:** What type of teacher or educational specialist should the AI model embody?",
        height=80,
        placeholder="Example: Act as an experienced English teacher who specializes in literature circles and student-led discussions...",
        key="persona_disc"
    )
    
    context_disc = st.text_area(
        "**Context:** What's the specific teaching situation, student background, and topic?",
        height=100,
        placeholder="Example: I'm teaching Romeo and Juliet to 9th graders who have completed reading through Act 3. Many students find Shakespeare's language challenging...",
        key="context_disc"
    )
    
    task_disc = st.text_area(
        "**Task:** What specific type of discussion questions do you need?",
        height=80,
        placeholder="Example: Create a set of discussion questions for a 30-minute small group activity that will help students analyze character motivations and conflicts...",
        key="task_disc"
    )
    
    format_disc = st.text_area(
        "**Format:** How should the questions be structured and organized?",
        height=100,
        placeholder="Example: Provide 8-10 questions organized into categories: Opening Questions, Character Analysis Questions, Theme Questions, and Modern Connection Questions...",
        key="format_disc"
    )
    
    reference_disc = st.text_area(
        "**Reference Materials:** What specific content, standards, or materials should inform the questions?",
        height=120,
        placeholder="Example: Key scenes include the balcony scene, the fight between Mercutio and Tybalt, and Romeo's banishment. Themes include love vs. hate, fate vs. free will...",
        key="reference_disc"
    )
    
    # Assembling the complete prompt
    if persona_disc and context_disc and task_disc and format_disc and reference_disc:
        st.success("You've created all components for a comprehensive PCTFR prompt. Here's your complete prompt:")
        
        st.markdown("### Your Complete PCTFR Prompt for Discussion Questions:")
        
        st.code(f"""
{persona_disc}

{context_disc}

{task_disc}

{format_disc}

{reference_disc}
        """)
        
        st.markdown("""
        #### Analyzing Your Prompt's Effectiveness
        
        Review your prompt and check if it includes these characteristics of effective discussion question prompts:
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.checkbox("Specifies the educational approach or philosophy", key="check_approach")
            st.checkbox("Identifies student background knowledge", key="check_background")
            st.checkbox("Notes specific topic or content focus", key="check_topic")
            st.checkbox("Indicates purpose of the discussion", key="check_purpose")
        
        with col2:
            st.checkbox("Requests questions at multiple cognitive levels", key="check_cognitive")
            st.checkbox("Includes organization or sequencing guidelines", key="check_sequence")
            st.checkbox("References specific content details", key="check_content")
            st.checkbox("Mentions learning standards or objectives", key="check_standards")
    
    # Activity 3: Instructional Content Design
    st.markdown("## Activity 3: Instructional Content Design")
    
    st.markdown("""
    In this activity, you'll practice creating a prompt for a specific type of instructional content
    relevant to your teaching context.
    """)
    
    # Content type selection
    content_type = st.selectbox(
        "Select the type of instructional content you want to create:",
        [
            "Select a content type...",
            "Guided Notes",
            "Graphic Organizer",
            "Case Study or Scenario",
            "Lab or Investigation Procedure",
            "Visual Aid or Infographic",
            "Differentiated Learning Station",
            "Formative Assessment",
            "Interactive Digital Activity"
        ],
        key="content_type"
    )
    
    if content_type and content_type != "Select a content type...":
        st.markdown(f"### Creating a Prompt for: {content_type}")
        
        # Target info
        grade_level = st.text_input("Target grade level or course:", key="grade_level")
        subject_area = st.text_input("Subject area:", key="subject_area")
        topic_content = st.text_input("Specific topic:", key="topic_content")
        
        if grade_level and subject_area and topic_content:
            st.markdown("### Define your content requirements:")
            
            # Content requirements
            learning_obj = st.text_area(
                "Learning objectives this content will address:",
                height=80,
                key="learning_obj"
            )
            
            special_needs = st.text_area(
                "Any specific student needs or differentiation requirements:",
                height=80,
                key="special_needs"
            )
            
            content_components = st.text_area(
                "Key components or sections you want included:",
                height=100,
                placeholder="Example: For Guided Notes - vocabulary section, main concept explanations, example problems, practice section...",
                key="content_components"
            )
            
            content_features = st.text_area(
                "Special features or formatting requirements:",
                height=80,
                placeholder="Example: Visual supports, scaffolded prompts, extension activities...",
                key="content_features"
            )
            
            # Creating the content prompt
            if learning_obj and content_components:
                st.success("Based on your inputs, here's a structured prompt for creating your instructional content:")
                
                st.markdown("### Your Instructional Content Prompt:")
                
                # Construct persona based on content type
                persona_mapping = {
                    "Guided Notes": f"Act as an experienced {subject_area} educator who specializes in creating structured yet engaging guided notes that support student learning through active note-taking",
                    "Graphic Organizer": f"Act as an {subject_area} curriculum designer who creates visual learning tools that help students organize information and see connections between concepts",
                    "Case Study or Scenario": f"Act as a {subject_area} specialist who develops authentic, engaging case studies that connect academic content to real-world applications",
                    "Lab or Investigation Procedure": f"Act as a {subject_area} teacher with expertise in designing inquiry-based investigations that develop scientific practices and critical thinking",
                    "Visual Aid or Infographic": f"Act as an instructional designer specialized in creating visual learning tools that communicate complex {subject_area} concepts clearly and engagingly",
                    "Differentiated Learning Station": f"Act as an inclusive education specialist who creates multi-level learning experiences that address diverse student needs while focusing on common learning goals",
                    "Formative Assessment": f"Act as an assessment expert who designs meaningful, low-stakes assessments that provide insight into student understanding and inform instruction",
                    "Interactive Digital Activity": f"Act as an educational technology specialist who creates engaging digital learning experiences that promote active learning in {subject_area}"
                }
                
                persona_content = persona_mapping.get(content_type, f"Act as an experienced {subject_area} educator")
                
                # Construct context
                context_content = f"I teach {subject_area} to {grade_level} students, and we're studying {topic_content}. "
                if special_needs:
                    context_content += f"My students have the following needs or characteristics: {special_needs}. "
                
                # Construct task
                task_content = f"Create a {content_type} that will help students master the following learning objectives: {learning_obj}."
                
                # Construct format
                format_content = f"The {content_type} should include the following components: {content_components}. "
                if content_features:
                    format_content += f"It should also feature: {content_features}."
                
                # Reference materials would be added by the user in real practice
                reference_content = "The content should align with grade-level standards and accurately represent the subject matter. [Note: In an actual prompt, you would add specific standards, key vocabulary, or content details here.]"
                
                # Display the complete prompt
                st.code(f"""
{persona_content}

{context_content}

{task_content}

{format_content}

{reference_content}
                """)
                
                st.markdown("""
                #### Next Steps
                
                This prompt template provides a strong starting point for generating instructional content. 
                To make it even more effective:
                
                1. **Add specific reference materials** like standards, key vocabulary, or content details
                2. **Include examples** of similar content you've used successfully
                3. **Specify any school or district requirements** that should be reflected
                4. **Note any particular teaching approaches** you prefer (inquiry-based, direct instruction, etc.)
                
                Remember that the generated content will be a starting point - you'll want to review and refine 
                it to perfectly match your teaching context and students' needs.
                """)
    
    # Activity 4: Content Differentiation Strategies
    st.markdown("## Activity 4: Content Differentiation Strategies")
    
    st.markdown("""
    In this activity, you'll explore strategies for requesting differentiated content that meets diverse student needs.
    """)
    
    differentiation_focus = st.selectbox(
        "Select a differentiation focus area:",
        [
            "Select a focus area...",
            "Readiness levels (different performance levels)",
            "Learning preferences (visual, auditory, kinesthetic)",
            "English language learners",
            "Students with learning disabilities",
            "Gifted and advanced learners"
        ],
        key="diff_focus"
    )
    
    if differentiation_focus and differentiation_focus != "Select a focus area...":
        st.markdown(f"### Differentiation Strategies for: {differentiation_focus}")
        
        st.markdown("""
        For your selected differentiation focus, identify 3-4 specific strategies you could request in a prompt
        to ensure content is appropriately differentiated.
        """)
        
        diff_strategy1 = st.text_area(
            "Strategy 1:",
            height=80,
            key="diff_strategy1"
        )
        
        diff_strategy2 = st.text_area(
            "Strategy 2:",
            height=80,
            key="diff_strategy2"
        )
        
        diff_strategy3 = st.text_area(
            "Strategy 3:",
            height=80,
            key="diff_strategy3"
        )
        
        diff_strategy4 = st.text_area(
            "Strategy 4 (optional):",
            height=80,
            key="diff_strategy4"
        )
        
        if diff_strategy1 and diff_strategy2 and diff_strategy3:
            st.success("You've identified multiple differentiation strategies! Now, create a prompt section that integrates these approaches.")
            
            st.markdown("### Create a differentiation-focused prompt section:")
            
            st.markdown("""
            Write a paragraph that could be added to a prompt to request the differentiation strategies you've identified.
            This should clearly explain how you want the content differentiated for your target group.
            """)
            
            diff_prompt = st.text_area(
                "Your differentiation prompt section:",
                height=150,
                key="diff_prompt"
            )
            
            if diff_prompt:
                st.success("""
                Excellent work! Explicit differentiation requests are crucial for creating truly inclusive content.
                
                When requesting differentiated content, remember to:
                - Be specific about the needs of your learners
                - Request concrete strategies rather than general "differentiation"
                - Consider multiple access points to the same content
                - Maintain high expectations while providing appropriate support
                - Request options that you can select from based on individual student needs
                
                These approaches ensure that all students can engage with rigorous content in ways that 
                support their learning needs.
                """)
    
    # Reflection and key takeaways
    st.markdown("## Activity Reflection")
    
    st.markdown("""
    Take a moment to reflect on what you've learned from these activities:
    
    1. **Effective discussion questions** span multiple cognitive levels, follow a logical sequence,
       and include prepared follow-up strategies to deepen thinking.
    
    2. **The PCTFR framework** provides a comprehensive structure for requesting discussion questions
       that are aligned with your specific teaching context and student needs.
    
    3. **Instructional content prompts** should clearly specify the type of content, learning objectives,
       components, and special features needed for your classroom.
    
    4. **Differentiation strategies** can and should be explicitly requested in prompts to ensure
       the generated content meets the needs of all learners.
    
    As you incorporate these prompt engineering techniques into your planning process, you'll be able
    to create more engaging, effective learning experiences while saving valuable preparation time.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Encourage participants to save their work from these activities as templates they can adapt for future use
    * Remind participants that the PCTFR framework is flexible and can be adapted to meet their specific needs
    * Suggest participants share their prompts with colleagues to get feedback and additional ideas
    * Emphasize that prompt engineering is an iterative process - prompts often improve with refinement
    
    **Common Challenges:**
    
    * Creating questions that truly target higher cognitive levels (versus knowledge questions in disguise)
    * Specifying differentiation approaches concretely rather than generally
    * Including enough detail in prompts without making them excessively long
    * Finding the right balance between structure and flexibility in instructional content
    
    **Extension Ideas:**
    
    * Have participants exchange prompts and evaluate each other's effectiveness using the provided criteria
    * Encourage creation of a prompt library organized by content type and educational purpose
    * Suggest testing prompts with AI tools and refining based on the results
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