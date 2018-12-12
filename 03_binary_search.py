

def search(nums,key):
    start = 0
    end = len(nums)-1
    mid = -1

    while(start <= end):
        mid = (start+end)/2
        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def search_dup(nums,key):
    start = 0
    end = len(nums) - 1
    mid = -1

    while(start <= end):
        mid = (start + end)/2
        if nums[mid] >= key:
            end = mid - 1
        elif nums[mid] < key:
            start = mid + 1
    return mid

if __name__ == '__main__':
    print(search([1,1,2,3,4,5,6,7,7],1))
    print(search_dup([1,1,1,1,1,1,1,1],1))
