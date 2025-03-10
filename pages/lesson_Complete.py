import streamlit as st
import os
import sys
from utils.navigation import scroll_to_top, get_all_pages
from utils.state_management import initialize_session_state
from components.course_navigation import render_course_navigation

# Configure page
st.set_page_config(
    page_title="Course Completion",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Get the current directory and add to path if needed
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_Complete"
st.session_state.current_page = current_page

# Get all available pages for navigation
try:
    all_pages = get_all_pages()
except Exception as e:
    st.error(f"Error loading pages: {str(e)}")
    all_pages = []

# Scroll to top when page loads
scroll_to_top()

# Create main layout with content area on the left and navigation on the right
content_col, nav_col = st.columns([4, 1])

# Render the main content area
with content_col:
    # Course completion content
    st.markdown("# 🎓 Congratulations on Completing the Course!")
    
    st.markdown("""
    ## You've Mastered Prompt Engineering for Educators!
    
    You have successfully completed all lessons in this comprehensive course on prompt engineering
    for educational applications. This journey has equipped you with the knowledge, skills, and
    strategies to leverage AI effectively in your teaching practice.
    
    ### What You've Accomplished:
    
    - Mastered the PCTFR framework for creating effective AI prompts
    - Learned specialized techniques for different educational contexts
    - Developed skills to create personalized learning experiences
    - Built a toolkit of prompting strategies for various teaching needs
    - Gained confidence in using AI as a powerful educational assistant
    
    ### Your Learning Journey Continues
    
    This course is just the beginning of your journey with AI in education. As these technologies
    continue to evolve, we encourage you to:
    
    - **Practice regularly** with the techniques you've learned
    - **Experiment** with different approaches in your specific teaching context
    - **Share** your discoveries and successes with colleagues
    - **Stay updated** on emerging best practices and capabilities
    - **Join our community** of educational innovators
    """)
    
    # Feedback section
    st.markdown("## Help Us Improve")
    
    st.markdown("""
    Your feedback is invaluable to us! Please consider sharing your thoughts on:
    
    - Which lessons or activities were most valuable to you
    - What additional topics you'd like to see covered
    - How you plan to implement these techniques in your teaching
    - Any suggestions for improving the course
    
    Please send your feedback to: feedback@aixponential.org
    """)
    
    # About AIxponential section with mission
    st.markdown("## About AIxponential")
    
    st.image("https://placehold.co/600x200?text=AIxponential+Logo", width=400)
    
    st.markdown("""
    [AIxponential](http://aixponential.org) is dedicated to advancing AI education for all. We empower 
    teachers with the knowledge and tools to effectively integrate AI into their classrooms, fostering 
    a new generation of AI-literate students. 
    
    Through innovative curricula, teacher training programs, and the development of open-source 
    educational resources such as AI Summer Camp and AI Clubs, we strive to make AI accessible 
    and understandable, preparing learners of all backgrounds, ages, and professions to navigate 
    the future of work and society.
    
    Our work promotes disseminating knowledge, transparency, accessibility, and respect for the 
    responsible use of AI for the benefit of all.
    
    ### Join Our Community
    
    - Visit [aixponential.org](http://aixponential.org) to learn more
    - Follow us on social media for the latest updates and resources
    - Sign up for our newsletter to stay informed about new courses and opportunities
    - Become an AI education ambassador in your school or district
    """)
    
    # Certificate or acknowledgment
    st.markdown("## Share Your Achievement")
    
    st.markdown("""
    We encourage you to share your accomplishment with your professional network:
    
    "I've completed the Prompt Engineering for Educators course by AIxponential! 
    Excited to apply these AI skills in my teaching practice. #AIinEducation #ProfessionalDevelopment 
    #AIxponential"
    
    Consider downloading your certificate of completion and adding this credential to your 
    professional portfolio or resume.
    """)
    
    # Next steps
    st.markdown("## What's Next?")
    
    st.markdown("""
    Ready to continue your AI in education journey? Here are some next steps:
    
    - Explore our advanced courses on specific AI applications in education
    - Join our upcoming webinars and learning cohorts
    - Access our library of resources and prompt templates
    - Apply to become a mentor or contributor to our community
    
    Thank you for learning with us! We look forward to seeing how you transform 
    education with the power of AI.
    """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    **Prompt Engineering for Educators** | &copy; 2025 | A comprehensive course for teaching staff  
     ***Presenting an [AIxponential](http://aixponential.org) experience***            
    """)

# No navigation in the sidebar for the completion page
# This hides it from the regular course navigation

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