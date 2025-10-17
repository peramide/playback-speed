def main():
    userInput = input("Statement: ")
    print(playback(userInput))

def playback(input):
    return input.replace(" ", "...")


if __name__ == "__main__":
    main()