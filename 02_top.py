# 1,2,3,x,10,8,7,11,12,13,0

def top(nums):
    if nums[0] > nums[1]:
        return nums[1]
    if nums[-1] > nums[-2]:
        return nums[-1]
    
    start = 0
    end = len(nums)
    mid = 0
    while(start < end):
        mid = (start+end)/2
        if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
            return nums[mid]
        elif nums[mid] < nums[mid-1]:
            end = mid
        else:
            start = mid 
    return nums[mid]

if __name__ == '__main__':
    print(top([1,2,3,4,5,8,7,6,2]))
    print(top([1,2,3,4,5,6,7,8,9,0]))