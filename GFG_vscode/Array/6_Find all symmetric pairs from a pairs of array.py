def symmetric_pair(arr):
    
    hash_map={}
    i=0
    while i<len(arr):
        first=arr[i][0]
        sec=arr[i][1]

        if sec in hash_map.keys() and hash_map[sec]==first:
            print(f"({sec},{first})")
        else:
            hash_map[first]=sec
        i+=1

def main():
    arr=[(1,5),(2,3),(4,2),(5,1),(2,4)]
    symmetric_pair(arr)

if __name__=="__main__":
    main()