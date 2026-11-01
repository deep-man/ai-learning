# Day17 学习记录

## 一、学习目标
- 理解JSON格式，知道它和Python字典/列表的区别
- 掌握四个核心函数：`json.dumps` `json.loads` `json.dump` `json.load`
- 会用`ensure_ascii=False`处理中文
- 会用`indent=2`格式化输出
- 能完成配置管理工具和学生数据存储两个实际项目

---

## 二、完成情况

### 已掌握

- `josn.dumps()`:Python对象——JSON字符串
- `json.loads()`:JSON字符串——Python对象
- `json.dump()`:Python对象——写入文件
- `json.load()`:从文件读取——Python对象
- 带`s`操作字符串，不带`s`操作文件
- `ensure_ascii=False`让中文正常显示
- `indent=2`格式化输出
- JSON读出来的数字已经是整数，不需要`int()`转换
- JSON里的`True`/`False`/`null`转换成Python的`True`/`False`/`None`

### 完成的项目

- `json_test.py`：四个核心函数的最小示例
- `config_manager.py`：配置管理工具（查看、修改、保存）
- `student_json.py`：学生数据 JSON 存储（添加、查看、保存

---

## 三、遇到的问题与原因

### 问题1：`load_config`文件不存在时返回了`filename`
- 题目要求文件不存在时返回默认配置字典，不是文件名
- 教训：异常处理的返回值要和正路径的返回值类型一致。正常路径返回字典，异常路径也要返回字典，否则调用方会崩

### 问题2：`load_config`里变量名用了`filename1`
- 教训：变量名要反映它存的是什么

### 问题3：`save_config` 参数名 `filename1` 不规范
- 教训：参数名要一看就懂
- `filename`是文件名，`config`是配置字典，`students`是学生列表