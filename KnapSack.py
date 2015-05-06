"""
A dynamic programming solution to the 0-1 knapsack problem

Problem 16.2-2, p.427 of the text. Do the following:

1. Come up with a recursive characterization of the solution. Then explain why it has optimal substructure.
Both these should be included in your submission.

2. Design a corresponding non-recursive bottom-up table lookup algorithm to solve the problem.
This should be included in your written submission.

3. Do an approximate analysis of the efficiency of your algorithm to show it is O(nW).
This should be included in your written submission.

4. Implement your algorithm in a program. It should read an input text file named input.txt formatted as follows:
The first line contains the integer W, the capacity of the knapsack, and the integer m, the number of available items.
(b) The second line has m integers, the weights of the m items. Assumes that the m items are numbered with ids 1..m.
(c) The third line has m integers, the values of the m items. Your program should output a text file formatted as follows:
(a) The first line should contain the total value of the optimal solution, as determined by your algorithm.
(b) The second line should contain up to m integers, the numbers (ids) of the chosen items in the optimal solution.

Hint: Turning your recursive characterization into a recursive algorithm and working out its recursion tree for
    particular problem instances might help you figure out what kind of table to use and how to fill the table bottom-up.
    But you do not need to submit any of this.
"""





class Knapsack(object):

    """ The format of the file is:
        Line 1: Capacity  + number of items
        Line 2: value1   weight1
        Line 3: value2   weight2
        ...
    """
    def __init__(self, inFile):
        try:
            inFile = open(inFile, 'r')
        except IOError as e:
            print("Cannot open file:" + str(e))

        weights = []
        values = []

        # read the first line
        W, m = inFile.readline().split()
        # print W, m

        # read all the rest lines
        for i in range(int(m)):
            fields = inFile.readline().split()
            values.append(int(fields[0]))
            weights.append(int(fields[1]))

        self.W, self.m, self.values, self.weights = int(W), int(m), values, weights




    """ If the format of the file is 3 lines:
        Line 1: Capacity  + number of items
        Line 2: value1   value2    ...
        Line 3: weight1  weight2   ...
    """
    # def __init__(self, inFile):
    #     try:
    #         inFile = open(inFile, 'r')
    #     except IOError as e:
    #         print("Cannot open file:" + str(e))
    #
    #     # read the first line
    #     W, m = inFile.readline().split()
    #
    #     # read values, 2nd line
    #     read = inFile.readline().split()
    #     values = [int(v) for v in read]
    #
    #     # read weights, 3rd line
    #     read = inFile.readline().split()
    #     weights = [int(w) for w in read]
    #
    #     self.W, self.m, self.values, self.weights = int(W), int(m), values, weights




    #######################
    # Helper functions    #
    #######################
    def getCapacity(self):
        return self.W

    def getValues(self):
        return self.values

    def getNumItems(self):
        return self.m

    def getWeights(self):
        return self.weights


    def printKnapsack(self):
        print self.W, self.m
        for i in range(len(self.weights)):
            print i, " ", self.values[i], " ", self.weights[i]




    # top-down recursive algorithm
    # very slow
    def recursive(self, m, W, weights, values):

        if m == 0 or W <= 0: return 0
        taken = []

        # cannot take item[m-1]
        if weights[m-1] > W:
            return self.recursive(m-1, W, weights, values)
        else:
            # can take it
            # but compared with not to take, which is better
            return max(self.recursive(m-1, W, weights, values),
                       self.recursive(m-1, W - weights[m-1], weights, values) + values[m-1])

        return tot





    # neoclassical memoized bottom up with 2-dimemsional memoized table with returned values
    def memoizedBottomUp(self, m, W, weights, values):

        """
        lookup table (m+1) x (W+1)
        base case is that index of W or m is 0
        index adjustment: at line, the process is for weights[i-1]
        and values[i-1] as python supports from-zero index
        """

        T = [[-1 for __ in range(W+1)] for _ in range(m+1)]

        for i in range(m+1):
            for x in range(W+1):          #pseudonomial time O(mW)
                # base case
                if i == 0 or x == 0:
                    T[i][x] = 0

                # has room for item i, processing item (i-1) actually
                elif x >= weights[i-1]:
                    # choose not to take item i
                    if T[i-1][x] > T[i-1][x - weights[i-1]] + values[i-1]:
                        T[i][x] = T[i-1][x]
                    else:
                        T[i][x] = T[i-1][x - weights[i-1]] + values[i-1]

                # not enough capacity for this item
                else:
                    T[i][x] = T[i-1][x]


					
        # record taken values, from top-down
        taken = []
        x = W
        for i in reversed(range(1, m+1)):
                # taken
                if T[i][x] != T[i-1][x]:
                    taken.append((i-1, "val", values[i-1], "weight", weights[i-1]))
                    x -= weights[i-1]


		# printout lookup table (optional) 
        # for i in reversed(range(m+1)): print i, T[i][W - weights[i-1]] , T[i][W]
         #    for j in range(W+1):
         #        print T[i][j],
         #    print ""

        #print out taken items
        print "Taken item(s): "
        check = 0
        for t in taken:
            check += values[t[0]]
            print t,
        #
        #
        # # output to file
        # f = open('output.txt', 'w')
        # print >> f, T[m][W], "\n"
        # for r in taken: print >> f, r
        # f.close()

        # print "\ndouble check: " + str(check)
        return T[m][W]



		
		
		
    # This solution just uses 2 array current[0...W+1] and next[0..W+1] to store the results
    # This is correct as level i+1 just needs results from level i
    # The running performance proves that it saves memory a lot
	# however, this method (as well as parent pointer) has not solved the retrieval of the problem
	# still a question? ...

    def optimizedMemoizedBottomUp(self, m, W, weights, values):

        current = [0 for _ in range(W+1)]
        next = [0 for _ in range(W+1)]

        for i in range(1, m+1):
            for x in range(1, W+1):          #pseudonomial time O(mW)

                # case 1: has room for item i, processing item (i-1) actually
                if x - weights[i-1] >= 0:
                    # choose not to take item i
                    next[x] = max(current[x], current[x - weights[i-1]] + values[i-1])

                # case 2: not enough capacity for this item
                else:
                    next[x] = current[x]

            # switch role of current and next
            current = [_ for _ in next]

        # output to file
        # f = open('C:/tmp/output.txt', 'w')
        # print >> f, current[W]
        # for r in taken: print >> f, r,
        # f.close()

        return current[W]









	# This solution just uses 2 array current[0...W+1] and next[0..W+1] to store the results
    # This is correct as level i+1 just needs results from level i
    # The running performance proves that it saves memory a lot
	# using solution of parent pointers
	# still testing... not yet completed 
    def opz(self, m, W, weights, values):

        current = [0 for _ in range(W+1)]
        next = [0 for _ in range(W+1)]

        # taken = []
        pointers = [(False, 0) for _ in range(m+1)]


        for i in range(1, m+1):
            for x in range(1, W+1):          #pseudonomial time O(mW)

                # case 1: has room for item i, processing item (i-1) actually
                if x - weights[i-1] >= 0:
                    # choose not to take item i
                    if current[x] > current[x - weights[i-1]] + values[i-1]:
                        next[x] = current[x]
                        pointers[i] = (False, i-1)
                    else:
                        next[x] = current[x - weights[i-1]] + values[i-1]

                        if current[x - weights[i-1]] == 0:
                            pointers[i] = (True, 0)
                        else:
                            pointers[i] = (True, i-1)

                else:
                    next[x] = current[x]
                    pointers[i] = (False, i-1)

            # switch role of current and next
            current = [_ for _ in next]

        # output to file
        # f = open('C:/tmp/output.txt', 'w')
        # print >> f, current[W]
        # for r in taken: print >> f, r,
        # f.close()

        # print pointers
        print "pointers"
        for p in pointers:
            print p
            # if p[0]:
            # #     print p[1],
            #     check += values[p[1]-1]
        print




        return current[W]











####TEST DIRVER#####

inputFile = 'C:/tmp/knapsackbig.txt'
# inputFile = 'C:/tmp/knapsack2.txt'
# inputFile = 'C:/tmp/knapsack.txt'
# inputFile = raw_input("Enter your input file: ")
testKnapsack = Knapsack(inputFile)

# for i in testKnapsack.getWeights(): print i,

print "Testing the bottom up program with table lookup"
tot2 =  testKnapsack.memoizedBottomUp(testKnapsack.getNumItems(),
                                      testKnapsack.getCapacity(), testKnapsack.getWeights(), testKnapsack.getValues())
print "\ntotal value is", tot2

print "Testing the bottom up program with 2 arrays lookup"
import time
start_time = time.time()
print "first result"
print testKnapsack.optimizedMemoizedBottomUp(testKnapsack.getNumItems(),
                                    testKnapsack.getCapacity(), testKnapsack.getWeights(), testKnapsack.getValues())
print "second result"
tot3 =  testKnapsack.opz(testKnapsack.getNumItems(),
                         testKnapsack.getCapacity(), testKnapsack.getWeights(), testKnapsack.getValues())
print "total time executed is: ", time.time() - start_time, " seconds"
print "\ntotal value is", tot3




