import flet as ft

def main(page: ft.Page):
    page.title = "Suma de dos números"
    page.window_width = 400
    page.window_height = 300

    # Campos de texto
    num1 = ft.TextField(label="Número 1", width=200)
    num2 = ft.TextField(label="Número 2", width=200)

    # Texto resultado
    resultado = ft.Text("Resultado: ", size=20)

    # Función sumar
    def sumar(e):
        try:
            r = float(num1.value) + float(num2.value)
            resultado.value = f"Resultado: {r}"
        except:
            resultado.value = "Error: Ingresa números válidos"
        page.update()

    # Botón
    boton = ft.ElevatedButton("Sumar",on_click=sumar)

    # Agregar a la ventana
    page.add(
        ft.Column(
            [
                num1,
                num2,
                boton,
                resultado
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

# Ejecutar app
ft.app(target=main)