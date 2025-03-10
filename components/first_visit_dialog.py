import streamlit as st
import time

def show_first_visit_dialog(page_id, section, title, message):
    """
    Shows an informational popover the first time a user visits a page.
    Uses a simplified approach that works reliably after the page loads.
    
    Parameters:
    - page_id: Unique identifier for the page
    - section: The current section (introduction, examples, etc.)
    - title: Title of the dialog
    - message: Message to display in the dialog
    
    Returns:
    - True if dialog was shown, False if it was previously shown
    """
    # Create session state keys for this specific page
    dialog_key = f"first_visit_{page_id}"
    delay_key = f"delay_complete_{page_id}"
    
    # Initialize keys if needed
    if dialog_key not in st.session_state:
        st.session_state[dialog_key] = True
    
    if delay_key not in st.session_state:
        st.session_state[delay_key] = False
        st.session_state[f"{delay_key}_time"] = time.time()
    
    # Check if enough time has passed (2 seconds)
    if not st.session_state[delay_key] and time.time() - st.session_state.get(f"{delay_key}_time", 0) > 2:
        st.session_state[delay_key] = True
    
    # Create a container for the popover that only shows after delay
    popover_container = st.empty()
    
    # Check if we should show the popover
    if st.session_state[dialog_key] and st.session_state[delay_key]:
        with popover_container:
            # Use standard parameters only
            with st.popover(f"📣 {title}"):
                st.markdown(message)
                
                # Add a button to dismiss the dialog and prevent it from showing again
                if st.button("Got it!", key=f"dismiss_{dialog_key}"):
                    st.session_state[dialog_key] = False
                    # Force a rerun to remove the dialog completely
                    st.rerun()
        return True
    
    return False

# Dictionary of page descriptions for course pages
PAGE_DESCRIPTIONS = {
    "course_introduction": {
        "title": "About the Course Introduction",
        "message": """
        **This is your starting point for the Prompt Engineering course.**
        
        Here you'll find:
        - An overview of the course structure and navigation
        - Explanations of the core concepts
        - Guidance on how to progress through the lessons
        
        To navigate, use the tabs at the top to explore different sections,
        and complete the Reflection to unlock Lesson 1.
        """
    },
    "course_examples": {
        "title": "About the Examples Section",
        "message": """
        **This section showcases real-world applications of prompt engineering.**
        
        You'll see:
        - Side-by-side comparisons of basic vs. engineered prompts
        - Analysis of effective prompt components
        - Educational examples relevant to teaching
        
        These examples provide a preview of the skills you'll develop throughout the course.
        """
    },
    "course_activities": {
        "title": "About the Activities Section",
        "message": """
        **This section offers hands-on practice with prompt engineering.**
        
        You'll be able to:
        - Analyze your current prompting habits
        - Experiment with a simple framework
        - Set personal learning goals
        
        Try the activities to establish a baseline for your skills and clarify what you
        want to gain from the course.
        """
    },
    "course_reflection": {
        "title": "About the Reflection Section",
        "message": """
        **This is where you reflect on your goals and experience.**
        
        ✨ **Important:** Completing this reflection by saving your responses will:
        - Mark the Course Introduction as complete 
        - Unlock Lesson 1
        - Establish your baseline for measuring progress
        
        Throughout the course, completing each lesson's reflection will unlock the next lesson.
        """
    }
} 