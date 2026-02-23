import flet as ft

def main(page: ft.Page):
    txt = ft.TextField(value="",width=250,read_only=True)

    def add_digit(e):
        digit = e.control.text
        txt.value += digit
        txt.update()

    def calculate(e):
        formula = txt.value
        result = eval(formula)
        txt.value = result        
        txt.update()

    def delete(e):
        txt.value = ""
        txt.update()

    def tax(e):
        per = str(float(txt.value)*1.1)
        txt.value = per
        txt.update()

    def back(e):
        txt.value = txt.value[:-1]
        txt.update()

    bt1 = ft.ElevatedButton(text="c",height=60,width=60,on_click=delete)
    bt2 = ft.ElevatedButton(text="税込",height=60,width=60,on_click=tax)
    bt3 = ft.ElevatedButton(text="BS",height=60,width=60,on_click=back)
    bt4 = ft.ElevatedButton(text="/",height=60,width=60,on_click=add_digit)

    bt5 = ft.ElevatedButton(text="7",height=60,width=60,on_click=add_digit)
    bt6 = ft.ElevatedButton(text="8",height=60,width=60,on_click=add_digit)
    bt6 = ft.ElevatedButton(text="8",height=60,width=60,on_click=add_digit)
    bt7 = ft.ElevatedButton(text="9",height=60,width=60,on_click=add_digit)
    bt8 = ft.ElevatedButton(text="*",height=60,width=60,on_click=add_digit)

    bt9 = ft.ElevatedButton(text="4",height=60,width=60,on_click=add_digit)
    bt10 = ft.ElevatedButton(text="5",height=60,width=60,on_click=add_digit)
    bt11 = ft.ElevatedButton(text="6",height=60,width=60,on_click=add_digit)
    bt12 = ft.ElevatedButton(text="-",height=60,width=60,on_click=add_digit)

    bt13 = ft.ElevatedButton(text="1",height=60,width=60,on_click=add_digit)
    bt14 = ft.ElevatedButton(text="2",height=60,width=60,on_click=add_digit)
    bt15 = ft.ElevatedButton(text="3",height=60,width=60,on_click=add_digit)
    bt16 = ft.ElevatedButton(text="+",height=60,width=60,on_click=add_digit)

    bt17 = ft.ElevatedButton(text="0",height=60,width=60,on_click=add_digit)
    bt18 = ft.ElevatedButton(text="00",height=60,width=60,on_click=add_digit)
    bt19 = ft.ElevatedButton(text=".",height=60,width=60,on_click=add_digit)
    bt20 = ft.ElevatedButton(text="=",height=60,width=60,on_click=calculate)

    row1 = ft.Row(controls=[bt1,bt2,bt3,bt4])
    row2 = ft.Row(controls=[bt5,bt6,bt7,bt8])
    row3 = ft.Row(controls=[bt9,bt10,bt11,bt12])
    row4 = ft.Row(controls=[bt13,bt14,bt15,bt16])
    row5 = ft.Row(controls=[bt17,bt18,bt19,bt20])

    column = ft.Column(controls=[row1,row2,row3,row4,row5])

    page.add(txt,column)
ft.app(target=main)
