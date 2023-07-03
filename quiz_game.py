# A program that sends a quiz via SMS


''' ----------------- PART I ----------------- '''

# function that returns a message, using Twilio credentials
def send_sms(account_sid:str, auth_token:str, to_phone_number, from_phone_number, message:str):

    from twilio.rest import Client

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to = to_phone_number,
        from_ = from_phone_number,
        body = message
    )

    return message


''' ----------------- PART II ----------------- '''

# creating a Question class
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# list of questions/prompts and subsequent answers
question_prompts = [
    'What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n',
    'What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n',
    'What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n'
]

# here I'm creating 3 questions objects, each of them having a different question prompt and an answer 
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
] 

# creating a function that will return a message with the previously specified questions
def quiz_message(questions):
    
    message = ''
    for i, question in enumerate(questions,start=1):
        message += f'Question {i}:\n{question.prompt}'
    
    return message


# Parameterize the Twilio credentials and phone numbers
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
to_phone_number = 'destination_phone_number'
from_phone_number = 'your_twilio_generated_phone_number'


message_body = quiz_message(questions)


''' ----------------- PART III ----------------- '''

# calling the main function to send the message to the specified number
send_sms(account_sid, auth_token, to_phone_number, from_phone_number, message_body)
