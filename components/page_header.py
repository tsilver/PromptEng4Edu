import streamlit as st

def render_page_header():
    """
    Renders a consistent header for all pages, including logo and AIxponential branding.
    """
    # Create a header row with logo and AIxponential branding
    header_col1, header_col2 = st.columns([1, 3])
    
    with header_col1:
        # Use AIxponential logo directly since we know it exists
        aix_logo_path = "images/aix_logo.png"
        st.image(aix_logo_path, width=100)
        
   
    with header_col2:
        # Custom header with reduced spacing
        st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0;">
            <div>
                <h1 style="margin-bottom: 0;">Prompt Engineering for Educators</h1>
                <div style="font-style: italic; margin-top: 0;">
                    <a href="http://aixponential.org" target="_blank" style="text-decoration: none; color: #0068C9;">
                        Presenting an AIxponential experience
                    </a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True) 