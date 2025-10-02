messages = ['Hola', 'Como', 'Estas', 'Amigo']
new_messages = []
def show_messages(messages):
    while messages:
        new_messages.append(messages.pop())
    send_messages(new_messages)

def send_messages(new_messages):
    for n in new_messages:
        print(n)

show_messages(messages[::-1])