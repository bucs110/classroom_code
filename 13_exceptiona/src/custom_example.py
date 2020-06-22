class MyBadException(Exception):
    pass
class MyTerribleException(Exception):
    pass


try:
    doSomething()
except MyBadException:
    fixBadThing()
except MyTerribleException:
    fixTerribleThing()
