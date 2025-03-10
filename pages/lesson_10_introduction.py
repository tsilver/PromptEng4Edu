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
    page_title="Lesson 10: Few-Shot Prompting",
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
    "title": "Few-Shot Prompting",
    "lesson": "10",
    "section": "introduction",
    "order": 1
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_10_introduction"
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
    "lesson_10_introduction",
    "introduction",
    "Lesson 10: Few-Shot Prompting",
    """
    **Welcome to Lesson 10 on Few-Shot Prompting.**
    
    In this lesson, you'll learn:
    - What few-shot prompting is and how it differs from zero-shot
    - How to use examples to guide AI responses
    - When to use few-shot versus zero-shot approaches
    - Techniques for creating effective example sets
    
    Navigate through the sections using the tabs at the top.
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
    st.markdown(f"# Lesson 10: {PAGE_INFO['title']}")
    
    # Objective
    st.markdown("## Objective")
    st.markdown("""
    To understand few-shot prompting and learn how to use examples to guide AI responses for 
    more precise and consistent results.
    """)
    
    # Real-world hook
    st.info("""
    ### Real-World Hook
    
    Think about how you might teach a new teaching assistant to provide feedback on student essays. Instead of just saying "give constructive feedback," you'd likely show them a few examples of what good feedback looks like. This simple but powerful technique—showing examples of what you want—is the essence of few-shot prompting, and it can dramatically improve the consistency and quality of AI-generated content for your educational needs.
    """)
    
    # Jargon-Free Explanation
    st.markdown("## Understanding Few-Shot Prompting")
    
    st.markdown("""
    **Few-shot prompting** means providing the AI with a small number of examples of the task you want it to perform, followed by a new instance for it to complete in the same pattern.
    
    Think of it like this: You're showing the AI "Here are a few examples of how I want you to approach this task" before asking it to do something similar.
    
    For instance, if you want the AI to create question-answer pairs about a reading passage, you might show it 2-3 examples of good question-answer pairs before asking it to generate more of the same.
    
    Few-shot prompting leverages the AI's ability to recognize patterns and adapt its response style to match your examples.
    """)
    
    # Zero-Shot vs. Few-Shot
    st.markdown("## Zero-Shot vs. Few-Shot: A Comparison")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Zero-Shot Approach
        
        ```
        Create 5 discussion questions for a 7th-grade 
        class studying ancient Egypt.
        ```
        
        **When to Use Zero-Shot:**
        - When you need something quickly
        - For standard educational formats
        - When specific style isn't critical
        - When you trust the AI's default approach
        - For general content generation
        """)
        
    with col2:
        st.markdown("""
        ### Few-Shot Approach
        
        ```
        Here are examples of the kind of discussion 
        questions I want for a 7th-grade class studying 
        ancient Egypt:
        
        Example 1: How did the Nile River shape Egyptian 
        civilization? Consider agriculture, transportation, 
        and religious beliefs in your answer.
        
        Example 2: What evidence suggests that ancient 
        Egyptians had advanced knowledge of mathematics 
        and engineering? Cite specific monuments or practices.
        
        Please create 5 more discussion questions in this style.
        ```
        
        **When to Use Few-Shot:**
        - When format consistency is important
        - For specialized question types
        - When you have a specific style in mind
        - To match your teaching approach
        - For more complex or nuanced content
        """)
    
    # Key Concepts
    st.markdown("## Key Concepts in Few-Shot Prompting")
    
    st.markdown("""
    ### 1. Example Selection
    
    The examples you provide guide the AI's understanding of:
    - **Content Focus**: What topics or concepts to emphasize
    - **Complexity Level**: How sophisticated the response should be
    - **Question/Task Type**: What form the output should take (e.g., analytical questions vs. factual recall)
    - **Style and Tone**: The linguistic approach and voice to use
    
    ### 2. Pattern Recognition
    
    The AI analyzes your examples to identify patterns in:
    - Structure (how information is organized)
    - Format (how content is presented)
    - Language features (vocabulary, sentence structure)
    - Content elements (what components to include)
    
    ### 3. Example Quantity
    
    - **One Example**: Provides basic guidance on format and approach
    - **Two to Three Examples**: Helps establish a clear pattern
    - **Four or More Examples**: Usually unnecessary for most educational tasks
    
    ### 4. Example Diversity
    
    Varies based on your goal:
    - **Similar Examples**: For consistent, predictable outputs
    - **Diverse Examples**: To demonstrate range and flexibility
    - **Progressive Examples**: To show sequence or increasing complexity
    """)
    
    # Few-Shot Patterns
    st.markdown("## Common Few-Shot Patterns")
    
    st.markdown("""
    ### Pattern 1: Input-Output Pairs
    ```
    Input: [question/prompt]
    Output: [answer/response]
    
    Input: [new question/prompt]
    Output: [AI completes this]
    ```
    
    ### Pattern 2: Format Demonstration
    ```
    Example 1:
    [shows complete example with desired format]
    
    Example 2:
    [shows another complete example with the same format]
    
    Now create another example following the same format.
    ```
    
    ### Pattern 3: Content Transform
    ```
    Original: [source content]
    Simplified version: [simplified version]
    
    Original: [new source content]
    Simplified version: [AI completes this]
    ```
    
    ### Pattern 4: Quality Spectrum
    ```
    Weak example: [shows lower quality response]
    Strong example: [shows higher quality response]
    
    Create a strong response for: [new prompt]
    ```
    """)
    
    # Tips for Creating Effective Examples
    st.markdown("## Tips for Creating Effective Examples")
    
    st.markdown("""
    ### Clarity and Consistency
    
    - Make your examples clear and consistent in structure
    - Ensure examples genuinely represent what you want
    - Use the same format across all examples
    
    ### Explicit Formatting
    
    - Include all formatting elements you want replicated
    - Show exactly how you want content organized
    - Demonstrate desired headers, bullet points, etc.
    
    ### Progressive Complexity
    
    - Order examples from simple to complex if appropriate
    - Show range (e.g., different question types or approaches)
    - Demonstrate variations you want the AI to incorporate
    
    ### Education-Specific Considerations
    
    - Include grade-appropriate language in your examples
    - Demonstrate proper pedagogical techniques
    - Show appropriate scaffolding or differentiation
    """)
    
    # Few-Shot vs. PTC-FREI Framework
    st.markdown("## Few-Shot and the PTC-FREI Framework")
    
    st.markdown("""
    Few-shot prompting works well with the PTC-FREI framework:
    
    1. **Persona**: Can be established in your examples (e.g., examples written in teacher voice)
    
    2. **Task**: Still clearly define what you want, but examples demonstrate the approach
    
    3. **Context**: Provide before your examples, as it frames the whole interaction
    
    4. **Format**: Demonstrated concretely through examples rather than just described
    
    5. **Reference**: Can be incorporated into your examples to show proper integration
    
    6. **Evaluation and Iteration**: Still essential for refining both your prompt and examples
    
    The key difference is that with few-shot, you're providing concrete demonstrations of what you want rather than relying solely on descriptions.
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific notes
    render_teacher_notes("""
    **Teaching Tips:**
    
    * Help participants see few-shot prompting as an extension of their existing teaching strategies (modeling desired outcomes)
    * Emphasize that the time investment in creating good examples often pays off in higher quality, more consistent results
    * Encourage thinking about collecting a "library" of examples for frequently used educational content types
    * Point out that once created, few-shot examples can be reused and refined over time
    
    **Common Challenges:**
    
    * Some participants may be unsure about how many examples are needed - remind them that 2-3 is usually sufficient
    * Others may struggle with selecting appropriate examples - suggest focusing on exemplars that clearly show the desired qualities
    * Participants might miss that examples need to be consistent in format - emphasize pattern recognition
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