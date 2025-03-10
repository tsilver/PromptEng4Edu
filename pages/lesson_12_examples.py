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
    page_title="Lesson 12: Examples",
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
    "title": "Role Prompting: Examples",
    "lesson": "12",
    "section": "examples",
    "order": 2
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_12_examples"
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
    "lesson_12_examples",
    "examples",
    "Role Prompting: Examples",
    """
    **This section provides practical examples of role prompting in education.**
    
    You'll see:
    - Examples of different educational personas and their effects
    - Comparisons between basic prompts and role-based prompts
    - Applications across various subject areas and grade levels
    
    These examples will help you understand how to craft effective role-based prompts
    for your specific teaching context.
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
    st.markdown("## Role Prompting Examples")
    
    st.markdown("""
    The following examples demonstrate how role prompting can enhance AI-generated content 
    for various educational purposes. Each example contrasts a basic prompt with a role-based 
    prompt to highlight the differences in the responses.
    """)
    
    # Example 1: Elementary Education
    st.markdown("### Example 1: Elementary Education")
    
    st.markdown("""
    **Basic Prompt:**
    ```
    Explain how plants grow to students.
    ```
    
    **Role-Based Prompt:**
    ```
    Act as a friendly gardener talking to a class of 1st-grade students. 
    Explain how plants grow using simple language, nature metaphors, 
    and an enthusiastic tone that will engage young learners. Include 
    a simple activity they could do to observe plant growth.
    ```
    
    **How the Role Improves the Response:**
    
    The gardener persona creates several advantages:
    
    1. **Authentic Voice:** The gardener speaks from practical experience, not just theory
    
    2. **Child-Friendly Language:** The persona naturally uses simpler explanations appropriate for 1st graders
    
    3. **Engaging Approach:** The enthusiasm and metaphors make the topic more relatable
    
    4. **Practical Connection:** Including an activity creates a hands-on learning opportunity
    
    **Sample Response Excerpt:**
    
    *"Hello little gardeners! I'm Farmer Jo, and I LOVE watching plants grow! Plants are like magic—they start as tiny seeds, smaller than your fingernail, but they can grow taller than your parents! Every plant needs four special things to grow: seeds, soil, water, and sunshine—just like you need food, water, and rest to grow big and strong!..."*
    
    *[Continues with simple explanation and suggests planting bean seeds in wet paper towels to observe growth]*
    """)
    
    # Example 2: Middle School Science
    st.markdown("### Example 2: Middle School Science")
    
    st.markdown("""
    **Basic Prompt:**
    ```
    Explain the concept of density.
    ```
    
    **Role-Based Prompt:**
    ```
    Act as a fun science lab instructor for 7th-grade students who loves 
    demonstrations and real-world examples. Explain the concept of density 
    by using everyday objects and phenomena that middle schoolers would 
    recognize. Include a "myth vs. fact" section to address common misconceptions.
    ```
    
    **How the Role Improves the Response:**
    
    The lab instructor persona creates several advantages:
    
    1. **Demonstration-Based Learning:** The role naturally incorporates examples and experiments
    
    2. **Age-Appropriate Examples:** Using objects familiar to middle schoolers increases relevance
    
    3. **Engaging Format:** The "fun" aspect encourages a tone that captures student interest
    
    4. **Misconception Targeting:** The myth vs. fact section addresses common confusion points
    
    **Sample Response Excerpt:**
    
    *"Welcome to the Density Lab, scientists! Today we're investigating why some things float and others sink. Density is like a material's 'crowdedness' - how much mass is packed into a certain space. Imagine a school hallway: when it's super crowded with students (high density), it's hard to move through; when it's nearly empty (low density), you can zoom right through!..."*
    
    *[Continues with everyday examples and a myth vs. fact section addressing misconceptions like "heavy things always sink"]*
    """)
    
    # Example 3: High School Literature
    st.markdown("### Example 3: High School Literature")
    
    st.markdown("""
    **Basic Prompt:**
    ```
    Analyze the themes in "To Kill a Mockingbird" by Harper Lee.
    ```
    
    **Role-Based Prompt:**
    ```
    Act as a thoughtful high school English teacher who specializes in 
    American literature and creates engaging discussions about complex 
    themes. Analyze three key themes in "To Kill a Mockingbird" by Harper Lee 
    in a way that would resonate with 10th-grade students. For each theme, 
    provide one discussion question that encourages critical thinking and 
    personal connection to the text.
    ```
    
    **How the Role Improves the Response:**
    
    The English teacher persona creates several advantages:
    
    1. **Structured Analysis:** The role naturally organizes content in a teaching-ready format
    
    2. **Engaging Discussion:** The focus on questions promotes active learning
    
    3. **Grade-Appropriate Analysis:** The content is pitched at the right level of complexity
    
    4. **Personal Connection:** The prompt encourages relating themes to student experiences
    
    **Sample Response Excerpt:**
    
    *"As we explore Harper Lee's powerful novel, let's look at how three key themes develop throughout the narrative and connect to our own experiences...*
    
    *Theme 1: Moral Education and Growth*
    *Scout and Jem's journey from innocence to awareness represents one of literature's most compelling coming-of-age narratives. Their moral education doesn't come from school lessons but from witnessing injustice firsthand..."*
    
    *Discussion Question: Consider a time when you learned an important moral lesson not from being told, but from experiencing or witnessing something yourself. How does this connect to Scout's development in the novel?*
    
    *[Continues with additional themes and discussion questions]*
    """)
    
    # Example 4: Historical Perspectives
    st.markdown("### Example 4: Historical Perspectives")
    
    st.markdown("""
    **Basic Prompt:**
    ```
    Describe the causes of World War I.
    ```
    
    **Role-Based Prompt:**
    ```
    Create three different perspectives on the causes of World War I by 
    adopting these three roles:
    
    1. A British historian writing in the 1920s
    2. A German historian writing in the 1950s
    3. A modern international relations professor
    
    For each perspective, write 1-2 paragraphs that reflect how their 
    historical context, nationality, and time period would influence 
    their analysis of the war's causes.
    ```
    
    **How the Role Improves the Response:**
    
    The multiple historical perspectives create several advantages:
    
    1. **Critical Thinking Development:** Students learn to evaluate source perspective
    
    2. **Historiography Lesson:** Shows how historical analysis changes over time
    
    3. **Multiple Viewpoints:** Encourages understanding complex events from various angles
    
    4. **Historical Context:** Demonstrates how time period affects interpretation
    
    **Sample Response Excerpt:**
    
    *"British Historian (1920s):*
    *The Great War was fundamentally a result of German militarism and imperial ambition. Kaiser Wilhelm II's desire to challenge British naval supremacy and establish a German colonial empire directly threatened the balance of power in Europe. While the assassination of Archduke Franz Ferdinand provided the spark, it was Germany's blank check to Austria-Hungary and subsequent invasion of neutral Belgium that transformed a regional dispute into a global catastrophe. The Treaty of Versailles rightfully acknowledges German war guilt...*
    
    *German Historian (1950s):*
    *The origins of the First World War cannot be attributed to any single nation. Rather, a complex web of alliances, colonial rivalries, and mutual fear created a powder keg that needed only a spark. All major powers share responsibility: Russia's early mobilization, France's desire for revenge over Alsace-Lorraine, Britain's determination to maintain naval supremacy, and yes, Germany's military planning. The Treaty of Versailles' war guilt clause served political purposes rather than historical truth...*
    
    *[Continues with modern perspective]*
    """)
    
    # Role Prompting Techniques Library
    st.markdown("## Role Prompting Techniques Library")
    
    st.markdown("""
    From these examples, we can identify several effective role prompting techniques for educators:
    
    ### 1. Age-Appropriate Personas
    Use roles that naturally communicate at the right level for your students' age group:
    - **Elementary:** Friendly storytellers, nature guides, superheroes
    - **Middle School:** Explorers, coaches, cool scientists
    - **High School:** Mentors, field experts, relatable peers
    - **College:** Professional colleagues, industry insiders, thought leaders
    
    ### 2. Subject-Specific Experts
    Match the persona to your subject area to bring authentic expertise:
    - **Science:** Lab instructors, researchers, naturalists
    - **Math:** Engineers, statisticians, problem-solving coaches
    - **Language Arts:** Writers, editors, literary critics
    - **History:** Time travelers, museum curators, era-specific journalists
    - **Arts:** Working artists, critics, art historians
    
    ### 3. Purpose-Driven Roles
    Select personas based on your instructional goals:
    - **For Introductions:** Enthusiastic guides, storytellers
    - **For Explanations:** Patient tutors, clear communicators
    - **For Application:** Coaches, mentors, practitioners
    - **For Analysis:** Critical thinkers, debate moderators
    - **For Evaluation:** Feedback providers, constructive critics
    
    ### 4. Multi-Perspective Approach
    Use contrasting personas to show different viewpoints:
    - Historical figures from different eras
    - Experts from different disciplines
    - Advocates for opposing positions
    - Representatives from different cultures
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Encourage educators to consider their students' interests when selecting personas - using roles students find interesting increases engagement
    * Remind participants that role prompting works best when the persona is clearly defined with specific characteristics, not just a generic label
    * Point out that role prompting can be particularly effective for difficult topics where the right voice or approach matters
    * Suggest combining role prompting with the chain-of-thought technique from the previous lesson
    
    **Discussion Questions:**
    
    * Which personas would be particularly effective for your specific student population?
    * How might different personas help address diversity and representation in your content?
    * What challenging concepts in your curriculum might benefit from explanation by a specific persona?
    * How could you use contrasting personas to help students understand multiple perspectives on controversial topics?
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