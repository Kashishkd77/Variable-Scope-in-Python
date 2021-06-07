# variable scope illustration
# HIERARCHY -- nonlocal > local > global > built-in

print("LOCAL & GLOBAL SCOPE Illustration 1 : ")
a = 5
def valueA():
    a = 10

    def valueB():
        # local variable
        a = 20
        print("valueB : value of a : ",a)

    def valueC():
        # local variable
        global a
        a = 30
        print("valueC : value of a : ",a)

    valueB()
    print("valueA : value of a : ",a)
    valueC()
    print("valueA : value of a : ",a)
valueA()
print("value of a : ",a)                        # a=5 is outer most global value hencce , a=30 innermost global value is preferred
print()


print("GLOBAL SCOPE Illustration 2 : ")
def valueA():
    a = 10
    def valueB():
        global a
        a = 20
        def valueC():
            global a
            a = 30
            print("valueC : value of a : ", a)
        valueC()
        print("valueB : value of a : ", a)
    def valueD():
        print("valueD : value of a : ", a)

    valueD()                                            # since , local a = 10
    valueB()                                            # in valueC , since global local a = 30
                                                        # in valueB , since ,innermost global a= 30 > outer global a = 20
    valueD()                                            # since , local a = 10 > innermost global a = 30
    print("valueA : value of a : ", a)                  # since , local a = 10 > innermost global a = 30
valueA()
print()


# nonlocal variable can be used within a function when they are already used in a function outside it
print("NONLOCAL SCOPE Illustration 3 : ")
def valueA():
    a = 10                          # in case if this was missing , SyntaxError : no binding for nonlocal 'a' found
    def valueB():
        nonlocal a
        a = 20
        def valueC():
            global a
            a = 30
            print("valueC : value of a : ", a)
        valueC()
        print("valueB : value of a : ", a)
    def valueD():
        print("valueD : value of a : ", a)

    valueD()                                            # since , local a = 10
    valueB()                                            # in valueC , since no local or non local a so , global a = 30
                                                        # in valueB , since ,non local a= 20 > global a = 30
    valueD()                                            # since , non local a= 20 > local a = 10
    print("valueA : value of a : ", a)                  # since , non local a= 20 > local a = 10
valueA()
print()


print("Without using non local variable scope in Illustration 3 :")
def valueA():
    a = 10
    def valueB():
        a = 20
        def valueC():
            global a
            a = 30
            print("valueC : value of a : ", a)
        valueC()
        print("valueB : value of a : ", a)
    def valueD():
        print("valueD : value of a : ", a)

    valueD()
    valueB()
    valueD()
    print("valueA : value of a : ", a)
valueA()
print()


# Priority : innermost > outermost
print("NONLOCAL SCOPE Illustration 4 : ")
def valueA():
    a = 10
    def valueB():
        nonlocal a
        a = 20
        def valueC():
            nonlocal a
            a = 30
            print("valueC : value of a : ", a)
        valueC()
        print("valueB : value of a : ", a)
    def valueD():
        print("valueD : value of a : ", a)

    valueD()                                            # since , local a = 10
    valueB()                                            # in valueC , since non local a = 30
                                                        # in valueB , since ,innermost non local a= 30 > outer non local = 20 (which is also local for valueB)
    valueD()                                            # since , innermost non local a= 30 > local a = 10
    print("valueA : value of a : ", a)                  # since , innermost non local a= 20 > local a = 10
valueA()
print()
