import numpy as np

truth_table = np.array([
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1]
], dtype=np.uint8)

print("---- 1. Input Truth Table Matrix (8x3) ----")
print("A B C")
print(truth_table)
print()

A = truth_table[:, 0]
B = truth_table[:, 1]
C = truth_table[:, 2]

alarm_method_A = (A & B) | (B & C) | (A & C)

sensor_sum = np.sum(truth_table, axis=1)
alarm_method_B = (sensor_sum >= 2).astype(np.uint8)

is_identical = np.array_equal(alarm_method_A, alarm_method_B)

print("---- 2. Logic Evaluation ----")
print(f"Active Sensor Count per Row : {sensor_sum}")
print(f"Evaluated Alarm Output      : {alarm_method_B}")
print(f"Both Logic Methods Match?   : {is_identical}\n")

full_circuit_table = np.column_stack((truth_table, alarm_method_B))

print("---- 3. Complete Circuit Verification Table ----")
print("A  B  C | ALARM")
print("----------------")

for row in full_circuit_table:
    print(f"{row[0]}  {row[1]}  {row[2]} |   {row[3]}")
