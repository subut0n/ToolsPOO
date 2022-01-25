
"""
Nous reprenons l’exemple du concessionnaire. Vous devez coder le cas suivant en testant les méthodes critiques:
Le concessionnaire possède un inventaire qui est une liste de véhicules. 
Il a sinon une adresse et un siret et également le moyen d’obtenir rapidement le nombre de véhicule de chaque marque dans son inventaire
Il peut ajouter des véhicules et en retirer à son inventaire.
Chaque véhicule a une couleur, une marque, un modèle, un prix hors taxe et TTC et une réduction applicable.
Chaque type de véhicules (voiture, moto, camion) a des options spécifiques.
Le magasin possède une liste de vendeurs, tous les vendeurs peuvent réaliser des ventes mais seuls les vendeurs seniors peuvent accorder la réduction. 
Dans ce cas là, la vente aura deux vendeurs.
Il existe trois types de vendeur, les vendeurs payés à l’heure, ceux freelance à la mission et ceux payés au mois. Une méthode permettra de calculer leur paie chaque mois.
Une vente correspond toujours à un véhicule, et à un vendeur. Il est possible d’exporter la facture au format pdf avec l’ensemble des informations de la vente
"""


from asyncio.windows_events import NULL
from msilib.schema import Error


class Vehicle:

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self._tax = NULL
        self._xtprice = NULL
        self._itprice = NULL
        self._reduction = NULL

    # Set the price without taxes
    def set_xtprice(self, xtprice: float):
        self._xtprice = xtprice

    # Return and print the price without taxes
    def get_xtprice(self):
        print(f"Exclude tax price:  {self._xtprice}")

    # Set the tax (%) for the vehicule
    def set_tax(self, tax: float):
        self._tax = tax

    # Return and print the tax(%)
    def get_tax(self):
        print(self._tax)
        return self._tax

    # Return the price including tax
    def get_itprice(self):
        if self._tax == NULL or self._xtprice == NULL:
            print("Tax or priceXT is not defined.")

        else:
            self._itprice = ((self._tax / 100) + 1) * self._xtprice
            print(f"Include tax price : {self._itprice}")

    # Set the reduction(%) for the vehicule
    def set_reduction(self, reduction: float):
        self._reduction = reduction

    # Return the price with tax and reduction include
    def get_price(self):
        if self._itprice == NULL or self._reduction == NULL:
            print("Reduction value or priceIT is not defined.")
        else:
            self._price = self._itprice * (100 - self._reduction)
            print(self._price)


class Car(Vehicle):
    pass


class Motorbike(Vehicle):
    pass


class Truck(Vehicle):
    pass


class Inventory:

    def __init__(self, name):
        self.name = name
        self.list_vehicules = []
        self.nb_vehicules = 0

    # Add a vehicule on the inventory list and adjust the number of vehicles on the inventory
    def add_vehicule(self, vehicle: "Vehicle"):
        self.list_vehicules.append(vehicle)
        self.nb_vehicules = self.nb_vehicules + 1

    def pop_vehicule(self, vehicle: "Vehicle"):
        pass

# potentiel classe abstraite


class Salesman:

    #grade = junior | confirmed | senior
    def __init__(self, grade):
        self._grade = grade
        if self.grade == "junior":
            self.__permission = "No"
        elif self.grade == "confirmed":
            self.__permission = "No"
        elif self.grade == "senior":
            self.__permission = "Yes"
        self._sale = 0


class HourSalesman(Salesman):
    pass


class MissionSalesman(Salesman):

    def __init__(self, grade, nb_workdays: int):
        super().__init__(self, grade)
        self._nb_workdays = nb_workdays
        if self.grade == "junior":
            self._daily_salary = 75
        elif self.grade == "confirmed":
            self._daily_salary = 150
        elif self.grade == "senior":
            self._daily_salary = 300

    def get_salary(self):
        self._salary = self._daily_salary * self._nb_workdays
        print(f"The salary for this salesman will be {self._salary} dollars.")


class MonthSalesman(Salesman):

    def __init__(self, grade):
        super().__init__(self, grade)
        if self.grade == "junior":
            self._base_salary = 1500
        elif self.grade == "confirmed":
            self._base_salary = 2000
        elif self.grade == "senior":
            self._base_salary = 2500

    def get_salary(self):
        self._salary = self._base_salary + self._sale * 200
        print(f"The salary for this salesman will be {self._salary} dollars.")


class Sale:

    def __init__(self, description, vehicle: Vehicle, salesman: Salesman):
        self.description = description
        self.vehicle = vehicle
        self.salesman = salesman
        self.init = 0

    def set_sale_conditions(self, xt_price, tax, reduction):
        self.vehicle.set_xtprice(xt_price)
        self.vehicle.set_tax(tax)
        self.vehicle.set_reduction(reduction)
        self.init = 1

    def get_sale_conditions(self):
        if self.init == 1:
            self.vehicle.get_price()
        else:
            print("Sale conditions are not defined.")
            return Error


class Dealer:
    def __init__(self, name, address, siret):
        self.name = name
        self.address = address
        self.siret = siret
        self.list_salesman = []
        self.list_sales = []
        self.list_inventories = []

    def add_sale_list(self, sale: Sale):
        pass

    def pop_sale_list(self, sale: Sale):
        pass

    def add_salesman_list(self, salesman: Salesman):
        pass

    def pop_salesman_list(self, salesman: Salesman):
        pass

    def add_inventory(self, inventory: Inventory):
        pass

    def pop_inventory(self, inventory: Inventory):
        pass
