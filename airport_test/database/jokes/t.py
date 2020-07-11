with open('j1.txt','r') as f:
    jokes = []
    s=''
    for line in f:
        if line.startswith('----'):
            jokes.append(s)
            s=''
        else:
            s+=line

    print(jokes)
    print(len(jokes))
    print('\n\n\n\n')
    for i in jokes:
        print(i)
        print('-------------------------')

