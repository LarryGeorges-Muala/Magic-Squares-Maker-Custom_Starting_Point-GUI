#App Name: Magic Square Maker with Custom starting point - Python
#Python Version 3.5
#Developper: Larry Georges Muala

import tkinter
from tkinter import messagebox

window = tkinter.Tk()

window.title('Magic Square Maker')

#Disable maximize button
window.resizable(0,0)

#Modify window icon
#window.wm_iconbitmap('lelu.ico')

#Set window background color
window.configure(background="gray2")

#############################################################
#Menu Bar

def about_app():
	print("App Name: Magic Square Maker with Custom starting point - GUI")
	print("App Description: Magic Square Maker with Custom starting point GUI using tkinter")
	print("Python Version 3.5")
	print("Developper: Larry Georges Muala")
	
	messagebox.showinfo("App Info", "App Name: Magic Square Maker GUI\n" + 
						"\nApp description: Magic Square Maker GUI using tkinter\n" + 
						"\nPython Version 3.5 \n" + 
						"\nDevelopper: Larry Georges Muala")
#Menu design
menubar = tkinter.Menu(window)
myMenu = tkinter.Menu(menubar, tearoff=0)
myMenu.add_command(label="About", command=about_app)
myMenu.add_separator()
myMenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="App Info", menu=myMenu)

#Display menu
window.config(menu=menubar)

#############################################################

#magic square maker command
def squareMaker():		
	#ask user for size of magic square
	var_size = ent_size.get()
	
	#check that the input is a number
	if var_size.isdigit():
	
		n = int(var_size)
	
		#check that the input is odd
		if n % 2 != 0:
			clear_all()
			btn_generate = tkinter.Button(window, text="Create", command=squareMaker)
			btn_generate.grid()
			magicSquare(n)
			ent_size.focus()

		
		else:
			messagebox.showerror("Error", "Please enter an odd number")
			ent_size.delete(0, tkinter.END)
			ent_size.focus()
	else:
		messagebox.showerror("Error", "Please enter an odd number")
		ent_size.delete(0, tkinter.END)
		ent_size.focus()

#magic square maker on Enter button keyboard		
def squareMakerOnEnter(event):		
	#ask user for size of magic square
	var_size = ent_size.get()
	
	#check that the input is a number
	if var_size.isdigit():
	
		n = int(var_size)
	
		#check that the input is odd
		if n % 2 != 0:
			clear_all()
			btn_generate = tkinter.Button(window, text="Create", command=squareMaker)
			btn_generate.grid()
			magicSquare(n)
			ent_size.focus()

		
		else:
			messagebox.showerror("Error", "Please enter an odd number")
			ent_size.delete(0, tkinter.END)
			ent_size.focus()
	else:
		messagebox.showerror("Error", "Please enter an odd number")
		ent_size.delete(0, tkinter.END)
		ent_size.focus()

		
#magic square drawing function		
def magicSquare(n):	
	
	
	#creating the magic square layout and populating it with zeros
	magic_list = [[ 0 for column_s in range(n) ] for row_s in range(n)]
	
	magic_list_reverse = []
	magic_list_temp = []
	magic_list_temp2 = []
	magic_list_temp3 = []
	magic_list_temp4 = []
	
	
	#Top Middle Starting Point Function
	def top_Middle():
		#loops to assign magic square values to each entry in magic_list
		#using formula:
		# for Ith row and Jth column
		# value = { n*[(I + J - 1 + (n//2)) % n)] } + { [(I + 2*J - 2) % n] + 1 }

		for row_s in range(n):
			for column_s in range(n):
			
				row_value = row_s + 1
				column_value = column_s + 1

				value = ( n * ((row_value + column_value - 1 + (n//2)) % n) ) + ( ((row_value + 2 * column_value - 2) % n) + 1 )
				
				magic_list[row_s][column_s] = value
				
				#creating single buttons for GUI with each value

				btn = tkinter.Button(window, text=value, font=("Helvetica", 10), height = 1, width = 5)
				btn.grid(row=row_value, column=column_value)

				
		print("")
		#formatting magic_list by splitting elements and joining by 4 digits space
		for m in range(n):
			print(' '.join( '{:4d}'.format(x) for x in magic_list[m] ))
	
	
	#Bottom Middle Starting Point Function
	def bottom_Middle():
		#loops to assign magic square values to each entry in magic_list
		#using formula:
		# for Ith row and Jth column
		# value = { n*[(I + J - 1 + (n//2)) % n)] } + { [(I + 2*J - 2) % n] + 1 }

		for row_s in range(n):
			for column_s in range(n):
			
				row_value = row_s + 1
				column_value = column_s + 1

				value = ( n * ((row_value + column_value - 1 + (n//2)) % n) ) + ( ((row_value + 2 * column_value - 2) % n) + 1 )
				
				magic_list[row_s][column_s] = value
				

		magic_list_reverse = magic_list[::-1]
		
		#creating single buttons for GUI with each value
		for x in range(len(magic_list_reverse)):
			for y in range(len(magic_list_reverse)):
				
				value = magic_list_reverse[x][y]
				
				row_value = x + 1
				column_value = y + 1
				
				btn = tkinter.Button(window, text=value, font=("Helvetica", 10), height = 1, width = 5)
				btn.grid(row=row_value, column=column_value)

				
		print("")
		#formatting magic_list by splitting elements and joining by 4 digits space
		for m in range(n):
			print(' '.join( '{:4d}'.format(x) for x in magic_list_reverse[m] ))
			
	
	#Left Middle Starting Point Function
	def left_Middle():
		#loops to assign magic square values to each entry in magic_list
		#using formula:
		# for Ith row and Jth column
		# value = { n*[(I + J - 1 + (n//2)) % n)] } + { [(I + 2*J - 2) % n] + 1 }

		for row_s in range(n):
			for column_s in range(n):
			
				row_value = row_s + 1
				column_value = column_s + 1

				value = ( n * ((row_value + column_value - 1 + (n//2)) % n) ) + ( ((row_value + 2 * column_value - 2) % n) + 1 )
				
				magic_list[row_s][column_s] = value
		
		
		#looping through magic_list to retrieve every single element of the list
		for y in range(n):
			for x in magic_list:
				magic_list_temp.append(x[y])
		
		#grouping elements to create a new positioning
		magic_list_temp2 = [magic_list_temp[x:x+n] for x in range(0, len(magic_list_temp), n)]
		
		#creating single buttons for GUI with each value
		for x in range(len(magic_list_temp2)):
			for y in range(len(magic_list_temp2)):
				
				value = magic_list_temp2[x][y]
				
				row_value = x + 1
				column_value = y + 1
				
				btn = tkinter.Button(window, text=value, font=("Helvetica", 10), height = 1, width = 5)
				btn.grid(row=row_value, column=column_value)

				
		print("")
		#formatting magic_list by splitting elements and joining by 4 digits space
		for m in range(n):
			print(' '.join( '{:4d}'.format(x) for x in magic_list_temp2[m] ))
			
			
	#Right Middle Starting Point Function
	def right_Middle():
		#loops to assign magic square values to each entry in magic_list
		#using formula:
		# for Ith row and Jth column
		# value = { n*[(I + J - 1 + (n//2)) % n)] } + { [(I + 2*J - 2) % n] + 1 }

		for row_s in range(n):
			for column_s in range(n):
			
				row_value = row_s + 1
				column_value = column_s + 1

				value = ( n * ((row_value + column_value - 1 + (n//2)) % n) ) + ( ((row_value + 2 * column_value - 2) % n) + 1 )
				
				magic_list[row_s][column_s] = value
				
		
		magic_list_reverse = magic_list[::-1]
		
		#looping through magic_list to retrieve every single element of the list
		for y in range(n):
			for x in magic_list_reverse:
				magic_list_temp3.append(x[y])
		
		#grouping elements to create a new positioning
		magic_list_temp4 = [magic_list_temp3[x:x+n] for x in range(0, len(magic_list_temp3), n)]
		
		#creating single buttons for GUI with each value
		for x in range(len(magic_list_temp4)):
			for y in range(len(magic_list_temp4)):
				
				value = magic_list_temp4[x][y]
				
				row_value = x + 1
				column_value = y + 1
				
				btn = tkinter.Button(window, text=value, font=("Helvetica", 10), height = 1, width = 5)
				btn.grid(row=row_value, column=column_value)

				
		print("")
		#formatting magic_list by splitting elements and joining by 4 digits space
		for m in range(n):
			print(' '.join( '{:4d}'.format(x) for x in magic_list_temp4[m] ))	

	
	
	if v.get() == 2:
		bottom_Middle()
		
	elif v.get() == 3:
		left_Middle()
		
	elif v.get() == 4:
		right_Middle()
		
	else:
		top_Middle()
	
	
#delete buttons created by previous magic squares		
def clear_all():
    for widget in window.winfo_children():      
        if widget.winfo_class() == 'Button':   
            widget.grid_remove()              

#welcome label
lbl_size = tkinter.Label(window, text="Please enter the size of the magic square: ", bg="gray2", fg="white")
lbl_size.grid()		

#size text entry
ent_size = tkinter.Entry(window)
ent_size.grid()
ent_size.focus()


#blankspace label
lbl_blank = tkinter.Label(window, text="", bg="gray2", fg="white")
lbl_blank.grid(sticky = tkinter.W)	

#starting point label
lbl_st = tkinter.Label(window, text="Starting Points: ", bg="gray2", fg="white")
lbl_st.grid(sticky = tkinter.W)	

#Starting points radio buttons

v = tkinter.IntVar()

rdb_top = tkinter.Radiobutton(window, text="Top Middle", variable=v, value=1, bg="gray2", fg="white", selectcolor="brown")
rdb_top.grid(sticky = tkinter.W)
rdb_top.select()

rdb_bottom = tkinter.Radiobutton(window, text="Bottom Middle", variable= v, value=2, bg="gray2", fg="white", selectcolor="brown")
rdb_bottom.grid(sticky = tkinter.W)

rdb_left = tkinter.Radiobutton(window, text="Left Middle", variable= v, value=3, bg="gray2", fg="white", selectcolor="brown")
rdb_left.grid(sticky = tkinter.W)

rdb_right = tkinter.Radiobutton(window, text="Right Middle", variable= v, value=4, bg="gray2", fg="white", selectcolor="brown")
rdb_right.grid(sticky = tkinter.W)


#bind function squareMaker to button Enter		
window.bind("<Return>", squareMakerOnEnter)

#square maker button		
btn_generate = tkinter.Button(window, text="Create", command=squareMaker)
btn_generate.grid()


	
window.mainloop()