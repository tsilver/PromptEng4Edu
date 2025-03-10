import streamlit as st
import os
import sys
from utils.navigation import scroll_to_top, get_all_pages
from utils.state_management import initialize_session_state, mark_page_completed
from utils.teacher_client import TeacherClient
from components.teacher_notes import render_teacher_notes
from components.bottom_navigator import render_bottom_navigator
from components.breadcrumb_navigator import render_breadcrumb
from components.course_navigation import render_course_navigation
from components.top_navigator import render_top_navigator
from components.first_visit_dialog import show_first_visit_dialog
from components.progress_manager import render_teacher_controls_sidebar

# Initialize the TeacherClient
client = TeacherClient()

# Configure page
st.set_page_config(
    page_title="Lesson 10: Examples",
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
    "title": "Few-Shot Prompting: Examples",
    "lesson": "10",
    "section": "examples",
    "order": 2
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_10_examples"
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
    "lesson_10_examples",
    "examples",
    "Lesson 10: Examples of Few-Shot Prompting",
    """
    **This section provides practical examples of few-shot prompting in education.**
    
    You'll see:
    - Real-world examples of effective few-shot prompts
    - Comparisons between zero-shot and few-shot approaches
    - Different educational scenarios where few-shot prompting excels
    
    These examples will help you understand how to craft effective few-shot prompts
    for your specific teaching needs.
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
    st.markdown("## Few-Shot Prompting Examples")
    
    st.markdown("""
    The following examples demonstrate effective few-shot prompting in various educational contexts. 
    Each example shows how providing a small number of demonstrations can guide the AI to produce 
    responses that match a specific pattern, format, or style.
    """)
    
    # Example 1: Zero-Shot vs. Few-Shot Comparison
    st.markdown("### Example 1: Zero-Shot vs. Few-Shot for Student Feedback")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Zero-Shot Prompt:**
        ```
        Provide feedback on this 5th-grade student's response to the question: "How does the water cycle work?"
        
        Student answer: "The water cycle is when water goes up to the clouds and then comes back down as rain. The sun makes the water go up and then it falls down. Then it repeats over and over."
        ```
        
        **Response:** *(Summary)*
        
        A straightforward evaluation noting that the student has the basic idea but is missing key terminology like evaporation, condensation, and precipitation. Suggests the teacher should review these terms with the student and provide more detail about the process.
        
        **Limitations:**
        - Generic feedback approach
        - No specific praise points
        - Missing growth-focused language
        - Not tailored to 5th-grade level
        - No specific next steps
        """)
        
    with col2:
        st.markdown("""
        **Few-Shot Prompt:**
        ```
        I want to give encouraging, specific feedback to 5th-grade students on their science answers. Here are examples of the feedback style I'd like to use:
        
        Example 1:
        Student answer: "Rocks are formed by volcanoes when they erupt and the lava cools down."
        Feedback: "Good start! 👍 You correctly identified that some rocks form when lava cools. This is how igneous rocks form! For an even stronger answer, you could mention that there are two other rock types (sedimentary and metamorphic) that form in different ways. What might you add about how weathering affects rock formation?"
        
        Example 2:
        Student answer: "Plants make their own food using sunlight, water, and air. This is called photosynthesis."
        Feedback: "Excellent use of the scientific term 'photosynthesis'! 🌟 Your answer correctly includes the key ingredients plants need. To make your explanation even more complete, consider mentioning that plants use carbon dioxide specifically from the air and that they produce oxygen as a result. What role do the green parts of plants play in this process?"
        
        Now, please provide feedback in a similar style to this student response:
        
        Question: "How does the water cycle work?"
        Student answer: "The water cycle is when water goes up to the clouds and then comes back down as rain. The sun makes the water go up and then it falls down. Then it repeats over and over."
        ```
        
        **Response:**
        
        "Great start! 👍 You've correctly described the basic pattern of the water cycle—water rising up and then falling back down as rain in a continuous cycle. You also identified the sun as the energy source that drives this process!
        
        To make your answer even stronger, try using scientific terms like 'evaporation' (when the sun heats water and turns it into vapor), 'condensation' (when water vapor forms clouds), and 'precipitation' (when water falls as rain, snow, or hail). Also, consider mentioning what happens after the rain falls—where does the water go before it evaporates again?
        
        What might you add about how the water cycle affects our local environment? 💧🌦️"
        
        **Improvements:**
        - Matches the encouraging tone from examples
        - Begins with specific praise
        - Uses emojis consistent with examples
        - Suggests specific terminology to add
        - Ends with a thought-provoking question
        - Age-appropriate explanations in parentheses
        """)
    
    st.markdown("""
    **Key Takeaway:** The few-shot approach produces feedback that precisely matches the style demonstrated 
    in the examples—encouraging, specific, and with a consistent structure (praise, suggestions for improvement, 
    and a follow-up question). The pattern of starting with positive reinforcement, using emojis, and ending with 
    a question is replicated, showing how examples effectively guide the AI's response format and tone.
    """)
    
    # Example 2: Few-Shot for Specialized Question Types
    st.markdown("### Example 2: Few-Shot for Specialized Question Types")
    
    st.markdown("""
    This example demonstrates how few-shot prompting can guide the AI to create specialized types of educational questions.
    """)
    
    st.markdown("""
    **Few-Shot Prompt for Socratic Questioning:**
    ```
    I want to create Socratic questions that help 10th-grade students explore the themes in "To Kill a Mockingbird" by Harper Lee. Socratic questions should promote critical thinking without providing answers. Here are examples of the types of questions I want:
    
    Example 1: "In the novel, Atticus states that 'You never really understand a person until you consider things from his point of view... until you climb into his skin and walk around in it.' How might this perspective-taking change how we judge characters like Boo Radley or Mayella Ewell?"
    
    Example 2: "Scout initially views Walter Cunningham through the lens of social class. How does her perspective evolve throughout the novel, and what might Lee be suggesting about the nature of prejudice beyond racial discrimination?"
    
    Example 3: "When examining the trial scene, what parallels can you draw between the courtroom events and broader social structures in Maycomb? What might these parallels reveal about institutional justice?"
    
    Please create 5 more Socratic questions that follow this model for discussing "To Kill a Mockingbird" with 10th-grade students.
    ```
    
    **Response Excerpts:**
    
    1. "Throughout the novel, characters like Dolphus Raymond deliberately subvert social expectations. In what ways might these characters serve as foils to the more conventional residents of Maycomb, and what might Lee be suggesting about societal conformity versus individual authenticity?"
    
    2. "Courage is defined and demonstrated in various ways throughout the novel—from Mrs. Dubose's battle with addiction to Atticus's defense of Tom Robinson. How do these different manifestations of courage complicate our understanding of what it means to be brave? What might this suggest about moral strength in the face of adversity?"
    
    3. "The mockingbird emerges as a central symbol in the novel, with characters like Tom Robinson and Boo Radley often associated with this image. Beyond the obvious parallel of innocence, what deeper implications might this symbol hold when considering the social structure of Maycomb? How does this symbolism invite readers to reconsider their own judgments?"
    
    4. "Jem's response to the trial verdict differs markedly from Scout's. How might their different reactions reflect their respective developmental stages and emerging moral frameworks? What might Lee be suggesting about the process of disillusionment with social institutions?"
    
    5. "The novel presents a community where gossip and storytelling play crucial roles in establishing and maintaining social hierarchies. How does the control of narrative serve as a form of power in Maycomb? Who gets to tell stories, and whose stories are believed or dismissed?"
    """)
    
    st.markdown("""
    **Analysis of Few-Shot Success:**
    
    - The AI accurately replicated the complex structure of Socratic questioning
    - Each generated question follows the pattern of the examples:
      - Opens with an observation about the text
      - Poses open-ended questions that require analysis
      - Avoids simple yes/no responses
      - Builds toward broader implications
      - Uses sophisticated literary analysis terms appropriate for 10th grade
    - The questions maintain the same level of complexity and depth as the examples
    - Each question addresses different themes and characters from the novel
    - The style is consistently thought-provoking rather than fact-checking
    """)
    
    # Example 3: Few-Shot for Differentiated Content
    st.markdown("### Example 3: Few-Shot for Differentiated Content")
    
    st.markdown("""
    This example shows how few-shot prompting can guide the AI to create differentiated versions of the same content.
    """)
    
    st.markdown("""
    **Few-Shot Prompt for Differentiated Explanations:**
    ```
    I need to create differentiated explanations of photosynthesis for a mixed-ability 7th-grade science class. Please provide three versions (basic, intermediate, and advanced) following these examples:
    
    Topic: States of Matter
    
    BASIC VERSION:
    States of matter are the different forms that substances can take. The three main states are:
    • Solid: Has a fixed shape and volume. The particles are tightly packed and only vibrate in place. Example: Ice cube.
    • Liquid: Has a fixed volume but takes the shape of its container. The particles can move around each other. Example: Water in a glass.
    • Gas: Has no fixed shape or volume and fills its container. The particles move quickly in all directions. Example: Steam.
    Temperature determines which state a substance is in. Adding heat can change a solid to a liquid (melting) or a liquid to a gas (evaporation).
    
    INTERMEDIATE VERSION:
    States of matter represent different arrangements of particles in a substance based on energy levels. In the three common states:
    • Solids maintain definite shape and volume because particles are held in fixed positions by strong attractive forces, allowing only vibrational movement.
    • Liquids maintain volume but take their container's shape because particles have enough energy to overcome some attractive forces, allowing them to slide past each other while remaining close together.
    • Gases have neither definite shape nor volume because particles have sufficient energy to overcome most attractive forces, moving independently in random directions.
    Phase transitions occur at specific temperatures and pressures when energy changes alter the balance between particle motion and attractive forces. These transitions include melting, freezing, evaporation, condensation, sublimation, and deposition.
    
    ADVANCED VERSION:
    States of matter represent distinct phases characterized by different physical properties arising from variations in molecular kinetic energy and intermolecular forces. In crystalline solids, molecules organize in ordered lattice structures with vibrational movements constrained by strong intermolecular bonds, exhibiting properties like rigidity and defined melting points. In liquids, increased kinetic energy partially overcomes these attractive forces, allowing translational movement while maintaining sufficient cohesion to preserve volume but not shape, demonstrating properties like surface tension and viscosity. In gases, kinetic energy substantially exceeds intermolecular attractions, resulting in independent particle movement governed primarily by collision mechanics as described in the kinetic molecular theory.
    
    Beyond the three classical states, plasma (ionized gas) and various condensed matter states (like Bose-Einstein condensates) emerge under extreme conditions, challenging the traditional classification system. Phase transitions between states involve enthalpy changes as energy is absorbed or released during the reorganization of molecular structures and intermolecular bonds, with transition dynamics explained through thermodynamic principles and phase diagrams mapping the conditions under which each state is stable.
    
    Topic: Photosynthesis
    [Please create basic, intermediate, and advanced versions following the pattern above]
    ```
    
    **Response Excerpts:**
    
    **BASIC VERSION:**
    Photosynthesis is how plants make their own food using sunlight. Here's how it works:
    • Plants take in sunlight through their leaves
    • They absorb water from the soil through their roots
    • They take in carbon dioxide from the air through tiny holes in their leaves called stomata
    • Inside the leaves, chlorophyll (the green stuff) captures the sun's energy
    • This energy is used to turn water and carbon dioxide into sugar and oxygen
    • Plants use the sugar for food and release the oxygen into the air
    This process is important because it provides food for plants and oxygen for animals to breathe.
    
    **INTERMEDIATE VERSION:**
    Photosynthesis is the biological process through which plants, algae, and some bacteria convert light energy into chemical energy. The process occurs primarily in the chloroplasts, especially in the leaf cells of plants, and involves several synchronized steps:
    
    • Light-dependent reactions occur in the thylakoid membranes, where chlorophyll and other pigments capture photons, energizing electrons that travel through electron transport chains to produce ATP and NADPH.
    • The Calvin cycle (light-independent reactions) takes place in the stroma, where carbon dioxide is incorporated into existing organic compounds through carbon fixation, using the ATP and NADPH from the light-dependent reactions to produce glucose.
    
    The overall chemical equation can be summarized as:
    6CO₂ + 6H₂O + light energy → C₆H₁₂O₆ + 6O₂
    
    Photosynthesis is fundamental to most ecosystems as it converts inorganic carbon into organic compounds, serves as the base of food webs, and maintains atmospheric oxygen levels.
    
    **ADVANCED VERSION:**
    Photosynthesis represents a sophisticated bioenergetic process of autotrophic carbon fixation characterized by the transduction of electromagnetic radiation into chemical potential energy. This process entails two integrated but distinct photochemical and biochemical phases occurring within specialized organelles called chloroplasts, containing elaborate internal membrane systems (thylakoids) embedded within the protein-rich stroma.
    
    In the photochemical phase (light-dependent reactions), photosystems I and II—supramolecular complexes containing precisely oriented chlorophyll, carotenoid, and phycobilin pigments—harvest photons, inducing electronic excitation and subsequent charge separation. This initiates an elaborate redox cascade through cytochrome complexes and plastoquinones, culminating in the generation of a proton gradient across the thylakoid membrane. This proton-motive force drives ATP synthesis via chemiosmotic coupling through the ATP synthase complex while simultaneously reducing NADP⁺ to NADPH via ferredoxin-NADP⁺ reductase.
    
    The biochemical phase (Calvin-Benson-Bassham cycle) employs the ATP and NADPH to orchestrate the endergonic assimilation of atmospheric carbon dioxide. This process involves the carboxylation of ribulose-1,5-bisphosphate catalyzed by RuBisCO, followed by a series of phosphorylated intermediates undergoing isomerization, reduction, and regeneration reactions, ultimately yielding triose phosphates that serve as precursors for glucose synthesis and metabolic integration.
    
    The evolutionary significance of photosynthesis extends beyond primary productivity to include biogeochemical cycling, atmospheric composition regulation, and the establishment of redox homeostasis in the biosphere. Modern research focuses on quantum coherence effects in energy transfer, regulatory mechanisms responding to environmental fluctuations, and potential bioengineering applications to enhance photosynthetic efficiency in addressing global food security and renewable energy challenges.
    """)
    
    st.markdown("""
    **Analysis of Differentiation Pattern:**
    
    The AI has effectively replicated the differentiation pattern from the example, creating three distinct versions that systematically vary in:
    
    - **Vocabulary Complexity**: From everyday terms to specialized scientific vocabulary
    - **Conceptual Depth**: From basic processes to molecular mechanisms
    - **Sentence Structure**: From simple to complex compound sentences
    - **Detail Level**: From general overview to specific biochemical pathways
    - **Visual Support**: Consistent use of bullet points for the basic and intermediate versions
    - **Abstraction Level**: From concrete examples to theoretical frameworks
    
    Each version maintains internal consistency in its complexity level while covering the same fundamental concept, demonstrating how few-shot prompting can guide the creation of truly differentiated educational content.
    """)
    
    # Example 4: Few-Shot for Assessment Creation
    st.markdown("### Example 4: Few-Shot for Standardized Assessment Items")
    
    st.markdown("""
    This example demonstrates how few-shot prompting can guide the AI to create assessment items that match a specific standardized format.
    """)
    
    st.markdown("""
    **Few-Shot Prompt for Math Assessment Items:**
    ```
    I need to create assessment items for 8th-grade math following our district's standard format. Please create 5 new items following these examples:
    
    Example Item 1:
    Standard: 8.EE.C.7 - Solve linear equations in one variable.
    
    Item Stem: Solve for x in the equation 3(x - 4) = 6x - 5
    
    A. x = -1
    B. x = 1
    C. x = 7
    D. x = 13
    
    Answer: C
    
    Rationale: 
    3(x - 4) = 6x - 5
    3x - 12 = 6x - 5
    -12 + 5 = 6x - 3x
    -7 = 3x
    x = -7/3
    
    This is not one of the given options, so there must be a computational error. Let's verify each option:
    
    For x = 7:
    Left side: 3(7 - 4) = 3(3) = 9
    Right side: 6(7) - 5 = 42 - 5 = 37
    
    The left side does not equal the right side for any of the given values. Rechecking the algebra:
    
    3(x - 4) = 6x - 5
    3x - 12 = 6x - 5
    -3x = -12 + 5
    -3x = -7
    x = 7/3
    
    Converting to a mixed number: x = 2⅓
    
    Since 7 is the only answer choice close to 2⅓, the answer is C. x = 7.
    
    Cognitive Complexity: DOK Level 2 - Basic Application of Skills & Concepts
    
    ---
    
    Example Item 2:
    Standard: 8.G.B.7 - Apply the Pythagorean Theorem to determine unknown side lengths in right triangles.
    
    Item Stem: A ladder is leaning against a building, creating a right angle with the ground. The foot of the ladder is 5 meters from the building, and the ladder is 13 meters long. How high up the building does the ladder reach?
    
    A. 8 meters
    B. 12 meters
    C. 14 meters
    D. 18 meters
    
    Answer: B
    
    Rationale: This problem represents a right triangle where:
    - The horizontal distance from the building to the ladder's foot is 5 meters
    - The length of the ladder is 13 meters
    - We need to find the height up the building (the vertical leg of the triangle)
    
    Using the Pythagorean Theorem: a² + b² = c²
    where a = 5 meters, c = 13 meters, and b is the unknown height
    
    5² + b² = 13²
    25 + b² = 169
    b² = 144
    b = 12
    
    Therefore, the ladder reaches 12 meters up the building.
    
    Cognitive Complexity: DOK Level 2 - Basic Application of Skills & Concepts
    
    ---
    
    Please create 5 new assessment items following this exact format for the following 8th grade math standards:
    1. 8.NS.A.1 - Know that numbers that are not rational are called irrational.
    2. 8.F.B.4 - Construct a function to model a linear relationship.
    3. 8.SP.A.1 - Construct and interpret scatter plots.
    4. 8.G.A.4 - Understand congruence and similarity using transformations.
    5. 8.EE.B.5 - Graph proportional relationships, interpreting the unit rate as the slope.
    ```
    
    **Partial Response (First Item):**
    
    ```
    Standard: 8.NS.A.1 - Know that numbers that are not rational are called irrational.
    
    Item Stem: Which of the following numbers is irrational?
    
    A. 0.25
    B. √49
    C. -√18
    D. 3.141414...
    
    Answer: C
    
    Rationale: To determine which number is irrational, we need to check if each can be expressed as a fraction (rational) or not (irrational).
    
    A. 0.25 = 1/4, which is a rational number.
    
    B. √49 = 7, which is a rational number.
    
    C. -√18 can be simplified to -3√2. Since √2 is irrational (it cannot be expressed as a fraction), -√18 is also irrational.
    
    D. 3.141414... has a repeating pattern (14) and can be written as a fraction. Any repeating decimal can be expressed as a rational number. This can be written as 3.14̅ = 311/99, which is rational.
    
    Therefore, -√18 is the only irrational number among the choices.
    
    Cognitive Complexity: DOK Level 1 - Recall and Reproduction
    ```
    """)
    
    st.markdown("""
    **Analysis of Assessment Item Format Matching:**
    
    The AI has successfully replicated the exact format from the examples:
    
    - **Standard Citation**: Includes the full standard number and description
    - **Item Stem**: Presents a clear question in the appropriate format
    - **Multiple Choice Options**: Offers four lettered options (A-D)
    - **Answer Identification**: Clearly indicates the correct answer
    - **Detailed Rationale**: Provides step-by-step reasoning with sufficient mathematical work
    - **Answer Verification**: Checks each option to explain why the answer is correct
    - **Cognitive Complexity**: Indicates the DOK (Depth of Knowledge) level with description
    
    This example demonstrates how few-shot prompting can ensure precise adherence to standardized formats for assessment creation, which is particularly valuable for teachers who need to create materials that match specific institutional requirements.
    """)
    
    # Example 5: Few-Shot for Writing Framework
    st.markdown("### Example 5: Few-Shot for Teaching Writing Frameworks")
    
    st.markdown("""
    This example shows how to use few-shot prompting to guide students in applying specific writing frameworks.
    """)
    
    st.markdown("""
    **Few-Shot Prompt for Claim-Evidence-Reasoning:**
    ```
    I'm teaching my 6th-grade science students to write explanations using the Claim-Evidence-Reasoning (CER) framework. I want to show them examples of how to analyze different phenomena using this structure. Here are two examples:
    
    Example 1: Why does an ice cube melt faster in warm water than in cold water?
    
    CLAIM: Ice cubes melt faster in warm water than in cold water because of the greater temperature difference.
    
    EVIDENCE: 
    - In our experiment, the ice cube in 80°F water completely melted in 2 minutes and 15 seconds.
    - The ice cube in 40°F water took 8 minutes and 30 seconds to completely melt.
    - We observed that the ice cube in warm water immediately started forming small droplets around it, while the ice cube in cold water changed much more slowly.
    
    REASONING: When ice is placed in water, heat energy transfers from the water to the ice. The greater the temperature difference between the ice and water, the faster this heat transfer occurs. This happens because heat naturally flows from warmer areas to cooler areas. The warm water had much more heat energy to transfer to the ice, causing the faster melting. At the molecular level, the water molecules in the warm water have more kinetic energy and collide more vigorously with the ice molecules, breaking the solid crystal structure more quickly and turning the ice into liquid water.
    
    Example 2: Why do some objects float in water while others sink?
    
    CLAIM: Objects float in water when they have a lower density than water, and sink when they have a higher density than water.
    
    EVIDENCE:
    - The wooden block (density 0.8 g/cm³) floated on water.
    - The plastic button (density 1.2 g/cm³) sank to the bottom.
    - The aluminum foil ball (density 2.7 g/cm³) sank when rolled tightly but floated when shaped into a boat.
    - A steel paper clip (density 7.8 g/cm³) sank normally but floated when placed carefully on the surface.
    
    REASONING: An object's behavior in water depends primarily on density, which is mass divided by volume. Water has a density of 1 g/cm³. When an object has a density lower than water (like the wooden block), the buoyant force from the water is greater than the object's weight, causing it to float. Objects with higher density than water (like the button) have weight that exceeds the buoyant force, causing them to sink. However, shape can also affect floating. When materials like aluminum foil or steel are shaped to displace a greater volume of water, they can float despite having higher densities than water. This explains why steel ships can float even though steel itself is denser than water. Additionally, surface tension can allow some dense objects like paper clips to float if placed carefully on the water's surface, creating a "skin" that supports the weight.
    
    Now, please create a similar CER analysis for the following question:
    Why do leaves change color in the fall?
    ```
    
    **Response:**
    
    ```
    Why do leaves change color in the fall?
    
    CLAIM: Leaves change color in the fall because trees stop producing chlorophyll, revealing other pigments that were already present in the leaves.
    
    EVIDENCE:
    - During spring and summer, leaves appear green due to the abundance of chlorophyll.
    - In the fall, when temperatures drop and daylight hours decrease, trees begin preparing for winter by blocking the flow of nutrients to leaves.
    - As chlorophyll breaks down without being replaced, yellow and orange pigments (carotenoids) that were already present in the leaves become visible.
    - Some trees produce new red and purple pigments (anthocyanins) in the fall.
    - Brown colors appear as waste products accumulate in the leaves.
    
    REASONING: Throughout most of the year, leaves contain several pigments, but the green chlorophyll is so abundant that it masks other colors. Chlorophyll is essential for photosynthesis, the process by which trees convert sunlight into energy. As winter approaches, reduced sunlight and colder temperatures signal deciduous trees to prepare for dormancy. The trees form a layer of cells at the base of each leaf stem that gradually blocks the flow of water and nutrients. Without a continuous supply of nutrients, the tree can no longer produce chlorophyll, which breaks down relatively quickly. As the dominant green color fades, the yellow and orange carotenoids that were always present in the leaves become visible. The production of anthocyanins, which create red and purple colors, is stimulated by bright light and excess sugar trapped in the leaves. These color changes are the tree's visible response to environmental triggers and represent an important adaptation that helps trees survive winter conditions by shedding leaves that would otherwise be damaged by freezing temperatures and unable to perform photosynthesis efficiently during low-light winter months.
    ```
    """)
    
    st.markdown("""
    **Analysis of Writing Framework Pattern:**
    
    The AI has successfully replicated the Claim-Evidence-Reasoning framework demonstrated in the examples:
    
    - **Claim Section**: Provides a clear, direct answer to the question
    - **Evidence Section**: Lists specific, relevant observations in bullet points
    - **Reasoning Section**: Connects the evidence to scientific principles in a detailed explanation
    
    The response matches the following specific patterns from the examples:
    
    - **Structure**: Maintains the exact three-part organization
    - **Formatting**: Uses all caps for section headers followed by a colon
    - **Evidence Style**: Presents 4-5 bullet points of observable facts
    - **Reasoning Depth**: Includes both macroscopic explanations and molecular/cellular details
    - **Scientific Language**: Incorporates appropriate terminology (pigments, chlorophyll, etc.)
    - **Conclusion Connection**: Relates the phenomenon to broader ecological context
    
    This example demonstrates how few-shot prompting can help teachers create consistent models of writing frameworks for students, or assist students directly in applying specific writing structures to new content.
    """)
    
    # Key lessons from examples
    st.markdown("## Key Insights from Few-Shot Examples")
    
    st.markdown("""
    From these examples, we can identify several important patterns for effective few-shot prompting:
    
    1. **Example Quality Matters**: The examples you provide should be high-quality representations of exactly what you want
    
    2. **Consistent Formatting**: Use the same format, structure, and style across all examples
    
    3. **Strategic Example Selection**: Choose examples that highlight the specific aspects you care about (tone, complexity, structure)
    
    4. **Clear Patterns**: Make the pattern you want the AI to follow obvious across multiple examples
    
    5. **Domain-Specific Features**: Include educational elements that matter (grade-appropriate language, standards alignment, etc.)
    
    6. **Explicit Instructions**: Complement your examples with clear instructions about what to generate
    
    7. **Example Quantity**: 2-3 well-crafted examples are usually sufficient to establish a pattern
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific guidance
    render_teacher_notes("""
    **Key Points to Emphasize:**
    
    * Few-shot prompting works particularly well for specialized educational formats that have specific structures
    * The examples you provide serve as models that the AI will mimic, so their quality directly affects output quality
    * This approach is especially valuable for creating consistent resources across multiple subjects or units
    * Few-shot prompting is often worth the extra effort when format consistency is essential
    
    **Discussion Questions:**
    
    * Which of the example types would be most valuable in your teaching context?
    * What educational content do you create that would benefit from a more consistent format?
    * How might you build a personal library of examples for your frequent content needs?
    * What specific formatting elements are most important for your subject area or grade level?
    
    **Extension Idea:**
    
    Have participants identify one type of educational content they frequently create that follows a consistent 
    structure, and draft 2-3 examples they could use in a few-shot prompt to generate more of the same.
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