import tkinter as tk
from tkinter import *
from tkinter import * 
from tkinter import ttk
import random
import time


mai_camel=0
barlist=[]
datalist=[]
size=0
window=0
canv=0
tim=0
max_value=0
ti=0.3
oblist=[]
win=0
choice=0
flag=0
click_num=0
root=0
t=0
shuf_1=0
ab=[]
scrollbar=0


def del_create(obid0,n):
    global datalist
    global barlist
    global ti
    global window
    global oblist
    canv.delete(oblist[n])
    max_value=max(datalist)
    muit=(480/max_value)
    print("Objectdelete",obid0)
    print(barlist)
    ax1,ay1,ax2,ay2=canv.coords(obid0)
    
    canv.delete(obid0)
    obid1=canv.create_rectangle(ax1,(480-(datalist[n]*muit)),ax2,ay2,fill="red",outline='GhostWhite')
    ob=canv.create_text(ax1+10, 450, text=datalist[n])
    oblist[n]=ob
    barlist[n]=obid1    
    window.update()
    time.sleep(ti)
    canv.itemconfig(obid1, fill='ivory4')
    return obid1




def swap_pos(obid0,obid1,obp0,obp1):
     global datalist
     global barlist
     global ti
     canv.itemconfig(obid0, fill='red')
     canv.itemconfig(obid1, fill='blue')
     bar_minx1, bar_miny1, bar_minx2, bar_miny2 = canv.coords(obid0)
     barx1,bary1,barx2,bary2=canv.coords(obid1)
     
     x1,y1=canv.coords(obp0)
     x2,y2=canv.coords(obp1)
     print(canv.coords(obp1))

     canv.move(obid0,barx1-bar_minx1,0)#canv.move(objectId,x,y)
     canv.move(obid1,bar_minx2-barx2,0)
     canv.move(obp0,x2-x1,0)
     canv.move(obp1,x1-x2,0)
     window.update()
     canv.itemconfig(obid0, fill='ivory4')
     canv.itemconfig(obid1, fill='ivory4')
     time.sleep(ti)

     

    

    
def selection_sort():
    global tim
    tim=Tk()
    tim.title("Selection Sort")
    tim.geometry("800x400+700+400")
    label = Label( tim, text="Time Complexity=θ(n^2)" )
    l1=Label( tim, text="Application Of Selection Sort" )
    l2=Label( tim, text="Small list is to be sorted.")
    l3=Label( tim, text="cost of swapping does not matter.")
    l4=Label( tim, text=" checking of all the elements is compulsory.")
    l5=Label( tim, text=" cost of writing to a memory matters like in flash memory (number of writes/swaps is O(n) as compared to O(n2) of bubble sort)")
    
   
    

    label.grid()
    l1.grid()
    l2.grid()
    l3.grid()
    l4.grid()
    l5.grid()
   
    tim.after(400,lambda:select())

def select():
    global barlist    
    global datalist

    for i in range(len(datalist)):
        min = i
        for j in range(i + 1 ,len(datalist)):
            if(datalist[j] < datalist[min]):
                min = j
        datalist[min], datalist[i] = datalist[i] ,datalist[min]
        barlist[min] , barlist[i] = barlist[i] , barlist[min]
        oblist[min],oblist[i]=oblist[i],oblist[min]
        swap_pos(barlist[min],barlist[i],oblist[min],oblist[i])
        



def bubble_sort():
    global tim
    tim=Tk()
    tim.title("Bubble Sort")
    tim.geometry("800x400+700+400")
    label = Label( tim, text="Time Complexity=O(n^2)" )
     
    l1=Label( tim, text="Application Of Bubble Sort" )
    l2=Label( tim, text="Bubble sort is a sorting algorithm that is used to sort the elements in an ascending order. ")
    l3=Label( tim, text="It uses less storage space. Bubble sort can be beneficial to sort the unsorted elements in a specific order.")
    l4=Label( tim, text=" It can be used to sort the students on basis of their height")
   
    

    label.grid()
    l1.grid()
    l2.grid()
    l3.grid()
    l4.grid()

    
    
    tim.after(400,lambda:bubble())

def bubble():
    global barlist
    global datalist
    global oblist
    
    for i in range(len(datalist) - 1):
        for j in range(len(datalist) - i - 1):
            if(datalist[j] > datalist[j + 1]):
                datalist[j] , datalist[j + 1] = datalist[j + 1] , datalist[j]
                barlist[j], barlist[j + 1] = barlist[j + 1] , barlist[j]
                oblist[j],oblist[j+1]=oblist[j+1],oblist[j]
                swap_pos(barlist[j + 1] , barlist[j],oblist[j+1],oblist[j])
  
        
def insertion_sort():
    global tim
    tim=Tk()
    tim.title("Insertion Sort")
    tim.geometry("800x400+700+400")
    label = Label( tim, text="Time Complexity=O(n^2)" )
    l1=Label( tim, text="Application Of Insertion Sort" )
    l2=Label( tim, text="Insertion sort is the best algorithm when the number of elements is small i.e. for a small input size.")
    l3=Label( tim, text="Insertion sort is also the best when the data is already sorted.")
    l4=Label( tim, text=" This is because insertion sort takes the least execution time in such a case as compared to other sorting techniques.")
    l5=Label( tim, text=" When we don't have access to all the data initially, we use insertion sort.")
    l6=Label( tim, text=" This is because insertion sort never requires all the elements at a time for sorting.")
    

    label.grid()
    l1.grid()
    l2.grid()
    l3.grid()
    l4.grid()
    l5.grid()
    l6.grid()
    
    tim.after(4,lambda:insert())
def insert():
    global barlist
    global datalist
    global oblist

    for i in range(len(datalist)):
        cursor = datalist[i]
        cursorBar = barlist[i]
        pos = i

        while pos > 0 and datalist[pos - 1] > cursor:
            datalist[pos] = datalist[pos - 1]
            barlist[pos], barlist[pos - 1] = barlist[pos - 1], barlist[pos]
            oblist[pos],oblist[pos-1]=oblist[pos-1],oblist[pos]
            swap_pos(barlist[pos],barlist[pos-1],oblist[pos],oblist[pos-1])                                        
            pos -= 1                                   

        datalist[pos] = cursor
        barlist[pos] = cursorBar

def partition(array, start, end):
    global datalist
    global barlist
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
            barlist[low],barlist[high]=barlist[high],barlist[low]
            oblist[low],oblist[high]=oblist[high],oblist[low]
            swap_pos(barlist[low],barlist[high],oblist[low],oblist[high])
        else:
            break

    array[start], array[high] = array[high], array[start]
    barlist[start],barlist[high]=barlist[high],barlist[start]
    oblist[start],oblist[high]=oblist[high],oblist[start]
    swap_pos(barlist[start],barlist[high],oblist[start],oblist[high])
    return high

def quick_sort(array, start, end):
    global barlist
    global datalist
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


def Quick_sort():
    global tim
    tim=Tk()
    tim.title("Quick Sort")
    tim.geometry("800x400+700+400")
    label = Label( tim, text="Time Complexity=O(n*logn)" )
    l1=Label( tim, text="Application Of Quick Sort" )
    l2=Label( tim, text="Quicksort is a cache-friendly algorithm as it has a good locality of reference when used for arrays.")
    l3=Label( tim, text="It is tail -recursive and hence all the call optimization can be done.")
    l4=Label( tim, text="It is an in-place sort that does not require any extra storage memory.")

    label.grid()
    l1.grid()
    l2.grid()
    l3.grid()
    l4.grid()

   
    tim.after(400,lambda:quick())
    
    
    
    

def quick():
    global tim
    global barlist
    global datalist
    


    data = datalist
    print("Unsorted Array")
    print(data)
    print("quick",barlist)
 
    size = len(data)
 
    quick_sort(data, 0, size - 1)
 
    print('Sorted Array in Ascending Order:')
    print(data)
    print("Barlist sort",barlist)


def heapify(n, i):

    
    global datalist
    global barlist
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and datalist[i] < datalist[l]:
        largest = l

    if r < n and datalist[largest] < datalist[r]:
        largest = r

    if largest != i:
        datalist[i], datalist[largest] = datalist[largest], datalist[i]
        barlist[i], barlist[largest] = barlist[largest], barlist[i]
        oblist[i], oblist[largest] = oblist[largest], oblist[i]
        
        swap_pos(barlist[i],barlist[largest],oblist[i],oblist[largest])

        
        heapify(n, largest)


def heap_sort():
    global tim
    tim=Tk()
    tim.title("Heap Sort")
    tim.geometry("800x400+700+400")
    label = Label( tim, text="Time Complexity=O(n*logn)" )
    l1=Label( tim, text="Application Of Heap Sort" )
    l2=Label( tim, text="Heap Sort in Data Structure is used when the smallest (shortest) or highest (longest) value is needed instantly. ")
    l3=Label( tim, text="Other usages include finding the order in statistics, dealing with priority queues in Prim's algorithm ")
    l4=Label(tim,text="(also called the minimum spanning tree) and Huffman encoding or data compression")
    l5=Label( tim, text="Heap Sorting can be applied to a sim card store where there are many customers in line.")
    l6=Label( tim, text="The customers who have to pay bills can be dealt with first because their work will take less time.")
    l7=Label( tim, text="This method will save time for many customers in line and avoid unnecessary waiting.")
    label.grid()
    l1.grid()
    l2.grid()
    l3.grid()
    l4.grid()
    l5.grid()
    l6.grid()
    l7.grid()
    
    
    tim.after(400,lambda:heap())

def heap():
    global datalist
    global barlist
    n = len(datalist)

    for i in range(n // 2, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        datalist[i], datalist[0] = datalist[0], datalist[i]
        barlist[i], barlist[0] = barlist[0], barlist[i]
        oblist[i], oblist[0] = oblist[0], oblist[i]
        swap_pos(barlist[0],barlist[i],oblist[0],oblist[i])

        heapify(i, 0)






def cocktailSort():
    global tim
    tim=Tk()
    tim.title("Cocktail Sort")
    tim.geometry("800x400+700+400")
    label = Label( tim, text="Time Complexity=O(n^2)" )
    l1=Label( tim, text="Application Of Cocktail Sort" )
    l2=Label( tim, text="Cocktail sort passes through the list both from left to right and from right to left.")
    l3=Label( tim, text="However, bubble sort just passes through in one direction in each iteration.")
    l4=Label( tim, text="Another advantage of the cocktail sort is that since it checks the list in both directions, the range of possible swaps will reduce per pass.")
    label.grid()
    l1.grid()
    l2.grid()
    l3.grid()
    l4.grid()
    tim.after(400,lambda:csort())


def csort():
    global datalist
    global barlist
    n = len(datalist)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):

  
        swapped = False

        for i in range(start, end):      #MAYBE WE CAN USE barlist here. like the elements which needs to be swapped and are being compared
            if (datalist[i] > datalist[i + 1]):
                datalist[i], datalist[i + 1] = datalist[i + 1], datalist[i]
                barlist[i],barlist[i+1]=barlist[i+1],barlist[i]
                oblist[i],oblist[i+1]=oblist[i+1],oblist[i]
                swap_pos(barlist[i+1],barlist[i],oblist[i+1],oblist[i])
                swapped = True


        if (swapped == False):
            break

        swapped = False


        end = end-1


        for i in range(end-1, start-1, -1):
            if (datalist[i] > datalist[i + 1]):
                datalist[i], datalist[i + 1] =datalist[i + 1],datalist[i]
                barlist[i],barlist[i+1]=barlist[i+1],barlist[i]
                oblist[i],oblist[i+1]=oblist[i+1],oblist[i]
                swap_pos(barlist[i+1],barlist[i],oblist[i+1],oblist[i])
                swapped = True

    start = start + 1


def ShellSort():
    global tim
    tim=Tk()
    tim.title("Shell Sort")
    tim.geometry("800x400+700+400")
    label = Label( tim, text="Time Complexity=θ(n log(n))" )
    l1=Label( tim, text="Application Of Shell Sort" )
    l2=Label( tim, text="Shellsort performs more operations and has higher cache miss ratio than quicksort.")
    l3=Label( tim, text="However, since it can be implemented using little code and does not use the call stack,")
    l4=Label(tim,text=" some implementations of the qsort function in the C standard library targeted at embedded systems use it instead of quicksort. ")
    l5=Label( tim, text=" Shellsort is, for example, used in the uClibc library.")
    l6=Label( tim, text=" For similar reasons, an implementation of Shellsort is present in the Linux kernel.")
    l7=Label( tim, text=" Shellsort can also serve as a sub-algorithm of introspective sort, to sort short subarrays and to prevent a slowdown when the recursion depth exceeds a given limit")
    label.grid()
    l1.grid()
    l2.grid()
    l3.grid()
    l4.grid()
    l5.grid()
    l6.grid()
    l7.grid()
    tim.after(400,lambda:shell_sort())






def shell_sort():
    global datalist
    global barlist
    global oblist
    n=len(datalist)
 
    h = n // 2
    while h > 0:
        for i in range(h, n):
            t = datalist[i]
            j = i
            while j >= h and datalist[j - h] > t:
                datalist[j],datalist[j-h] = datalist[j - h],datalist[j]
                barlist[j],barlist[j-h] = barlist[j-h],barlist[j]
                oblist[j],oblist[j-h] = oblist[j-h],oblist[j]
                swap_pos(barlist[j-h],barlist[j],oblist[j-h],oblist[j]) 
                j -= h
 
            datalist[j] = t
        h = h // 2

def merge(l, m, r):
    global datalist
    global barlist
    global oblist
    global ab
    
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
    Lbar = [0] * (n1)
    Rbar = [0] * (n2)
    Lnum = [0] * (n1)
    Rnum = [0] * (n2)
    
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = datalist[l + i]
        Lbar[i]=barlist[l+i]
        Lnum[i]=oblist[l+i]
        
    
 
    for j in range(0, n2):
        R[j] = datalist[m + 1 + j]
        Rbar[j] = barlist[m + 1 + j]
        Rnum[j] = oblist[m + 1 + j]

    print("Barlist",barlist)
    print("right",Rbar)
    print("Left",Lbar)
        
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
    print("Lbar",Lbar)
    print("Rbar",Rbar)

    while i < n1 and j < n2:
        if L[i] <= R[j]:
           
            
            datalist[k] = L[i]
            t=Lbar[i]
            Obet= del_create(barlist[k],k)
            Lbar[i]=Obet
            barlist[k]=Lbar[i]
            for z in range(len(Rbar)):
                if (t==Rbar[z]):
                    Rbar[z]=Lbar[i]
                    print("new Rbar",Rbar)
                    print("New Lbar",Lbar)
                    
            
            
            
           
            
            i += 1
        else:
            
            datalist[k] = R[j]
            
            
            t=Rbar[j]
            obet=del_create(barlist[k],k)
            Rbar[j]=obet
            for z in range(len(Lbar)):
                if (t==Lbar[z]):
                    Lbar[z]=Rbar[j]
                    print("new Rbar",Rbar)
                    print("New Lbar",Lbar)
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
       
        datalist[k] = L[i]
        
        t=Lbar[i]
        obet= del_create(barlist[k],k)
        Lbar[i]=obet
        for z in range(len(Rbar)):
            if (t==Rbar[z]):
                Rbar[z]=Lbar[i]
                print("new Rbar",Rbar)
                print("New Lbar",Lbar)

            

        
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
      
        datalist[k] = R[j]
        
        t=Rbar[j]
        obet=del_create(barlist[k],k)
        Rbar[j]=obet
        for z in range(len(Lbar)):
            if (t==Lbar[z]):
                Lbar[z]=Rbar[j]
                print("new Rbar",Rbar)
                print("New Lbar",Lbar)
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(l, r):
    
    global datalist
    global barlist
    global ab
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort( l, m)
        mergeSort (m+1, r)
        merge(l,m, r)
        print("datalist",datalist)
        print("barlist",barlist)
        print("ab",ab)



def merge_sort():
    global datalist
    global oblist
    global window
    n=len(datalist)
    global tim
    tim=Tk()
    tim.title("Merge Sort")
    tim.geometry("800x400+700+400")
    label = Label( tim, text="Time Complexity=θ(n log(n))" )
    l1=Label( tim, text="Application Of Merge Sort" )
    l2=Label( tim, text="Merge Sort is useful for sorting linked lists in O(n Log n) time.")
    l3=Label( tim, text="Merge sort can be implemented without extra space for linked lists.")
    l4=Label(tim,text=" Merge sort is used for counting inversions in a list. ")
    l5=Label( tim, text=" Merge sort is used in external sorting.")
   
    label.grid()
    l1.grid()
    l2.grid()
    l3.grid()
    l4.grid()
    l5.grid()
  
    tim.after(400,lambda:mergeSort(0,n-1))
    
    


def odd_even_sort():
    global datalist
    global barlist
    global oblist
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(datalist)-1, 2):
            if datalist[i] > datalist[i+1]:
                datalist[i], datalist[i+1] = datalist[i+1], datalist[i]
                barlist[i], barlist[i+1] = barlist[i+1], barlist[i]
                oblist[i], oblist[i+1] = oblist[i+1], oblist[i]
                swap_pos(barlist[i],barlist[i+1],oblist[i],oblist[i+1])
                sorted = False

        for i in range(0, len(datalist)-1, 2):
            if datalist[i] > datalist[i+1]:
                datalist[i], datalist[i+1] = datalist[i+1], datalist[i]
                barlist[i], barlist[i+1] = barlist[i+1], barlist[i]
                oblist[i], oblist[i+1] = oblist[i+1], oblist[i]
                swap_pos(barlist[i],barlist[i+1],oblist[i],oblist[i+1])
                sorted = False
    print(datalist)


def bricksort():
    global tim
    tim=Tk()
    tim.title("Brick Sort")
    tim.geometry("800x400+700+400")
    label = Label( tim, text="Time Complexity=O(N^2)" )
    l1=Label( tim, text="Application Of Brick Sort" )
    l2=Label( tim, text="Brick Sort uses parallel algorithm which is based on bubble sort technique.")
    l3=Label( tim, text="Sorting a list of elements is a very common operation")
    l4=Label(tim,text="  A sequential sorting algorithm may not be efficient enough when we have to sort a huge volume of data. ")
    l5=Label( tim, text=" Therefore, parallel algorithms are used in sorting.")
    
    label.grid()
    l1.grid()
    l2.grid()
    l3.grid()
    l4.grid()
    l5.grid()
    
    tim.after(400,lambda:odd_even_sort())





def flip(k):
    global datalist
    global barlist
    global oblist
  
    left = 0
    while left < k:
        datalist[left], datalist[k] = datalist[k], datalist[left]
        barlist[left], barlist[k] = barlist[k], barlist[left]
        oblist[left], oblist[k] = oblist[k], oblist[left]
        swap_pos(barlist[left],barlist[k],oblist[left],oblist[k])

        k -= 1
        left += 1

def max_index(k):
    global datalist

    index = 0
    for i in range(k):
        if datalist[i] > datalist[index]:
            index = i
    return index

def pancake_sort():
    global datalist
    n = len(datalist)
    while n > 1:
        maxdex = max_index(n)
        if maxdex != n:
            flip(maxdex)
            flip(n - 1)
        n -= 1

def pancake_display():
    global tim
    tim=Tk()
    tim.title("Pancake Sort")
    tim.geometry("800x400+700+400")
    label = Label( tim, text="Time Complexity= O(n^2)" )
    l1=Label( tim, text="Application Of Pancake Sort" )
    l2=Label( tim, text="Pancake sorting appears in applications in parallel processor networks,")
    l3=Label( tim, text="in which it can provide an effective routing algorithm between processors.")
    l4=Label(tim,text="  It is used when the only allowed operation to sort a sequence is reversing. ")
   
    
    label.grid()
    l1.grid()
    l2.grid()
    l3.grid()
    l4.grid()
    
    
    tim.after(400,lambda:pancake_sort())
    



def gnomeSort():
    global datalist
    global barlist
    global oblist
    n=len(datalist)

    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if datalist[index] >= datalist[index - 1]:
            index = index + 1
        else:
            datalist[index], datalist[index-1] = datalist[index-1], datalist[index]
            barlist[index], barlist[index-1] = barlist[index-1], barlist[index]
            oblist[index], oblist[index-1] = oblist[index-1], oblist[index]
            swap_pos(barlist[index],barlist[index-1],oblist[index],oblist[index-1])
            index = index - 1

def gnome_display():
    global tim
    tim=Tk()
    tim.title("Gnome Sort")
    tim.geometry("800x400+700+400")
    label = Label( tim, text="Time Complexity= O(N^2)" )
    l1=Label( tim, text="Application Of Gnome Sort" )
    l2=Label( tim, text="Gnome Sort also called Stupid sort is based on the concept of a Garden Gnome sorting his flower pots.")
    l3=Label( tim, text="Gnome sort works by building a sorted list one element at a time,")
    l4=Label(tim,text="  getting each item to the proper place in a series of swaps. ")
    l5=Label(tim,text="Gnome sort performs at least as many comparisons as insertion sort,")
    l6=Label(tim,text="and has the same asymptotic runtime characteristics")
   
   
    
    label.grid()
    l1.grid()
    l2.grid()
    l3.grid()
    l4.grid()
    l5.grid()
    l6.grid()
    
    
    tim.after(400,lambda:gnomeSort())
    





def getNextGap(gap):
 
   
    gap = (gap * 10)//13
    if gap < 1:
        return 1
    return gap
 

def combSort():
    global datalist
    global barlist
    global oblist
    n = len(datalist)
 
   
    gap = n
 
   
    
    swapped = True
 
    
    while gap !=1 or swapped == 1:
 
        
        gap = getNextGap(gap)
 
       
        swapped = False
 
        
        for i in range(0, n-gap):
            if datalist[i] > datalist[i + gap]:
                datalist[i], datalist[i + gap]=datalist[i + gap], datalist[i]
                barlist[i], barlist[i + gap]=barlist[i + gap], barlist[i]
                oblist[i], oblist[i + gap]=oblist[i + gap], oblist[i]
                swap_pos(barlist[i],barlist[i+gap],oblist[i],oblist[i+gap])
                swapped = True







 

def compAndSwap(a, i, j, dire):
    global datalist
    global barlist
    global oblist
    if (dire==1 and a[i] > a[j]) or (dire==0 and a[i] < a[j]):
        a[i],a[j] = a[j],a[i]
        barlist[i],barlist[j] = barlist[j],barlist[i]
        oblist[i],oblist[j] = oblist[j],oblist[i]
        swap_pos(barlist[i],barlist[j],oblist[i],oblist[j])

def comb_display():
    global tim
    tim=Tk()
    tim.title("Comb Sort")
    tim.geometry("800x400+700+400")
    label = Label( tim, text="Time Complexity= Ω(N^2/2^p)" )
    l1=Label( tim, text="Application Of Comb Sort" )
    l2=Label( tim, text="Comb Sort is mainly an improvement over Bubble Sort.")
    l3=Label( tim, text="Bubble sort always compares adjacent values. So all  are removed one by one.")
    l4=Label(tim,text="  Comb Sort improves on Bubble Sort by using a gap of the size of more than 1 ")
    l5=Label(tim,text="The gap starts with a large value and shrinks by a factor of 1.3 in every iteration until it reaches the value 1. ")
    l6=Label(tim,text="Thus Comb Sort removes more than one inversion count with one swap and performs better than Bubble Sort.")
   
   
    
    label.grid()
    l1.grid()
    l2.grid()
    l3.grid()
    l4.grid()
    l5.grid()
    l6.grid()
    
    
    tim.after(400,lambda:combSort())



 
# It recursively sorts a bitonic sequence in ascending order,
# if dir = 1, and in descending order otherwise (means dir=0).
# The sequence to be sorted starts at index position low,
# the parameter cnt is the number of elements to be sorted.
def bitonicMerge(a, low, cnt, dire):
    if cnt > 1:
        k = cnt//2
        for i in range(low , low+k):
            compAndSwap(a, i, i+k, dire)
        bitonicMerge(a, low, k, dire)
        bitonicMerge(a, low+k, k, dire)
 
# This function first produces a bitonic sequence by recursively
# sorting its two halves in opposite sorting orders, and then
# calls bitonicMerge to make them in the same order
def bitonicSort(a, low, cnt,dire):
    if cnt > 1:
          k = cnt//2
          bitonicSort(a, low, k, 1)
          bitonicSort(a, low+k, k, 0)
          bitonicMerge(a, low, cnt, dire)
 
# Caller of bitonicSort for sorting the entire array of length N
# in ASCENDING order
def sort():
    global tim
    global datalist
    a=datalist
    n = len(a)
    up = 1
    
    
 
    tim=Tk()
    tim.title("Bitonic Sort")
    tim.geometry("800x400+700+400")
    label = Label( tim, text="Time Complexity= O(log^2 n)" )
    l1=Label( tim, text="Application Of Bitonic Sort" )
    l2=Label( tim, text="Bitonic Sort is a classic parallel algorithm for sorting")
    l3=Label( tim, text="Bitonic Sort can only be done if the number of elements to sort is 2^n.")
    l4=Label(tim,text="  The procedure of bitonic sequence fails if the number of elements is not in the aforementioned quantity precisely.")
    l5=Label(tim,text="The number of comparisons done by Bitonic sort is more than popular sorting algorithms like Merge Sort. ")
    l6=Label(tim,text=", but Bitonic sort is better for parallel implementation because we always compare elements in a predefined,")
    l7=Label(tim,text="sequence and the sequence of comparison doesn’t depend on data. ")
    l8=Label(tim,text="Therefore it is suitable for implementation in hardware and parallel processor array.")
   
   
    
    label.grid()
    l1.grid()
    l2.grid()
    l3.grid()
    l4.grid()
    l5.grid()
    l6.grid()
    
    
    tim.after(400,lambda:bitonicSort(a,0, n, up))
   









 
    


def generate_data():
    global barlist
    global datalist
    global size
    global max_value
    global oblist
    global flag
    global ab
    global scrollbar
    
    
    if(flag==0):
        barlist=[]
        datalist=[]
        for i in range(size):
            random_num=random.randint(1,max_value)
            datalist.append(random_num)
            ab.append(random_num)

    canv.delete('all')
    x1_barstart=5
    x2_barend=25
    y=10
    
    
    muit=(480/max_value)
    
    for i in range(size):
        print(i)
        bar=canv.create_rectangle(x1_barstart, (480-(datalist[i]*muit)), x2_barend,480, fill="ivory4",outline='GhostWhite',tag=datalist)
        ob=canv.create_text(x1_barstart+10, 450, text=datalist[i])
        
        x1_barstart+=30
        x2_barend+=30
        barlist.append(bar)
        oblist.append(ob)
        
    print("total",barlist)
    for i in range(len(datalist)):
        if datalist[i] == min(datalist):
            canv.itemconfig(barlist[i], fill='aquamarine4')
        elif datalist[i] == max(datalist):
            canv.itemconfig(barlist[i], fill='gold')
    
    scrollbar.config( command = canv.xview )
    
  
    
           






def Sorting_visualizer():
    global size
    global window
    global canv
    global max_value
    global ti
    global datalist
    global choice
    global flag
    global root
    global t
    global shuf_1
    global scrollbar
    if(flag==0):
        if(t==0):
            choice=int(d.get())
            t=1
    if(choice==1 and shuf_1==0):
        size=int(a.get())
        max_value=int(b.get())
        ti=float(c.get())
        shuf_1=1
    elif(flag==1 and choice!=1):
        size=len(datalist)
        max_value=max(datalist)
        ti=0.3
    elif(shuf_1==0):
        draw_input()
    
    if(win!=0):
        win.destroy()

    window=Tk()
    window.title("Sorting Visualizer")
    canv = Canvas(window, bg="snow1",height=480, width=1550)
    scrollbar = Scrollbar(window, orient='horizontal')
    
    generate_data()
    if(root!=0 and t==1):
        root.destroy()
        root=0
    
    
    
    Shuf=Button(window,text="Shuffle" ,command=choice_enter)
    Dest=Button(window,text="STOP",command=window.destroy)
    
    Insert=Button(window,text="Insertion Sort",command=insertion_sort)
    Bubble=Button(window,text="Bubble Sort",command=bubble_sort)
    Select=Button(window,text="Selection Sort",command=selection_sort)
    Quick=Button(window,text="Quicksort",command=Quick_sort)
    Heap=Button(window,text="Heapsort",command=heap_sort)
    Cocktail=Button(window,text="Cocktail Sort",command=cocktailSort)
    shell=Button(window,text="Shell Sort",command=ShellSort)
    Merge=Button(window,text="Merge Sort",command=merge_sort)
    brick=Button(window,text="Brick sort",command=bricksort)
    pancake=Button(window,text="Pancake Sort",command=pancake_display)
    gnome=Button(window,text="Gnome Sort",command=gnome_display)
    comb=Button(window,text="Comb Sort",command=comb_display)
    biot=Button(window,text="Bitonic Sort",command=sort)
    


    canv.grid(row=0,column=0,columnspan=60)
    Shuf.grid(row=1,column=0)
   
    Insert.grid(row=1,column=1)
    Bubble.grid(row=1,column=2)
    Select.grid(row=1,column=3)
    Quick.grid(row=1,column=4)
    Heap.grid(row=1,column=5)
    Cocktail.grid(row=1,column=6)
    shell.grid(row=1,column=7)
    Merge.grid(row=1,column=8)
    brick.grid(row=1,column=9)
    pancake.grid(row=1,column=10)
    gnome.grid(row=1,column=11)
    comb.grid(row=1,column=12)
    biot.grid(row=1,column=13)
    


    
    Dest.grid(row=1,column=14)
    scrollbar.grid()
    
    
    



    window.state('zoomed')#fullscreen
    






# Import the required libraries
import math
def draw_input():
    global win
    global flag
# Create an instance of tkinter frame or window
    win=Tk()
# Set the size of the window
    win.title("Creative Input")
    win.geometry("700x500")
    flag=1

# Define a function to draw the line between two points
    def draw_line(event):
        global datalist
        global click_num
        global x1,y1
        global arr
        canvas.delete('all')
        if click_num==0:
                x1=event.x
                y1=event.y
                click_num=1
        else:
            x2=event.x
            y2=event.y
   # Draw the line in the given co-ordinates
            canvas.create_line(x1,y1,x2,y2, fill="ivory4", width=10)
            euclidian_dist=int(math.sqrt(math.pow((x2-x1),2)+math.pow((x2-x1),2)))
            datalist.append(euclidian_dist)
            ab.append(euclidian_dist)
            print(datalist)
    
   

# Create a canvas widget
    canvas=Canvas(win, width=700, height=350, background="ghostwhite")
    canvas.grid(row=0, column=0)
    canvas.bind('<Button-1>', draw_line)
    click_num=0

    Dest=Button(win,text="SUBMIT",command=Sorting_visualizer)
    Dest.grid(row=1,column=0)
    win.mainloop()



def choice_enter():
    global window
    global datalist
    global barlist
    global oblist
    oblist=[]
    datalist=[]
    barlist=[]
    window.destroy()
    if(flag==1):
        draw_input()
    else:
        Sorting_visualizer()


if(mai_camel==0):
    root=Tk()
    root.title("Input Window")
    root.geometry('600x400')
    text=Label(root, text="Enter the size of the array :", font=('Calibri 10'))
    text.pack()
    a=Entry(root, width=35)
    a.pack()
    text_1=Label(root, text="Maximum value :", font=('Calibri 10'))
    text_1.pack()
    b=Entry(root, width=35)
    b.pack()
    text_2=Label(root, text="Speed in seconds :", font=('Calibri 10'))
    text_2.pack()
    c=Entry(root, width=35)
    c.pack()
    text_3=Label(root, text="Press 1 for normal input ; Press any other number for creative input :", font=('Calibri 10'))
    text_3.pack()
    d=Entry(root, width=35)
    d.pack()
    btn = Button(root,text ="SUBMIT",command = Sorting_visualizer)

    btn.pack(pady=10)
    mai_camel=1
    mainloop()
