# Mathematical Academic Writing

[![Version](https://img.shields.io/badge/version-v0.3.0-365E8D)](#validation)
[![License: MIT](https://img.shields.io/badge/license-MIT-5F8C70)](LICENSE)
[![Verify public core](https://github.com/JiahaoLi-creator/mathematical-academic-writing/actions/workflows/verify-core.yml/badge.svg)](https://github.com/JiahaoLi-creator/mathematical-academic-writing/actions/workflows/verify-core.yml)

![Mathematical Academic Writing workflow](assets/usage-workflow.png)

[Quick start](#quick-start--快速开始) · [English](#english) · [中文](#中文) · [Worked example](#worked-example--双语示例) · [Validation](#validation)

**A source-grounded Codex skill that treats mathematical meaning as an explicit constraint and
reduces repetitive or generic defensive prose.**

**一个面向数学学术写作的 Codex skill：以来源为依据，将数学含义作为明确约束，并减少重复和空泛的防御性表达。**

---

## Quick start | 快速开始

Install the public runtime into the Codex skills directory:

将公开 runtime 安装到 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/JiahaoLi-creator/mathematical-academic-writing.git \
  ~/.codex/skills/mathematical-academic-writing
```

Start a new Codex task after installation, then invoke the skill explicitly:

```text
$mathematical-academic-writing

Task: Revision
Genre: Visual companion
Primary source: [lecture notes, chapter or section]
Audience: [intended reader]
Preserve: [notation, assumptions, formulas, citations, and figure numbers]
Request: [the exact writing task]
```

安装后开启一个新的 Codex task，再通过 `$mathematical-academic-writing` 显式调用。

Update an existing public installation:

更新已有的公开安装版本：

```bash
git -C ~/.codex/skills/mathematical-academic-writing pull --ff-only
```

---

## English

### Overview

`mathematical-academic-writing` helps Codex draft, revise, review, and verify mathematical prose in
probability, stochastic processes, stochastic analysis and stochastic calculus, quantitative
finance, optimization, and numerical analysis. It is designed for work built around definitions,
assumptions, formal results, derivations, computations, figures, simulations, and source-specific
notation.

The skill organises a writing task around five questions:

1. What mathematical object is under discussion?
2. Which assumptions and notation govern it?
3. What claim is being made?
4. What evidence supports that claim?
5. Where should the claim be stated once, clearly and at the correct strength?

The resulting workflow treats supplied notation, assumptions, claims, citations, and numerical
values as explicit commitments. The final integrity pass compares the result with those
commitments and identifies material departures.

### Why this skill was created

The project began while developing a set of MATH3015 Visual Companion notebooks. Those notebooks
used plots, simulations, and short interpretations to explain topics such as conditional
expectation, martingales, Brownian motion, and the Itô integral. The lecture notes carried the
formal course development; the notebooks focused on helping a new reader understand what the
objects and figures meant.

Early revisions exposed several recurring AI-writing problems:

- a paragraph opened with a disclaimer instead of the mathematical object;
- short notebooks repeated an executive summary, section recap, and final summary;
- figure interpretations were broken into generic `Results` and `Interpretation` bullet lists;
- a simulation or plot inherited proof-level language;
- stylistic rewriting changed notation, assumptions, quantifiers, or convergence modes;
- deleting every hedge also deleted valid limitations, failed converses, and mathematical
  negation.

The useful distinction was therefore functional rather than lexical. A sentence is retained when
it carries validity, scope, evidence, logic, or necessary reader guidance. It is rewritten or
removed when it only anticipates an unspecified objection or repeats a settled claim.

### From notebook revisions to a tested writing system

The skill developed in five stages.

1. **Concrete failures became review cases.** Notebook passages supplied examples of defensive
   framing, repeated conclusions, notation drift, and evidence inflation.
2. **Qualitative study shaped the first rule set.** Close reading of the probability and textbook
   materials informed the mathematical-writing rules in v0.1.0. Kiterlin's MIT-licensed
   [anti-defensive-writing](https://github.com/Kiterlin/anti-defensive-writing) project contributed
   the functional-classification, positive-scope, precision-preservation, and review-first ideas.
3. **Corpus measurements audited and revised those rules.** For v0.2.0, a selected local corpus of
   27 logical sources, 617 PDF pages, and 238,497 normalized words was assembled from probability,
   stochastic analysis, mathematical finance, optimization, and numerical methods. Its analysis
   profiles comprise 7 theory papers, 4 applied papers, 3 empirical or computational sources,
   7 rigorous textbooks, and 6 applied textbooks. The audit revised the v0.1 rule set: it expanded
   the notation record into the five-column working register, added claim siting and the pushback
   integrity gate, recalibrated evidence language, and refined the figure, simulation, and
   anti-defensive rules used in the current release.
4. **Rule changes became testable against known cases.** Deterministic checks, semantic
   assertions, blind cases, metric assertions, mutation tests, and human release review were
   expanded around the revised system.
5. **v0.3.0 widened the audit boundary.** Research-article workflows, a source-and-derivation
   correction protocol, artifact verification levels, and a quantitative-finance profile were
   added, then evaluated in fresh Review, Draft, Verification, and notebook contexts.

The project was developed iteratively with Codex. Model-generated drafts supplied candidate text
and failure cases; explicit rules, regression oracles, semantic reviews, and human release
decisions determined what entered the accepted skill.

The selected corpus is a calibration and audit source, not a redistributed training dataset or a
representative sample of all academic writing. The recurring model-draft problems came from project
observations; the corpus measurements describe the selected scholarly baseline rather than an
AI-versus-human comparison. Its aggregate measurements and bibliography are documented in the
[corpus manifest](references/corpus_manifest.md); source PDFs and extracted text remain outside the
public repository.

### Core design

| Principle | Operational meaning |
| --- | --- |
| Mathematical truth first | Preserve objects, domains, quantifiers, assumptions, implication direction, and convergence modes. |
| Source fidelity | Use the designated primary source for notation, theorem scope, numbering, and topic boundaries. |
| Working register | Lock each material claim to its support, evidence level, site, and citation; show the register only when traceability is material. |
| Evidence-matched verbs | Proofs establish; derivations yield; examples exhibit; figures display; simulations estimate or agree numerically. |
| Claim siting | State a claim where its support is strongest, then refer to the theorem, equation, section, or figure. |
| Correction authority | Diagnose source conflicts and suspected errors without silently replacing the governing source. |
| Verification depth | Distinguish text-, source-, execution-, and render-bound checks and report only the depth actually reached. |
| Functional revision | Preserve meaningful negation, contrasts, limitations, and counterexamples; remove generic disclaimers and recapitulation. |
| Genre and reader fit | Let research articles, proofs, lectures, computational studies, and visual companions use different structures. |

### How the workflow operates

1. **Select the task mode.** Choose Draft, Revision, Review, or Verification.
2. **Select the genre and reader.** Identify whether the output is a research passage,
   theorem-proof exposition, teaching explanation, computational analysis, or visual companion.
3. **Establish source and correction authority.** Name the primary source, auxiliary sources, and
   whether diagnosis or substantive correction is requested.
4. **Set the verification depth.** Distinguish text, source, execution, and rendered-artifact
   checks; do not claim a level that was not performed.
5. **Build the working register.** Lock notation, objects, assumptions, claims, support, evidence
   level, site, and citation. Keep it internal for a routine light edit and show it when
   traceability is material.
6. **Draft or revise by paragraph function.** Each paragraph performs one main job: motivation,
   definition, theorem, proof, example, caption, interpretation, or limitation.
7. **Match language to evidence.** The evidence ladder fixes the strongest verb available to each
   claim.
8. **Run the anti-defensive audit.** Retain content that changes validity or interpretation;
   rewrite framing that delays the mathematical content.
9. **Compare the result with the register.** Check symbols, assumptions, quantifiers, claims,
   citations, numerical values, execution evidence, and visible rendering before returning the
   work.

### Task and genre modes

| Mode | Use it for | Typical output |
| --- | --- | --- |
| Draft | Create prose from supplied mathematical content and sources. | Original prose; compact register, `Omit`, or `Flag` when material. |
| Revision | Improve existing prose while preserving or source-authorizing its mathematical semantics. | Revised passage and only material register entries or notes. |
| Review | Diagnose problems without rewriting the source. | Prioritised findings or `Keep`, `Rewrite`, `Compress`, `Delete`, and `Flag` decisions. |
| Verification | Check claims, derivations, citations, numerical conclusions, or artifacts against evidence. | Verdict, decisive support, verification depth, and correction authority. |

Genre profiles cover research articles, theorem-proof exposition, textbook and lecture
explanations, computational and empirical analysis, and visual companions.

### How to invoke it

Name the skill explicitly and supply the task contract:

```text
$mathematical-academic-writing

Task: [Draft | Revision | Review | Verification]
Genre: [research article | theorem-proof | lecture explanation |
        computational analysis | visual companion]
Audience: [intended reader]
Primary source: [authoritative paper, textbook, lecture notes, or derivation]
Auxiliary sources: [optional]
Preserve: [notation, claims, structure, citations, parameters, figure numbers]
Output: [length, format, and whether explanation or findings are wanted]

Material:
[paste or attach the passage, source, derivation, figure, code, or results]
```

The most useful requests identify five things:

- the task and genre;
- the intended reader;
- the governing source;
- the elements that must remain fixed;
- the desired output form and length.

Codex may also select the skill automatically when the primary deliverable is mathematical prose.
Explicit invocation is preferable when notation, source hierarchy, or evidence strength is central
to the task.

### Example requests

**Revise a visual interpretation**

```text
$mathematical-academic-writing

Task: Revision
Genre: Visual companion
Primary source: my lecture notes, Chapter 3
Audience: Students meeting Brownian path regularity for the first time

Preserve every symbol, formula, parameter, and figure number. Rewrite the figure
interpretation as one concise paragraph. Explain the encoding before the conclusion,
match every verb to its evidence, and remove repeated generic disclaimers.

Current passage:
[paste the caption or interpretation]
```

**Review theorem-proof exposition**

```text
$mathematical-academic-writing

Task: Review
Genre: Theorem-proof exposition
Governing source: [paper, textbook, or supplied derivation]

Check the passage for missing assumptions, changed quantifiers, implication direction,
notation drift, and repeated conclusions. Return only prioritised findings.

Passage:
[paste the theorem and proof]
```

**Verify a computational claim**

```text
$mathematical-academic-writing

Task: Verification
Genre: Computational analysis
Primary result: [theorem or exact benchmark]
Experiment: [code, output, parameters, seed policy, and error definition]

Identify each material claim and its assumptions. Separate theorem support from
numerical evidence, Monte Carlo uncertainty, and discretisation error.
```

More reusable prompts are available in [examples/quick-start.md](examples/quick-start.md).

---

## 中文

### 项目简介

`mathematical-academic-writing` 用于辅助 Codex 起草、修改、审阅和核验数学写作，适用范围包括
概率论、随机过程、随机分析与随机微积分、数理金融、优化和数值分析。它特别适合围绕定义、
假设、定理、推导、计算、图表、模拟和来源特定记号展开的写作任务。

该 skill 会围绕五个问题组织写作：

1. 当前讨论的数学对象是什么？
2. 哪些假设和记号约束这个对象？
3. 文本正在提出什么论断？
4. 哪一类证据支撑该论断？
5. 这个论断应该在哪里以恰当的强度陈述一次？

工作流程会把用户提供的记号、假设、论断、引用和数值记录为明确约束，并在输出前将修改结果
与这些约束逐项比较，使实质性变化能够被识别出来。

### 这个 skill 是怎么来的

这个项目起源于 MATH3015 Visual Companion notebooks 的制作。notebook 通过图表、模拟和简短的
看图分析，辅助初学者理解条件期望、鞅、布朗运动和 Itô 积分等内容；讲义负责课程中的正式理论
展开，notebook 则负责解释数学对象、图形编码和直观含义。

在反复修改 notebook 的过程中，出现了几类稳定的 AI 写作问题：

- 段落先说明“这不是什么”，而没有先讲正在研究的数学对象；
- 篇幅不长的 notebook 同时出现 Executive Summary、分节总结和结尾 Summary；
- 看图分析被拆成缺乏内容的 `Results` 与 `Interpretation` 分点；
- 图表或模拟获得了只有证明才能支撑的论断强度；
- 语言润色改变了记号、假设、量词或收敛方式；
- 机械删除所有 hedge 时，也删除了真实限制、反例、逆命题失败和必要的数学否定。

因此，判断标准不能只是某个词是否出现，而要判断一句话在数学论证中的功能。凡是决定正确性、
适用范围、证据强度、逻辑关系或必要读者指引的内容都应保留；只是在预防不明确质疑、重复既有
结论或延迟数学内容的句子，则应改写或删除。

### 从 notebook 修改发展为可测试系统

整个 skill 经历了五个阶段：

1. **将实际失败转化为 review cases。** Notebook 中的防御型表达、重复结论、记号漂移和
   evidence inflation 成为最初的回归样本。
2. **定性阅读形成第一版规则。** 对 probability 与 textbook 材料的细读构成 v0.1.0
   数学写作规则的基础。Kiterlin 以 MIT License 发布的
   [anti-defensive-writing](https://github.com/Kiterlin/anti-defensive-writing) 提供了
   functional classification、positive scope、precision preservation 和 review-first
   的设计启发。
3. **语料测量审计并修订第一版规则。** 在 v0.2.0 阶段，项目从概率论、随机分析、数理金融、
   优化和数值方法材料中整理出一个本地精选语料，包含 27 个 logical sources、617 个选定 PDF
   页面和 238,497 个归一化正文词。其 analysis profiles 分为 7 篇理论论文、4 篇应用论文、
   3 个实证或计算来源、7 本严格教材和 6 本应用教材。该轮审计修订了 v0.1 的规则体系：将
   notation record 扩展为五列 working register，新增 claim siting 与 pushback integrity
   gate，重新校准证据用语，并完善当前版本中的图表、模拟和 anti-defensive rules。
4. **让规则修改可以通过已知案例检验。** 修订后的系统扩展了确定性检查、语义断言、blind
   cases、metric assertions、mutation tests 和人工 release review。
5. **v0.3.0 扩展审计边界。** 新增 research-article workflows、来源与推导纠错协议、artifact
   verification 层级和 quantitative-finance profile，并在全新的 Review、Draft、Verification
   与 notebook 上下文中完成检验。

该项目由 Codex 参与迭代：模型生成的稿件提供 candidate text 和失败案例，明确规则、回归
oracle（预先锁定的预期结果）、语义审阅和人工 release 决定共同控制哪些修改可以进入正式版本。

这套精选 corpus 用于校准和审计写作规则，不是随公开仓库分发的训练集，也不代表全部学术写作。
反复出现的模型写作问题来自项目实践观察；corpus 指标描述的是精选学术样本，不能解释为
AI 与人类学者之间的量化比较。公开的
[corpus manifest](references/corpus_manifest.md) 记录了聚合指标与参考书目；PDF 和抽取正文保留在
私有验证环境中。

### 核心设计

| 原则 | 实际作用 |
| --- | --- |
| 数学正确性优先 | 保留对象、定义域、量词、假设、蕴含方向和收敛方式。 |
| 遵循权威来源 | 由用户指定的 primary source 决定记号、定理范围、编号和主题边界。 |
| Working register | 锁定论断、支撑、证据层级、陈述位置和引用；仅在需要追溯时展示。 |
| 证据与动词匹配 | 证明可以 establish；推导可以 yield；例子可以 exhibit；图表负责 display；模拟负责 estimate 或报告数值一致性。 |
| Claim siting | 在支撑最强的位置陈述一次，后文通过定理、公式、章节或图号回指。 |
| 纠错权限 | 诊断来源冲突与疑似错误，但不静默替换 governing source。 |
| Verification depth | 区分 text-bound、source-bound、execution-bound 与 render-bound 检查，只报告实际达到的层级。 |
| 功能型修改 | 保留必要否定、对比、限制和反例，减少空泛免责声明与重复总结。 |
| 适配体裁和读者 | 研究论文、定理证明、课堂解释、计算研究和 visual companion 使用不同结构。 |

### 工作流程

1. **选择任务模式：** Draft、Revision、Review 或 Verification。
2. **确定体裁和读者：** 明确输出是研究论文、定理证明、课堂讲解、计算分析还是 visual
   companion，以及读者已有的背景。
3. **确定来源与纠错权限：** 指定 primary source、辅助来源，以及任务只需诊断还是允许实质纠错。
4. **确定 verification depth：** 区分文本、来源、执行与渲染检查，不声称未实际完成的层级。
5. **建立 working register：** 锁定记号、对象、假设、论断、支撑、证据层级、陈述位置和引用；
   常规轻量修改可保留在内部，需要可追溯性时再展示。
6. **按段落功能写作：** 每段主要完成 motivation、definition、theorem、proof、example、
   caption、interpretation 或 limitation 中的一项任务。
7. **让用词服从证据：** 根据 evidence ladder 选择证据允许的最强动词。
8. **运行 anti-defensive audit：** 保留影响数学含义的限定，将延迟正文的防御型框架改为直接
   陈述对象、关系和范围。
9. **与 register 终检：** 核对符号、假设、量词、论断、引用、数值、执行证据和可见渲染。

### 四种任务模式

| 模式 | 适用场景 | 典型输出 |
| --- | --- | --- |
| Draft | 根据用户提供的数学内容和来源起草新文本。 | 原创正文；必要时附 compact register、`Omit` 或 `Flag`。 |
| Revision | 保留或经来源授权纠正数学语义并改进文本。 | 修改稿 + 仅必要的 register 条目或说明。 |
| Review | 诊断问题，不直接重写原文。 | 优先级 findings，或 `Keep`、`Rewrite`、`Compress`、`Delete`、`Flag`。 |
| Verification | 根据证据核验论断、推导、引用、数值结论或 artifact。 | verdict、决定性依据、verification depth 与纠错权限。 |

支持的 genre 包括研究论文、定理证明、教材与课堂讲解、计算或实证分析，以及 visual
companion。

### 如何调用

在任务中明确写出 skill 名称，并提供任务约束：

```text
$mathematical-academic-writing

Task: [Draft | Revision | Review | Verification]
Genre: [research article | theorem-proof | lecture explanation |
        computational analysis | visual companion]
Audience: [目标读者]
Primary source: [权威论文、教材、讲义或推导]
Auxiliary sources: [可选]
Preserve: [必须保留的记号、论断、结构、引用、参数和图号]
Output: [篇幅、格式，以及需要正文还是 findings]

Material:
[粘贴或附上原文、来源、推导、图片、代码或结果]
```

高质量请求通常包含五项信息：

- 任务模式和体裁；
- 目标读者；
- 决定记号与范围的 primary source；
- 必须保持不变的内容；
- 期望的篇幅和输出形式。

当主要交付物是数学写作时，Codex 也可能自动选择该 skill。若任务特别重视记号、来源层级或
证据强度，建议显式调用。

### 使用示例

**修改 notebook 看图分析**

```text
$mathematical-academic-writing

Task: Revision
Genre: Visual companion
Primary source: 我的讲义 Chapter 3
Audience: 第一次接触布朗运动路径正则性的学生

保留所有符号、公式、参数和图号。将 interpretation 改写为一个简洁段落，
先解释图形编码，再说明数学含义，并让每个动词与证据强度匹配。

Current passage:
[粘贴 caption 或 interpretation]
```

**审阅定理与证明**

```text
$mathematical-academic-writing

Task: Review
Genre: Theorem-proof exposition
Governing source: [论文、教材或用户提供的推导]

检查遗漏假设、量词变化、蕴含方向、记号漂移和重复结论。
只返回按优先级排序的 findings，不重写正文。

Passage:
[粘贴定理和证明]
```

**核验计算结论**

```text
$mathematical-academic-writing

Task: Verification
Genre: Computational analysis
Primary result: [定理或精确 benchmark]
Experiment: [代码、输出、参数、随机种子策略和误差定义]

识别每项实质性论断及其假设。区分定理支撑、数值证据、Monte Carlo uncertainty
和 discretisation error。
```

更多可直接复用的 prompts 见 [examples/quick-start.md](examples/quick-start.md)。

---

## Worked example | 双语示例

The following example shows why notation, evidence, and prose style are reviewed together.

下面的例子说明为什么记号、证据和写作方式需要同时检查。

Assume that the task supplies MATH3015, Chapter 3 as the primary source together with Figure 6.

假设任务同时提供 MATH3015 Chapter 3 作为 primary source，并附上 Figure 6。

### Working register

**Notation | 记号**

| Object / 对象 | Authoritative notation / 权威记号 | Local abbreviation / 局部缩写 |
| --- | --- | --- |
| Standard Brownian motion / 标准布朗运动 | $B=(B_t)_{t\geq 0}$ | None / 无 |
| Positive time increment / 正时间增量 | $h>0$ | None / 无 |
| Standard normal variable / 标准正态变量 | $Z\sim N(0,1)$ | None / 无 |
| Standard normal CDF / 标准正态分布函数 | $\Phi$ | None / 无 |

**Claims | 论断**

| Claim / 论断 | Support / 支撑 | Ladder rung / 证据层级 | Site / 陈述位置 | Citation / 引用 |
| --- | --- | --- | --- | --- |
| $(B_{t+h}-B_t)/h\overset{d}=Z/\sqrt h$ | Brownian increment law / 布朗运动增量分布 | Exact derivation / 精确推导 | Figure interpretation / 看图分析 | MATH3015, Chapter 3 |
| The median absolute quotient is $\Phi^{-1}(0.75)h^{-1/2}$ / 绝对差商中位数为该表达式 | Distributional calculation / 分布计算 | Exact derivation / 精确推导 | Figure interpretation / 看图分析 | MATH3015, Chapter 3 |
| The plotted medians follow the reference scale / 图中的中位数沿参考尺度变化 | Supplied Figure 6 / 用户提供的 Figure 6 | Figure / 图表 | Figure interpretation / 看图分析 | Supplied Figure 6 / 用户提供的 Figure 6 |
| Brownian sample paths are almost surely nowhere differentiable / 布朗运动样本路径几乎必然处处不可微 | Governing theorem / 相应定理 | Formal proof / 正式证明 | Figure interpretation / 看图分析 | MATH3015, Chapter 3 |

An empty support entry is flagged instead of being converted into a stronger claim.

支撑为空的论断会被标记，而不会被自动加强。

### Before | 修改前

**English**

> Figure 6 is not a proof that Brownian sample paths are almost surely nowhere differentiable. It
> should only be regarded as an illustration, and the plotted slopes should not be overinterpreted.

**中文**

> Figure 6 并不能证明布朗运动样本路径几乎必然处处不可微。它只能被视为一种图示，因此不应
> 过度解读图中的斜率。

### After | 修改后

**English**

For an increment of length $h$,

$$
\frac{B_{t+h}-B_t}{h}\overset{d}=\frac{Z}{\sqrt h},
\qquad Z\sim N(0,1).
$$

Hence the median absolute difference quotient is
$\Phi^{-1}(0.75)h^{-1/2}\approx0.674h^{-1/2}$. In the supplied Figure 6, the plotted
medians follow this reference scale across the displayed resolutions. The cited theorem
establishes that the sample paths of standard Brownian motion are almost surely nowhere
differentiable.

**中文**

对于长度为 $h$ 的增量，

$$
\frac{B_{t+h}-B_t}{h}\overset{d}=\frac{Z}{\sqrt h},
\qquad Z\sim N(0,1).
$$

因此，绝对差商的中位数为
$\Phi^{-1}(0.75)h^{-1/2}\approx0.674h^{-1/2}$。在任务提供的 Figure 6 中，图示中位数在各个
分辨率下均沿该参考尺度变化。引用的定理说明，标准布朗运动的样本路径几乎必然处处不可微。

The revision first states the governing relation, then describes the plotted evidence, and finally
attributes the formal conclusion to its theorem.

修改稿先给出决定性关系，再描述图中证据，最后把正式结论归于相应定理。

---

## FAQ | 常见问题

### Does it remove every hedge or negative sentence? | 它会删除所有 hedge 和否定句吗？

No. The functional audit retains assumptions, genuine uncertainty, method limitations,
counterexamples, failed converses, admissibility conditions, and mathematical negation. It targets
generic disclaimers and repeated clarification whose removal leaves the mathematical content
unchanged.

不会。Functional audit 会保留假设、真实不确定性、方法限制、反例、逆命题失败、可容许条件和
数学否定。它处理的是不影响数学内容的空泛免责声明与重复澄清。

### Can it verify a theorem without a source? | 没有来源时能核验定理吗？

Verification mode needs the governing theorem, derivation, data, code, or numerical benchmark. A
claim without evidence is classified as `unsupported`; inconclusive supplied evidence is
classified as `ambiguous`.

Verification mode 需要相应定理、推导、数据、代码或数值 benchmark。没有证据的论断归为
`unsupported`；已有证据无法得出明确判断时归为 `ambiguous`。

### Does the skill retrieve sources or execute notebooks? | Skill 会自行获取来源或运行 notebook 吗？

The skill defines the writing and verification workflow. Access to papers, notebook execution,
browser inspection, and file rendering depends on the tools and permissions available to the
surrounding Codex environment.

该 skill 规定写作与核验流程。论文访问、notebook 执行、浏览器检查和文件渲染取决于当前 Codex
环境提供的工具与权限。

### Is it only for MATH3015? | 它只适用于 MATH3015 吗？

No. MATH3015 supplied the original notebook cases and retains a dedicated project profile. The
general rules cover the mathematical fields listed above. Expansion to a distant academic field
should begin with a field-specific corpus and genre review.

不是。MATH3015 提供了最初的 notebook cases，并拥有独立 project profile；通用规则适用于上述
数学领域。若扩展到差异较大的学科，应先进行该领域的 corpus 和 genre review。

---

<a id="validation"></a>

## Validation | 验证

The accepted private v0.3.0 snapshot passed the selected cases below in fresh first-stage contexts
and separate semantic review contexts.

私有 v0.3.0 accepted snapshot 在全新的一阶段上下文和分开的语义审阅上下文中通过了以下选定案例：

| Suite / 测试套件 | First-stage result / 一阶段结果 | Semantic result / 语义结果 |
| --- | ---: | ---: |
| Synthetic review / 合成审阅 | 25/25 decisions | 54/54 assertions |
| MATH3015 notebook review / MATH3015 notebook 审阅 | 14/14 decisions | 29/29 assertions |
| Evidence-grounded drafting / 证据约束的起草 | 7/7 cases | 26/26 assertions |
| Source, derivation, and artifact verification / 来源、推导与 artifact 核验 | 10/10 verdicts | 30/30 assertions |

The same private release passed 78/78 main mutation cases and 45/45 corpus mutation cases. These
figures describe the accepted private validation lineage; the public repository contains the
runtime binding rather than the private corpus or blind oracles.

同一私有发布版本通过了 78/78 个主 mutation cases 和 45/45 个 corpus mutation cases。公开仓库
保存 runtime binding；私有 corpus 和 blind oracles 保留在私有验证环境中。

The twelve byte-identical runtime files reproduce the accepted core binding:

十二个逐字节一致的 runtime 文件共同复现 accepted core binding：

```text
Core skill aggregate SHA-256
160b00a502b136e2827ea897722e5402c1fb51c5661a116d6701743797eb479c

Private validation-harness lineage SHA-256
71f12d684bf852f9c535074cf0a1df70313fad99ac76cc088e81aea0f4efce80
```

Run the public check locally:

可在本地运行以下公开检查：

```bash
python3 -B scripts/verify_public_core.py
```

The check verifies the exact public file allowlist, regular-file and link constraints, the twelve
core file hashes, their ordered aggregate, and a limited credential/path pattern scan. See
[`provenance/public-release.v1.json`](provenance/public-release.v1.json) for the public binding.

该检查核对公开文件 allowlist、普通文件与链接约束、十二个 core 文件 hash、它们按顺序计算的
aggregate hash，以及有限的 credential/path pattern。公开 binding 记录在
[`provenance/public-release.v1.json`](provenance/public-release.v1.json)。

## Public repository boundary | 公开仓库边界

This repository is the public runtime distribution. It includes the reusable skill, original
documentation, public provenance, and CI. Source-derived or security-sensitive validation
materials remain in the private release environment.

本仓库是公开 runtime distribution，包含可复用 skill、原创说明、公开 provenance 和 CI。来自
原始资料或涉及验证安全边界的材料保留在私有 release 环境中。

| Included / 已公开 | Private release only / 仅私有发布环境 |
| --- | --- |
| `SKILL.md` and Codex metadata / `SKILL.md` 与 Codex metadata | Source PDFs and textbook files / 来源 PDF 与教材文件 |
| Integrity, genre, research-article, source-audit, and artifact guidance / 完整性、体裁、论文、来源审计与 artifact 指引 | Extracted or normalized source text / 抽取或归一化后的来源正文 |
| Anti-defensive, visual-writing, MATH3015, and quantitative-finance profiles / Anti-defensive、可视化、MATH3015 与数理金融 profiles | Local notebooks and rendered fixtures / 本地 notebooks 与渲染 fixtures |
| Public examples and workflow graphic / 公开示例与流程图 | Signing keys and trust configuration / 签名密钥与信任配置 |
| License, notices, provenance, and public CI / 许可、声明、provenance 与公开 CI | Internal evidence registry and approval records / 内部 evidence registry 与审批记录 |
| Notice-only fixture stubs / 仅含说明的 fixture stubs | Blind regression oracles and source-derived samples / 盲测回归 oracles 与来源衍生样本 |

The cited publications remain subject to their own terms and are not redistributed here. The
public repository can verify the accepted runtime binding; corpus recalibration uses the private
evidence package.

被引用的出版物仍适用其各自条款，本仓库不会重新分发这些材料。公开仓库可核验 accepted runtime
binding；corpus 重新校准则使用私有 evidence package。

## Public package structure | 公开包结构

```text
.
├── .github/workflows/verify-core.yml
├── SKILL.md
├── agents/openai.yaml
├── references/
├── project_profiles/
│   ├── math3015.md
│   └── quantitative_finance.md
├── examples/quick-start.md
├── assets/usage-workflow.png
├── provenance/public-release.v1.json
├── scripts/verify_public_core.py
├── tests/                         # notice-only public stubs
├── CHANGELOG.md
├── MAINTENANCE.md
├── LICENSE
├── THIRD_PARTY_NOTICES.md
└── README.md
```

## Attribution | 致谢

The anti-defensive audit adapts the functional-classification, positive-scope,
precision-preservation, and review-first ideas of Kiterlin's MIT-licensed
[anti-defensive-writing](https://github.com/Kiterlin/anti-defensive-writing) skill.

本项目的 anti-defensive audit 借鉴了 Kiterlin 以 MIT License 发布的
[anti-defensive-writing](https://github.com/Kiterlin/anti-defensive-writing) skill 中的
functional classification、positive scope、precision preservation 和 review-first，并将其
应用于数学假设、形式否定、记号一致性、证据层级、图表解释、随机过程论断和验证系统。完整
upstream notice 见
[`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)。

## License | 许可

Original code and documentation in this repository are available under the [MIT License](LICENSE).
Third-party publications and course materials retain their own terms and are not included.

本仓库原创代码和文档采用 [MIT License](LICENSE)。第三方论文、教材和课程资料适用其各自许可，
不包含在本仓库中。
