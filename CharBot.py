import openai
import streamlit as st
from streamlit_chat import message
from config import *

st.write("""
# This is a personal AI-powered app created for Charlene *Lee* :sunglasses:! 
""")



openai.api_key = api_key

st.image("/Users/charlottegao/Downloads/pictures/download.jpeg", width=80)
st.title("Charlene Lee's ChatBot AKA CharBot")
        

# Initialize the session state
if 'unpolished' not in st.session_state:
    st.session_state['unpolished'] = []
if 'polished' not in st.session_state:
    st.session_state['polished'] = []
if 'polishing' not in st.session_state:
    st.session_state['polishing'] = []

# Get the user input   
user_input_polish = st.text_input("Hi Charlene, I'm your personal assistant CharBot, l can help make your English more native. Please enter your message.", key="user_polish")

def polish_message(user_input_polish):
    # Append the user's Polish input to the prompt
    prompt = 'Can you make the following message more native?\n  ' + user_input_polish
    
    # Generate a polished English message using the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=500
    )

    # Extract the polished English message from the API response
    output_english = response.choices[0].text.strip()
    return output_english

def display_polished():
    if user_input_polish:
        # Call the polish_message() function with the user's Polish input
        output_english = polish_message(user_input_polish)
        # Store the user input and generated response
        st.session_state['unpolished'].append(user_input_polish)
        st.session_state['polished'].append(output_english)
        st.session_state['polishing'].append({"role": "assistant", "content": output_english})
        # Clear the user input field
        st.session_state['user_polish'] = ""

# Create a "Polish" button that calls the display_polished() function on click
display_polished_button = st.button("Polish", on_click=display_polished)

if st.session_state['polished']:
    # Display each message and response in reverse order
    for i in range(len(st.session_state['polished'])-1, -1, -1):
        tab1, tab2 = st.tabs(['User Input', 'Polished Version'])
        with tab1:
            st.write(f"Bot: {st.session_state['polished'][i]}")
            # st.write(f"Bot: {st.session_state['generated'][i]}")
        with tab2:
            st.write(f"You: {st.session_state['unpolished'][i]}")
            
            
#------------------------------------------------------------------translation
if 'prompts' not in st.session_state:
    st.session_state['prompts'] = []
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
    
    
# Get the user input
chinese_text = st.text_input("l can also help you translate Chinese into English, please enter your Chinese text.", key="user_chinese")

def translate_chinese_to_english(chinese_text):
    # Define the prompt for translation
    prompt = "Please translate the following Chinese text to English:\n" + chinese_text
        # + "\n\nEnglish translation:"

    # Generate the translation using the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=500,
    )

    # Extract the translated text from the API response
    english_text = response.choices[0].text.strip()
    
    return english_text


# Define a function to handle the translation
def translate():
    if chinese_text:
        # Call the translate_chinese_to_english() function with the user's Chinese input
        english_text = translate_chinese_to_english(chinese_text)
        # Store the user input and generated response
        st.session_state['past'].append(chinese_text)
        st.session_state['generated'].append(english_text)
        # Clear the user input field
        st.session_state['user_chinese'] = ""

# Create a "Translate" button that calls the translate() function on click
translate_button = st.button("Translate Chinese", on_click=translate)

if st.session_state['generated']:
    # Display each message and response in reverse order
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        tab1, tab2 = st.tabs(['Chinese Input', 'English Translation'])
        with tab1:
            st.write(f"Bot: {st.session_state['generated'][i]}")
        with tab2:
            st.write(f"You: {st.session_state['past'][i]}")

            
            
            
            
            
#-----------------------------------------------------translate English to Chinese
if 'translating' not in st.session_state:
    st.session_state['translating'] = []
if 'Chinese_ouput' not in st.session_state:
    st.session_state['Chinese_ouput'] = []
if 'English_input' not in st.session_state:
    st.session_state['English_input'] = []

# Get the user input
english_text = st.text_input("I can also help you translate English into Chinese, please enter your English text.", key="user_english")

def translate_english_to_chinese(english_text):
    # Define the prompt for translation
    prompt = "请把以下英文翻译成中文：\n" + english_text

    # Generate the translation using the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=500,
    )

    # Extract the translated text from the API response
    chinese_text = response.choices[0].text.strip()

    return chinese_text

# Define a function to handle the translation
def translate():
    if english_text:
        # Call the translate_english_to_chinese() function with the user's English input
        chinese_text = translate_english_to_chinese(english_text)
        # Store the user input and generated response
        st.session_state['English_input'].append(english_text)
        st.session_state['Chinese_ouput'].append(chinese_text)
        # Clear the user input field
        st.session_state['user_english'] = ""

# Create a "Translate" button that calls the translate() function on click
translate_button_2 = st.button("Translate English", on_click=translate)

if st.session_state['Chinese_ouput']:
    # Display each message and response in reverse order
    for i in range(len(st.session_state['Chinese_ouput'])-1, -1, -1):
        tab1, tab2 = st.tabs(['English Input', 'Chinese Translation'])
        with tab1:
            st.write(f"You: {st.session_state['Chinese_ouput'][i]}")
        with tab2:
            st.write(f"Bot: {st.session_state['English_input'][i]}")

            
            
#----------------------------------------------------chatbot           

def greet():
    return "You can ask me any question!"

# Display the greeting message
st.write(greet())


if 'chatting' not in st.session_state:
    st.session_state['chatting'] = []
if 'answer' not in st.session_state:
    st.session_state['answer'] = []
if 'question' not in st.session_state:
    st.session_state['question'] = []

def generate_response(chat_input):
    prompt = "You're an incredibly helpful assistant. Please respond concisely, and if you can manage to slip in a little humor, all the better!\n" + chat_input
    response=openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=500,
    )
    
    message=response.choices[0].text.strip()
    return message
            
            

def end_click():
    # st.session_state['chatting'] = [{"role": "system", "content": "You're an incredibly helpful assistant. Please respond concisely, and if you can manage to slip in a little humor, all the better!"}]
    st.session_state['question'] = []
    st.session_state['answer'] = []
    st.session_state['user_chat'] = ""

def chat_click():
    if st.session_state['user_chat']!= '':
        chat_input = st.session_state['user_chat']
        output=generate_response(chat_input)
        #store the output
        st.session_state['question'].append(chat_input)
        st.session_state['answer'].append(output)
        st.session_state['chatting'].append({"role": "assistant", "content": output})
        st.session_state['user_chat'] = ""
        
# user_input=st.text_input("Type a message and press Enter to send", key="user_chat")

message("Hello, how can I help you?", is_user=False, avatar_style="fun-emoji")

user_input=st.text_input("Charlene:", key="user_chat")

chat_button=st.button("Send", on_click=chat_click)
end_button=st.button("New Chat", on_click=end_click)

if st.session_state['answer']:
    for i in range(len(st.session_state['answer'])-1, -1, -1):
        tab1, tab2 = st.tabs(["Answer", "Questions"])
        with tab1:
            message(st.session_state['answer'][i], is_user=False, key=str(i),avatar_style="fun-emoji")
            # st.write(f"Bot: {st.session_state['answer'][i]}")
        with tab2:
            # st.markdown(st.session_state['answer'][i])
            message(st.session_state['question'][i], is_user=True, key=str(i) + '_user',avatar_style="adventurer")
            # st.write(f"Charlene: {st.session_state['question'][i]}")
