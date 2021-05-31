import time

start_time = time.time()
loops = 0
while time.time() - start_time < 1:
    loops += 1
end_time = time.time()

loops_for = 0
for _ in range(loops):
    a_var = 1

for_time = time.time() - end_time
print(for_time)
