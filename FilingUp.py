n = int(input())

for i in range(n):

    length = int(input())
    nums = list(map(int, input().strip().split(" ")))
    queue = []
    flag = True

    # print("nums = " + str(nums))
    # print("queue = " + str(queue))

    while len(nums) > 1:

        if len(queue) != 0:
            if queue[len(queue) - 1] < nums[0] or queue[len(queue) - 1] < nums[-1]:
                print("No")
                flag = False
                break

        if nums[0] > nums[-1]:

            queue.append(nums.pop(0))
        elif nums[0] < nums[-1]:

            queue.append(nums.pop(len(nums) - 1))
        elif nums[0] == nums[-1]:

            queue.append(nums.pop(0))
            queue.append(nums.pop(len(nums) - 1))

        # print("nums = " + str(nums))
        # print("queue = " + str(queue))

    if len(nums) == 1:
        if nums[0] > queue[len(queue) - 1]:
            print("No")
            flag = False

    if flag:
        print("Yes")