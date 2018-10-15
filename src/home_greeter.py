from home_greeter.greeter.greeter import Greeter

def main():
    greeter = Greeter()

    while True:
        greeter.welcome()

        name = greeter.ask_for_name()
        print(name)

        # detect delivery or not

        person = greeter.ask_for_person()
        print(person)

        greeter.update_while_finding_if_person_is_avaiable(name, person)

        # check if person is available

        # if not available then take and tweet image

        tweet_image()

def tweet_image():
    raise NotImplementedError()

main()
