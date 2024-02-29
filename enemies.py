#Enemy
class Enemy(object):
    """base class for all enemies"""
    def __init__(self, name, lifepoints, damage):
        self.name = name
        self.lifepoints = lifepoints
        self.damage = damage
 
    def is_alive(self):
        return self.lifepoints > 0

class Guilt(Enemy):
    def __init__(self):
        super(Guilt, self).__init__(name="Guilt", lifepoints = 10, damage = 2)
        
class Homework(Enemy):
    def __init__(self):
        super(Homework, self).__init__(name="Homework assignment", lifepoints=100, damage=2)
 
 
class ResearchPaper(Enemy):
    def __init__(self):
        super(ResearchPaper, self).__init__(name="Research Paper", lifepoints=30, damage=10)

#boss 
class Procrastination(Enemy):
    def __init__(self):
        super(Procrastination, self).__init__(name="Procrastination", lifepoints=80, damage=15)
