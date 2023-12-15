def  LLM(list_of_herbs):
    # Install python-dotenv, openai=0.28 only
    from dotenv import load_dotenv
    import os
    import openai

    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')

    context_for_gpt = 'Convert the list of medicines such that it sound like a doctor giving diagnosis'
    messages = [
        {'role':'system', 'content' :context_for_gpt}
    ]    

    # To answer based on previous conversation
    messages.append({'role' : "user", 'content':list_of_herbs})

    completion = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = messages
    )
    chat_response = completion.choices[0].message.content
    return chat_response
    # messages.append({'role':'assistant', 'content':chat_response})

print(LLM(list_of_herbs='Godnati bhasma, Chandrakala rasa, Kamadugha rasa (mouktika yukta), Bhoonimbadi khada, Shirashooladi vajra rasa, Pathyadi khada are used in the treatment.'))