
#server code:
import Pyro4

@Pyro4.expose
class StringConcatenator:
    def concatenate(self, str1, str2):
        return str1 + str2

concatenator = StringConcatenator()

daemon = Pyro4.Daemon()
uri = daemon.register(concatenator)

print("Server URI :",uri)
print("Server is ready...")

daemon.requestLoop()

#client code:
import Pyro4

uri = input("Enter Server,s URI:")
concatenator = Pyro4.Proxy(uri)

str1 = input("Enter First String:")
str2 = input("Enter Second String:")

print("Concatenated String:",concatenator.concatenate(str1,str2))
