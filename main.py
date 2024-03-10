import streamlit as st
import openai
import os
from dotenv import load_dotenv


load_dotenv()

  # Replace with your OpenAI API key
client = openai.OpenAI(api_key=os.getenv('API_KEY'))

paypal_button_html = """
<form action="https://www.paypal.com/donate" method="post" target="_top">
<input type="hidden" name="business" value="GPLLUAHVF8E4W" />
<input type="hidden" name="no_recurring" value="0" />
<input type="hidden" name="item_name" value="If you are interested in donating to this page for upkeep of openai costs, it would be appreciated! " />
<input type="hidden" name="currency_code" value="USD" />
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
<img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1" />
</form>
"""
def generate_description(prompt):
    with st.spinner('Loading...'):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"""You are a helpful assistant for the card game Perfect Draw. You know that in Perfect Draw!, players have a deck made of cards. 
                    These cards come in various types like Warrior Cards and Items. Warrior Cards act as continuous forces on the board, able to attack your enemies and defend you against oncoming threats within the game. They have a “Strength” which can be Weak Normal and Strong. 
                    Items are similar to Warriors, but cannot attack, and can’t defeat an opposing warrior when they Decide the Outcome of a Clash. Please return everything in beautiful markdown format
                    Invocations are cards that don’t create permanent fixtures onto the
                    battlefield. They don’t have a strength rating, and they go to the
                    graveyard immediately upon being played.
                    When you cast an invocation, you may forgo your ability to play a staple
                    this turn to play the invocation in addition to another card. This allows
                    you to play one card of any kind (Warrior, Item, Invocation) alongside that
                    invocation, rather than one card and one staple. You may only do this as
                    many times as you can play a staple this turn (usually only once).
                    Invocations often represent an action being undertaken or a spell being
                    cast, but can represent many things, such as an event or the presence of
                    something supernatural. In the game, there are many different types of
                    texts that can be found on the cards that are keywords. 
                    Keywords are special abilities that can be found on cards.
                    Here are some examples of keywords:
                    - Overwork: When you play a card from your hand
                    with  Overwork, you cannot play a card
                    from your hand as part of your actions
                    next turn.
                    - Overwhelm:  When a warrior or item with
                    would Decide the Outcome of a Clash, it
                    always wins.                   
                    - Piercer: When a warrior with Piercer [ x ] would 
                    defeats another warrior or item in battle,
                    it deals [x] damage to that warrior’s
                    controller.
                    - Teamwork: When a warrior with Teamwork attacks,
                    it can attack alongside any number of other warriors that also
                    have Teamwork. If two weak warriors with Teamwork attack attack as if they were a single normal warrior.
                    - Sniper: When a warrior with Sniper attacks, it deals [ x ] extra damage to the opposing player.
                    - Blocker: When a warrior or item is attached to a warrior or item with Blocker, they can intercept attacks that would be directed at the warrior to themselves.
                    - Inconspicuous: When a warrior with Inconspicuous attacks, it cannot be targeted by the opposing player. (Unless it is the only warrior on the battlefield.)
                    - Underwhelm: When a warrior or item with Underwhelm would Decide the Outcome of a Clash, it always loses.
                    - Follow-up: When you play a card with Follow-up, you may play another card with Follow-up from your hand for free.
                    - Pressure: [ x ] While a card with Pressure [ x ] is on the battlefield, you roll with an addition + [ x ]  to your dice rolls for the turn. 
                    - Fumble: When you fumble an opponent describe a specific action they could take, a type of card they could play, or a kind of game action they could take
                    Once between now and your next turn, NPCs may use a response move without spending advantage or using their limited response moves.
                    
                    """
                    
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
    return response.choices[0].message.content

def generate_npc(npc_type):
      # Generates an NPC description using OpenAI
      prompts = {
          "npc_description": f"Describe a {npc_type} NPC. Include their appearance, personality, and a short backstory for the character. The world is related to card games.",
          "deck-gimmick": f"Describe a {npc_type} NPC's deck gimmick. This should be a unique mechanic or theme that the deck is built around. Examples: A deck that focuses on a specific keyword, a deck that focuses on a specific type of warrior, or a deck that focuses on a specific type of item.",
          "power_moves": f"""Generate a 2-4 of Power Card Moves for a {npc_type} NPC in a card game. These moves should be based on the following rules: 1. Protect Your Game Plan: Play a Normal warrior, Normal item, or Invocation that protects the deck’s gameplan, such as by making it harder to remove a key game piece, or harder for the player to perform a disruptive action. Examples: Giving a warrior you control Inconspicuous or Blocker, creating a small number of Weak warriors to sit in the way, or anything else that may protect against the player’s ability to win the game. Use a Simple Card Move.
                2. Create a New Threat: Play a Normal warrior with 1-2 features that makes it a threat to the player, such as: It is actually a Strong warrior, it can attack directly, it has some amount of Piercer or Sniper, or anything else that may make it an immediate threat. Use 1 Simple Card Move if you selected 2 features. Use 2 Simple Card Moves if you selected only 1 feature.
                3. Create an Advantage: Play a Normal warrior, or a Strong Item with some form of protection that creates an advantage for you in some minor but useful way, such as: Giving a warrior you control a useful keyword once per turn, creating a Weak warrior once per turn, or something else that may become difficult to deal with over time. Use a Simple Card Move.
                4. Remove the Immediate Problems: Play an Invocation that deals with one or more problems the player has created, removing those warriors/items/effects from the battlefield or immediate gameplay. Use two Simple Card Moves if the player still has a significant threat. Use one Simple Card Moves if the player does not have a significant threat, but still has some amount of resources. Otherwise, use no Simple Card Moves.
                5. Disrupt the Players’ Plans: Play a Normal warrior or Normal item that disrupts the players’ plans and gives them a disadvantage of some kind, such as: Giving a warrior Underwhelm each turn, weakening the player’s main gameplan, or anything else that makes the players life somewhat more difficult. Use a Simple Card Move.
                6. Dawdle: Use a Simple Card Move up to 4 times. If you have no Simple Card.""",
          "simple_moves": f"""Can you just pick 3 of these simple moves based on {npc_type} These moves should be based on the following rules: 
          1. Create a Weak warrior with Blocker.
          2. Strengthen a warrior you control until the end of turn.
          3. Create a Normal warrior.
          4. Sacrifice a warrior you control to destroy a warrior your opponent controls with less or equal strength.
          5. Target warrior your opponent controls loses all text until the start of your next turn.
          6. Give a warrior or item your opponent controls Underwhelm.
          7. Gain 1 Life.
          8. Play an invocation that produces a minor benefit based on your gimmick/plan to win.""",
      }
      return {key: generate_description(value) for key, value in prompts.items()}
  
def print_markdown(npc):
      for key, value in npc.items():
          st.subheader(key.replace("_", " ").title(), divider="rainbow")
          st.markdown(value)
  
st.title(":rainbow[Perfect Draw Npc Generator] :crystal_ball:")

st.write("This app generates a description for a non-player character (NPC) in the world of Perfect Draw, a TTRPG game. The description includes the NPC's appearance, personality, and a short backstory. It also generates a deck gimmick, power card moves, and simple card moves for the NPC.")
st.write("Generated text is in markdown format, so it can be easily copied and pasted into a markdown file. :smile:")
st.write("The generation time takes around 5-10 seconds :sunglasses: . Please be patient.")
st.write("Any feedback is welcome! Feel free to reach out to me on discord: @adamkostandy (I am on the Perfect Draw server)")
st.write("If you are interested in donating to this page for upkeep of openai costs, it would be appreciated! ")
st.markdown(paypal_button_html, unsafe_allow_html=True)
# Textbox for user input
npc_type = st.text_input("Enter a type of NPC (e.g., shopkeeper, mage, psychotic):")
  
  # Generate button
if st.button("Generate NPC"):
      npc = generate_npc(npc_type)
      print_markdown(npc)
      