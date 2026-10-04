# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 

# for j in range(1,6,1):
#     for i in range(1,j+1,1):
#         print(j,end=" ")
#     print()


#         1 
#       2 2 
#     3 3 3 
#   4 4 4 4 
# 5 5 5 5 5 
# for j in range(1,6,1):
#     for s in range(5,j,-1):
#         print(" ",end=" ")
#     for i in range(1,j+1,1):
#         print(j,end=" ")
#     print()


# 5 
# 4 4 
# 3 3 3 
# 2 2 2 2 
# 1 1 1 1 1 

# for j in range(5,0,-1):
#     for i in range(5,j-1,-1):
#         print(j,end=" ")
#     print()


# 5 5 5 5 5 
#   4 4 4 4 
#     3 3 3 
#       2 2 
#         1 

# for j in range(5,0,-1):
#     for s in range(j,5,1):
#         print(" ",end=" ")
#     for i in range(1,j+1,1):
#         print(j,end=" ")
#     print()

#         1 
#       2 2 2 
#     3 3 3 3 3 
#   4 4 4 4 4 4 4 
# 5 5 5 5 5 5 5 5 5 
# for j in range(1,6,1):
#     for s in range(j,5,1):
#         print(" ",end=" ")
#     for i in range(1,j+1,1):
#         print(j,end=" ")
#     for k in range(2,j+1,1):
#         print(i,end=" ")
#     print()

# 5 5 5 5 5  5 5 5 5 
#   4 4 4 4  4 4 4 
#     3 3 3  3 3 
#       2 2  2 
#         1 
# for j in range(5,0,-1):
#     for s in range(j,5,1):
#         print(" ",end=" ")
#     for i in range(1,j+1,1):
#         print(j,end=" ")
#     for k in range(2,j+1,1):
#         print(i,end=" ")
#     print()


#         5 
#       4 4 4 
#     3 3 3 3 3 
#   2 2 2 2 2 2 2 
# 1 1 1 1 1 1 1 1 1 

# for j in range(5,0,-1):
#     for s in range(1,j,1):
#         print(" ",end=" ")
#     for i in range(5,j-1,-1):
#         print(j,end=" ")
#     for k in range(4,j-1,-1):
#         print(i,end=" ")
#     print()



# 1 1 1 1 1 1 1 1 1 
#   2 2 2 2 2 2 2 
#     3 3 3 3 3 
#       4 4 4 
#         5 

# for j in range(1,6,1):
    
#     for s in range(1,j,1):
#         print(" ",end=" ")
#     for i in range(5,j-1,-1):
#         print(j,end=" ")
#     for k in range(4,j-1,-1):
#         print(i,end=" ")
#     print()



#         5 
#       4 4 4 
#     3 3 3 3 3 
#   2 2 2 2 2 2 2 
# 1 1 1 1 1 1 1 1 1 
#   2 2 2 2 2 2 2 
#     3 3 3 3 3 
#       4 4 4 
#         5 

# for j in range(5,0,-1):
#     for s in range(1,j,1):
#         print(" ",end=" ")
#     for i in range(5,j-1,-1):
#         print(j,end=" ")
#     for k in range(4,j-1,-1):
#         print(i,end=" ")
#     print()
# for j in range(2,6,1):
#     for s in range(1,j,1):
#         print(" ",end=" ")
#     for i in range(5,j-1,-1):
#         print(j,end=" ")
#     for k in range(4,j-1,-1):
#         print(i,end=" ")
#     print()


#         5 
#       4 5 4 
#     3 4 5 4 3 
#   2 3 4 5 4 3 2 
# 1 2 3 4 5 4 3 2 1 
# for i in range(5,0,-1):
#     for s in range(1,i,1):
#         print(" ",end=" ")
#     for j in range(i,6):
#         print(j,end=" ")
#     for k in range(4,i-1,-1):
#         print(k,end=" ")
#     print()


#         5 
#       5 4 5 
#     5 4 3 4 5 
#   5 4 3 2 3 4 5 
# 5 4 3 2 1 2 3 4 5 
# for j in range(5,0,-1):
#     for s in range(1,j,1):
#         print(" ",end=" ")
#     for i in range(5,j-1,-1):
#         print(i,end=" ")
#     for k in range(j+1,6,1):
#         print(k,end=" ")
#     print()



# 5 4 3 2 1 2 3 4 5 
#   5 4 3 2 3 4 5 
#     5 4 3 4 5 
#       5 4 5 
#         5 
# for j in range(1,6,1):
#     for s in range(1,j,1):
#         print(" ",end=" ")
#     for i in range(5,j-1,-1):
#         print(i,end=" ")
#     for k in range(j+1,6,1):
#         print(k,end=" ") 
#     print()

# 1 2 3 4 5 4 3 2 1 
#   1 2 3 4 3 2 1 
#     1 2 3 2 1 
#       1 2 1 
#         1 
# for j in range(5,0,-1):
#     for s in range(5,j,-1):
#         print(" ",end=" ")
#     for i in range(1,j+1,1):
#         print(i,end=" ")
#     for k in range(j-1,0,-1):
#         print(k,end=" ") 
#     print()

# 5 4 3 2 1 2 3 4 5 
#   4 3 2 1 2 3 4 
#     3 2 1 2 3 
#       2 1 2 
#         1 
# for j in range(5,0,-1):
#     for s in range(5,j,-1):
#         print(" ",end=" ")
#     for i in range(j,0,-1):
#         print(i,end=" ")
#     for k in range(2,j+1,1):
#         print(k,end=" ")
#     print()


# 1 2 3 4 5 4 3 2 1 
#   2 3 4 5 4 3 2 
#     3 4 5 4 3 
#       4 5 4 
#         5 
# for j in range(1,6,1):
#     for s in range(1,j,1):
#         print(" ",end=" ")
#     for i in range(j,6,1):
#         print(i,end=" ")
#     for k in range(4,j-1,-1):
#         print(k,end=" ") 
#     print()
