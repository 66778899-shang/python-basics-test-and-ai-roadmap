# 人工智能方向 · 个人学习路线图

> 面向对象：有一定 Python 接触经验、但基础不牢、想往人工智能方向发展的学生
> 使用方式：先做 [Python基础自测卷.md](./Python基础自测卷.md) 定位起点，再从下面对应的阶段开始
> 总周期：约 6 个月达到「能独立做 AI 小项目」，12 个月达到「可投实习/初级岗」

---

## 0. 起点定位（先做这一步）

在开始之前先完成自测卷，根据得分确定起点：

| 自测卷得分 | 你的起点 | 说明 |
| --- | --- | --- |
| 90 ~ 100 | 跳到 **阶段 B** | 基础语法过关，直接补数据工具 |
| 75 ~ 89 | **阶段 A（速通版，1 周）** | 只补错题涉及的知识点，然后进入阶段 B |
| 60 ~ 74 | **阶段 A（标准版，2~3 周）** | 系统重过一遍基础，重做自测卷到 85 分以上 |
| 60 分以下 | **阶段 A（零基础版，3~4 周）** | 不要跳过，基础不牢后面全是坑 |

一句话原则：**阶段 A 没达标，不要开始机器学习。** 否则你会在后面花 10 倍时间补债。

---

## 1. 路线总览

| 阶段 | 周期 | 核心内容 | 可验证的产出 |
| --- | --- | --- | --- |
| A. Python 基础补强 | 1 ~ 4 周 | 语法、数据结构、函数、文件、异常、面向对象入门 | 自测卷 ≥ 85 分；独立完成 30+ 基础练习题 |
| B. 数据处理三件套 | 3 ~ 4 周 | NumPy、Pandas、Matplotlib、Jupyter | 一个数据分析小项目（含 3 张图表） |
| C. 数学与统计基础 | 4 ~ 6 周（可与 B 并行） | 线性代数、微积分、概率统计（够用为准） | 能手推梯度下降；看懂论文里的公式符号 |
| D. 经典机器学习 | 6 ~ 8 周 | scikit-learn、特征工程、模型评估 | Kaggle 入门赛（泰坦尼克/房价）完整提交 |
| E. 深度学习入门 | 8 ~ 10 周 | PyTorch、神经网络、CNN、Transformer 概念 | 手写数字识别 ≥ 97%；从零实现一个小 GPT |
| F. 方向选择与深耕 | 持续 | LLM 应用工程 / 模型算法 / 数据方向 | 一个能写进简历的完整项目 |
| G. 作品集与求职 | 长期 | GitHub 作品集、简历、面试八股 | 3 个项目 + 简历 + 面经复盘 |

> 每周建议投入 **10 ~ 12 小时**：工作日每天 1~1.5 小时 + 周末 3~4 小时。
> 时间分配原则：**理论 : 动手编码 = 3 : 7**。只看不写等于没学。

---

## 2. 各阶段详解

### 阶段 A：Python 基础补强

**目标**：能把一个想法直接翻译成能跑的 Python 代码，不再卡在语法上。

**学习内容清单**

- 变量、数据类型（int / float / str / bool）、类型转换
- 运算符、字符串常用方法（split / join / strip / replace / format / f-string）
- 条件判断、循环（for / while / break / continue）
- 列表、元组、字典、集合的常用操作与区别
- 函数：参数、默认值、返回值、作用域、`*args` / `**kwargs`
- 文件读写（`open` / `with`）、异常处理（`try / except / finally`）
- 模块与包（`import`、`pip install`、虚拟环境 venv）
- 面向对象入门（类、属性、方法、`__init__`）
- 基础算法训练：递归、二分查找、简单排序

**练习资源（GitHub 开源，可挑 1~2 个坚持刷完）**

- [zhiwehu/Python-programming-exercises](https://github.com/zhiwehu/Python-programming-exercises) —— 100+ 道分级练习题，附答案，最适合刷基础
- [Yixiaohan/show-me-the-code](https://github.com/Yixiaohan/show-me-the-code) —— Python 练习册，每天一个小程序，题目贴近真实使用场景
- [realpython/python-basics-exercises](https://github.com/realpython/python-basics-exercises) —— 系统化基础练习，配套讲解
- [jerry-git/learn-python3](https://github.com/jerry-git/learn-python3) —— Jupyter Notebook 形式，讲一节练一节，适合零基础
- [trekhleb/learn-python](https://github.com/trekhleb/learn-python) —— 当成「速查手册 + 可运行测试」使用

**产出验收**：自测卷 ≥ 85 分，且错题不再重复错；能不看资料写出「统计词频」「读写文件」这类小脚本。

---

### 阶段 B：数据处理三件套（NumPy / Pandas / Matplotlib）

**目标**：AI 的原料是数据，这一步是学会「处理数据」而不是「学 AI」。

**学习内容**

- NumPy：`ndarray`、形状 shape、切片、广播机制、向量化运算
- Pandas：`Series` / `DataFrame`、读取 CSV/Excel、筛选、分组 `groupby`、合并 `merge`、缺失值处理
- Matplotlib / Seaborn：折线图、柱状图、散点图、直方图
- Jupyter 使用习惯：写 Markdown 记录思路、保存实验

**资源**

- [Kaggle Learn: Python / Pandas](https://www.kaggle.com/learn) —— 免费、交互式、带数据集，性价比最高
- NumPy / Pandas 官方文档的 Quickstart（遇到问题优先查官方文档）
- 数据：Kaggle Datasets、国家统计局公开数据等

**产出验收**：找一个自己感兴趣的 CSV 数据（游戏、电影、成绩、电商都行），完成一次完整分析：清洗 → 统计 → 3 张图 → 一段结论文字，写成一份 Jupyter Notebook 并保存到 GitHub。

---

### 阶段 C：数学与统计基础（够用原则）

**目标**：看懂模型背后的公式，而不是只会调库。

**学习内容**

- 线性代数：向量、矩阵、矩阵乘法、转置、特征值（理解概念即可）
- 微积分：导数、偏导数、链式法则、梯度（**梯度下降必须手推一遍**）
- 概率统计：随机变量、常见分布、期望方差、条件概率、贝叶斯、最大似然
- 优化：损失函数、学习率、过拟合与正则化

**资源**

- [dair-ai/Mathematics-for-ML](https://github.com/dair-ai/Mathematics-for-ML) —— 线代/微积分/概率的精选资料合集，按需查阅
- 3Blue1Brown（B 站有官方中文账号）：《线性代数的本质》《微积分的本质》《神经网络》系列，用可视化建立直觉
- 遇到卡住的公式，用你已配好的 `%ask` 魔法命令让 AI 逐行解释

**产出验收**：能自己推导线性回归的损失函数与梯度更新公式；能解释「为什么需要学习率」；能说出过拟合的三种应对方式。

---

### 阶段 D：经典机器学习

**目标**：掌握机器学习完整流程：数据 → 特征 → 模型 → 评估 → 调优。

**学习内容**

- 监督学习：线性回归、逻辑回归、决策树、随机森林、KNN、SVM
- 无监督学习：K-Means、PCA
- 模型评估：训练集/验证集/测试集、交叉验证、准确率/精确率/召回率/F1、混淆矩阵、ROC-AUC
- 特征工程：缺失值、独热编码、标准化/归一化
- scikit-learn 的 `fit / predict / score` 统一范式

**资源**

- [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) —— 微软官方 12 周课程，24 节课，scikit-learn 为主，循序渐进
- [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) —— 微软 AI 通识课程，覆盖符号 AI 到神经网络，建立全局观
- [ZuzooVn/machine-learning-for-software-engineers](https://github.com/ZuzooVn/machine-learning-for-software-engineers) —— 有编程基础的人学 ML 的路线图
- Kaggle 入门竞赛：Titanic、House Prices（从这两个开始，别一上来就冲高难度赛）

**产出验收**：独立完成 Kaggle「泰坦尼克」或「房价预测」，包含特征工程、交叉验证、模型对比，提交分数并写下复盘。

---

### 阶段 E：深度学习入门

**目标**：会用 PyTorch 搭网络，理解训练过程在发生什么。

**学习内容**

- 神经网络基础：神经元、激活函数、前向传播、反向传播
- PyTorch：Tensor、`Dataset` / `DataLoader`、`nn.Module`、损失函数、优化器、GPU 训练
- CNN（图像）、RNN/LSTM（序列）、Transformer 与注意力机制（重点）
- 训练技巧：批大小、学习率调度、Dropout、早停、可视化训练曲线

**资源**

- [karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero) —— 从零手写反向传播与 Transformer，看完对原理的理解会发生质变
- [d2l-ai/d2l-zh](https://github.com/d2l-ai/d2l-zh) —— 《动手学深度学习》中文版，理论与代码并重，国内最主流教材
- [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) —— 逐步从零实现 GPT，代码清晰
- [AMAI-GmbH/AI-Expert-Roadmap](https://github.com/AMAI-GmbH/AI-Expert-Roadmap) —— 完整 AI 知识地图，用来自查「我漏了什么」

**产出验收**：用 PyTorch 完成 MNIST 手写数字识别（准确率 ≥ 97%，画出 loss 曲线）；跟完 `nn-zero-to-hero` 前 4 讲并能自己解释 backprop。

---

### 阶段 F：方向选择与深耕（三选一）

到这一步你已经能做选择，按兴趣和就业现实考虑：

**F1. LLM 应用 / AI 工程方向（推荐作为第一落点）**

- 门槛相对低、见效快、岗位需求大；适合「先就业再深挖」
- 内容：Prompt 工程、RAG（检索增强生成）、Agent 与工具调用、向量数据库、FastAPI 服务化、模型 API 调用与成本控制
- 资源：[microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)（21 节课，讲 RAG/Agent/函数调用）；[Hugging Face 课程](https://huggingface.co/learn)；[rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)（2026 年新出的从零 AI 工程长课程，523 节，按阶段推进）
- 落地项目：本地知识库问答机器人（RAG）、把 API 封装成带界面的小产品

**F2. 模型 / 算法研究方向**

- 需要更强的数学与论文阅读能力，适合准备读研或走研究岗
- 内容：论文精读、模型复现、微调（LoRA）、实验设计与消融
- 资源：[rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)、[dair-ai/Mathematics-for-ML](https://github.com/dair-ai/Mathematics-for-ML)、Papers with Code、arXiv
- 落地项目：复现一篇小论文；对开源小模型做一次 LoRA 微调并评测

**F3. 数据 / 分析方向**

- 内容：SQL、数据清洗与可视化、统计建模、A/B 实验、业务指标
- 落地项目：一个完整的数据分析报告（含业务结论）

**快速筛选技巧**：三个方向各花一个周末做一个小 demo，哪个做得最投入、最有成就感，就往哪个方向走。

---

### 阶段 G：作品集与求职准备

- **作品集**：把阶段 B / D / E / F 的项目整理到 GitHub，每个项目要有 README（背景、方法、结果、截图、如何运行）
- **简历**：1 页，用「项目 + 结果数字」说话（如「MNIST 准确率 98.2%」「RAG 问答命中率从 60% 提升到 85%」）
- **面试准备**：Python 基础（本仓库自测卷就是很好的复习材料）、机器学习八股、项目细节追问
- **持续输入**：每周读 1 篇技术文章/论文摘要，保持手感

---

## 3. 每周节奏模板

| 时间 | 安排 | 内容 |
| --- | --- | --- |
| 周一 | 1 ~ 1.5 h | 看理论：新知识点 + 记笔记 |
| 周二 | 1 ~ 1.5 h | 跟着敲代码，复现示例 |
| 周三 | 1 ~ 1.5 h | 做练习题（阶段 A 刷题库 / 阶段 D 用 Kaggle） |
| 周四 | 1 ~ 1.5 h | 继续练习 + 记录 bug 与解决方式 |
| 周五 | 1 ~ 1.5 h | 整理本周笔记，写 200 字总结 |
| 周末 | 3 ~ 4 h | 推进项目（阶段产出） |
| 周日晚上 | 30 min | 复盘：本周目标完成度？下周要改什么？ |

**防掉队机制**：连续 3 天没学，就只在第 4 天做「最小任务」（看 10 分钟笔记 + 写 5 行代码），先把习惯保住，再谈进度。

---

## 4. 里程碑检查点（可勾选）

- [ ] 自测卷得分 ≥ 85，题库刷完 30 道以上基础题
- [ ] 能用 Pandas 独立完成一次完整数据分析并出图
- [ ] 能手推线性回归梯度下降，能解释损失函数与学习率
- [ ] 完成 Kaggle Titanic / House Prices 并写下复盘
- [ ] PyTorch 完成 MNIST 训练，准确率 ≥ 97%
- [ ] 从零实现一个小 GPT（或跟完 nn-zero-to-hero 前 4 讲）
- [ ] 完成一个 LLM 应用项目（如 RAG 问答机器人）并部署可访问
- [ ] 3 个项目上传 GitHub，每个都有完整 README
- [ ] 简历定稿，完成 3 次模拟面试复盘

---

## 5. 资源总表

| 类型 | 资源 | 链接 | 用途 |
| --- | --- | --- | --- |
| 练习题库 | Python-programming-exercises | https://github.com/zhiwehu/Python-programming-exercises | 阶段 A 刷题 |
| 练习题库 | show-me-the-code（Python 练习册） | https://github.com/Yixiaohan/show-me-the-code | 阶段 A 小项目练习 |
| 练习题库 | python-basics-exercises | https://github.com/realpython/python-basics-exercises | 阶段 A 系统练习 |
| 教程 | learn-python3 | https://github.com/jerry-git/learn-python3 | 阶段 A 零基础教程 |
| 手册 | learn-python | https://github.com/trekhleb/learn-python | 阶段 A 速查 |
| 机器学习的数学 | Mathematics-for-ML | https://github.com/dair-ai/Mathematics-for-ML | 阶段 C |
| 机器学习课程 | ML-For-Beginners（微软） | https://github.com/microsoft/ML-For-Beginners | 阶段 D 主线 |
| AI 通识课程 | AI-For-Beginners（微软） | https://github.com/microsoft/AI-For-Beginners | 阶段 D 补充 |
| 深度学习教材 | 动手学深度学习（中文） | https://github.com/d2l-ai/d2l-zh | 阶段 E 主线 |
| 深度学习实战 | nn-zero-to-hero（Karpathy） | https://github.com/karpathy/nn-zero-to-hero | 阶段 E 原理突破 |
| LLM 实现 | LLMs-from-scratch | https://github.com/rasbt/LLMs-from-scratch | 阶段 E/F |
| AI 路线图 | AI-Expert-Roadmap | https://github.com/AMAI-GmbH/AI-Expert-Roadmap | 全局自查 |
| 转行路线图 | machine-learning-for-software-engineers | https://github.com/ZuzooVn/machine-learning-for-software-engineers | 全局规划 |
| 生成式 AI 应用 | generative-ai-for-beginners（微软） | https://github.com/microsoft/generative-ai-for-beginners | 阶段 F1 主线 |
| 交互式练习 | Kaggle Learn | https://www.kaggle.com/learn | 阶段 B/D 动手 |
| 模型与数据集 | Hugging Face | https://huggingface.co/learn | 阶段 E/F |

---

## 6. 避坑清单

1. **收藏 ≠ 学会**。资源表里的仓库挑 1~2 个刷透，比收藏 20 个强。
2. **只看视频不敲代码**。每看 10 分钟，至少敲 20 分钟。
3. **跳过数学直接调库**。调库能出结果，但你会在「效果不好时不知道为什么」卡死。
4. **用 AI 代写作业**。AI 用来解释概念、批改代码、出练习题；不要用来替你写完作业，否则自测卷会诚实地暴露你。
5. **一上来就想微调大模型**。先把 Python、数据处理、经典 ML、深度学习基础走完。
6. **追求「学完再做项目」**。每个阶段都要有一个能跑起来的小产出，学中做。
7. **只在一个方向反复横跳**。阶段 F 选定方向后至少坚持 2 个月再评估。

---

## 7. 把你已有的环境用起来

你本机已经配置好了几样工具，可以直接变成学习助力：

- **JupyterLab + DeepSeek 助手**：在 notebook 单元格里用 `%ask` 提问、用 `%%deepseek` 让 AI 生成代码或讲解。推荐用法：
  - `%ask 用一句话解释列表推导式和 for 循环的区别`
  - `%ask 帮我解释这段代码每一步在做什么`（配合选中代码）
  - `%ask 根据我这段代码出一道同类练习题`
- **PyCharm + Continue 插件**：写代码时用 Tab 补全练手感，但**先自己想清楚再补全**，否则会形成依赖。
- **本仓库的两个产物**：`Python基础自测卷.md` 做定位与阶段 A 验收；`quiz.py` 自动判分卷一、卷二。

---

## 8. 参考来源

本路线图参考了以下开源项目与公开资料（GitHub 仓库检索结果）：

- [zhiwehu/Python-programming-exercises](https://github.com/zhiwehu/Python-programming-exercises)、[Yixiaohan/show-me-the-code](https://github.com/Yixiaohan/show-me-the-code)、[realpython/python-basics-exercises](https://github.com/realpython/python-basics-exercises)、[jerry-git/learn-python3](https://github.com/jerry-git/learn-python3)、[trekhleb/learn-python](https://github.com/trekhleb/learn-python)
- [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners)、[microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners)、[microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [AMAI-GmbH/AI-Expert-Roadmap](https://github.com/AMAI-GmbH/AI-Expert-Roadmap)、[ZuzooVn/machine-learning-for-software-engineers](https://github.com/ZuzooVn/machine-learning-for-software-engineers)、[dair-ai/Mathematics-for-ML](https://github.com/dair-ai/Mathematics-for-ML)
- [karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero)、[rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)、[d2l-ai/d2l-zh](https://github.com/d2l-ai/d2l-zh)