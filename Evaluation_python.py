"""Créer un système de gestion de bibliothèque simple qui permette de gérer les livres et les utilisateurs de la bibliothèque. Le système doit permettre aux utilisateurs dʼajouter et de
retirer des livres de la bibliothèque, de rechercher des livres par titre, par auteur ou catégorie, dʼenregistrer de nouveaux utilisateurs de la bibliothèque, dʼemprunter et de retourner
des livres, et de savoir qui détient un livre.
FONCTIONNALITÉS
1. Ajout et retrait de livres : Permettre à lʼutilisateur dʼajouter ou de retirer des livres de la bibliothèque.
2. Recherche de livres : Rechercher des livres par titre, par auteur ou par catégorie.
3. Enregistrement des utilisateurs : Enregistrer de nouveaux utilisateurs de la bibliothèque.
4. Emprunt et retour de livres : Permettre aux utilisateurs dʼemprunter et de retourner des livres (si un livre est pris, il nʼest plus disponible).
5. Sauvegarde de lʼétat : Sauvegarder lʼétat de la bibliothèque dans un fichier au format JSON.
"""
import json
import os
import sys
from abc import ABC, abstractmethod

class BaseLibrary(ABC):
    @abstractmethod
    def add_book(self, book):
        pass
    @abstractmethod
    def remove_book(self, book):
        pass
    @abstractmethod
    def search_book_by_title(self, book):
        pass
    @abstractmethod
    def search_user(self, user):
        pass
    @abstractmethod
    def add_user(self, user):
        pass
    @abstractmethod
    def remove_user(self, user):
        pass
    @abstractmethod
    def borrow_book(self, book):
        pass
    @abstractmethod
    def return_book(self, book):
        pass
    @abstractmethod
    def save(self):
        pass
    @abstractmethod
    def load(self):
        pass

class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category
        self.borrowed = False
        self.borrowed_by = None

class User:
    def __init__(self, name, surname, age, mail):
        self.name = name
        self.surname = surname
        self.age = age
        self.mail = mail
    def notifier(self, message = "Votre livre est désormais disponible"):
        print ("les utilisateurs ont bien été avertis")

class Library(BaseLibrary):
    
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, book):
        print(self.books)
        self.books.append(book)
    
    def display_books(self):
        print("Liste des livres:")
        if self.books != []:
            for book in self.books:
                print(f"- {book.title} par {book.author} ({book.category})")
        else :
            print("Aucun livre n'est disponible!")

    def remove_book(self, book):
        for b in self.books:
            if b == book:
                self.books.remove(b)
                break
            else:
                print(f"Book '{b.title}' by {b.author} not found in library.")
                
    def search_book_by_title(self, book):
        for b in self.books:
            if b.title == book:
                return b
            else :
                return None

    def search_book_by_author(self, book):
        for b in self.books:
            if b.author == book:
                return b
            else :
                return None

    def search_book_by_category(self, book):
        for b in self.books:
            if b.category == book:
                return b
            else :
                return None

    def search_user(self, mail):
        for u in self.users:
            if u.mail == mail:
                return u.mail
            else :
                return None  

    def add_user(self, user):
        self.users.append(user)
    
    def remove_user(self, user):
        for u in self.users:
            if u == user:
                self.users.remove(u)
                break
            else:
                print(f"Utilisateur non trouvé dans le registre.")
    
    def display_user(self):
        print("Liste des utilisateurs:")
        if self.users != []:
            for user in self.users:
                print(f"- {user.name} {user.surname} ({user.age})")
        else :
            print("Aucun utilisateur n'est disponible!")

    def borrow_book(self, book, user):
        if book.borrowed == False:
            book.borrowed = True
            book.borrowed_by = user
            print(user)
            print(f"L'utilisateur {user} a emprunté le livre {book.title}")
        else:
            print(f"Le livre {book.title} est déjà emprunté")
    
    def return_book(self, book, user):
        if book.borrowed == True:
            book.borrowed = False
            book.borrowed_by = None
            print(f"L'utilisateur {user.mail} a retourné le livre {book.title}")
        else:
            print(f"Le livre {book.title} n'est pas emprunté")
    
    def notifier(self, message):
        for user in self.users:
            user.notifier(message)

    def save(self):
        data = {
            "books": [book.__dict__ for book in self.books],
            "users": [user.__dict__ for user in self.users]
        }
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    
    def load(self):
        if os.path.exists("data.json"):
            with open("data.json", "r") as file:
                data = json.load(file)
                self.books = [Book(book["title"], book["author"], book["category"]) for book in data["books"]]
                self.users = [User(user["name"], user["surname"], user["age"], user["mail"]) for user in data["users"]]
        else:
            print("Aucune sauvegarde trouvée")
"""
Vous devez idéalement implémenter ces 4 design patterns (et/ou dʼautres) et les utiliser dans votre code, là où vous pensez que cela a du sens, les utilisations décrites ici sont de
simples suggestions.
1. Singleton : Pour gérer une instance unique de la base de données de la bibliothèque.
2. Factory : Pour créer des objets Livre ou Utilisateur.
3. Observer : Pour notifier les utilisateurs lorsquʼun livre recherché devient disponible.
4. Strategy : Pour différentes stratégies de recherche de livres.

Utilisation des design patterns 


class Singleton:
    pass
class Factory:
    pass

    
#strategy
class Search :
    def execute(self, book):
        pass
class Search_by_title(Search) :
    def execute(self, book):
        for b in self.books:
            if b.title == book:
                return b
            else :
                return None
            
class Search_by_author(Search):
    def execute(self, book):
        for b in self.books:
            if b.author == book:
                return b
            else :
                return None

class Search_by_category(Search):
    def execute(self, book):
        for b in self.books:
            if b.category == book:
                return b
            else :
                return None

class contexte:
    def __init__(self, strategie):
        self._strategie = strategie
    def execute(self, book):
        return self._strategie.execute(book)

#test
s1 = Search_by_title()
s2 = Search_by_author()
s3 = Search_by_category()
if choice == "3":
    contexte1 = contexte(s1)
if choice == "4":
    contexte2 = contexte(s2)
if choice == "5":
    contexte3 = contexte(s3)

"""

def main():
    library = Library()
    library.load()
    while True:
        print("1. Ajouter un livre")
        print("2. Retirer un livre")
        print("3. Rechercher un livre par titre")
        print("4. Rechercher un livre par auteur")
        print("5. Rechercher un livre par catégorie")
        print("6. Ajouter un utilisateur")
        print("7. Retirer un utilisateur")
        print("8. Emprunter un livre")
        print("9. Retourner un livre")
        print("10. Sauvegarder")
        print("11. Afficher les livres")
        print("12. Afficher les utilisateurs")
        print("13. Notifier les utilisateurs")
        print("14. Quitter")
        choice = input("Entrez votre choix: ")
    
        if choice == "1":
            title = input("Entrez le titre du livre: ")
            author = input("Entrez l'auteur du livre: ")
            category = input("Entrez la catégorie du livre: ")
            print("ajout en cours")
            book = Book(title, author, category)
            library.add_book(book)
            print("ajouté !")

        elif choice == "2":
            title = input("Entrez le titre du livre: ")
            book = library.search_book_by_title(title)
            library.remove_book(book)
            print("retrait effectué")
    
        elif choice == "3":
            title = input("Entrez le titre du livre: ")
            book = library.search_book_by_title(title)
            print(book)
        elif choice == "4":
            author = input("Entrez l'auteur du livre: ")
            book = library.search_book_by_author(author)
            print(book)
        elif choice == "5":
            category = input("Entrez la catégorie du livre: ")
            book = library.search_book_by_category(category)
            print(book)

        elif choice == "6":
            name = input("Entrez le nom de l'utilisateur: ")
            surname = input("Entrez le prénom de l'utilisateur: ")
            age = input("Entrez l'âge de l'utilisateur: ")
            mail = input("Entrez le mail de l'utilisateur: ")
            user = User(name, surname, age, mail)
            library.add_user(user)
    
        elif choice == "7":
            mail = input("Entrez le mail de l'utilisateur a supprimer: ")
            user = library.search_user(mail)
            print(user)
    
        elif choice == "8":
            title = input("Entrez le titre du livre: ")
            book = library.search_book_by_title(title)
            mail = input("Entrez le mail de l'utilisateur: ")
            print(mail)
            user = library.search_user(mail)
            print ("user", user)
            library.borrow_book(book, user)
    
        elif choice == "9":
            title = input("Entrez le titre du livre: ")
            book = library.search_book_by_title(title)
            mail = input("Entrez le mail de l'utilisateur: ")
            user = library.search_user(mail)
            library.return_book(book, user)
    
        elif choice == "10":
            library.save()
    
        elif choice == "11":
            library.display_books()
        elif choice == "12":
            library.display_user()
            
        elif choice == "13":
            library.notifier("livre disponible")

        elif choice == "14":
            library.save()
            sys.exit()
        else:
            print("Choix invalide")

if __name__ == "__main__":
    main()



