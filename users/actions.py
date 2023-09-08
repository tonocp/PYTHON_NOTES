import users.user as model
import notes.actions


class Actions:
    def register(self):
        print("\nOk!, vayamos al registro!")

        name = input("¿Cuál es tu nombre?: ")
        surnames = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        user = model.User(name, surnames, email, password)
        register = user.register()

        if (register[0] >= 1):
            print(
                f"'{register[1].name}' te has registrado correctamente con el email: '{register[1].email}'")
        else:
            print("El registro no ha sido posible")

    def login(self):
        print("\nOk!, identifícate!")

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            user = model.User('', '', email, password)
            login = user.identify()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}!")
                self.actionMenu(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"\nLogin incorrecto!")

    def actionMenu(self, user):
        print("""
        Menú de Python Notes:
        - Crear Nota (crear)
        - Mostrar tus Notas (mostrar)
        - Eliminar Nota (eliminar)
        - Salir (salir)
        """)
        selection = input('¿Qué quieres hacer?: ')
        action = notes.actions.Actions()

        if selection == "crear":
            action.create(user)
            self.actionMenu(user)
        elif selection == "mostrar":
            action.list(user)
            self.actionMenu(user)
        elif selection == "eliminar":
            action.delete(user)
            self.actionMenu(user)
        elif selection == "salir":
            print(f"\n Hasta pronto, {user[1]}!")
            exit()
