# 第一題 : 使用迴圈計算最小值到最大值之間，所有整數的總和。


def calculate(min, max):
    sum = 0
    for n in range(min, max+1):
        sum = sum+n
    print(sum)


calculate(1, 3)  # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8)  # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

###################################################################################################################

# 第二題 : 正確計算出員工的平均薪資，請考慮員工數量會變動的情況。


def avg(data):
    sum = 0
    for i in data['employees']:
        sum = sum+i['salary']
        avgSalary = sum/data['count']
    print(avgSalary)


avg({
    "count": 3,
    "employees": [
        {
            "name": "John",
            "salary": 30000
        },
        {
            "name": "Bob",
            "salary": 60000
        },
        {
            "name": "Jenny",
            "salary": 50000
        }
    ]
})

###################################################################################################################

# 第三題 : 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。


def maxProduct(nums):
    arr = []
    max_value = None
    for i in range(0, len(nums)):
        x = nums[i]
        for j in range(i+1, len(nums)):
            y = nums[j]
            arr.append(x*y)
            max_value = max(arr)
    print(max_value)


maxProduct([5, 20, 2, 6])  # 得到 120
maxProduct([10, -20, 0, 3])  # 得到 30
maxProduct([-1, 2])  # 得到 -2
maxProduct([-1, 0, 2])  # 得到 0
maxProduct([-1, -2, 0])  # 得到 2

###################################################################################################################

# 第四題 : Given an array of integers, show indices of the two numbers such that they add up to a specific target.


def twoSum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


result = twoSum([2, 11, 7, 15], 9)
print(result)  # show [0, 2] because nums[0]+nums[2] is 9

###################################################################################################################

# 第五題 : 給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大長度。


def maxZeros(nums):
    sum = 0
    max = 0
    for i in nums:
        if i == 0:
            sum = sum+1
        else:
            sum = 0
        if max < sum:
            max = sum
    print(max)
    return max


maxZeros([0, 1, 0, 0])  # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])  # 得到 4
maxZeros([1, 1, 1, 1, 1])  # 得到 0
maxZeros([0, 0, 0, 1, 1])  # 得到 3
