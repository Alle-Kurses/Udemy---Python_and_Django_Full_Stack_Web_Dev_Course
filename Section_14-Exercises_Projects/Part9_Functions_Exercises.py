#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

'''def arrayCheck(nums):
    # CODE GOES HERE
    count =0
    lst = nums.split()
    num_sets = []
    MY_SETS = [1, 2, 3]

    for i in lst:
	    num_sets.append(int(i))

    for i in MY_SETS:
    	if i in num_sets:
    		count += 1
    	else:
    		return False
    	if count == len(MY_SETS):
    		return True

numbers = input("Enter sets of numbers:")
print(arrayCheck(numbers))'''

#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(str):
    # CODE GOES HERE
    d

#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

'''def end_other(a, b):
    # CODE GOES HERE
    long_var = ""
    short_var = ""
    outcome = ""
    variable_diff = 0

    if len(a) > len(b):
        long_var = a
        short_var = b
    else:
        long_var = b
        short_var = a

    variable_diff = len(long_var) - len(short_var)
    outcome = long_var[variable_diff : len(long_var)]

    if outcome == short_var:
        return True
    else:
        return False

first = input("Enter the 1st string: ").lower()
second = input("Enter the 2nd string: ").lower()

print(end_other(first, second))'''

#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

'''def doubleChar(string):
  # CODE GOES HERE
    temp_string = ""
    for i in string:
        temp_string += i*2
    return temp_string

reply = input("Enter string here: ")
print(doubleChar(reply))'''

#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

'''def no_teen_sum(a, b, c):
  # CODE GOES HERE
  res = 0
  lst = (a, b, c)
  for i in lst:
      if fix_teen(i) == True:
          res += i
      else:
          continue
  return res

def fix_teen(n):
  # CODE GOES HERE
    lst = [13, 14, 17, 18, 19]
    if n in lst:
        return False
    else:
        return True
    
lst = [0, 0, 0]
x = 0

while x < 3:
    lst[x] = int(input("Enter something: "))
    x += 1

print(no_teen_sum(lst[0], lst[1], lst[2]))'''


#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
  # CODE GOES HERE
    count = 0
    for i in nums:
        if i%2 == 0:
            count += 1
        else:
            continue
    return count

lst = []
n = (int(input("Enter numbers of inputs: ")))
i = 0

while i < n:
    lst.append(int(input("Enter number: ")))
    i += 1

print(count_evens(lst))
