import time
from datetime import datetime

from python.cracking_the_coding_interview.linked_list import LinkedList


def get_time():
    return datetime.utcnow()


class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)


class AnimalShelter:
    def __init__(self):
        self.dog = LinkedList()
        self.cat = LinkedList()

    def enqueue(self, animal):
        current_time = get_time()
        if type(animal) is Dog:
            self.dog.add(animal.name, created_at=current_time)
        elif type(animal) is Cat:
            self.cat.add(animal.name, created_at=current_time)

    def peek(self, queue):
        return queue.head

    @staticmethod
    def remove_first(ll):
        value = ll.head.value
        ll.head = ll.head.next
        return value

    def dequeue_any(self):
        if not self.dog.is_empty() and not self.cat.is_empty():
            dog_time = self.peek(self.dog).created_at
            cat_time = self.peek(self.cat).created_at

            if dog_time <= cat_time:
                return self.remove_first(self.dog)
            else:
                return self.remove_first(self.cat)
        elif not self.dog.is_empty():
            return self.remove_first(self.dog)
        elif not self.cat.is_empty():
            return self.remove_first(self.cat)


def test_animal_shelter():
    shelter = AnimalShelter()
    shelter.enqueue(Dog('James'))
    time.sleep(1)
    shelter.enqueue(Cat("Kitty"))
    time.sleep(1)
    shelter.enqueue(Dog('Sandy'))
    time.sleep(1)
    shelter.enqueue(Cat("Pussy"))

    assert shelter.dequeue_any() == 'James'
    assert shelter.dequeue_any() == 'Kitty'
