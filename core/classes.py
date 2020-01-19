class Car:
  # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
  # Поля должны задаваться через конструктор
  def __init__(self, mark, model):
    self.mark = mark
    self.model = model

  def __repr__(self):
    return '{} {}'.format(self.mark, self.model)

class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars):
      self.cars = cars
    
    def __len__(self):
      return len(self.cars)

    def __getitem__(self, index):
      return self.cars[index]

    def additem(self, mark, model):
      self.cars.append(Car(mark, model))
    
    def __delitem__(self, index):
      del self.cars[index]