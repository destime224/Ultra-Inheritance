import random

class Entity:
    def __init__(self,tp,damage,speed,health,strEntity):
        self.type = tp
        self._health = health * self.type.healthFactor
        self._damage = damage * self.type.damageFactor
        self._speed = speed * self.type.speedFactor
        self._strEntity = strEntity

    def attack(self,point):
        point._get_damage(self._damage)

    def _get_damage(self,damage):
        self._health -= damage

    @property
    def get_params(self):
        return self._damage,self._speed,self._health

    def __str__(self):
        return self._strEntity

class EntityType:
    def __init__(self,damageF,speedF,healthF,strType):
        self.healthFactor = healthF
        self.damageFactor = damageF
        self.speedFactor = speedF
        self._strType = strType

    def __str__(self):
        return self._strType

# Entities
# --------------------------------------

class Zombie(Entity):
    def __init__(self,tp):
        super().__init__(tp,5,7,75,"Zombie")

class Spider(Entity):
    def __init__(self,tp):
        super().__init__(tp,4,9,90,"Spider")

class Slime(Entity):
    def __init__(self,tp):
        super().__init__(tp,7,4,120,"Slime")

# Types
# --------------------------------------

class Common(EntityType):
    def __init__(self):
        super().__init__(1,1,1,"Common")

class Uncommon(EntityType):
    def __init__(self):
        super().__init__(1.3,1.3,1.5,"Uncommon")

class Elite(EntityType):
    def __init__(self):
        super().__init__(2.1,2,2,"Elite")

class Boss(EntityType):
    def __init__(self):
        super().__init__(3.2,3,3,"Boss")

# Factory
# --------------------------------------

class EntitiesFactory:
    def __init__(self):
        self.entities = (Zombie,Spider,Slime)
        self.types = (Common,Uncommon,Elite,Boss)

    def get_entity(self):
        entityType = random.choice(self.types)()
        entity = random.choice(self.entities)(entityType)
        return entity

# Main
# --------------------------------------

if __name__ == "__main__":
    factory = EntitiesFactory()
    entity1 = factory.get_entity()
    print(entity1.type,entity1)
    print(entity1.get_params)
