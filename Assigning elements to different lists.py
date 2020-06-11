if __name__=='__main__' :
    list = [1,2,3,4,4,5,5,6]
    print(list[2])

    Name_list = ['file','edit','format','run']
    print(Name_list[2])

    List_list = [2,3,4]
    List_list.append(list)
    List_list.append(Name_list)
    List_list.extend(list)
    print(List_list)
