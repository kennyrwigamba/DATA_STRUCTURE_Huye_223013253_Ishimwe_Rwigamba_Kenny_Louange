from collections import deque

stack = []

queue = deque()

sessions = {
            'AI Hackton' : {'session_name':'AI Hackton', 'attendees':[]}
           }

def add_session(session_name):
    if session_name not in sessions:
        sessions[session_name] = {'session_name': session_name, 'attendees': []}
        print(f"Added session: {session_name}")
    else:
        print(f"Session '{session_name}' already exists.")


def push(attendee, session_name):
    if session_name in sessions:
        stack.append((attendee, session_name))
        sessions[session_name]['attendees'].append(attendee)
        print(f"Session '{session_name}' booked for {attendee}.")
    else:
        print(f"Session '{session_name}' is not available.")

def pop():
    if stack:
        attendee, session_name = stack.pop()
        sessions[session_name]['attendees'].remove(attendee)
        print(f"Undo booking: Session '{session_name}' for {attendee} has been removed.")
    else:
        print("No booking to undo.")


def enqueue(attendee):
    queue.append(attendee)
    print(f"{attendee} added to the waitlist.")


def dequeue(session_name):
    if queue:
        attendee = queue.popleft()
        push(attendee, session_name)
    else:
        print("No attendees in the queue.")


def display_sessions():
    if sessions:
        print("Current sessions:")
        for session_name in sessions:
            print(f"- {session_name}")
    else:
        print("No sessions booked yet.")




def main():
    while True:
        print("\nMenu: ")
        print("1. Add an attendee to a session.")
        print("2. Undo last session booking.")
        print("3. Add attendee on waiting list.")
        print("4. Book session for attendee in waiting list.")
        print("5. Display all sessions")
        print("6. Add new session")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            attendee = input("Enter Attendee name: ")
            session_name = input("Enter session name: ")
            print()
            push(attendee, session_name)

        elif choice == '2':
            pop()

        elif choice == '3':
            attendee = input("Enter attendee name to add on waiting list: ")
            print()
            enqueue(attendee)

        elif choice == '4':
            attendee = input("Enter session to book for attendee on waiting list: ")
            print()
            dequeue(attendee)

        elif choice == '5':
            display_sessions()
        
        elif choice == '6':
            session_name = input("Enter session name to add: ")
            add_session(session_name)

        elif choice == '7':
            break

        else:
            print("Invalid option. Please try again.")


main()