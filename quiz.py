#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python 基础自测 · 自动判分脚本

覆盖《Python基础自测卷》卷一（单选 20 题 × 2 分）与卷二（判断 10 题 × 1 分），共 50 分。
卷三填空题、卷四代码阅读题、卷五编程题请对照《Python基础自测卷-答案解析.md》自行打分。

用法：
    python quiz.py            # 按试卷原顺序作答
    python quiz.py --shuffle  # 打乱题目与选项顺序（重测时推荐，避免靠记忆作答）
"""

import random
import sys

# ---------------------------------------------------------------------------
# 题库：与《Python基础自测卷》卷一、卷二完全一致
# 单选 answer 取 "A"/"B"/"C"/"D"；判断 answer 取 "√"/"×"
# ---------------------------------------------------------------------------
QUESTIONS = [
    {
        "type": "choice",
        "q": "下列变量名中，合法的是？",
        "options": ["2name", "my-name", "_count", "class"],
        "answer": "C",
        "explain": "标识符不能用数字开头、不能含连字符、不能使用关键字 class；_count 以下划线开头合法。",
    },
    {
        "type": "choice",
        "q": "type(3.14) 的结果是？",
        "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'double'>"],
        "answer": "B",
        "explain": "带小数点的字面量是 float 类型；Python 没有 double 类型。",
    },
    {
        "type": "choice",
        "q": "表达式 10 // 3 的结果是？",
        "options": ["3.3333333333333335", "3", "4", "1"],
        "answer": "B",
        "explain": "// 是整除（向下取整），结果是 3；10 / 3 才是 3.3333...，10 % 3 是 1。",
    },
    {
        "type": "choice",
        "q": 'bool("") 的值是？',
        "options": ["True", "False", "报错", "None"],
        "answer": "B",
        "explain": "空字符串、0、空列表、空字典、None 在布尔上下文中都是 False。",
    },
    {
        "type": "choice",
        "q": "下列不属于 Python 内置可变类型的是？",
        "options": ["list", "dict", "tuple", "set"],
        "answer": "C",
        "explain": "tuple 不可变，创建后不能增删改元素；list、dict、set 都是可变的。",
    },
    {
        "type": "choice",
        "q": '"Python"[1:4] 的结果是？',
        "options": ['"Pyt"', '"yth"', '"ytho"', '"tho"'],
        "answer": "B",
        "explain": "切片 [1:4] 取索引 1、2、3（不包含 4），即 y、t、h。",
    },
    {
        "type": "choice",
        "q": '表达式 3 * "ab" 的结果是？',
        "options": ['"ababab"', '"ab3"', "报错", '"abab"'],
        "answer": "A",
        "explain": "字符串可以用整数相乘进行重复，得到 ababab。",
    },
    {
        "type": "choice",
        "q": "下列哪个方法可以正确地向列表末尾添加一个元素？",
        "options": ["lst.add(1)", "lst.append(1)", "lst.push(1)", "lst.insert(1)"],
        "answer": "B",
        "explain": "列表用 append()；add() 是集合的方法，push() 是别的语言的写法，insert(1) 缺参数会报错。",
    },
    {
        "type": "choice",
        "q": "len([1, [2, 3], 4]) 的值是？",
        "options": ["4", "3", "2", "5"],
        "answer": "B",
        "explain": "长度按元素个数算，[2, 3] 整体算 1 个元素，所以是 3。",
    },
    {
        "type": "choice",
        "q": '已知 d = {"a": 1, "b": 2}，要取出键 "a" 对应的值，正确写法是？',
        "options": ['d["a"]', 'd("a")', "d -> a", 'd.get{"a"}'],
        "answer": "A",
        "explain": "字典取值用方括号 d[\"a\"]；d(\"a\") 是调用语法，会报错。",
    },
    {
        "type": "choice",
        "q": "代码 x = 5 后，if x > 3 打印 A，elif x > 1 打印 B，else 打印 C，输出是？",
        "options": ["A", "B", "AB", "C"],
        "answer": "A",
        "explain": "x > 3 成立就进入第一个分支，elif 不会被检查，只打印 A。",
    },
    {
        "type": "choice",
        "q": "for i in range(1, 5): 这个循环一共会执行几次？",
        "options": ["4 次", "5 次", "3 次", "报错"],
        "answer": "A",
        "explain": "range(1, 5) 生成 1、2、3、4，左闭右开，共 4 次。",
    },
    {
        "type": "choice",
        "q": "关于 while 循环，下列说法正确的是？",
        "options": [
            "while 循环至少会执行一次循环体",
            "while 循环有可能一次都不执行",
            "while 循环的条件必须是 True",
            "while 循环不能和 else 一起使用",
        ],
        "answer": "B",
        "explain": "while 先判断后执行，条件一开始不成立就一次也不执行；条件永远为 True 会死循环；while 可以搭配 else。",
    },
    {
        "type": "choice",
        "q": "def f(a, b=10): return a * b，调用 f(3, 4) 的返回值是？",
        "options": ["34", "12", "40", "报错"],
        "answer": "B",
        "explain": "传入的 4 覆盖默认值 10，3 * 4 = 12。",
    },
    {
        "type": "choice",
        "q": "关于变量作用域，下列说法正确的是？",
        "options": [
            "函数内部可以随意修改外部全局变量，不需要任何声明",
            "函数内部定义的变量，在函数外部可以直接访问",
            "函数内部读取（不修改）全局变量是允许的",
            "Python 没有作用域的概念",
        ],
        "answer": "C",
        "explain": "读取全局变量允许；修改全局变量需要 global；局部变量在函数外访问会 NameError。",
    },
    {
        "type": "choice",
        "q": "要打开一个文本文件并读取内容，正确写法是？",
        "options": ['open("a.txt", "r")', 'open("a.txt", "read")', 'open("a.txt", "w")', "open(\"a.txt\", r)"],
        "answer": "A",
        "explain": "\"r\" 是只读模式；\"w\" 会清空文件；r 不加引号会被当成变量名报错。",
    },
    {
        "type": "choice",
        "q": 'print(1, 2, sep="-") 的输出是？',
        "options": ["1-2", "12", "1 2", "-1-2"],
        "answer": "A",
        "explain": "sep 指定多个输出值之间的分隔符，默认是空格。",
    },
    {
        "type": "choice",
        "q": "列表推导式 [x * x for x in range(4)] 的结果是？",
        "options": ["[0, 1, 4, 9]", "[1, 4, 9, 16]", "[0, 1, 2, 3]", "[1, 2, 3, 4]"],
        "answer": "A",
        "explain": "range(4) 生成 0、1、2、3，平方后为 [0, 1, 4, 9]。",
    },
    {
        "type": "choice",
        "q": "关于 try / except，下列说法正确的是？",
        "options": [
            "异常如果不处理，程序一定会崩溃且无法捕获",
            "except 可以捕获指定类型的异常",
            "finally 代码块只在发生异常时执行",
            "try 必须搭配 finally 使用",
        ],
        "answer": "B",
        "explain": "except ValueError: 可只捕获指定异常；finally 无论是否异常都执行；try 搭配 except 或 finally 均可。",
    },
    {
        "type": "choice",
        "q": '表达式 "1" + 1 的结果是？',
        "options": ["2", '"11"', "抛出 TypeError", "1"],
        "answer": "C",
        "explain": "字符串与整数不能直接相加会抛 TypeError；int(\"1\") + 1 得 2，\"1\" + str(1) 得 \"11\"。",
    },
    {
        "type": "judge",
        "q": "Python 中的缩进只是为了好看，不影响程序的运行结果。",
        "options": ["对", "错"],
        "answer": "×",
        "explain": "缩进是语法的一部分，缩进错误会直接导致 IndentationError。",
    },
    {
        "type": "judge",
        "q": "== 用于比较两个值是否相等，is 用于比较两个变量是否指向同一个对象。",
        "options": ["对", "错"],
        "answer": "√",
        "explain": "[1] == [1] 为 True，但 [1] is [1] 为 False。",
    },
    {
        "type": "judge",
        "q": "元组（tuple）创建之后，可以修改它的元素。",
        "options": ["对", "错"],
        "answer": "×",
        "explain": "元组不可变，修改元素会报 TypeError。",
    },
    {
        "type": "judge",
        "q": "input() 函数返回的数据类型是字符串。",
        "options": ["对", "错"],
        "answer": "√",
        "explain": "参与数值计算前必须先 int() 或 float() 转换。",
    },
    {
        "type": "judge",
        "q": "列表和字符串都支持用 + 进行拼接。",
        "options": ["对", "错"],
        "answer": "√",
        "explain": "两者都支持 + 拼接，但字符串和列表之间不能直接相加。",
    },
    {
        "type": "judge",
        "q": "range(5) 生成的序列中包含数字 5。",
        "options": ["对", "错"],
        "answer": "×",
        "explain": "range(5) 生成 0、1、2、3、4，不含 5。",
    },
    {
        "type": "judge",
        "q": "函数如果没有写 return 语句，默认返回 None。",
        "options": ["对", "错"],
        "answer": "√",
        "explain": "没有 return 或只有 return 时，函数返回 None。",
    },
    {
        "type": "judge",
        "q": "集合（set）中可以保存重复的元素。",
        "options": ["对", "错"],
        "answer": "×",
        "explain": "集合元素唯一，重复元素会被自动去重。",
    },
    {
        "type": "judge",
        "q": "使用 with open(\"a.txt\") as f: 可以让文件在代码块结束后自动关闭。",
        "options": ["对", "错"],
        "answer": "√",
        "explain": "with 是上下文管理器，即使中途抛异常也会自动关闭文件。",
    },
    {
        "type": "judge",
        "q": 'int("3.5") 可以正常执行，并得到结果 3。',
        "options": ["对", "错"],
        "answer": "×",
        "explain": "int(\"3.5\") 会抛 ValueError，正确写法是 int(float(\"3.5\"))。",
    },
]

POINTS = {"choice": 2, "judge": 1}          # 单选 2 分，判断 1 分
TYPE_NAME = {"choice": "单选", "judge": "判断"}

CHOICE_KEYS = {"A": 0, "B": 1, "C": 2, "D": 3}
JUDGE_YES = {"对", "正确", "√", "y", "yes", "1", "true", "t"}
JUDGE_NO = {"错", "错误", "×", "x", "no", "0", "false", "f"}


def parse_choice(raw):
    """把用户输入解析成选项字母，无法识别时返回 None。"""
    text = raw.strip().upper()
    if text in CHOICE_KEYS:
        return text
    if text in {"1", "2", "3", "4"}:
        return "ABCD"[int(text) - 1]
    return None


def parse_judge(raw):
    """把用户输入解析成 √ / ×，无法识别时返回 None。"""
    text = raw.strip().lower()
    if text in JUDGE_YES:
        return "√"
    if text in JUDGE_NO:
        return "×"
    return None


def build_quiz(shuffle=False):
    """返回本次作答的题单；shuffle=True 时打乱题目顺序与单选选项顺序。"""
    questions = []
    for question in QUESTIONS:
        item = dict(question)
        if shuffle and item["type"] == "choice":
            correct = CHOICE_KEYS[item["answer"]]
            order = list(range(len(question["options"])))
            random.shuffle(order)
            item["options"] = [question["options"][i] for i in order]
            item["answer"] = "ABCD"[order.index(correct)]
        questions.append(item)
    if shuffle:
        random.shuffle(questions)
    return questions


def ask_one(index, question):
    """展示一道题并获取用户答案，返回 (用户答案, 是否放弃)。"""
    label = TYPE_NAME[question["type"]]
    print(f"\n第 {index} 题（{label}，{POINTS[question['type']]} 分）")
    print(f"  {question['q']}")
    for order, option in enumerate(question["options"]):
        print(f"    {chr(65 + order)}. {option}" if question["type"] == "choice" else f"    {option}")

    hint = "请输入 A/B/C/D（直接回车放弃本题）：" if question["type"] == "choice" else "请输入 对/错（直接回车放弃本题）："
    while True:
        raw = input(hint)
        if raw.strip() == "":
            return None, True
        answer = parse_choice(raw) if question["type"] == "choice" else parse_judge(raw)
        if answer is not None:
            return answer, False
        print("  输入无法识别，请重新输入。")


def grade(score, full_score):
    """根据得分率给出评语与建议。"""
    rate = score / full_score
    if rate >= 0.9:
        return "基础扎实", "可以直接从学习路线图的「阶段 B：数据处理三件套」开始。"
    if rate >= 0.75:
        return "基础较好，有个别漏洞", "先把错题对应的知识点补齐（1 周内），再进入阶段 B。"
    if rate >= 0.6:
        return "基础不牢", "走「阶段 A：Python 基础补强」，用 2~3 周重新过一遍基础并重做本卷。"
    return "需要系统重学基础", "从「阶段 A」的零基础资源开始，不要急着碰机器学习。"


def main():
    shuffle = "--shuffle" in sys.argv
    questions = build_quiz(shuffle)
    full_score = sum(POINTS[q["type"]] for q in questions)
    print("=" * 56)
    print("Python 基础自测 · 自动判分（卷一 + 卷二）")
    if shuffle:
        print("（重测模式：题目与选项顺序已打乱）")
    print(f"共 {len(questions)} 题，满分 {full_score} 分；填空题、代码阅读题、编程题请自行对照答案解析")
    print("=" * 56)

    score = 0
    records = []          # (题号, 题目, 你的答案, 正确答案, 解析, 是否答对, 是否放弃)
    for index, question in enumerate(questions, 1):
        user_answer, gave_up = ask_one(index, question)
        correct = (not gave_up) and user_answer == question["answer"]
        if correct:
            score += POINTS[question["type"]]
        records.append((index, question, user_answer, correct, gave_up))

    # ---- 结果统计 ----
    print("\n" + "=" * 56)
    print("成绩单")
    print("=" * 56)
    print(f"得分：{score} / {full_score}    正确率：{score / full_score:.0%}")
    level, advice = grade(score, full_score)
    print(f"评级：{level}")
    print(f"建议：{advice}")

    wrong = [r for r in records if not r[3]]
    if not wrong:
        print("\n全部答对，非常棒！")
    else:
        print(f"\n错题回顾（共 {len(wrong)} 题）")
        print("-" * 56)
        for index, question, user_answer, _correct, gave_up in wrong:
            shown = "（放弃）" if gave_up else user_answer
            print(f"\n第 {index} 题　你的答案：{shown}　正确答案：{question['answer']}")
            print(f"  题目：{question['q']}")
            print(f"  解析：{question['explain']}")

    print("\n提示：把错题对应的知识点记到错题本，一周后重做本卷验收。")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n已中断，本次作答不计分。下次再来！")