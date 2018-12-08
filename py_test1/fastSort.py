import random
import datetime

array = [32, 4, 54, 84, 89, 213, 456, 4984, 856, 5, 894, 5616, 32, 63, 55, 152, 9, 110, 120, 119, 386]
arrRandom = []
arrRandom1 = []
arrRandom2 = []
for m in range(10000000):
    arrRandom.append(random.randint(1, 1000000))
    arrRandom2.append(random.randint(1, 1000000))

for m in range(10000):
    arrRandom1.append(random.randint(1, 1000000))


# fastSort
def fast(arr, i, j):
    if i >= j or i < 0 or j > len(arr):
        return
    key = arr[i]
    start = i
    end = j
    while start < end:
        while arr[end] > key and start < end:
            end -= 1
        arr[start] = arr[end]
        start += 1

        while arr[start] < key and start < end:
            start += 1
        arr[end] = arr[start]
        end -= 1
        arr[start] = key
    fast(arr, i, end)
    fast(arr, end + 1, j)


# 冒泡
def sort(arr):
    for x in range(len(arr)-1):
        for p in range(len(arr)-x-1):
            if arr[p] > arr[p+1]:
                temp = arr[p]
                arr[p] = arr[p+1]
                arr[p+1] = temp


# 二分查找
def binarysearch(arr, key):
    length = len(arr)
    index = int(length/2)
    interval = int(index/2)
    while interval >= 1:
        interval = int(interval)
        if arr[index] == key:
            return index
        if arr[index] > key:
            index = index - interval
            if interval == 1:
                if arr[index-1] == key:
                    return index-1
        else:
            index = index + interval
            if interval == 1:
                if arr[index+1] == key:
                    return index+1
        interval = interval / 2


def search(arr, start, end, key):
    while start < end:
        mid = start+((start-end) >> 1)
        if key == arr[mid]:
            return mid
        if key < arr[mid]:
            search(arr, start, mid-1, key)
        if key > arr[mid]:
            search(arr, mid+1, end, key)


# 获取当前时间
def getnow():
    return datetime.datetime.now()


print()
print('开始排序: fastSort')
print('排序长度 : ', len(arrRandom))
time = getnow()
print(time)
fast(arrRandom, 0, len(arrRandom) - 1)
print('结束排序: fastSort')
print(getnow())
print('总共耗时', (getnow()-time).seconds, '秒', (getnow()-time).microseconds, '毫秒')
print()

print()
print('开始排序: 系统排序')
print('排序长度 : ', len(arrRandom2))
time = getnow()
print(time)
arrRandom2.sort()
# print(arrRandom2)
print('结束排序: 系统排序')
print(getnow())
print('总共耗时', (getnow()-time).seconds, '秒', (getnow()-time).microseconds, '毫秒')
print()

print('开始排序 :冒泡')
print('排序长度 :', len(arrRandom1))
time = getnow()
print(time)
sort(arrRandom1)
print('结束排序 :冒泡')
print(getnow())
print('总共耗时', (getnow()-time).seconds, '秒', (getnow()-time).microseconds, '毫秒')
print()


# 进行二分查找
keys = random.randint(0, len(arrRandom))
print('开始查找 :二分')
print('查找的长度为 :', len(arrRandom))
print('查找的值为 :', arrRandom[keys])
time = getnow()
print(time)
result = binarysearch(arrRandom, arrRandom[keys])
print('查找的值所在坐标', result)
print('返回的结果', arrRandom[result])
print('结束查找 :二分')
print(getnow())
print('总共耗时', (getnow()-time).seconds, '秒', (getnow()-time).microseconds, '毫秒')
print()

# 系统查找
print('开始查找 :系统查找')
print('查找的长度为 :', len(arrRandom))
print('查找的值为 :', arrRandom[keys])
time = getnow()
print(time)
result = arrRandom.index(arrRandom[keys])
print('查找的值所在坐标', result)
print('返回的结果', arrRandom[result])
print('结束查找 :系统查找')
print(getnow())
print('总共耗时', (getnow()-time).seconds, '秒', (getnow()-time).microseconds, '毫秒')