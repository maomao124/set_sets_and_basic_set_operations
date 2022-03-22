"""
 * Project name(项目名称)：set集合和集合基本操作
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/22 
 * Time(创建时间)： 20:11
 * Version(版本): 1.0
 * Description(描述)：
 向 set 集合中添加元素
set 集合中添加元素，可以使用 set 类型提供的 add() 方法实现
set name.add(element)
其中，set name 表示要添加元素的集合，element 表示要添加的元素内容。

从set集合中删除元素
删除现有 set 集合中的指定元素，可以使用 remove() 方法，该方法的语法格式如下：
set name.remove(element)
使用此方法删除集合中元素，需要注意的是，如果被删除元素本就不包含在集合中，则此方法会抛出 KeyError 错误

运算操作	Python运算符	    含义  	例子
交集	&	取两集合公共的元素	>>> set1 & set2
{3}
并集	|	取两集合全部的元素	>>> set1 | set2
{1,2,3,4,5}
差集	-	取一个集合中另一集合没有的元素	>>> set1 - set2
{1,2}
>>> set2 - set1
{4,5}
对称差集	^	取集合 A 和 B 中不属于 A&B 的元素	>>> set1 ^ set2
{1,2,4,5}
 """

if __name__ == '__main__':
    a = set(range(0, 20))
    print(a)
    a.add(44)
    a.add(23)
    print(a)

    a.remove(7)
    print(a)
    a.remove(9)
    print(a)

    a.discard(1)
    print(a)
    a.discard(1)
    print(a)

    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7, 8}
    print(s1)
    print(s2)
    s3 = s1 & s2
    print(s3)
    s4 = s1 | s2
    print(s4)
    s5 = s1 - s2
    print(s5)
    s6 = s2 - s1
    print(s6)
    s7 = s1 ^ s2
    print(s7)

    input()
