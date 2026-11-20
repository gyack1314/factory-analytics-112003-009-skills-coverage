# 培训成效归因与关键工位能力覆盖

本目录保存工业园内的合成业务资料。员工岗位与培训邀请、上岗机会、操作者记录、作业许可与班表约束。工作日相对于培训台账起点，班表小时是各厂本地工作时钟。attempts 中 person 为原登记的受评人，operator 为实际操作人。许可证可以有来自另一个系统的授权，因此 evidence 为空表示未提供对应实操编号。

数据文件位于 `data/`，采用 UTF-8 JSON。表由对象数组组成，单份配置由对象表示。字段后缀 `min`、`day`、`hour`、`cents`、`kg` 和 `m` 标记单位。未提供的事实用 `null` 表示，绝对区间右端不包含在内。名称和编号为本目录内的资料标识。

运行环境为 Python 3.11，资料检查只使用标准库。

- 查看目录与样本数量：`python3 inspect_inputs.py`
- 运行资料测试：`python3 -m unittest discover -s tests -v`
- 编译检查：`python3 -m compileall -q inspect_inputs.py tests`
