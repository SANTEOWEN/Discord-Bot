import random
def handle_response(message) -> str:
    p_message  = message.lower()

    if p_message == 'hello':
        return 'Dont wake me up'
    
    if p_message == 'roll':
        return str(random.randint(1, 600))
    
    if p_message == 'help':
        return "`this is a help fucking message that you can modify.`"

    return "Dont fucking talk to me"