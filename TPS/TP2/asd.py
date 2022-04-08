import sys
from six.moves import input as raw_input

def main():
    transition = [[[0,1],[0]], [[4],[2]], [[4],[3]], [[4],[4]]]
    input = raw_input("enter the string: ")
    input = list(input) #copy the input in list because python strings are immutable and thus can't be changed directly
    for index in range(len(input)): #parse the string of a,b in 0,1 for simplicity
        if input[index]=='a':
            input[index]='0' 
        else:
            input[index]='1'

    final = "3" #set of final states = {3}
    start = 0

    trans(transition, input, final, start)
    print("rejected")


def trans(transition, input, final, state):
    for each in transition[state][int(input[0])]: #check for each possibility       
        if each < 4:                              #move further only if you are at non-hypothetical state
            state = each
            if len(input)==1:
                if (str(state) in final): #last symbol is read and current state lies in the set of final states
                    print("accepted")
                    sys.exit()
                else:
                    continue
            trans(transition, input[1:], final, state) #input string for next transition is input[i+1:]

main()