def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:    #this will execute even the function return something before that
        print('I am inside finally.')

main()

    