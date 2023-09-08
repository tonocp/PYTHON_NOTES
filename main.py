from users import actions

print("""
Acciones disponibles:
      - registro
      - login
      """)

actions = actions.Actions()

selection = input("¿Qué quieres hacer?: ")

if selection == "registro":
    actions.register()

elif selection == "login":
    actions.login()
