
class Component:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __lt__(self, other):
        if self.name != other.name:
            return self.name < other.name
        else:
            if self.version == other.version:
                return False
            else:
                return greaterOrEqualVersion(other.version, self.version)


def greaterOrEqualVersion(v1,v2): #Retorna true se v1 eh a versao mais recente ou a mesma que v2
    i = 0
    version1 = v1.split(".")
    version2 = v2.split(".")
    while True:
        if i >= len(version1) or i >= len(version2):
            if len(version2) > len(version1):
                return False
            else:
                return True
        if int(version1[i]) < int(version2[i]):
            return False
        elif int(version1[i]) > int(version2[i]):
            return True
        i += 1
