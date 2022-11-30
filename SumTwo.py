# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Michael Rivera
import math



# def getTermIndexes(nums, target):


#     # print(snums[midind:len(snums)])
#     return

def getTermIndexes(nums, target):
 #         Use Dict to initiate Hashmap
        hMap = {}

#     For every element in the list
        for (i,k) in enumerate(nums):
#         If the complement of the target minus the element value exists in the hash, already found match, return indexes
            if target - k in hMap:
                return hMap[target - k], i
            else:
#                 Add calculated complement to target to hashmap
                hMap[k] = i
#     If Not found return empty list
        return []

def main():
    nums = [2,4,11,15,5]
    target = 9

    print(getTermIndexes(nums,target))
    

if __name__ == "__main__":
    main()