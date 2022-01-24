"""
'Exercice' Ecrire le diagramme de classe correspondant au cas suivant:
Fort de votre expérience en pâtisserie, vous décidez de créer un forum en ligne pour parler de gâteaux !
- Vous devez définir et instancier trois classes: Utilisateurs (et ses héritiers), fil de discussion et post (et ses héritiers)


Sur ce forum
- les utilisateurs fans de pâtisserie pourront : s’inscrire et se connecter ;
- parler de leurs gâteaux préférés, en créant de nouveaux fils de discussion ;
- répondre à des messages, dans les fils existants.
- Un fil de discussion sur ce forum a un titre, une date de création et une collection de posts lui correspondant.
- Chaque post contient du texte, l’utilisateur qui l’a publié et la date de publication.
- Les utilisateurs ont la possibilité d’attacher des fichiers à leurs posts :
- Partez du principe qu’il peut y avoir de nombreux types de fichiers, mais nous sommes surtout intéressés par les fichiers images (GIF ou JPEP).
- Un post peut avoir un fichier attaché, ce qui changera la façon dont le post est affiché. Ce serait donc un nouveau type de post.
- Enfin, il y a des utilisateurs spéciaux nommés modérateurs, qui ont la capacité de modifier un post pour qu’il contienne du contenu nouveau,
et de supprimer ceux qui ne parlent pas de gâteaux.
"""

from datetime import datetime


class User:
    users = {}

    def __init__(self, name):
        self.name = name

    def signin(self, password):
        self.password = password
        print('You create an account!')

    def login(self, password):
        if self.password == password:
            self.status = "Connected"
        else:
            print("No account or incorrect password")

    def new_thread(self):
        return Thread()

    def new_post(self, th, post):
        th.add_post(post)
        print(f"A new post has been added to {th}")
        return post


class Moderator(User):
    def modify_post(self, th, post):
        if post in th.content:
            post.text = self.new_text


class Post:
    def __init__(self, user, text):
        self.user = user
        self.text = text
        self.creation_date = datetime.now()


class Thread:
    def __init__(self, title):
        self.title = title
        self.content = []
        self.creation_date = datetime.now()

    def add_post(self, post: Post):
        self.content.append(post)


class AttachmentPost(Post):
    def __init__(self, user, text, filetype):
        self.user = user
        self.text = text
        self.filetype = filetype
        self.creation_date = datetime.now()


my_name = User('Adrien')
my_name.signin('1234')

my_thread = Thread("The best cheesecake ever")
my_post = Post(my_name, "This is a text for the post.")
my_name.new_post(my_thread, my_post)
my_post_with_file = my_name.new_post(
    my_thread, AttachmentPost(my_name, "Content of my first post", filetype="GIF"))
print(my_thread.content)
