import flet as ft


def main(page: ft.Page):
    page.title = 'Simple calculator'
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(ft.SafeArea(ft.Text("Simple calculator")))
    
    def somar(e, r_text):
        n1 = float(caixa_n1.value)
        n2 = float(caixa_n2.value)
        op = caixa_op.value
        if op == '+':
            r = n1 + n2
        elif op == '-':
            r = n1 - n2
        elif op == '*':
            r = n1 * n2
        elif op == '/':
            r = n1 / n2
        else:
            r_text.value = 'erro'
            page.update()
            return
        print(r)
        r_text.value = str(r)
        page.update()

    # Criar os itens
    caixa_n1 = ft.TextField(value='0', width=100, text_align=ft.TextAlign.CENTER)
    caixa_op = ft.Dropdown(label='', options=[ft.dropdown.Option("+"),ft.dropdown.Option("-"), ft.dropdown.Option("*"), ft.dropdown.Option("/")],  width=50)
    caixa_n2 = ft.TextField(value='0', width=100, text_align=ft.TextAlign.CENTER)
    botao_somar = ft.OutlinedButton('=', on_click=lambda e: somar(e, r_text))
    r_text = ft.Text(value="0")

    # Adicionar os itens na página
    page.add(
        ft.Row([caixa_n1, caixa_op, caixa_n2], 
                alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([botao_somar], 
                alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([r_text], 
                alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(main)
