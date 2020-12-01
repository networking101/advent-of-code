with open('input.txt') as fp:
    line = fp.readline()
    mylist = line.split(',')
    orig_list = [int(i) for i in mylist]

    for k in range(10000):
        x = int(k/100)
        y = int(k%100)

        test_list = list(orig_list)
        test_list[1] = x
        test_list[2] = y

        for j in range(len(test_list)):
            if j%4 == 0:
                #print("index: " + str(j))
                if test_list[j] == 1:
                    #print(str(test_list[j+1]) + ":" + str(test_list[test_list[j+1]]) + " + " + str(test_list[j+2]) + ":" + str(test_list[test_list[j+2]]) + " = " + str(test_list[j+3]) + ":" + str(test_list[test_list[j+3]]))
                    test_list[test_list[j+3]] = test_list[test_list[j+1]] + test_list[test_list[j+2]]
                if test_list[j] == 2:
                    #print(str(test_list[j+1]) + ":" + str(test_list[test_list[j+1]]) + " * " + str(test_list[j+2]) + ":" + str(test_list[test_list[j+2]]) + " = " + str(test_list[j+3]) + ":" + str(test_list[test_list[j+3]]))
                    test_list[test_list[j+3]] = test_list[test_list[j+1]] * test_list[test_list[j+2]]
                if test_list[j] == 99:
                    #print("COMPLETE!")
                    #print test_list[0]
                    break
        if test_list[0] == 19690720:
            print("ANSWER: " + str((100*x) + y))
            break

print test_list
