
def quick_sort(nums,start,end):
    low = start
    high = end
    pivot = nums[high]
    print(low,high,pivot)
    while low < high:
        # print(low,high,pivot)
        while low < high and nums[low] < pivot:
            low += 1
        if low < high:
            nums[high] = nums[low]
            high -= 1
        while low < high and nums[high] > pivot:
            high -= 1
        if low < high:
            nums[low] = nums[high]
            low += 1
    # print(low,high)
    nums[low] = pivot
    print(nums,start,end,low,high)
    if start < low:
        quick_sort(nums,start,low-1)
    if end > high:
        quick_sort(nums,high+1,end)
        
        




if __name__ == '__main__':
    # quick_sort([8,6,1,3,5,9,7,2],0,7)
    quick_sort([9,8,3,2,5,4,7,6],0,7)
