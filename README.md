# Python 基础自测卷 & AI 方向学习路线图

一份给「想往人工智能方向发展、但 Python 基础还不牢」的人用的自测 + 规划工具包。

- 📝 **一份 100 分的 Python 基础自测卷**（含完整答案解析），用来定位自己的真实水平
- 🖥️ **一个自动判分脚本** `quiz.py`，选择 + 判断题当场出分、给出错题解析
- 🗺️ **一份 AI 方向个人学习路线图**，从基础补强一路排到作品集与求职

## 文件清单

| 文件 | 说明 |
| --- | --- |
| [Python基础自测卷.md](./Python基础自测卷.md) | 试卷：单选 20 题 + 判断 10 题 + 填空 10 空 + 代码阅读 3 题 + 编程 3 题，满分 100 分 |
| [Python基础自测卷-答案解析.md](./Python基础自测卷-答案解析.md) | 全部题目的答案、逐题解析、参考代码、成绩记录表与分数对照建议 |
| [quiz.py](./quiz.py) | 交互式自动判分脚本，覆盖卷一、卷二共 50 分，含错题解析与评级建议 |
| [Python基础补强讲义.md](./Python基础补强讲义.md) | 针对自测薄弱点的补强讲义：索引与区间、类型可变性、运算符、真假值、循环、函数作用域、文件与异常，每章含可运行示例、常见坑、练习与答案 |
| [AI方向学习路线图.md](./AI方向学习路线图.md) | 阶段 A~G 学习路线、每周节奏、里程碑检查点、资源总表、避坑清单 |

## 三步上手

**第 1 步：做题**

打开 [Python基础自测卷.md](./Python基础自测卷.md)，闭卷作答，建议 90 分钟完成。

**第 2 步：判分**

- 卷一、卷二用脚本自动判分：

```powershell
python quiz.py
```

按提示输入 A/B/C/D 或 对/错，脚本最后会给出得分、评级、错题解析与下一步建议。

- 卷三、卷四、卷五对照 [Python基础自测卷-答案解析.md](./Python基础自测卷-答案解析.md) 自行打分，并把成绩填入成绩记录表。

**第 3 步：按分数选起点**

打开 [AI方向学习路线图.md](./AI方向学习路线图.md) 的「第 0 节 起点定位」：

| 得分 | 起点 |
| --- | --- |
| 90 ~ 100 | 阶段 B：数据处理三件套 |
| 75 ~ 89 | 阶段 A 速通版（1 周）→ 阶段 B |
| 60 ~ 74 | 阶段 A 标准版（2~3 周） |
| 60 分以下 | 阶段 A 零基础版（3~4 周） |

## 试卷覆盖的知识点

变量与命名规范、数据类型与类型转换、运算符、字符串与切片、列表 / 元组 / 字典 / 集合、条件判断、for / while 循环与 break / continue、函数定义与默认参数、作用域、文件读写、异常处理、模块导入、常用内置函数、列表推导式、可变与不可变类型、字典 get 取值、默认参数陷阱。

## 设计原则

- **基础为主**：只考「写出正确代码所必需」的语法与概念，不涉及算法竞赛难度的题目
- **答案解析到位**：每题都说明「为什么错」，而不只是给正确答案
- **可自测**：有自动判分脚本，练习闭环不用等人批改
- **路线衔接**：自测分数直接对应学习路线的起点与周期，做完测试就能开工

## 参考资料

路线图与题库设计参考了以下开源项目：

- Python 练习：[zhiwehu/Python-programming-exercises](https://github.com/zhiwehu/Python-programming-exercises)、[Yixiaohan/show-me-the-code](https://github.com/Yixiaohan/show-me-the-code)、[realpython/python-basics-exercises](https://github.com/realpython/python-basics-exercises)、[jerry-git/learn-python3](https://github.com/jerry-git/learn-python3)
- AI 学习：[microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners)、[microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners)、[microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)、[karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero)、[rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)、[d2l-ai/d2l-zh](https://github.com/d2l-ai/d2l-zh)、[AMAI-GmbH/AI-Expert-Roadmap](https://github.com/AMAI-GmbH/AI-Expert-Roadmap)

## 环境要求

- Python 3.8+（`quiz.py` 只用标准库，无需安装第三方依赖）

## License

MIT