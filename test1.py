"""
 * Project name(项目名称)：set集合和集合基本操作
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/22 
 * Time(创建时间)： 20:01
 * Version(版本): 1.0
 * Description(描述)： 
 """

if __name__ == '__main__':
    a = {1, 2, 3, 4, 5, 1, 3, 7}
    print(a)
    print(type(a))

    b = set(range(1, 30))
    print(b)
    set1 = set("hello")
    set2 = set([1, 2, 3, 4, 5])
    set3 = set((1, 2, 3, 4, 5))
    print(set1)
    print(set2)
    print(set3)
    for ele in a:
        print(ele,end=' ')
    print()
    for ele in b:
        print(ele,end=' ')
    print()
    for ele in set1:
        print(ele,end=' ')
    print()
    for ele in set2:
        print(ele,end=' ')
    print()
    for ele in set3:
        print(ele,end=' ')
    print()

    del a
    # print(a)

    input()