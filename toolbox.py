"""
Exercice

Créer des classes: boite à outils, marteau, tournevis, clou, visse
Une boite à outil possède 5 emplacements. (classe attributs)
Régulièrement le constructeur des boites à outils sort un nouveau modèle qui permet d'etendre la capacité des boites à outils de 1.
Instanciez une boîte à outils, un tournevis, et un marteau.
Placez le marteau et le tournevis dans la boîte à outils.
Instanciez une vis, et serrez-la avec le tournevis. Affichez la vis avant et après avoir été serrée.
Instanciez un clou, puis enfoncez-le avec le marteau. Affichez le clou avant et après avoir été enfoncé.
Pour chaque classe vous devez définir les attributs et les méthodes qui permettront d'éxecuter et de rapporter dans le terminal ces actions et ces états.
"""


class ToolBox:
    compartment = 5
    tools = []

    def __init__(self):
        self.tools = []

    def new_version(self):
        self.compartment = self.compartment + 1
        print(f"New version, number of compartments now: {self.compartment}")

    def add_tool(self, tool):
        if len(self.tools) < self.compartment:
            self.tools.append(tool)
            self.compartment = self.compartment - 1
            print(
                f"You had a {tool} on the case, number of compartments free now: {self.compartment}")
        else:
            print("Too much tools in the box.")


class Nail:

    def __init__(self, status=False):
        self.status = status

    def to_nail(self):
        return self.status == True


class Hammer:

    def __init__(self):
        pass


class Screw:
    def __init__(self, type, status=False):
        self.status = status
        self.type = type

    def to_screw(self):
        self.status == True


class ScrewDriver:

    def __init__(self, type):
        self.type = type

    def is_ok_to_screw(self, screw: Screw):
        if self.type == screw.type:
            print("OK to Screw")
        else:
            print("NOT OK to Screw")


my_tool_box = ToolBox()
my_tool_box.new_version()
my_tool_box.new_version()
my_tool_box.new_version()
my_screwdriver = ScrewDriver('x')
my_hammer = Hammer()
my_tool_box.add_tool(my_screwdriver)
my_tool_box.add_tool(my_hammer)
my_screw = Screw('x')
my_nail = Nail()

my_screwdriver.is_ok_to_screw(my_screw)
print(my_screw.status)
my_screw.to_screw()
print(my_screw.status)

print(my_nail.status)
my_nail.to_nail()
print(my_nail.status)
