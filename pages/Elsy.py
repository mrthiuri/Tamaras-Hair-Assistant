import re
from autocorrect import Speller
spell = Speller(lang='en')
import streamlit as st

intents = {
    'greeting': ["hello","hi","morning","afternoon","evening"],
    'identification': ["who are you"],
    'farewell': ["goodbye",'goodnight','sleep','bye'],
    'business': ["tamara's",'do','business'],
    'procedure': ['how does it work','recommend'],
    'product inquiry': ['haircare','products','shampoo','conditioner','detanglers','oils','mousse'],
    'product details': ['do','help with','sell','catalogue','contents','chemicals','recommendation'],
    'bookings': ['visit','order','pruchase','buy','treatment'],
    'hours': ['when','open'],
    'location': ['where','visit','see','come','go','shop','store'],
    'contact': ['talk','message','reach','communicate','speak'],
    'price': ['cost','price','how much','pay']
}


responses = {
    'greeting': "Hi, I'm Elsy 🤖. Welcome to Tamara's Hair! What can I help you with today? 😊",

    'identification': "I'm Elsy 🤖, your virtual assistant at Tamara's Hair. How can I assist you today? 😊",

    'farewell': "Goodbye! You're always welcome back to Tamara's Hair — your one-stop shop for all your haircare needs. ✨",

    'business': "Tamara’s Hair is a premium haircare brand specializing in products and services tailored for African hair, with a special focus on Black women’s hair needs. We’re located at Moi Avenue, Kilele Mall, Nairobi. Our range includes high-quality shampoos, conditioners, detanglers, scalp oils, and hair mousses. What makes Tamara’s Hair unique is our personalized product recommendation service, where clients undergo simple hair tests to determine the best products for their unique hair type. We’re dedicated to celebrating and nurturing natural hair textures, providing solutions that moisturize, strengthen, and enhance the beauty of African hair.",

    'procedure': "Our specialists conduct simple hair tests to assess your hair type and condition, helping us recommend the best products for you. We’re committed to offering top-tier care for Black hair.",

    'product inquiry': "We offer a curated selection of high-quality haircare products including shampoos, conditioners, detanglers, scalp oils, and hair mousses — all specially formulated for African hair.",

    'product details': "For detailed information about our products and services, please visit us at Moi Avenue, Kilele Mall. Our team will be happy to assist you in person!",

    'bookings': "We provide countrywide delivery for existing customers who've previously visited us for hair tests. New customers are encouraged to visit our store at Moi Avenue, Kilele Mall. We'd love for everyone to experience what Tamara's Hair has to offer.",

    'location': "You'll find us at Moi Avenue, Kilele Mall, Shop B3, Nairobi. We look forward to welcoming you soon! 😊",

    'contact': "You can reach us on +254 000 276512 or connect via our social media pages. We’re always happy to hear from you!",

    'price': "At Tamara’s Hair, we believe quality haircare should be accessible to all. For pricing details, please visit our store along Moi Avenue, Kilele Mall, and start your transformational hair journey with us. 🌞",

    'hours': "We are open from Monday - Friday 8.00 a.m to 6.00 p.m and on Saturdays from 9.00 a.m to 5.00 p.m."
}

def pre_process_text(text):
    """
    Checks for typos and removes any special chatcters
    Params:
        - text(str): user input
    Returns:
        - clean_text(str): transformed and corrected user input
    """
    no_typos = " ".join([spell(word) for word in text.split()])
    clean_text = re.sub(r'[^a-z ]',"",no_typos.lower())
    return clean_text

def match_intent(clean_input):
    """
    Determines user intent and appropriate response
    Params:
        - clean_input(str): pre-processed user input
    Returns:
        - intent"""
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in clean_input:
                return intent
    return None

st.title("💇🏾‍♀️Elsy- Your Haircare AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = [{'role': 'assistant', 'content': responses['greeting']}]

for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])


if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": responses["greeting"]}]

# Display past chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("What would you like to know about our services..."):
    # Append user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Process input
    clean = pre_process_text(prompt)
    intent = match_intent(clean)

    if intent:
        reply = responses[intent]
    else:
        reply = "I'm sorry, I didn’t quite get that 😔 Could you rephrase?"

    # Append assistant response
    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
