def merge(nums1,nums2):
    n = 3
    if n > 0:
        nums1[-n:] = nums2 #начиная с N-ого индекса в масиве nums1 меняем на nums2
        nums1.sort()
    return nums1

a = [1,2,3,0,0,0]
a1 = [4,5,6]
print(merge(a,a1))