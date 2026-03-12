\## 2026-XX-XX 初始化工程

\### Prompt

帮我初始化一个标准Python工程，包含src/源码目录和tests/测试目录，用于八皇后问题求解。

\### 结果

成功创建src/、tests/、prompt\_log.md、README.md文件结构。

\## 2026-03-09 自动化测试与Bug修复

\### 步骤1：编写单元测试

在 tests/ 目录下创建 test\_eight\_queens.py，编写 pytest 用例验证 N=1、N=4、N=8 的解数量。

\### 步骤2：导入问题排查

运行 pytest tests/ -v 时出现 ModuleNotFoundError，通过改用 python -m pytest tests/ -v 解决。

\### 步骤3：测试通过

执行 python -m pytest tests/ -v，所有用例 PASSED，验证解数量正确。

\### 步骤4：引入Bug

修改 is\_valid 函数，将对角线判断改为 if (row - i) == (col - board\[i])，去掉 abs()。

\### 步骤5：AI 修复

将报错信息发给 AI，AI 定位到对角线判断缺少 abs()，修复后测试再次通过。

