#Nesting List/Tuple/Set in List/Tuple/Set

aliens_pos = [ #(x,y)
	(3,4), # [0]
	(5,6), # [1]
	(-10, 50) # [2]
]

print("X1:", aliens_pos[0][0])
print("Y1:", aliens_pos[0][1])
print(aliens_pos[2][0]) #-10