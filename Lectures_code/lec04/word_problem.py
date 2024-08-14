# for alyssa in range(11):
#     for ben in range(11):
#         for cindy in range(11):
#             total = (alyssa + ben + cindy == 10)
#             two_less = (ben == alyssa - 2)
#             twice = (cindy == 2* alyssa)
#             if total and two_less and twice:
#                 print(f"alyssa sold {alyssa} tickets")
#                 print(f"ben sold {ben} tickets")
#                 print(f"cindy sold {cindy} tickets")

# more efficienty way:

for alyssa in range(1001):
    ben = max(alyssa - 20, 0)
    cindy = 2*alyssa
    if ben + alyssa + cindy == 1000:
        print(f"alyssa sold {alyssa} tickets")
        print(f"ben sold {ben} tickets")
        print(f"cindy sold {cindy} tickets")
