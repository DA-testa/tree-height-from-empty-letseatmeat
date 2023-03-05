# python3

import sys
import threading
        
def compute_height(n, parents):
    # Write this function
    x = {}
    def treeheight(i):
        if i in x:
            return x[i]
        
        if i == -1:
            return 0
        hx = 1 + treeheight(parents[i])
        x[i] = hx
        return hx
    max_height = 0
    # Your code here
    for i in range(n):
        max_height = max(max_height, treeheight(i))
    return max_height

def main():
    y = input()
    if "I" in y:
        z = int(input())
        inp = list(map(int,input().split()))
        print(compute_height(z,inp))
    if "F" in y:
        f1 = input()
        if "a" not in f1:
            with open("./test/" + f1, "r") as f2:
                e = int(f2.readLine())
                out=list(map(int, f2.readLine().split()))
                print(compute_height(z,out))
    
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
