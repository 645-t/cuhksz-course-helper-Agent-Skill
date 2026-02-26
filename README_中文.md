# CUHK-SZ Course Helper Agent Skill

一个用于将**香港中文大学（深圳）（CUHK-SZ）**的学术课程材料标准化、重新排版并丰富内容的 [Claude Code](https://claude.ai/claude-code) Skill。

---

## Who Is This For

- **学生**：希望获得CUHKSZ风格、格式统一、内容增强的课程材料，用于自学，或制作个人演示文稿、学术报告及会议幻灯片。您可以便捷的获取Exam past paper的可打印答案版用于检查和学习。
- **教授与TAs**：需要将Slides或Exam paper自动重排为接近 CUHK-SZ 官方部门模板格式。
- 任何需要将 CUHK-SZ 课程文件（PPTX、PDF、DOCX）快速转换为像素级精准 LaTeX Beamer PDF 的用户。

---

## 功能特性

### 三种官方模板

| 模板 | 来源课程 |  |
|---|---|---|
| **MATH** | MAT2040 | |
| **CS** | DDA3020 | |
| **STATS** | STA2001 | |

三种模板均通过 **LaTeX Beamer**（`\usetheme{Boadilla}`）生成，颜色数据直接提取自课件 PDF，还原度像素级精准。您也可以给Agent提供您自己的模板。

### 幻灯片结构标准化

将现有文件重排为目标模板格式，内容完整保留。

- 从 PPTX 中提取文字、排版及嵌入图片
- 将每张幻灯片归类为对应类型（标题页、目录、章节分隔、定义、正文、示例……）
- 生成 `.tex` 文件并通过 `pdflatex` 编译为 PDF
- 图片自动提取并以 `\includegraphics` 嵌入（无占位符）
- 编译中间文件（`.aux`、`.log`、`.nav` 等）隔离于临时目录并自动删除
- 输出文件：`[原文件名]_updated.pdf`

### 幻灯片内容增强

在结构标准化的基础上，额外执行：

- 检索关联教材与参考资料
- 识别内容薄弱环节或未解答的问题，并补充相应幻灯片
- 所有 AI 增补内容均有视觉标识（AI 强调色斜体文字 + `[Helper]` 角标）
- 输出文件：`[原文件名]_enhanced.pdf`

### 考卷 / 作业答案生成

根据考卷或作业 PDF，生成参考答案文档。

- 采用 `\documentclass{article}`（而非 Beamer），支持自然分页排版
- 每道题的解答紧接题目之后呈现
- 简洁黑白版式：细边框标题块、浅灰色解答框
- 包含免责声明：*"AI-generated reference answers. NOT official. Verify with instructors."*
- 输出文件：`[原文件名]_answers.pdf`

---

## 环境要求

**Python 3.8+** 是唯一需要手动安装的依赖项。**其余所有依赖均由 AI Agent 自动处理。**

---

## 安装 Claude Code

本 Skill 需要 [Claude Code](https://claude.ai/claude-code)——Anthropic 官方命令行工具。

**1. 安装 Node.js 18+**，请前往 [nodejs.org](https://nodejs.org) 下载（若已安装可跳过）。

**2. 安装 Claude Code：**

```bash
npm install -g @anthropic-ai/claude-code
```

**3. 登录账号：**

```bash
claude
```

按照提示完成 Anthropic 账号认证。Claude Code 可免费试用；长期使用需要 [Anthropic API 密钥](https://console.anthropic.com/)。

---

## 安装 Skill

### 第一步：将 Skill 文件放入技能目录

将 `cuhksz-course-helper` 文件夹复制到 Claude Code 的 Skill 目录：

| 平台 | 默认 Skill 目录 |
|---|---|
| Windows | `%USERPROFILE%\.claude\skills\` |
| macOS / Linux | `~/.claude/skills/` |

### 第二步：确认 Claude Code 已识别该 Skill

```bash
claude /skills
```

列表中出现 `cuhksz-course-helper` 即表示安装成功。

---

## 使用方法

直接用自然语言向 Claude Code 描述任务即可，以下情况会自动触发本 Skill：

- 任何 CUHK-SZ 课程代码（如 `MAT1001`、`DDA3020`、`STA2001`）
- 关键词：`"standardize slides"`、`"reformat course material"`、`"CUHK course material"`、`"update lecture PPT"`、`"生成答案版"` 等

**示例：**

```
把桌面上的 Ch5.pptx 换成 STA2001 风格的课件
```
```
Generate a reference answer version of the MAT1001 final exam on my desktop.
```
```
Reformat this lecture slides to match DDA3020 style, Level 1 only.
```

### 信息收集问答

收到文件后，Skill 会通过一次提问补全缺失信息：

1. **课程编号 + 授课教师姓名** — 用于页脚和标题元数据
2. **幻灯片风格** — 以课程代码形式呈现（STA2001 / DDA3020 / MAT2040）
3. **操作级别** — L1（仅重排格式）或 L2（重排 + 内容增强 / 生成答案）

若您在请求中已提供上述信息，对应问题将自动跳过。

---

## 文件结构

```
cuhksz-course-helper/
├── SKILL.md                          # Skill 定义与workflow说明
├── scripts/
│   ├── extract_content.py            # 从 PPTX 提取文字与图片 → JSON
│   ├── compile_latex.py              # pdflatex 封装（两次编译，临时目录自动清理）
│   └── convert_to_pdf.py             # PPTX → PDF（优先 PowerPoint COM，备用 LibreOffice）
└── references/
    ├── template_specs.md             # 三种模板的视觉规范与验证色值
    ├── math_latex_template.md        # MATH 模板完整 Beamer 导言区与帧模式
    ├── cs_latex_template.md          # CS 模板完整 Beamer 导言区与帧模式
    ├── stats_latex_template.md       # STATS 模板完整 Beamer 导言区与帧模式
    ├── slide_structure.md            # 幻灯片类型分类指南
    ├── level2_workflow.md            # L2 内容检索与增强工作流
    └── academic_standards.md        # 学术排版规范
```

---

## 输出文件命名

| 任务 | 输出文件 |
|---|---|
| 结构标准化 | `[原文件名]_updated.tex` + `[原文件名]_updated.pdf` |
| 内容增强 | `[原文件名]_enhanced.pdf` |
| 答案生成 | `[原文件名]_answers.tex` + `[原文件名]_answers.pdf` |

**原始文件永远不会被覆盖。**

---

## 注意事项

- AI 增补内容始终与原始内容在视觉上有明确区分。
- `.tex` 源文件与 PDF 同目录保留，便于手动进一步编辑。
- 从 PPTX 提取图片要求幻灯片中包含真正嵌入的图片对象（不支持链接图片或 OLE 对象）。
