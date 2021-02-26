import tkinter
import tkinter.ttk
import sqlite3
from tkinter import messagebox as mb
        
   
class Okno:
    def cost(self):
        try:
            id_price = self.c.execute(f"""SELECT id_type_of_price FROM type_of_prices
                                   WHERE type_of_price == '{self.combo_type_of_price.get()}';""").fetchall()
            self.cost = self.c.execute(f"""SELECT price FROM prices WHERE id_product == {self.entry_cod_product.get()}
                                   AND id_type_of_price == {id_price[0][0]};""").fetchall()
             
            self.label_cost.config(text=str(self.cost[0][0]))

            self.product = self.c.execute(f"""SELECT product_name FROM products
                                        WHERE id_product == {self.entry_cod_product.get()};""").fetchall()
             
            self.label1_product.config(text=str(self.product[0][0]))
             
        except Exception:
            mb.showerror('Ошибка',
                         'Указанный товар отсутствует в системе!')

    def calculate(self):
        try:
             self.value.config(text=str(float(self.quantity.get()) * self.cost[0][0]))
        except ValueError:
             mb.showerror('Ошибка',
                          'В поле "Количество" должно быть число!')
    def __del__(self):        
        self.c.close()
        self.conn.close()
        
    def __init__(self):
        self.conn = sqlite3.connect('sdelki_db.sqlite')
        self.c = self.conn.cursor()
               
        self.window = tkinter.Tk()
        self.window.title('Сделка')
        self.window.geometry("750x250")
        
        self.frame2 = tkinter.LabelFrame(self.window, padx=8, pady=8)
        self.frame2.pack(fill = 'both')

        self.frame1 = tkinter.LabelFrame(self.window, borderwidth = 4, relief = tkinter.GROOVE, padx=5, pady=5)
        self.frame1.pack(fill = 'both')
        
        self.label_cod_product = tkinter.Label(self.frame1, text = 'Код')
        self.label_cod_product.grid(column = 0, row = 7, pady = 10)
                

        self.entry_cod_product = tkinter.Entry(self.frame1, width = 10)
        self.entry_cod_product.grid(column = 0, row = 8)
        self.entry_cod_product.focus()

        self.label_product = tkinter.Label(self.frame1, text = 'Номенклатура')
        self.label_product.grid(column = 1, row = 7, pady = 10)
        

        self.label1_product = tkinter.Label(self.frame1, width = 35, bg = 'white', anchor="w")
        self.label1_product.grid(column = 1, row = 8, padx = 2)
        

        self.label_type_of_price = tkinter.Label(self.frame1, text = 'Вид цены')
        self.label_type_of_price.grid(column = 2, row = 7)
        
        self.combo_type_of_price = tkinter.ttk.Combobox(self.frame1, width = 10)
        self.combo_type_of_price['values'] = ('Розн','Worker','Опт')
        self.combo_type_of_price.grid(column = 2, row = 8)

        self.label_quantity = tkinter.Label(self.frame1, text = 'Количество', width = 12)
        self.label_quantity.grid(column = 3, row = 7)

        self.quantity = tkinter.Entry(self.frame1, width = 15)
        self.quantity.grid(column = 3, row = 8)

        self.label_price = tkinter.Label(self.frame1, text = 'Цена', width = 10)
        self.label_price.grid(column = 4, row = 7)

        self.label_cost = tkinter.Label(self.frame1, width = 15, bg = 'white')
        self.label_cost.grid(column = 4, row = 8, padx = 2)

        self.label_value = tkinter.Label(self.frame1, text = 'Стоимость', width = 15)
        self.label_value.grid(column = 5, row = 7)

        self.value = tkinter.Label(self.frame1, width = 15, bg = 'white')
        self.value.grid(column = 5, row = 8, padx = 2)
        

        self.button_exit = tkinter.Button(self.frame2, text = 'Закрыть', command = self.window.destroy, font=('Calibri', 10))
        self.button_exit.grid(column = 4, row = 0)

        self.button_cost = tkinter.Button(self.frame2, text = 'Заполнить цены и товары', command = self.cost, font=('Calibri', 10))
        self.button_cost.grid(column = 1, row = 0)

        self.button_calculate = tkinter.Button(self.frame2, text = 'Пересчитать цены', command = self.calculate, font=('Calibri', 10))
        self.button_calculate.grid(column = 2, row = 0)                                 
                                          
        
        self.label_status = tkinter.Label(self.frame2, text = 'Статус')
        self.label_status.grid(column = 5, row = 0)

        self.combo_status = tkinter.ttk.Combobox(self.frame2, width = 10)
        self.combo_status['values'] = ('В работе','Выиграна','К закрытию')
        self.combo_status.grid(column = 6, row = 0)

        self.chk_state = tkinter.BooleanVar()
              
        self.chk_complete = tkinter.ttk.Checkbutton(self.frame2, text = 'Завершена', var = self.chk_state)
        self.chk_complete.grid(column = 7, row = 0)

        tkinter.mainloop()

my_okno = Okno()
