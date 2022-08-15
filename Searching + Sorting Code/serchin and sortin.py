#nums=[28,5,7,8,9,10,11,22,4]
#print("Bubble Sort")
#import pygame
#pygame.init()
#------ROTATE-------
def draw_select(val,pos):
    BAR_LENGTH=val
    BAR_HEIGHT=2
    x=pos*10
    y=-90
    color=(255,255,255)
    if selected:
        color=(255,0,0)
    fill=(val/100)*(BAR_LENGTH-10)
    fill.rotate(surf,90)
    fill_rect=pygame.Rect(x,y,fill,BAR_HEIGHT-6)
    pygame.draw.rect(surf,color,fill_rect)
def draw_array(array):
    #for item in array:#increment and stuff
    BAR_LENGTH=val
    BAR_HEIGHT=2
    x=pos*10
    y=-90
    color=(255,255,255)
    if selected:
        color=(255,0,0)
    fill=(val/100)*(BAR_LENGTH-10)
    fill.rotate(surf,90)
    fill_rect=pygame.Rect(x,y,fill,BAR_HEIGHT-6)
    pygame.draw.rect(surf,color,fill_rect)
    
def bubble_sort(nums):
    i=0
    numslen=len(nums)
    fl=True
    while i<numslen and fl==True:
        fl=False
        for l in range(numslen-i-1):
            if nums[l]>nums[l+1]:
                t=nums[l]
                nums[l]=nums[l+1]
                nums[l+1]=t
                fl=True
        i=i+1
        print(nums)
#bubble_sort(nums)
#print("======================================")
#print("Insertion Sort")
def insertion_sort(nums):
    #i=1
    numslen=len(nums)
    for i in range(numslen):
        cv=nums[i]
        p=i
        while p>0 and nums[p-1]>cv:
            nums[p]=nums[p-1]
            p=p-1
        nums[p]=cv
        print(nums)
#nums=[28,5,7,8,9,10,11,22,4]
#insertion_sort(nums)
#print("======================================")
#print("Merge Sort")
def merge_sort(nums):
    if len(nums)>1:
        mid=len(nums)//2
        lh=nums[:mid]
        rh=nums[mid:]
        merge_sort(lh)
        merge_sort(rh)
        i=0
        j=0
        k=0
        while i<len(lh) and j<len(rh):
            if lh[i]<rh[j]:
                nums[k]=lh[i]
                i=i+1
            else:
                nums[k]=rh[j]
                j=j+1
            k=k+1

        while i<len(lh):
            nums[k]=lh[i]
            i=i+1
            k=k+1

        while j<len(rh):
            nums[k]=rh[j]
            j=j+1
            k=k+1
        print(lh," ",rh)
#nums=[28,5,7,8,9,10,11,22,4]
#merge_sort(nums)
#print("=====================")
#print("Quick sort")



def partition(nums,start,end):
    pivot=nums[start]
    lm=start+1
    rm=end
    done=False
    while done==False:
        while lm<=rm and nums[lm]<=pivot:
            lm=lm+1
        while nums[rm]>=pivot and rm>=lm:
            rm=rm-1
        if rm<lm:
            done=True
        else:
            temp=nums[lm]
            nums[lm]=nums[rm]
            nums[rm]=temp
    temp=nums[start]
    nums[start]=nums[rm]
    nums[rm]=temp
    return rm

def quick_sort(nums,start,end):
    if start<end:
        split=partition(nums,start,end)
        quick_sort(nums,start,split-1)
        quick_sort(nums,split+1,end)
    return nums

#nums=[28,5,7,8,9,10,11,22,4]
#print(quick_sort(nums,0,8))
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        sort=False
        n=0
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for item in nums2:
            nums1.append(item)
        while sort==False:
            n=0
            for i,item in enumerate(nums1):
                if i>0:
                    if item<nums1[i-1]:
                        n+=1
                        temp=nums1[i-1]
                        temp2=nums1[i]
                        nums1[i]=temp
                        nums1[i-1]=temp2
            if n==0:
                sort=True
                    
        indexmid=(len(nums1))//2
        if indexmid%(len(nums1)):
            print(nums1)
            return "median is {}".format(nums1[indexmid])
        indexmid1=indexmid+1
        indexmid2=indexmid-1
        print(nums1)
        return "median is {} ".format(((nums1[indexmid1])/(nums1[indexmid2])))
sol=Solution()
#print(sol.findMedianSortedArrays(([0,2,3,88,1,53,66,3,58]),([0,99,31,2,5,99])))
  
def linear_search(nums):
    findnum=int(input("Enter number you are searching for: "))
    for i, item in enumerate(nums):
        if i>0:
            nums[i-1]=temp
        if item==findnum:
            newitem=("!!!!{}!!!!").format(item)
            nums[i]=newitem
            return "Found number at index {}, highlighted here {}".format(i,nums)
        temp=nums[i]
        nums[i]=("!!!!{}!!!!").format(item)
        print(nums)
    return "Number not in list"
#nums=[28,5,7,8,9,10,11,22,4]
#print(linear_search(nums))
def binary_search(nums):
    findnum=int(input("Enter number you are searching for: "))
    i=-1
    done=False
    first=0
    last=len(nums)-1
    while first<=last and done==False:
        mid=((first+last)//2)
        if nums[mid]==findnum:
            done=True
            i=mid
        else:
            if nums[mid]<findnum:
                first=mid+1#[|][][][][]
                print(nums[mid:])
            else:
                last=mid-1#[][][][][|]
                print(nums[:mid+1])
    temp=nums[i]
    nums[i]="!!!!{}!!!!".format(temp)
    return "Found at index {} as highlighted here {}".format(i,nums)
#nums=[28,5,7,8,9,10,11,22,4]
#quick_sort(nums,0,8)
#print(binary_search(nums))


###### ------ CAN'T BE BOTHERED TO DO FILE HANDLING - UNNECCESSARY ------#########
def menu():
    i=0
    done=False
    run=True
    valid=False
    while run:
        if i>=1:
            print("Invalid value")
        print("######################")
        print("# 1.  Binary Search  #")
        print("# 2.  Linear Search  #")
        print("# 3.   Merge Sort    #")
        print("# 4. Insertion Sort  #")
        print("# 5.   Quick Sort    #")
        print("# 6.  Bubble Sort    #")
        print("######################")
        mode=int(input("What mode would you like to use?"))
        if mode in [1,2,3,4,5,6]:
            valid=True
            if done:
                redo=input("Do you want to make a new list, or reuse your last one? (Y/N) ")
                if redo.lower() in ["y","yes","ye"]:
                    with open("nums.txt","r") as file:
                        li1=file.readlines()
                        #li1=list(map(int,li1))
                        done=True
                else:
                    done=False
            if not done:
                li1=str(input("Please input list of values seperated by commas:  "))
                li1=li1.split(",")
                try:
                    li1=list(map(int,li1))
                except ValueError:
                    print("Numbers only please")
                    menu()
                with open("nums.txt","w") as file:
                    for i,num in enumerate(li1):
                        if i<len(li1):
                            nummy="{},".format(num)
                        file.write(nummy)
                        done=True
                    
        if valid:
            if mode==1:
                print(binary_search(li1))
            elif mode==2:
                print(linear_search(li1))
            elif mode==3:
                print(merge_sort(li1))
            elif mode==4:
                insertion_sort(li1)
            elif mode==5:
                print(quick_sort(li1,0,len(li1)-1))
            elif mode==6:
                bubble_sort(li1)
        else:
            i=i+1
            main()
####################################################################################################
            
def menu1():
    i=0
    run=True
    valid=False
    while run:
        if i>=1:
            print("Invalid value")
        print("######################")
        print("# 1.  Binary Search  #")
        print("# 2.  Linear Search  #")
        print("# 3.   Merge Sort    #")
        print("# 4. Insertion Sort  #")
        print("# 5.   Quick Sort    #")
        print("# 6.  Bubble Sort    #")
        print("# 7.  Find Median    #")
        print("######################")
        mode=int(input("What mode would you like to use?"))
        if mode in [1,2,3,4,5,6,7]:
            valid=True
            li1=str(input("Please input list of values seperated by commas:  "))
            li1=li1.split(",")
            try:
                li1=list(map(int,li1))
            except ValueError:
                print("Numbers only please")
                menu1()
                    
        if valid:
                if mode==1:
                    print(binary_search(li1))
                elif mode==2:
                    print(linear_search(li1))
                elif mode==3:
                    merge_sort(li1)
                    print(li1)
                elif mode==4:
                    insertion_sort(li1)
                    print(li1)
                elif mode==5:
                    print(quick_sort(li1,0,len(li1)-1))
                    print(li1)
                elif mode==6:
                    bubble_sort(li1)
                    print(li1)
                elif mode==7:
                    print("This mode combines and sorts two lists and finds the median")
                    li2=str(input("Please input another list of values seperated by commas:  "))
                    li2=li2.split(",")
                    try:
                        li2=list(map(int,li2))
                    except ValueError:
                        print("Numbers only please")
                        menu1()
                    print(sol.findMedianSortedArrays((li1),(li2)))
                else:
                    i=i+1
                    menu1()
menu1()
            
