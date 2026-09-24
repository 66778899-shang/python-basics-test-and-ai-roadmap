# Python 基础补强讲义（阶段 A 专用）

> **给谁看**：完成自测卷（卷一 + 卷二）得 29/50 的你——判断题 9/10、单选 10/20
> **结论先说**：你不是零基础，问题集中在三处，本讲义按优先级编排
> **怎么用**：每章 = 原理 → 可运行示例（输出已实测标注）→ 容易踩的坑 → 练习（答案在章末）
> **务必动手**：所有代码在 JupyterLab 里亲手敲一遍；卡住时用 `%ask 用一句话解释……` 追问，不要只看不练

## 你的错题 → 章节对照

| 错题 | 病根 | 看哪一章 |
| --- | --- | --- |
| 第 6、12、18、26 题 | **区间边界感**：0 基、右端不含 | 第 1 章（最高优先级） |
| 第 3、4、5 题 | **类型与运算符体系**：`//`、假值、可变性 | 第 2、3、4 章 |
| 第 1、10、13、15 题 | **语法细节**：命名、字典取值、while、作用域 | 第 6、8 章 |
| 卷四代码阅读第 3 题 | 默认参数陷阱 | 第 6.2 节 |

---

## 第 1 章 索引与区间：一切从 0 开始 ★重点

### 1.1 索引从 0 开始

```python
s = "Python"
print(s[0])   # 结果：P   ← 第 1 个字符的下标是 0，不是 1
print(s[1])   # 结果：y
print(s[5])   # 结果：n   ← 最后一个字符下标是 5（长度 6，最大下标 = 长度 - 1）
```

一句话记牢：**长度是 6，下标到 5 就结束了**。访问 `s[6]` 会报 `IndexError`。

### 1.2 负索引：从右边数

```python
s = "Python"
print(s[-1])  # 结果：n   ← 最后一个
print(s[-2])  # 结果：o   ← 倒数第二个
```

`-1` 是最后一位，这是 Python 最贴心的设计之一，取末位不用再写 `s[len(s)-1]`。

### 1.3 切片：`s[起:止:步长]`，**止不包含**

这是你第 6 题栽的地方。规则只有一句：**取到"止"的前一位，不含"止"**。

```python
s = "Python"
print(s[1:4])   # 结果：yth   ← 取下标 1、2、3；下标 4 不取
print(s[0:3])   # 结果：Pyt
print(s[:3])    # 结果：Pyt   ← 省略起点，默认从 0 开始
print(s[3:])    # 结果：hon   ← 省略终点，默认取到末尾
print(s[:])     # 结果：Python ← 全都要
print(s[::-1])  # 结果：nohtyP ← 步长 -1，字符串反转
print(s[::2])   # 结果：Pto    ← 步长 2，隔一个取一个
```

数数口诀：**"止 - 起 = 取几个字符"**。`s[1:4]` → 4 - 1 = 3 个字符（y、t、h）。

### 1.4 range：三种写法和"几次"的问题

这是第 12、18、26 题共同的病根。

```python
print(list(range(5)))       # 结果：[0, 1, 2, 3, 4]     ← 从 0 开始，到 5 之前结束（不含 5）
print(list(range(1, 5)))    # 结果：[1, 2, 3, 4]        ← 从 1 开始，到 5 之前结束
print(list(range(1, 10, 2)))  # 结果：[1, 3, 5, 7, 9]   ← 步长 2
print(len(range(1, 5)))     # 结果：4                  ← 循环执行 4 次，不是 3 次、也不是 5 次
```

三个必须形成的条件反射：

1. `range(n)`：从 **0** 开始 → 所以 `[x*x for x in range(4)]` 是 `[0, 1, 4, 9]`，不是 `[1, 4, 9, 16]`
2. `range(a, b)`：**不含 b** → 所以 `range(5)` 里没有 5，`range(1, 5)` 里没有 5
3. 循环次数 = **b - a** → 所以 `range(1, 5)` 执行 4 次

### 1.5 容易踩的坑

| 坑 | 错误写法 | 正确写法 |
| --- | --- | --- |
| 以为下标从 1 开始 | `s[1]` 想取首字母 | `s[0]` |
| 切片右端写错 | `s[1:4]` 以为得 `ytho` | 右端不含，得 `yth` |
| `range(5)` 以为含 5 | 想循环 5 次用 `range(5)` 得到 0~4 | 想要 1~5 用 `range(1, 6)` |
| 列表推导式起点 | 以为 `range(4)` 从 1 开始 | 从 0 开始 |

### 1.6 动手实验（在 JupyterLab 新建单元格里跑）

```python
for i in range(5):
    print(i, "→", i * i)
```

跑完问自己：打印了几行？最后一行是几？为什么？——然后用 `%ask 为什么 range(5) 不含 5` 验证你的理解。

### 1.7 练习（答案见 1.8）

1. `"abcdef"[2:5]` 的结果是什么？
2. `list(range(3, 8))` 的结果是什么？
3. `len(range(0, 10, 3))` 是多少？循环几次？
4. `"abcdef"[-3:]` 的结果是什么？
5. 要打印 1 到 100（含 100），`range` 怎么写？
6. `"abcdef"[::-2]` 的结果是什么？

### 1.8 练习答案

1. `cde`（下标 2、3、4）
2. `[3, 4, 5, 6, 7]`
3. `4`，循环 4 次（0、3、6、9）
4. `def`（从倒数第 3 个到末尾）
5. `range(1, 101)`
6. `fdb`（从末尾往前，隔一个取一个）

---

## 第 2 章 数据类型与"可变 / 不可变"

### 2.1 五种常用类型

| 类型 | 例子 | 可变吗 | 特点 |
| --- | --- | --- | --- |
| `int` 整数 | `10` | 不可变 | 加减乘除后生成新对象 |
| `float` 浮点 | `3.14` | 不可变 | 带小数点；Python 没有 `double` |
| `str` 字符串 | `"abc"` | 不可变 | 带引号；`len("abc")` 是 3 |
| `bool` 布尔 | `True` / `False` | 不可变 | 本质是 1 / 0 |
| `list` 列表 | `[1, 2, 3]` | **可变** | 有序、可改、可重复 |
| `tuple` 元组 | `(1, 2, 3)` | **不可变** | 有序、不能改 |
| `dict` 字典 | `{"a": 1}` | **可变** | 键值对 |
| `set` 集合 | `{1, 2, 3}` | **可变** | 无序、自动去重 |

**你第 5 题错在这里**：题目问"下列**不属于**可变类型的是"，答案是 `tuple`（不可变），你选了 `dict`——`dict` 恰恰是可变的。读题时把"不属于"圈出来。

### 2.2 "可变 / 不可变"到底意味着什么

```python
lst = [1, 2, 3]
lst.append(4)
print(lst)        # 结果：[1, 2, 3, 4]   ← 原对象被改了

t = (1, 2, 3)
t[0] = 9          # 报错：TypeError: 'tuple' object does not support item assignment

s = "abc"
s[0] = "x"        # 报错：TypeError: 'str' object does not support item assignment
```

记忆口诀：**能改的只有 list / dict / set；名字带 t 的（tuple）改不了，字符串也改不了**。

### 2.3 类型转换与常见报错

```python
print(int("123"))        # 结果：123
print(float("3.5"))      # 结果：3.5
print(int(float("3.5"))) # 结果：3      ← 字符串带小数点必须先 float 再 int
print(str(123))          # 结果："123"
```

```python
int("3.5")   # 报错：ValueError: invalid literal for int() with base 10: '3.5'
```

因为 `int()` 只认"整数字符串"。这是自测卷第 30 题的知识点。

### 2.4 容易踩的坑

| 坑 | 说明 |
| --- | --- |
| 集合会去重 | `{1, 2, 2, 3}` 实际是 `{1, 2, 3}`，长度 3 |
| `input()` 得到的是字符串 | 要做加法必须 `int(input(...))` |
| `"1" + 1` 报错 | 字符串和数字不能直接相加，要 `int("1") + 1` |
| 长度按元素个数算 | `len([1, [2, 3], 4])` 是 3，内层列表整体算 1 个元素 |

### 2.5 练习（答案见 2.6）

1. `{1, 2, 2, 3, 3}` 有几个元素？
2. `int("12") + 3` 的结果？
3. `str(1) + "2"` 的结果？
4. 下面哪行会报错：`(1,2)[0]`、`[1,2][0]`、`(1,2)[0] = 9`？
5. `bool(0)`、`bool("0")` 分别是？
6. `len("hello")` 和 `len([1, [2, 3], 4])` 分别是？

### 2.6 练习答案

1. 3 个
2. 15
3. `"12"`（字符串拼接）
4. 第三行会报 `TypeError`（元组不可改）
5. `False`、`True`（非空字符串为真，"0" 也是非空）
6. 5、3

---

## 第 3 章 运算符

### 3.1 算术运算符：`/`、`//`、`%`、`**`

```python
print(10 / 3)    # 结果：3.3333333333333335   ← 真除法，永远返回小数
print(10 // 3)   # 结果：3                    ← 整除，向下取整（你第 3 题错这里）
print(10 % 3)    # 结果：1                    ← 取余数
print(2 ** 10)   # 结果：1024                 ← 乘方
print(-10 // 3)  # 结果：-4                   ← "向下"取整：-4 比 -3.33 更小
```

自测卷第 3 题你选了 `1`——那是 `%` 的结果；`10 // 3` 是整除，答案是 `3`。

### 3.2 比较与逻辑

```python
print(3 > 2, 3 == 3.0, 3 != 4)        # 结果：True True True
print("a" == "a", [1] == [1])          # 结果：True True   ← 只比值
print([1] is [1])                      # 结果：False       ← is 比的是"是不是同一个对象"
print(True and False, True or False)   # 结果：False True
print(not True)                        # 结果：False
```

`and` / `or` 会"短路"：`and` 遇到第一个假值就停，`or` 遇到第一个真值就停。

### 3.3 字符串和列表也能"算"

```python
print(3 * "ab")    # 结果：ababab   ← 重复
print("ab" + "cd") # 结果：abcd     ← 拼接
print("1" * 3)     # 结果：111
print([1] + [2])   # 结果：[1, 2]
print([0] * 3)     # 结果：[0, 0, 0]
```

```python
"1" + 1            # 报错：TypeError: can only concatenate str (not "int") to str
```

### 3.4 练习（答案见 3.5）

1. `17 // 5` 和 `17 % 5` 分别是？
2. `3 ** 3` 是多少？
3. `-7 // 2` 是多少？
4. `"a" * 2 + "b"` 的结果？
5. `2 + 3 * 4` 的顺序与结果？
6. `"5" + str(5)` 和 `int("5") + 5` 分别是？

### 3.5 练习答案

1. `3` 和 `2`
2. `27`
3. `-4`
4. `aab`
5. 先乘后加（乘除优先），结果 `14`
6. `"55"` 和 `10`

---

## 第 4 章 真假值与条件判断

### 4.1 假值清单（一共只有这几个）

```python
print(bool(False), bool(0), bool(""), bool([]), bool({}), bool(None))
# 结果：False False False False False False
```

反过来，**非空的字符串 / 列表 / 字典、非 0 的数字，全是真**：

```python
print(bool("0"), bool(" "), bool([0]), bool(-1))
# 结果：True True True True
```

**你第 4 题错在这里**：`bool("")` 是 `False`——空字符串是假值，不是 `None`。

### 4.2 if / elif / else：只会进一个分支

```python
x = 5
if x > 3:
    print("A")     # 只有这一行会执行
elif x > 1:
    print("B")     # 前面成立时，这里连判断都不会做
else:
    print("C")
# 结果：A
```

条件是从上往下挨个判断，**命中一个就跳出整条 if 链**。

### 4.3 练习（答案见 4.4）

1. `bool([])`、`bool([0])` 分别是？
2. `x = 0` 时，`if x: print("真") else: print("假")` 输出什么？
3. 判断一个字符串是否为空的写法（用真值判断，不用 `len`）？
4. `bool(-1)` 是？

### 4.4 练习答案

1. `False`、`True`（列表里有元素就是真）
2. 输出 `假`（0 是假值）
3. `if not s: print("空")`
4. `True`（只要不是 0 就是真）

---

## 第 5 章 循环

### 5.1 for + range：算清边界和次数

```python
for i in range(1, 6):     # 1、2、3、4、5 → 共 5 次
    print(i)

for i in range(5):        # 0、1、2、3、4 → 共 5 次
    print(i)
```

要循环 n 次，习惯写法是 `range(n)`；要遍历 1~n，写 `range(1, n + 1)`。

### 5.2 while：可能一次都不执行

```python
n = 5
while n < 3:      # 一开始就不成立 → 循环体一次都不执行
    print("永远不会打印")
print("结束")
```

**你第 13 题错在这里**：`while` 是"先判断、后执行"，所以有可能一次都不执行；而"至少执行一次"是别的语言里 `do...while` 的特性。

另外：`while True:` 会死循环，必须靠 `break` 跳出。

### 5.3 break / continue / else

```python
for i in range(1, 6):
    if i == 3:
        continue      # 跳过本次，继续下一轮 → 只跳过 3
    if i == 5:
        break         # 结束整个循环 → 5 及以后都不执行
    print(i)          # 结果：1 2 4
```

```python
total = 0
for i in range(1, 6):
    if i % 2 == 0:
        continue
    total += i
print(total)          # 结果：9   ← 1 + 3 + 5（卷四第 1 题）
```

### 5.4 容易踩的坑

| 坑 | 说明 |
| --- | --- |
| 次数数错 | `range(1, 5)` 是 4 次：1、2、3、4 |
| 漏掉末位 | 想取到 5 要写 `range(6)` 或 `range(1, 6)` |
| 循环里改列表导致漏元素 | 尽量用新列表收集结果 |
| 死循环 | `while` 里别忘了改条件变量 |

### 5.5 练习（答案见 5.6）

1. `range(2, 10, 3)` 依次产生哪些数？循环几次？
2. 用循环求 1+2+...+100。
3. 打印 1~20 中所有偶数。
4. `for i in range(5): if i == 2: break` 实际打印几个数？
5. 下面代码输出什么？
   ```python
   for i in range(3):
       if i == 1:
           continue
       print(i)
   ```

### 5.6 练习答案

1. 2、5、8，共 3 次（不含 10）
2. `print(sum(range(1, 101)))` → 5050
3. `for i in range(2, 21, 2): print(i)`
4. 打印 0、1（到 2 就 break）
5. `0`、`2`

---

## 第 6 章 函数

### 6.1 定义、参数、返回值

```python
def add(a, b):        # 定义用 def，冒号不能少
    return a + b      # 有 return 才有返回值

print(add(3, 4))      # 结果：7

def greet(name):
    print("你好", name)   # 只打印，没有 return

result = greet("小明")    # 输出：你好 小明
print(result)             # 结果：None   ← 没有 return，默认返回 None
```

### 6.2 默认参数陷阱（卷四第 3 题）

```python
def f(x, lst=[]):     # 危险！默认值 [] 只创建一次，所有调用共用
    lst.append(x)
    return lst

print(f(1))   # 结果：[1]
print(f(2))   # 结果：[1, 2]   ← 不是 [2]！
```

正确写法：默认值用 `None`，函数里再创建新列表。

```python
def f(x, lst=None):
    if lst is None:
        lst = []
    lst.append(x)
    return lst

print(f(1))   # 结果：[1]
print(f(2))   # 结果：[2]     ← 每次都是新列表
```

（顺带一个细节：如果写成 `print(f(1), f(2))` 一行打印，结果会是 `[1, 2] [1, 2]`——因为两次调用返回的是同一个对象，打印时看到的都是最终状态。）

### 6.3 作用域：局部 vs 全局（你第 15 题错这里）

```python
count = 10              # 全局变量

def show():
    print(count)        # 结果：10   ← 读取全局变量是允许的

def change():
    count = 99          # 这只是创建了一个新的局部变量，不影响全局

def change_global():
    global count        # 声明后才能真正改到全局
    count = 99

show()
change()
print(count)            # 结果：10
change_global()
print(count)            # 结果：99
```

三条规则：

1. 函数里**读**全局变量：可以
2. 函数里**改**全局变量：必须写 `global`
3. 函数里定义的变量，函数外看不见，强行访问会 `NameError`

### 6.4 练习（答案见 6.5）

1. 没有 `return` 的函数返回什么？
2. `def f(a, b=2): return a * b`，`f(5)` 和 `f(5, 3)` 分别是？
3. 函数内部能直接改全局变量吗？
4. 为什么默认参数不建议写 `[]`？
5. 让函数返回两个值（元组）怎么写？

### 6.5 练习答案

1. `None`
2. `10`、`15`
3. 不能，需要先 `global`
4. 默认值只在定义时创建一次，多次调用会共享同一个列表
5. `def f(): return 1, 2`（实际返回元组 `(1, 2)`）

---

## 第 7 章 文件与异常

### 7.1 打开文件的三种模式

```python
with open("a.txt", "r", encoding="utf-8") as f:   # r：只读（默认）
    text = f.read()

with open("b.txt", "w", encoding="utf-8") as f:   # w：写入，会清空原内容
    f.write("hello")

with open("c.txt", "a", encoding="utf-8") as f:   # a：追加
    f.write("再来一行")
```

`with` 的好处：代码块结束自动关闭文件，中途报错也会关。模式名要加引号，`open("a.txt", r)` 会报 `NameError`（这是自测卷第 16 题的知识点）。

### 7.2 异常处理

```python
try:
    n = int(input("请输入数字："))
    print(10 / n)
except ValueError:
    print("你输入的不是数字")
except ZeroDivisionError:
    print("不能除以 0")
except Exception as e:
    print("其他错误：", e)
finally:
    print("无论如何都会执行")
```

- `except` 可以只捕获指定类型的异常
- `finally` 无论是否出错都会执行（不是只在出错时执行）

### 7.3 练习（答案见 7.4）

1. 哪个模式会清空文件？
2. `with` 的作用是什么？
3. 打开文件时为什么要写 `encoding="utf-8"`？
4. 捕获"除以 0"要用哪个异常名？

### 7.4 练习答案

1. `"w"`
2. 代码块结束后自动关闭文件
3. 避免中文在不同系统编码下乱码
4. `ZeroDivisionError`

---

## 第 8 章 命名规范与基本规矩

### 8.1 标识符规则（你第 1 题错这里）

```python
name = "ok"        # 合法
_name = "ok"       # 合法（下划线开头）
name2 = "ok"       # 合法（数字可以出现在中间/结尾）
2name = "no"       # 报错：SyntaxError，不能以数字开头
my-name = "no"     # 报错：SyntaxError，不能含减号
class = "no"       # 报错：SyntaxError，不能使用关键字
```

规则：**只能由字母、数字、下划线组成，不能以数字开头，不能用关键字**。

### 8.2 关键字列表（背不下来也要认得）

```
False  None  True  and  as  assert  async  await  break  class  continue
def  del  elif  else  except  finally  for  from  global  if  import  in
is  lambda  nonlocal  not  or  pass  raise  return  try  while  with  yield
```

### 8.3 缩进是语法，不是排版

```python
if True:
print("会报错")     # IndentationError：expected an indented block
```

缩进错了程序直接跑不起来，这是自测卷第 21 题的知识点。约定：**每级缩进 4 个空格**。

### 8.4 命名习惯

| 对象 | 推荐写法 | 例子 |
| --- | --- | --- |
| 变量 / 函数 | 全小写 + 下划线 | `user_name`、`count_words` |
| 常量 | 全大写 + 下划线 | `MAX_SIZE` |
| 类 | 大驼峰 | `StudentInfo` |

### 8.5 练习（答案见 8.6）

1. 下面哪些合法：`1a`、`a1`、`_a`、`a-b`、`for`、`myName`？
2. 一级缩进推荐几个空格？
3. `d_class`、`class_d` 哪个能用？

### 8.6 练习答案

1. 合法：`a1`、`_a`、`myName`；不合法：`1a`、`a-b`、`for`
2. 4 个空格
3. 都能用（它们不是关键字）

---

## 第 9 章 综合自测（20 题，答案见章末）

**一、看结果（不要上机）**

1. `list(range(2, 6))` = ?
2. `"hello"[1:3]` = ?
3. `"hello"[-2:]` = ?
4. `len(range(1, 9, 2))` = ?
5. `17 % 5` = ?
6. `"ab" * 2` = ?
7. `bool("")` = ?
8. `bool([0])` = ?
9. `list({1, 1, 2})` = ?
10. `int(float("2.9"))` = ?

**二、判断对错**

11. `range(5)` 包含 5。
12. 元组创建后可以修改元素。
13. `input()` 返回字符串。
14. 函数没有 `return` 就返回 `None`。
15. `while` 循环至少执行一次。
16. `finally` 只有出错时才执行。

**三、写代码**

17. 打印 1 到 n（含 n）之间的奇数。
18. 写 `avg(lst)` 返回列表平均值（空列表返回 0）。
19. 统计字符串里每个字符出现次数。
20. 读取 `data.txt` 并打印行数。

### 第 9 章答案

1. `[2, 3, 4, 5]`
2. `el`
3. `lo`
4. `4`（1、3、5、7）
5. `2`
6. `abab`
7. `False`
8. `True`
9. `[1, 2]`
10. `2`
11. 错（0~4，不含 5）
12. 错
13. 对
14. 对
15. 错（可能一次都不执行）
16. 错（无论是否出错都执行）

17.
```python
for i in range(1, n + 1):
    if i % 2 == 1:
        print(i)
```

18.
```python
def avg(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)
```

19.
```python
def count_chars(s):
    result = {}
    for ch in s:
        result[ch] = result.get(ch, 0) + 1
    return result
```

20.
```python
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print("行数：", len(lines))
```

---

## 附录 A 一页纸速查（贴在显示器边上）

1. **索引从 0 开始**，长度 6 的字符串最大下标是 5
2. **切片 `[起:止]` 不含"止"**；`[1:4]` 取 3 个字符
3. **`range(n)`：0 到 n-1**；`range(a, b)`：a 到 b-1；循环次数 = b - a
4. **假值只有**：`False`、`0`、`""`、`[]`、`{}`、`None`
5. **可变**：`list`、`dict`、`set`；**不可变**：`int`、`str`、`tuple`
6. `10 // 3` = 3（整除）、`10 % 3` = 1（余数）、`2 ** 10` = 1024
7. 取值 `d["k"]`，保险写法 `d.get("k", 默认值)`
8. 没有 `return` 的函数返回 `None`；改全局变量要 `global`
9. `break` 结束整个循环、`continue` 跳过本轮
10. 缩进是语法，一级 4 个空格；文件用 `with open(...)` 自动关闭

## 附录 B 四步验收（每过一步打个勾）

- [ ] 第 1 章练习 6 题全对（边界感专项）
- [ ] 第 2~5 章练习全对，能默写"可变 / 不可变"和"假值清单"
- [ ] 第 9 章综合自测 20 题 ≥ 18 题正确
- [ ] 重跑 `python quiz.py`，得分 ≥ 42 / 50 → 进入学习路线图「阶段 B」

## 附录 C 怎么用你已有的工具

- **JupyterLab**：把讲义里的每段代码亲手敲一遍，不要复制粘贴
- **`%ask` 魔法命令**：`%ask 为什么切片右端不包含`、`%ask 给我 3 道 range 边界的练习题`
- **quiz.py**：随时重测卷一、卷二，看错题是否真的消失
- **错题本**：把做错的题和原因记在一个 `错题本.md` 里，每周翻一次