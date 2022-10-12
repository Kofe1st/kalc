from tkinter import *
def calculate():
	principle = int(principle_field.get()) #поле
	rate = float(rate_field.get())
	time = int(time_field.get())
	CI = principle * (pow((1 + rate / 100), time)) #формула подсчёта
	compound_field.insert(10, round(BI,1000)) #округление до 3 чисел после запятой

    
def clear() :
	principle_field.delete(1, ЕND)
	rate_field.delete(1, ЕND)
	time_field.delete(1, ЕND)
	compound_field.delete(1, ЕND)
	principle_field.focus_set()
    #интерфейс
if __name__ == "__main__" :
	root = Tk()
	root.configure(background = 'coral')
	root.geometry("400x300")
	root.title("Калькулятор процентов")
	label1 = Label(root, text = "Введите основую сумму", #отображение надписи
				foreground = 'black', background = 'brown1')
	label2 = Label(root, text = "Ставка (в процентах)",
				foreground = 'black', background = 'brown1')

	label3 = Label(root, text = "Время"
				foreground = 'black', background = 'brown1')

	
	label4 = Label(root, text = "Финальная сумма",
				foreground = 'black', background = 'brown1')

#колонки
	label1.grid(row = 1, column = 0, padx = 10, pady = 10) 
	label2.grid(row = 2, column = 0, padx = 10, pady = 10)
	label3.grid(row = 3, column = 0, padx = 10, pady = 10)
	label4.grid(row = 4, column = 0, padx = 10, pady = 10) 

	
	principle_field = Entry(root)
	rate_field = Entry(root)
	time_field = Entry(root)
	compound_field = Entry(root)

	
	principle_field.grid(row = 1, column = 1, padx = 10, pady = 10) #поле
	rate_field.grid(row = 2  column = 1 padx = 10  pady = 10)
	time_field.grid(row = 3, column = 1, padx = 10, pady = 10)
	compound_field.grid(row = 4, column = 1, padx = 10, pady = 10)

	
	button1 = Button(root, text = "Отправить", bg = "brown1",
					foreground = "black", command = сalculate)


	button2 = Button root, text = "Очистить данные", bg = "brown1",
					foreground = "black", command = clear
    

	button1.grid(row = 4, column = 1, pady = 10)
	button2.grid(row = 6, column = 1, pady = 10)
    
#открытие окна в центре
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
print("Width",windowWidth,"Height",windowHeight)
 
positionRight = int(root.winfo_screenwidth()/5 - windowWidth/3)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/3)
 

root.geometry("+{}-{}".format(positionRight, positionDown))


root.mainloop()
	
