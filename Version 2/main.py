from src.UserCommunication import UserCommunication

def main():
    startConnection = UserCommunication()
    startConnection.applicationLoop()

if __name__ == "__main__":
    main()
