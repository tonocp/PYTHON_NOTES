import notes.note as model


class Actions:

    def create(self, user):
        print(f"\nOk, {user[1]}, vamos a crear una nueva nota...")
        title = input("Introduce el título el título de la nota: ")
        description = input("Introduce el título la descripción de la nota: ")

        note = model.Note(user[0], title, description)
        save = note.save()

        if save[0] >= 1:
            print(f"\nLa nota '{note.title}' ha sido guardada!")
        else:
            print(f"\nNo se ha podido guardar la nota, {user[1]}.")

    def list(sef, user):
        print(f"\nOk {user[1]}, estas son tus notas:")
        note = model.Note(user[0])
        notes = note.list()
        for note in notes:
            print("\n*************************************")
            print(f"Título: {note[2]}")
            print(f"Descripción: {note[3]}")
            print("*************************************")

    def delete(self, user):
        print(f"\nOk {user[1]}, vamos a borrar una nota!")
        title = input("Introduce el título de la nota a borrar: ")
        note = model.Note(user[0], title)
        delete = note.delete()
        if delete[0] >= 1:
            print(f"Nota '{note.title}' borrada!")
        else:
            print("No se ha borrado la nota.")
