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
    page_title="Lesson 11: Examples",
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
    "title": "Chain-of-Thought Prompting: Examples",
    "lesson": "11",
    "section": "examples",
    "order": 2
}

# Initialize session state
initialize_session_state()

# Set current page in session state
current_page = "lesson_11_examples"
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
    "lesson_11_examples",
    "examples",
    "Chain-of-Thought Prompting: Examples",
    """
    **This section provides practical examples of chain-of-thought prompting in education.**
    
    You'll see:
    - Real-world applications across different subject areas
    - Comparisons between basic prompts and chain-of-thought prompts
    - How this technique improves the quality and educational value of AI responses
    
    These examples will help you understand how to implement chain-of-thought prompting
    for various educational needs.
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
    st.markdown("## Chain-of-Thought Prompting Examples")
    
    st.markdown("""
    The following examples demonstrate how chain-of-thought prompting can improve AI-generated content 
    for various educational purposes. Each example contrasts a basic prompt with a chain-of-thought prompt
    to highlight the differences in the responses.
    """)
    
    # Example 1: Mathematics
    st.markdown("### Example 1: Mathematics Problem Solving")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Basic Prompt:**
        ```
        Calculate the final amount in a savings account 
        after 3 years if $5,000 is invested at an annual 
        interest rate of 4.5%, compounded quarterly.
        ```
        
        **Response:** *(Summary)*
        
        The final amount after 3 years is $5,713.54.
        """)
        
    with col2:
        st.markdown("""
        **Chain-of-Thought Prompt:**
        ```
        Calculate the final amount in a savings account 
        after 3 years if $5,000 is invested at an annual 
        interest rate of 4.5%, compounded quarterly.
        
        Think step-by-step, showing each stage of the 
        calculation and explaining the compound interest 
        formula being used.
        ```
        
        **Response:**
        
        To calculate the final amount with compound interest, I'll use the compound interest formula:
        
        A = P(1 + r/n)^(nt)
        
        Where:
        - A is the final amount
        - P is the principal (initial investment)
        - r is the annual interest rate (as a decimal)
        - n is the number of times interest is compounded per year
        - t is the time in years
        
        Given information:
        - Principal (P) = $5,000
        - Annual interest rate (r) = 4.5% = 0.045
        - Compounding frequency (n) = 4 (quarterly means 4 times per year)
        - Time (t) = 3 years
        
        Step 1: Identify the values to plug into the formula.
        A = $5,000(1 + 0.045/4)^(4×3)
        
        Step 2: Calculate r/n.
        0.045/4 = 0.01125
        
        Step 3: Calculate (1 + r/n).
        1 + 0.01125 = 1.01125
        
        Step 4: Calculate n×t to get the total number of compounding periods.
        4 × 3 = 12 compounding periods
        
        Step 5: Calculate (1 + r/n)^(nt).
        (1.01125)^12 ≈ 1.14271
        
        Step 6: Multiply by the principal to get the final amount.
        $5,000 × 1.14271 = $5,713.54
        
        Therefore, after 3 years, the savings account will have $5,713.54, which includes the original $5,000 plus $713.54 in compound interest.
        """)
    
    st.markdown("""
    **Key Benefits:**
    
    1. **Educational Value:** The step-by-step explanation teaches the compound interest concept, not just the answer
    2. **Transparency:** You can verify each calculation step for accuracy
    3. **Formula Explanation:** Clearly shows and explains the formula being used
    4. **Learning Aid:** Provides a model that students can follow for similar problems
    """)
    
    # Example 2: Science
    st.markdown("### Example 2: Scientific Explanation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Basic Prompt:**
        ```
        Explain how natural selection leads to 
        adaptation in species.
        ```
        
        **Response:** *(Summary)*
        
        A brief explanation of natural selection stating that organisms with advantageous traits survive and reproduce at higher rates, passing these traits to offspring, leading to adaptations over time as populations become better suited to their environments.
        """)
        
    with col2:
        st.markdown("""
        **Chain-of-Thought Prompt:**
        ```
        Explain how natural selection leads to adaptation 
        in species. Break down the process step-by-step,
        explaining the causal relationships between each 
        stage, and include a specific example to illustrate 
        the process.
        ```
        
        **Response:**
        
        Let me walk through how natural selection leads to adaptation in species:
        
        Step 1: Genetic Variation
        - All populations have genetic variation among individuals
        - This variation arises from mutations, genetic recombination during reproduction, and gene flow
        - For example, in a population of beetles, some might have slightly darker shells than others due to different alleles
        
        Step 2: Differential Reproduction
        - Resources in any environment are limited (food, water, territory, mates)
        - Individuals compete for these limited resources
        - Some traits provide advantages in this competition
        - Individuals with advantageous traits survive longer and produce more offspring
        - In our beetle example, if the environment has dark soil and predatory birds hunt by sight, darker beetles would be less visible to predators
        
        Step 3: Heritability of Traits
        - Advantageous traits must be heritable (genetically transmitted) to affect evolution
        - Surviving individuals pass their beneficial genes to their offspring
        - In our beetle example, the genes for darker coloration are passed to offspring
        
        Step 4: Accumulation of Changes
        - Over many generations, advantageous traits become more common in the population
        - Less advantageous traits become less common
        - The population's overall characteristics change over time
        - Our beetle population gradually becomes darker over many generations
        
        Step 5: Adaptation to Environment
        - The population becomes better suited (adapted) to its specific environment
        - This adaptation is relative to a specific environmental context
        - If the environment changes, different traits may become advantageous
        - In our example, if the soil changed to a lighter color due to environmental changes, the advantage would shift to lighter-colored beetles
        
        Real-world example: The peppered moth (Biston betularia) in England during the Industrial Revolution. Before industrialization, light-colored moths were common as they blended with light-colored tree bark. When pollution darkened the trees with soot, darker moths gained an advantage (predators couldn't see them as easily). The population shifted from predominantly light-colored to predominantly dark-colored moths within decades. When air quality laws reduced pollution, the trend began to reverse, demonstrating natural selection responding to environmental changes in real-time.
        
        This process explains how species become adapted to their environments over time - not through purposeful change, but through the differential survival and reproduction of individuals with traits that happen to be advantageous in their specific environment.
        """)
    
    st.markdown("""
    **Key Benefits:**
    
    1. **Logical Flow:** Breaks down a complex process into clear sequential steps
    2. **Causality:** Explains the cause-and-effect relationships between each stage
    3. **Concrete Example:** Uses both a theoretical example (beetles) and a real-world example (peppered moths)
    4. **Comprehensive Coverage:** Includes all key aspects of natural selection, not just a simplified version
    """)
    
    # Example 3: Literature Analysis
    st.markdown("### Example 3: Literary Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Basic Prompt:**
        ```
        Analyze the theme of appearance versus reality 
        in Shakespeare's "Macbeth."
        ```
        
        **Response:** *(Summary)*
        
        A standard analysis stating that the theme of appearance vs. reality runs throughout the play, with examples like the witches' prophecies, characters' deceptions, and Macbeth's internal conflict, concluding that Shakespeare uses this theme to explore human nature and deception.
        """)
        
    with col2:
        st.markdown("""
        **Chain-of-Thought Prompt:**
        ```
        Analyze the theme of appearance versus reality in 
        Shakespeare's "Macbeth." Walk through your analysis 
        by:
        
        1. First identifying key scenes or elements where 
           this theme appears
        2. Then analyzing each element's significance
        3. Exploring how the theme develops throughout the play
        4. Explaining how this theme connects to the play's 
           broader message
        
        Include specific textual evidence in your analysis.
        ```
        
        **Response:**
        
        # Analysis of Appearance vs. Reality in "Macbeth"
        
        ## Step 1: Identifying Key Elements
        
        Let me first identify the major instances where the theme of appearance versus reality appears in the play:
        
        1. The witches' prophecies and equivocation ("Fair is foul, and foul is fair")
        2. Macbeth and Lady Macbeth's deception and false appearances
        3. The supernatural elements (dagger, Banquo's ghost)
        4. Duncan's murder and the aftermath
        5. Macduff and Malcolm's testing scene
        
        ## Step 2: Analyzing Each Element
        
        ### The Witches' Equivocation
        
        The play opens with the witches declaring, "Fair is foul, and foul is fair" (Act 1, Scene 1). This paradoxical statement establishes the play's central tension between appearance and reality. The witches' prophecies are technically true but misleading:
        
        - They tell Macbeth he'll be king but don't reveal the moral cost
        - They tell him to "beware Macduff" but also that "none of woman born shall harm Macbeth"
        - They assure him he won't be defeated until "Birnam Wood to high Dunsinane Hill shall come"
        
        The significance: These prophecies are deliberately ambiguous, suggesting certainty while hiding their true meaning. Macbeth interprets them according to his desires, not realizing their deeper truth.
        
        ### Macbeth and Lady Macbeth's Deception
        
        Lady Macbeth specifically instructs her husband to "look like the innocent flower, but be the serpent under it" (Act 1, Scene 5). After Duncan's murder, Macbeth says:
        
        "False face must hide what the false heart doth know." (Act 1, Scene 7)
        
        The significance: Their external appearance of loyal hosts directly contradicts their murderous intentions. This deception extends to their public personas versus private guilt throughout the play.
        
        ### Supernatural Elements as Psychological Reality
        
        Macbeth sees a dagger leading him to Duncan's chamber:
        
        "Is this a dagger which I see before me,
        The handle toward my hand?" (Act 2, Scene 1)
        
        Later, he sees Banquo's ghost at the feast when others cannot.
        
        The significance: These visions represent Macbeth's internal reality (guilt, fear) manifesting externally, creating another layer of the appearance/reality dichotomy—are these real supernatural events or psychological projections?
        
        ## Step 3: Development Throughout the Play
        
        The theme evolves through the play's progression:
        
        1. Early stages: Deception is deliberate and calculated (Lady Macbeth's plotting)
        2. Middle: Appearances begin to crack under the weight of reality (Macbeth's vision of Banquo, Lady Macbeth's sleepwalking)
        3. End: Reality finally overwhelms false appearances (the moving forest, Macduff's birth, Lady Macbeth's madness)
        
        This progression shows how maintaining false appearances eventually becomes unsustainable as reality asserts itself.
        
        ## Step 4: Connection to Broader Message
        
        Shakespeare uses this theme to explore several deeper messages:
        
        1. Moral truth cannot be permanently obscured by deception
        2. Self-deception is ultimately self-destructive
        3. Political stability requires honest leadership, not just the appearance of legitimacy
        4. The psychological cost of maintaining false appearances leads to deterioration of the self
        
        The play ultimately suggests that while people can manipulate appearances temporarily, underlying reality eventually emerges—often with devastating consequences. Shakespeare's famous line spoken by Macbeth near the end captures this futility of deception:
        
        "Life's but a walking shadow, a poor player
        That struts and frets his hour upon the stage
        And then is heard no more." (Act 5, Scene 5)
        
        This melancholic reflection suggests that all human appearances are temporary illusions that cannot withstand the ultimate reality of mortality and moral consequence.
        """)
    
    st.markdown("""
    **Key Benefits:**
    
    1. **Structured Analysis:** Follows a clear analytical process from identification to significance
    2. **Evidence-Based:** Incorporates specific quotations and textual evidence
    3. **Developmental View:** Shows how the theme evolves and develops, not just where it appears
    4. **Depth of Interpretation:** Connects the theme to broader philosophical implications
    """)
    
    # Example 4: Historical Analysis
    st.markdown("### Example 4: Historical Causation Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Basic Prompt:**
        ```
        Explain the causes of the Great Depression.
        ```
        
        **Response:** *(Summary)*
        
        A list of causes including the stock market crash of 1929, banking failures, reduced purchasing, the Dust Bowl, economic policies, and international factors, without much analysis of how these factors interacted or their relative importance.
        """)
        
    with col2:
        st.markdown("""
        **Chain-of-Thought Prompt:**
        ```
        Explain the causes of the Great Depression. Analyze 
        this historical question by:
        
        1. Identifying the major causal factors
        2. Explaining how these factors interacted
        3. Evaluating their relative importance
        4. Distinguishing between immediate triggers and 
           underlying structural causes
        
        Develop your analysis logically, considering both 
        economic and social dimensions.
        ```
        
        **Response:**
        
        # Causes of the Great Depression: A Causal Analysis
        
        ## Step 1: Identifying Major Causal Factors
        
        The Great Depression (1929-1939) resulted from multiple interconnected factors:
        
        **Economic Factors:**
        - Stock market speculation and the 1929 crash
        - Banking system weaknesses and failures
        - Monetary policy constraints (gold standard)
        - Uneven distribution of wealth
        - Agricultural overproduction and price collapse
        - Industrial overproduction relative to consumption
        - High tariffs and trade policies (Smoot-Hawley Tariff)
        
        **Structural Factors:**
        - Weak international economic structure after WWI
        - Excessive consumer debt and installment buying
        - Dependence on a few key industries (auto, construction)
        - Imbalanced global debt structure (war reparations, loans)
        
        ## Step 2: Analyzing Factor Interactions
        
        These factors created a complex web of cause and effect:
        
        **Stock Market and Banking Connection:**
        The speculative bubble of the late 1920s was fueled by easy credit and margin buying. When the market crashed in October 1929, it triggered margin calls that forced liquidation of assets. This impacted banks who had invested in the market or made loans for stock purchases. As banks failed, they called in loans and reduced credit, further depressing economic activity.
        
        **Wealth Distribution and Consumption:**
        By 1929, the top 0.1% of Americans had a total income equal to the bottom 42%. This concentration meant:
        1. The economy relied heavily on luxury spending by the wealthy
        2. Most Americans lacked purchasing power to sustain mass consumption
        3. When investment declined after the crash, there wasn't enough consumer spending to compensate
        
        **Global Economic Interconnections:**
        The international economic system was fragile after WWI:
        1. Germany relied on American loans to pay war reparations to Britain and France
        2. Britain and France relied on these reparations to repay war debts to the US
        3. When American lending collapsed after 1929, this entire structure unraveled
        
        **Agricultural Crisis and Banking Failures:**
        Agricultural prices had been declining throughout the 1920s. Rural banks, heavily invested in farm mortgages, were already vulnerable. When urban banks began failing after 1929, the contagion quickly spread to rural institutions, completing a cycle of economic decline.
        
        ## Step 3: Evaluating Relative Importance
        
        While all factors contributed, we can assess their relative significance:
        
        **Most Critical Structural Causes:**
        
        1. **Weak banking and financial regulation** - The absence of deposit insurance and weak regulation allowed banking panics to spread unchecked
        
        2. **Wealth and income inequality** - This limited the economy's resilience by constraining aggregate demand
        
        3. **International financial imbalances** - The unstable structure of war debts and the rigid gold standard limited policy responses
        
        **Secondary Amplifying Factors:**
        
        1. Stock market speculation and crash - This triggered the crisis but didn't independently cause the Depression's severity
        
        2. Federal Reserve policy mistakes - Contractionary monetary policy worsened the situation but didn't create the underlying vulnerabilities
        
        3. Dust Bowl and agricultural problems - These exacerbated rural suffering but were more consequence than cause
        
        ## Step 4: Immediate Triggers vs. Structural Causes
        
        **Immediate Triggers** (sparked the crisis):
        - Stock Market Crash (October 1929) - The most visible trigger
        - Banking Panics (1930-1933) - Created financial contagion
        - Federal Reserve tightening of monetary policy in 1928-1929
        
        **Underlying Structural Causes** (made depression possible and severe):
        - Unregulated banking system vulnerable to panics
        - Concentration of wealth and limited middle-class purchasing power
        - Fragile international financial system dependent on American capital
        - Gold standard constraints on monetary policy
        - Lack of automatic stabilizers or social safety nets
        
        The Great Depression wasn't simply bad luck or the result of a single policy mistake. It represented the collapse of an economic system with multiple structural vulnerabilities that had developed throughout the 1920s. The combination of these weaknesses created conditions where an economic downturn could cascade into a prolonged depression rather than a typical recession.
        
        The structural nature of these causes explains why recovery required fundamental reforms (banking regulations, social security, labor protections) rather than just traditional economic stimuli.
        """)
    
    st.markdown("""
    **Key Benefits:**
    
    1. **Causal Analysis:** Distinguishes between triggers and underlying causes
    2. **System Thinking:** Shows how different factors interacted and reinforced each other
    3. **Evaluative Framework:** Provides assessment of relative importance of different factors
    4. **Conceptual Organization:** Structures a complex historical topic logically
    """)
    
    # Example 5: Combining CoT with Few-Shot Prompting
    st.markdown("### Example 5: Combining Chain-of-Thought with Few-Shot Prompting")
    
    st.markdown("""
    This example demonstrates how to combine chain-of-thought prompting with few-shot prompting for even better results.
    """)
    
    st.markdown("""
    **Combined Chain-of-Thought and Few-Shot Prompt:**
    ```
    I want to create word problems for 5th-grade students that practice multi-step problem solving with fractions.
    For each problem, I'd like you to provide step-by-step solution guidance that I can use to help students who are stuck.
    
    Here's an example of what I'm looking for:
    
    Problem: Maya was making cookies for the school bake sale. The recipe called for 3/4 cup of flour for each batch.
    She decided to make 2 1/2 batches of cookies. How much flour did Maya need altogether?
    
    Step-by-step solution:
    
    Step 1: Identify what we need to find.
    We need to find the total amount of flour Maya needs for 2 1/2 batches.
    
    Step 2: Identify the relevant information.
    - Each batch requires 3/4 cup of flour
    - Maya is making 2 1/2 batches
    
    Step 3: Determine the operation needed.
    We need to multiply the amount of flour per batch (3/4 cup) by the number of batches (2 1/2).
    
    Step 4: Convert the mixed number to an improper fraction.
    2 1/2 = (2 × 2 + 1)/2 = 5/2
    
    Step 5: Multiply the fractions.
    (3/4) × (5/2) = (3 × 5)/(4 × 2) = 15/8
    
    Step 6: Convert to a mixed number.
    15/8 = 1 + 7/8 = 1 7/8
    
    Step 7: State the answer with units.
    Maya needs 1 7/8 cups of flour to make 2 1/2 batches of cookies.
    
    Please create 3 new word problems, each with step-by-step solution guidance following this same pattern.
    ```
    
    **Response Excerpt (First Problem):**
    
    ```
    Problem 1: Carlos is making a vegetable garden. He wants to plant carrots in 1/3 of the garden, tomatoes in 2/5 of the garden, and peppers in the remaining space. What fraction of the garden will be used for peppers?
    
    Step-by-step solution:
    
    Step 1: Identify what we need to find.
    We need to find what fraction of the garden will be used for peppers.
    
    Step 2: Identify the relevant information.
    - Carrots will be planted in 1/3 of the garden
    - Tomatoes will be planted in 2/5 of the garden
    - Peppers will be planted in the remaining space
    
    Step 3: Determine the operation needed.
    We need to add the fractions for carrots and tomatoes, then subtract that sum from 1 (the whole garden).
    
    Step 4: Find a common denominator for 1/3 and 2/5.
    The least common multiple of 3 and 5 is 15.
    1/3 = 5/15
    2/5 = 6/15
    
    Step 5: Add the fractions for the space used by carrots and tomatoes.
    5/15 + 6/15 = 11/15
    
    Step 6: Subtract from the whole to find the remaining space.
    1 - 11/15 = 15/15 - 11/15 = 4/15
    
    Step 7: State the answer with units.
    Carlos will use 4/15 of his garden for peppers.
    ```
    """)
    
    st.markdown("""
    **Benefits of Combining Techniques:**
    
    1. **Structured Pattern:** The few-shot example establishes a clear structure for the response
    2. **Reasoning Process:** The chain-of-thought approach ensures detailed reasoning is shown
    3. **Pedagogical Value:** The resulting problems are not just correct, but educational
    4. **Consistent Format:** Each problem follows the same step-by-step pattern, making them ideal for teaching
    
    This example shows how combining different prompting techniques can create highly effective educational resources
    that model both content knowledge and reasoning processes.
    """)
    
    # Example 6: Explanation of Misconceptions
    st.markdown("### Example 6: Addressing Common Misconceptions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Basic Prompt:**
        ```
        What are common misconceptions students have 
        about photosynthesis?
        ```
        
        **Response:** *(Summary)*
        
        A simple list of misconceptions about photosynthesis, including confusion about plants getting food from soil, not understanding the role of light, confusion about gas exchange, and misconceptions about when photosynthesis occurs.
        """)
        
    with col2:
        st.markdown("""
        **Chain-of-Thought Prompt:**
        ```
        Analyze common misconceptions students have about 
        photosynthesis. For each misconception:
        
        1. Identify the incorrect belief
        2. Explain why students might develop this misconception
        3. Clarify the scientific reality
        4. Suggest a teaching approach that could help address 
           this misconception
        
        Structure your response to walk through this analysis 
        for each major misconception.
        ```
        
        **Response:**
        
        # Analysis of Common Photosynthesis Misconceptions
        
        ## Misconception 1: Plants get their food from the soil
        
        **The incorrect belief:**
        Many students believe that plants absorb their food from the soil through their roots, similar to how animals consume food.
        
        **Why students develop this misconception:**
        This misconception likely develops because:
        1. Students observe plants growing in soil and see roots absorbing water and minerals
        2. We often talk about "feeding" plants when adding fertilizer to soil
        3. The actual process of making food (photosynthesis) is invisible
        4. Students overgeneralize from their own experience of consuming food rather than making it
        
        **The scientific reality:**
        Plants make their own food (glucose) through photosynthesis, which occurs primarily in the leaves. The raw materials are:
        - Carbon dioxide (from the air)
        - Water (absorbed through roots)
        - Light energy (captured by chlorophyll)
        
        The soil provides water and minerals (like nitrogen and phosphorus), which are essential for plant growth and health but are not the plant's "food." The actual food is the glucose created within the plant cells.
        
        **Teaching approach:**
        A demonstration that can help is growing plants hydroponically (in water without soil) to show that soil itself isn't necessary for food. Labeling activities where students identify the inputs and outputs of photosynthesis can also help, as can analogies comparing chloroplasts to tiny factories that build sugar molecules. Having students trace the source of mass in a growing tree can be revealing—most comes from the air (CO₂), not the soil.
        
        ## Misconception 2: Photosynthesis and respiration are opposite processes that don't occur simultaneously
        
        **The incorrect belief:**
        Students often think plants photosynthesize during the day and respire only at night, or that photosynthesis and respiration are mutually exclusive processes that "cancel each other out."
        
        **Why students develop this misconception:**
        This misconception arises because:
        1. Textbooks often present these processes as opposites (one produces oxygen, one consumes it)
        2. The processes are typically taught separately rather than as integrated parts of plant metabolism
        3. Students notice that gas exchange patterns differ between day and night
        4. The idea that opposing processes occur simultaneously is conceptually challenging
        
        **The scientific reality:**
        Plants respire continuously (day and night) in all living cells, using glucose and oxygen to release energy for cellular processes. Photosynthesis occurs only in cells with chloroplasts and only when light is available. During daylight hours, both processes occur simultaneously, with photosynthesis typically producing more oxygen than respiration consumes, resulting in net oxygen release.
        
        **Teaching approach:**
        Use real-time CO₂ or O₂ monitoring with plants in light and dark conditions to show that respiration continues even during photosynthesis. A Venn diagram comparing and contrasting the two processes while showing their interconnections can help. Creating analogies like "photosynthesis is like earning money, respiration is like spending it" can also clarify that both can happen simultaneously.
        
        ## Misconception 3: Leaves are green because they "attract" green light
        
        **The incorrect belief:**
        Students often think leaves appear green because they absorb or are attracted to green light.
        
        **Why students develop this misconception:**
        This misunderstanding stems from:
        1. Confusion about how color perception works
        2. Logical but incorrect reasoning that "green plants use green light"
        3. Limited understanding of light absorption and reflection
        4. Insufficient discussions of chlorophyll's absorption spectrum
        
        **The scientific reality:**
        Leaves appear green because chlorophyll absorbs primarily blue and red wavelengths of light while reflecting green wavelengths. The reflected green light is what we see, making the leaves appear green. Ironically, green is the least used color of the visible spectrum for photosynthesis.
        
        **Teaching approach:**
        Classroom demonstrations with prisms or colored filters can help students understand light absorption. Having students grow plants under different colored lights can show which light colors support photosynthesis best. Spectroscopy labs or simulations that show chlorophyll's absorption spectrum make the concept more concrete. Analogies comparing light to a buffet where plants "eat" the red and blue "food" but "leave" the green can make the concept more accessible.
        
        ## Misconception 4: Carbon dioxide is only used to produce oxygen
        
        **The incorrect belief:**
        Many students think carbon dioxide's only role in photosynthesis is to be converted into oxygen.
        
        **Why students develop this misconception:**
        This misconception develops because:
        1. The oxygen-producing aspect of photosynthesis is frequently emphasized
        2. The simplified equation for photosynthesis is often memorized without understanding
        3. The carbon cycle is frequently taught separately from photosynthesis
        4. The connection between gaseous CO₂ and solid plant matter isn't intuitive
        
        **The scientific reality:**
        The primary purpose of photosynthesis isn't to produce oxygen but to produce glucose for the plant. Carbon from CO₂ becomes incorporated into the glucose molecules that form the plant's structures and energy storage. Oxygen is actually a byproduct of the process, released when water molecules are split during the light-dependent reactions.
        
        **Teaching approach:**
        Have students trace carbon atoms through the photosynthesis process using models or diagrams. Conducting investigations where plants grow in sealed environments can demonstrate mass increase despite limited soil. Historical context about experiments by van Helmont and others who discovered where plant mass comes from can provide perspective. Asking students, "Where does the mass of a tree trunk come from?" can reveal and address this misconception directly.
        """)
    
    st.markdown("""
    **Key Benefits:**
    
    1. **Deeper Analysis:** Goes beyond identifying misconceptions to explain their origins
    2. **Pedagogical Focus:** Includes specific teaching strategies to address each misconception
    3. **Conceptual Clarity:** Provides clear explanations of the correct scientific understanding
    4. **Structured Approach:** Organizes information in a way that's immediately useful for teachers
    """)
    
    # Key takeaways from examples
    st.markdown("## Key Insights from Chain-of-Thought Examples")
    
    st.markdown("""
    From these examples, we can identify several important patterns for effective chain-of-thought prompting:
    
    1. **Explicit Process Instructions**: Always explicitly ask for step-by-step thinking or reasoning
    
    2. **Structured Analysis**: Request specific analytical steps appropriate to the subject matter
    
    3. **Question Customization**: Tailor the thinking process to the type of problem (math vs. literature)
    
    4. **Enhanced Educational Value**: Emphasize the learning value of seeing the process, not just the answer
    
    5. **Verification Opportunity**: Use the exposed reasoning to check the quality of the response
    
    6. **Combining with Other Techniques**: Chain-of-thought works well with few-shot prompting
    """)
    
    # Mark this page as completed when viewed
    mark_page_completed(current_page)
    
    # Add horizontal bottom navigator
    st.markdown("---")
    render_bottom_navigator(PAGE_INFO)
    
    # Teacher-specific guidance
    render_teacher_notes("""
    **Key Points to Emphasize:**
    
    * Chain-of-thought prompting is particularly valuable when the reasoning process itself is educational
    * This approach helps create materials that model metacognitive strategies for students
    * The technique works across subject areas but needs to be customized for each discipline
    * For math and science, emphasize quantitative reasoning steps
    * For humanities, emphasize analytical frameworks and evidence-based reasoning
    
    **Discussion Questions:**
    
    * How could you use chain-of-thought prompting to create worked examples for difficult concepts?
    * What kinds of thinking processes do you want to model for your students?
    * How might this technique help identify misconceptions in student understanding?
    * How could you adapt these examples for your specific grade level or subject area?
    
    **Extension Idea:**
    
    Have participants select a complex concept from their curriculum and draft a chain-of-thought prompt
    that would help create step-by-step explanations tailored to their students' needs.
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