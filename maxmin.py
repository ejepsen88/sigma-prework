
entry = input("Enter array here: ")
entry = entry.replace("[", "")
entry = entry.replace("]", "")
nums = entry.split(",")

output = []
output.append(int(nums[0]))
output.append(int(nums[1]))

for num in nums:
    if int(num) < output[0]:
        output[0] = int(num)
    elif int(num) > output[1]:
        output[1] = int(num)
    else:
        continue
print(output)
