# A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time () to arrived late ().

# Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.

# Example




# The first  students arrived on. The last  were late. The threshold is  students, so class will go on. Return YES.

# Note: Non-positive arrival times () indicate the student arrived early or on time; positive arrival times () indicate the student arrived  minutes late.

# Function Description

# Complete the angryProfessor function in the editor below. It must return YES if class is cancelled, or NO otherwise.

# angryProfessor has the following parameter(s):

# int k: the threshold number of students
# int a[n]: the arrival times of the  students
# Returns

# string: either YES or NO


def angryProfessor(k, a):

    cnt = sum([1 for ontime in a if ontime <= 0])

    return "YES" if cnt < k else "NO"


t = int(input().strip())

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
a = list(map(int, input().rstrip().split()))

result = angryProfessor(k, a)
print(result)


