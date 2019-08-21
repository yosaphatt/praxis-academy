def quicksort(left,right,p):
        l=left
        r=right
        pivot=list[left]
        while(left<right):
                if p==1:
                        while((list[right]>=pivot) and left<right):
                                right=right-1
                        if(left!=right):
                                list[left]=list[right]
                                left=left+1
                        while((list[left]<=pivot) and left<right):
                                left=left+1
                        if(left!=right):
                                list[right]=list[left]
                                right=right-1
                else:
                        while((list[right]<=pivot) and left<right):
                                right=right-1
                        if(left!=right):
                                list[left]=list[right]
                                left=left+1
                        while((list[left]>=pivot) and left<right):
                                left=left+1
                        if(left!=right):
                                list[right]=list[left]
                                right=right-1
        list[left]=pivot
        pivot=left
        left=l
        right=r
        if left<pivot:
                quicksort(left,pivot-1,p)
        if right>pivot:
                quicksort(pivot+1,right,p)