"""
Lesson 15. Task 2.

Implement 2 classes, the first one is the Boss and the second one is the Worker.

Worker has a property 'boss', and its value must be an instance of Boss.

You can reassign this value, but you should check whether the new value is Boss. 
Each Boss has a list of his own workers. You should implement a method that allows 
you to add workers to a Boss. You're not allowed to add instances of Boss class to workers
list directly via access to attribute, use getters and setters instead!
"""
import uuid
from pprint import pprint


class Boss:
    def __init__(self, id_, name, company):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []
    
    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<Boss id={self.id} name={self.name} company={self.company}>"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Boss):
            return False

        return self.id == other.id
    
    def add_worker(self, name_or_obj):
        if isinstance(name_or_obj, Worker):
            if name_or_obj.boss is not None and name_or_obj.boss != self:
                name_or_obj.boss.remove_worker(name_or_obj)

            name_or_obj.company = self.company
            name_or_obj.boss = self

            self.workers.append(name_or_obj)

            return name_or_obj

        obj = Worker(str(uuid.uuid4()), name_or_obj, self.company, self)
        self.workers.append(obj)

        return obj
    
    def remove_worker(self, name_or_obj):
        if isinstance(name_or_obj, Worker):
            self.workers.remove(name_or_obj)
            return self

        self.workers = list(filter(lambda w: w.name != name_or_obj, self.workers))
        return self


class Worker:
    def __init__(self, id_, name, company=None, boss=None):
        self.id = id_
        self.name = name
        self.company = company

        self._boss = None

        if boss is not None:
            self.boss = boss

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<Worker id={self.id} name={self.name} company={self.company} boss={self._boss}>"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Worker):
            return False
        
        return self.id == other.id

    @property    
    def boss(self):
        return self._boss
    
    @boss.setter
    def boss(self, boss):
        if not isinstance(boss, Boss):
            raise ValueError("Should be an instance on the Boss class")

        self._boss = boss
        return self


def add_worker_to_boss(worker, boss):
    if worker.boss is not None and worker.boss != boss:
        worker.boss.remove_worker(worker)
    
    boss.add_worker(worker)


def main():
    boss1 = Boss(str(uuid.uuid4()), "Tracey Collins", "Coca Cola Ltd.")
    worker1 = Worker(str(uuid.uuid4()), "Calvin Ramos")
    boss1.add_worker(worker1)
    boss1.add_worker("Vivan Young")

    print(repr(boss1))
    pprint(boss1.workers)

    boss2 = Boss(str(uuid.uuid4()), "Arianna Douglas", "Pepsi Co.")
    worker3 = Worker(str(uuid.uuid4()), "Lesa Hall")
    boss2.add_worker(worker3)

    print(repr(boss2))
    pprint(boss2.workers)

    # ideal situation
    # boss2.remove_worker(worker3)
    # boss1.add_worker(worker3)
    add_worker_to_boss(worker3, boss1)

    pprint(boss1.workers)
    pprint(boss2.workers)

if __name__ == "__main__":
    main()
