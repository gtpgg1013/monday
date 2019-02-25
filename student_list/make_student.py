import os
from faker import Faker

fake = Faker("ko_KR")
print(fake.name())
for i in range(100):
    name = fake.name()
    cmd = f"touch {str(i)}_{name}.txt"
    os.system(cmd)