import random
# import the chatterbot package
# This is the chatbot engine we will use
from chatterbot import ChatBot
# Give our chatbot a name
chatbot = ChatBot("Iron Man")
# Packages used to Train your chatbot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
# Add a new personality about Mars here
# Just using a python list
# Format should be question from the user and the response from chatbot
personality_IronMan = [
    "Ironman!",
    "Hey kid, don't have time to talk right now. Here's an autograph.",
    "Hello",
    "What's up kid, kinda doing avengers stuff right now.",
    "Sorry",
    "No need to be sorry, well now I feel bad...",
    "What do you do?",
    "Im an avenger. You know 'Earths Mightiest Heros'.",
    "Who are you?",
    "Well, i'm Ironman. Or Tony Stark, whichever you know best. Probably Ironman.",
    "I dont like Captain America",
    "Yeah im not too big of a fan either.",
    "What do you think about the other avengers?",
    "That is a loaded question.",
    "What is your favorite food?",
    "Shawarma, definitly shawarma.",
    "What is your best weapon?",
    "The arc reactor, obviously. Who doesn't love big lasers?",
    "Who are you dating?",
    "Her name is Pepper Pots, kinda a pain sometimes. Who am I kidding I'm lucky to have her.",
    "Can I have one of your suits?",
    "Uh, no. They aren't for kids sweetheart.",
    "Can you help me.",
    "Sure kid let me just stop all of the avengers ",
    "How do you use the bathroom?",
    "Well, you could say I thought of everything.",
    "Hi",
    "uh, hi kid.",
    "Whats up",
    "Nothing much, just saving the world.",
    "Do you remember your dad?",
    "Yeah, I just wish I could ask him some more questions.",
    "What is JARVIS",
    "JARVIS is an AI that helps with my daily life.",   
]
# Set the trainers we want train
trainer_personality_IronMan=ListTrainer(chatbot)
trainer = ChatterBotCorpusTrainer(chatbot)
# Now here we actually train our chatbot on the corpus
# This is what gives our chatbot its personality 
# Train the personality you want to override should come first
# Standard personality chatterbot comes with
trainer.train('chatterbot.corpus.english')
trainer_personality_IronMan.train(personality_IronMan)
''' ******************* GUI Below Engine Above **************** '''
# Function that randomizes a random Iron Man quote
def random_quote(rQuote):
    quotes = [
    "Stark Tower is about to become a beacon of self sustaining clean energy.",
    "Grow a spine, J.A.R.V.I.S.. I got a date.",
    "You have reached the life model decoy of Tony Stark. Please leave a message.",
    "Yeah, apparently I'm volatile, self-obsessed, don't play well with others.",
    "Genius, billionaire, playboy philanthropist.",
    "Thanks buddy.",
    "You're not the director of me.",
    "Artificial intelligence. You never even hesitated.",
    "Right, so, if I lift it, I then rule Asgard?",
    "Like a computer. I believe I'm ciphering code."
    ]
    random.shuffle(quotes)
    rQuote = quotes[0]
    return rQuote
# Import for the GUI 
from chatbot_gui import ChatbotGUI
# create the chatbot app
"""
    Options
    - title: App window title.
    - gif_path: File Path to the ChatBot gif.
    - show_timestamps: If the chat has time-stamps.
    - default_voice_options: The voice options provided to the text-to-speech 
engine by default if not specified
                             when calling the send_ai_message() function.
"""
app = ChatbotGUI(
    title="Iron Man AI - Created by Chris Tomaskovic and Brendan Carlson",
    gif_path="IronMan.gif",
    show_timestamps=True,
    default_voice_options={
        "rate": 100,
        "volume": 0.8,
        "voice": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    }
)

# define the function that handles incoming user messages
@app.event
def on_message(chat: ChatbotGUI, text: str):
    """
    This is where you can add chat bot functionality!
    You can use chat.send_ai_message(text, callback, voice_options) to send a 
message as the AI.
        params:
            - text: the text you want the bot to say
            - callback: a function which will be executed when the AI is done 
talking
            - voice_options: a dictionary where you can provide options for the 
AI's speaking voice
                default: {
                   "rate": 100,
                   "volume": 0.8,
                   "voice": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\
Tokens\TTS_MS_EN-US_ZIRA_11.0"
                }
    You can use chat.start_gif() and chat.stop_gif() to start and stop the gif.
    You can use chat.clear() to clear the user and AI chat boxes.
    You can use chat.process_and_send_ai_message to offload chatbot processing to a
thread to prevent the GUI from
    freezing up.
        params:
            - ai_response_generator: A function which takes a string as it's input 
(user message) and responds with
                                     a string (AI's response).
            - text: The text that the ai is responding to.
            - callback: a function which will be executed when the AI is done 
talking
            - voice_options: a dictionary where you can provide options for the 
AI's speaking voice
                default: {
                   "rate": 100,
                   "volume": 0.8,
                   "voice": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\
Tokens\TTS_MS_EN-US_ZIRA_11.0"
                }
    :param chat: The chat box object.
    :param text: Text the user has entered.
    :return:
    """
    # this is where you can add chat bot functionality!
    # text is the text the user has entered into the chat
    # you can use chat.send_ai_message("some text") to send a message as the AI, 
    # this will do background
    # you can use chat.start_gif() and chat.stop_gif() to start and stop the gif
    # you can use chat.clear() to clear the user and AI chat boxes
    # print the text the user entered to console
    print("User Entered Message: " + text)             
    
    ''' Here you can intercept the user input and override the bot
    output with your own responses and commands.'''
    # if the user send the "clear" message clear the chats
    if text.lower().find("erase chat") != -1:
        chat.clear()
    # user can say any form of bye to close the chat.
    elif text.lower().find("bye") != -1:
        # define a callback which will close the application
        def close():
            chat.exit()
        # send the goodbye message and provide the close function as a callback
        chat.send_ai_message("It has been good talking with you. Have a great day! Later!", callback=close)
    elif text.lower().find("quote") != -1:
        chat.start_gif()
        chat.process_and_send_ai_message(random_quote, text)
    else:
        # offload chat bot processing to a worker thread and also send the result 
        #as an ai message
        chat.start_gif()
        chat.process_and_send_ai_message(chatbot.get_response, text)
        chat.__send_ai_message(text)
# run the chat bot application
app.run()