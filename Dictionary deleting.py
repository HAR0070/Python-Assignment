if __name__=='__main__' :
    #Deleting different dictionary element
    Options = ['File','Edit','Format','Run','Windows']
    Option_No = [1,2,3,4,6]
    D = zip(Option_No,Options)
    Dictionary = dict(D)
    print(Dictionary)
    Delete_4 = Dictionary.pop(4)
    print(Dictionary)
