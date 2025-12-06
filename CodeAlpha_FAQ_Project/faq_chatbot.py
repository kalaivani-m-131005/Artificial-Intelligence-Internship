# --- START OF faq_chatbot.py CODE (Task 2) ---

# 1. Collect FAQs (questions and their answers)
# This dictionary serves as your knowledge base.
faq_data = {
    "What is the internship duration?": "The internship duration is one month, as specified in the instructions.",
    "How can I submit my task?": "Submissions are made through the specified resource/WhatsApp group, as mentioned in the instructions.",
    "Who is CodeAlpha?": "CodeAlpha is a leading software development company focused on AI and emerging technologies.",
    "Do I get a certificate?": "Yes, upon successful completion, you will receive a Completion Certificate (CR Verified).",
    "What is the deadline for this task?": "Please refer to the submission details section in your official document for the exact deadline."
}

def get_answer(user_query):
    """
    Matches the user's query to the best FAQ question based on shared keywords.
    """
    user_query = user_query.lower()
    best_match_q = None
    max_keywords_matched = 0

    # Split the user query into keywords (ignore very short words)
    keywords = [word for word in user_query.split() if len(word) > 2] 

    # 2. Match user questions with the most similar FAQ
    for faq_question, answer in faq_data.items():
        faq_question_lower = faq_question.lower()
        
        # Count how many of the user's keywords appear in the FAQ question
        keywords_matched = sum(1 for keyword in keywords if keyword in faq_question_lower)
        
        if keywords_matched > max_keywords_matched:
            max_keywords_matched = keywords_matched
            best_match_q = faq_question

    # 3. Display the best matching answer
    if max_keywords_matched > 0:
        print("\n🤖 AI Assistant Response:")
        print(f"I found a close match: **{best_match_q}**")
        print(f"Answer: {faq_data[best_match_q]}")
        
    else:
        # If no match is found
        print("\n🤖 AI Assistant Response:")
        print("I'm sorry, I couldn't find a direct answer. Can you try rephrasing your question?")


# --- Main program loop to run the chatbot ---
print("--- FAQ Chatbot Initialized (Task 2) ---")
print("Ask a question about the internship (e.g., 'Do I get a certificate?'). Type 'exit' to quit.")

while True:
    try:
        user_input = input("\n👤 Your Question: ")
        if user_input.lower() == 'exit':
            print("Chatbot closing. Goodbye!")
            break
        get_answer(user_input)
    except Exception as e:
        print(f"An error occurred: {e}")

# --- END OF faq_chatbot.py CODE ---