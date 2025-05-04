
import random

servers = ["Server1", "Server2", "Server3"]

# Round Robin Load Balancer
class RoundRobinLB:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_server(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

# Random Load Balancer
class RandomLB:
    def __init__(self, servers):
        self.servers = servers

    def get_server(self):
        return random.choice(self.servers)

def simulate(lb, count):
    for i in range(1, count + 1):
        server = lb.get_server()      # Gets a server from the load balancer
        print(f"Request {i} routed to {server}")

print("Round Robin Load Balancing:")
simulate(RoundRobinLB(servers), 10)

print("\nRandom Load Balancing:")
simulate(RandomLB(servers), 10)

