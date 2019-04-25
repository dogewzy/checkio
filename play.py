class A:
    storage = 5

    @property
    def static(self):
        return self.storage

    @static.setter
    def static(self, d):
        self.storage = 8

a = A()
print(a.storage)
a.storage =6
print(a.storage)
