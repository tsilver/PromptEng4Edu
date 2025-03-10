import requests
import json
import streamlit as st

class TeacherClient:
    """Client for interacting with AI/LLM services."""
    
    def __init__(self):
        """Initialize the TeacherClient."""
        # For demo purposes, we'll simulate responses
        # In a real implementation, this would connect to an API
        self.demo_mode = True
    
    def send_prompt(self, prompt_text):
        """
        Send a prompt to the AI service and get a response.
        
        Args:
            prompt_text (str): The prompt text to send
            
        Returns:
            dict: Response from the AI service
        """
        if self.demo_mode:
            # Simulate an AI response for demo purposes
            return self._simulate_response(prompt_text)
        
        # In a real implementation, this would call an API
        # response = requests.post(
        #     "https://api.example.com/v1/generate",
        #     json={"prompt": prompt_text},
        #     headers={"Authorization": "Bearer YOUR_API_KEY"}
        # )
        # return response.json()
    
    def _simulate_response(self, prompt_text):
        """Simulate an AI response for demo purposes."""
        # This is a very simple simulation for demonstration
        # In a real implementation, this would be replaced with actual API calls
        
        if "restaurant" in prompt_text.lower():
            return {
                "response": """
                Here are some highly rated Italian restaurants near Times Square that are family-friendly and open late:

                1. **Carmine's Italian Restaurant**
                   - Address: 200 W 44th St, New York, NY 10036
                   - Review: A family-style restaurant with large portions perfect for sharing. Known for their homestyle Italian dishes and lively atmosphere. Open until midnight on weekdays and 1 AM on weekends.

                2. **Tony's Di Napoli**
                   - Address: 147 W 43rd St, New York, NY 10036
                   - Review: Another family-style option with generous portions. Their classic Italian dishes are crowd-pleasers, and they're accommodating to families with children. Open until 11 PM most nights.

                3. **Becco**
                   - Address: 355 W 46th St, New York, NY 10036
                   - Review: Slightly more upscale but still family-friendly, known for their pasta tasting menu. A short walk from Times Square in the Theater District. Open until 11:30 PM on weekdays and midnight on weekends.
                """
            }
        elif "inception" in prompt_text.lower():
            return {
                "response": """
                Dom Cobb (Leonardo DiCaprio) is a skilled thief who specializes in extracting secrets from people's dreams. He's offered a chance to have his criminal history erased in exchange for planting an idea in someone's mind, a process called "inception." Cobb assembles a team to help him navigate the complex layers of dreams within dreams. The central concept involves entering deeper levels of the subconscious, where time moves more slowly and reality becomes increasingly distorted. As they venture deeper into the target's mind, Cobb struggles with projections of his dead wife and his own guilt. The team must navigate each dream layer and plant the idea while escaping from hostile projections, all while maintaining their grip on what's real and what's a dream.
                """
            }
        elif "water cycle" in prompt_text.lower():
            return {
                "response": """
                The water cycle is how water moves around our Earth. First, the sun heats up water in oceans, lakes, and rivers, turning it into a gas called water vapor. This is called evaporation. The water vapor goes up into the air and cools down, forming clouds. This is called condensation. When the clouds get heavy with water, it falls back down as rain, snow, or hail. This is called precipitation. The water then flows through rivers back to the oceans, or soaks into the ground to become groundwater. Plants also help by releasing water vapor from their leaves. This whole cycle keeps repeating, giving us fresh water to drink and use every day!
                """
            }
        elif "romeo and juliet" in prompt_text.lower():
            return {
                "response": """
                1. How does the feud between the Montagues and Capulets shape Romeo and Juliet's perception of love? Is their love strengthened or compromised by this conflict?

                2. In what ways do both Romeo and Juliet rebel against fate? Are they ultimately successful, or does fate prevail?

                3. Compare the parent-child relationships in the play. How do these family dynamics contribute to the tragic outcome?

                4. How do the characters of Mercutio and the Nurse provide contrasting perspectives on love compared to Romeo and Juliet?

                5. The play begins with a prologue that reveals the ending. How does Shakespeare use dramatic irony throughout the play to create tension around the theme of fate?
                """
            }
        else:
            return {
                "response": "I've processed your prompt and here is a thoughtful response based on what you asked. To get more specific responses, try using more detailed prompts with clear tasks, context, and desired formats."
            }
