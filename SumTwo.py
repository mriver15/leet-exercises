# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Michael Rivera
import math



# def getTermIndexes(nums, target):


#     # print(snums[midind:len(snums)])
#     return

def getTermIndexes(nums, target):
    for (i,k) in enumerate(nums):
        for (j,k2) in enumerate(nums):
            if j > i:
                if k + k2 == target:
                    return [i,j]
    return []

def main():
    nums = [2,7,11,15,3]
    target = 9

    print(getTermIndexes(nums,target))
    

if __name__ == "__main__":
    main()