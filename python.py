import time


def revision():
    print('do you want to play a game')
    time.sleep(1)
    choice = int(input('choose the topic\nSystem architecture...1\nNetworks...2\n'))

    if choice == 1:
        system_arch()

        
    elif choice == 2:
        networks()


    elif choice == 69:
        test()

    
    
    else:
        print ("sorry that doesn't work")
        time.sleep(1)
        revision()

    

def system_arch():

    def multiple_choices_1():
        answer = str('C')
        print("What does CPU stand for?\n\n")
        time.sleep(0.1)
        print("A. Core Processing Unit \n")
        time.sleep(0.1)
        print("B. Control Processing Unit \n")
        time.sleep(0.1)
        print("C. Central Processing Unit \n")
        time.sleep(0.1)
        print("D. Computer Processing Unit \n")
        time.sleep(0.1)
        usranswer = input(">>> ")
        usranswer = usranswer.upper()
        if usranswer == answer:
            print ("Correct")
        else:
            print ("You are failing your GCSE's \n Try again")
            multiple_choices_1()

    def multiple_choices_2():
        answer = str('A')
        print("What does ALU stand for?\n\n")
        time.sleep(0.1)
        print("A. Arithmetic Logic Unit \n")
        time.sleep(0.1)
        print("B. Aluminium \n")
        time.sleep(0.1)
        print("C. Authentic Logic Unit \n")
        time.sleep(0.1)
        print("D. Actual Logic Unit \n")
        time.sleep(0.1)
        usranswer = input(">>> ")
        usranswer = usranswer.upper()
        if usranswer == answer:
            print ("Correct")
        else:
            print ("You are failing your GCSE's \n Try again")
            multiple_choices_2()

    def multiple_choices_3():
        answer = str('D')
        print("What does ROM stand for?\n\n")
        time.sleep(0.1)
        print("A. Random Only Memory \n")
        time.sleep(0.1)
        print("B. ROM Weasley \n")
        time.sleep(0.1)
        print("C. Ram Only Memory \n")
        time.sleep(0.1)
        print("D. Read Only Memory \n")
        time.sleep(0.1)
        usranswer = input(">>> ")
        usranswer = usranswer.upper()
        if usranswer == answer:
            print ("Correct")
        else:
            print ("You are failing your GCSE's \n Try again")
            multiple_choices_3()

    def multiple_choices_4():
        answer = str('B')
        print("What does RAM stand for?\n\n")
        time.sleep(0.1)
        print("A. Rant Ambient Memory \n")
        time.sleep(0.1)
        print("B. Random Access Memory \n")
        time.sleep(0.1)
        print("C. A Male Sheep \n")
        time.sleep(0.1)
        print("D. RON access Memory \n")
        time.sleep(0.1)
        usranswer = input(">>> ")
        usranswer = usranswer.upper()
        if usranswer == answer:
            print("Correct")
        else:
            print ("You are failing your GCSE's \n Try again")
            multiple_choices_4()

    multiple_choices_1()
    multiple_choices_2()
    multiple_choices_3()
    multiple_choices_4()


def networks():

    def open_1():
        print('what does WAN stand for')
        uranswer = input(">>>")
        uranswer = uranswer.upper()
        if uranswer == ('WIDE AREA NETWORK'):
            print("Correct")
        else:
            print ("You are failing your GCSE's \n Try again")
            open_1
        

    def multiple_choices_1():
        answer = str('C')
        print("What does LAN stand for?\n\n")
        time.sleep(0.1)
        print("A. Local Arianna Network \n")
        time.sleep(0.1)
        print("B. Little Area Network \n")
        time.sleep(0.1)
        print("C. Local Area Network \n")
        time.sleep(0.1)
        print("D. Local Arena Networking \n")
        time.sleep(0.1)
        usranswer = input(">>> ")
        usranswer = usranswer.upper()
        if usranswer == answer:
            print ("Correct")
        else:
            print ("You are failing your GCSE's \n Try again")
            multiple_choices_1()

    def multiple_choices_2():
        answer = str('D')
        print("Which Topology has everything connected?\n\n")
        time.sleep(0.1)
        print("A. Ring \n")
        time.sleep(0.1)
        print("B. Star \n")
        time.sleep(0.1)
        print("C. Bus \n")
        time.sleep(0.1)
        print("D. Mesh \n")
        time.sleep(0.1)
        usranswer = input(">>> ")
        usranswer = usranswer.upper()
        if usranswer == answer:
            print ("Correct")
        else:
            print ("You are failing your GCSE's \n Try again")
            multiple_choices_2()

    def multiple_choices_3():
        answer = str('B')
        print("which Topology is a straight line?\n\n")
        time.sleep(0.1)
        print("A. Ring \n")
        time.sleep(0.1)
        print("B. Bus \n")
        time.sleep(0.1)
        print("C. Star \n")
        time.sleep(0.1)
        print("D. Mesh \n")
        time.sleep(0.1)
        usranswer = input(">>> ")
        usranswer = usranswer.upper()
        if usranswer == answer:
            print ("Correct")
        else:
            print ("You are failing your GCSE's \n Try again")
            multiple_choices_3()

    def multiple_choices_4():
        answer = str('A')
        print("What sends data packets?\n\n")
        time.sleep(0.1)
        print("A. router \n")
        time.sleep(0.1)
        print("B. Hub \n")
        time.sleep(0.1)
        print("C. Switch \n")
        time.sleep(0.1)
        print("D. Server \n")
        time.sleep(0.1)
        usranswer = input(">>> ")
        usranswer = usranswer.upper()
        if usranswer == answer:
            print("Correct")
        else:
            print ("You are failing your GCSE's \n Try again")
            multiple_choices_4()

    multiple_choices_1()
    multiple_choices_2()
    open_1()
    multiple_choices_3()
    multiple_choices_4()

    print()



def test():
    print('oh ok then')

    
revision()

