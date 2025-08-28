# 贡献指南

感谢你考虑为 AI Agent文章生成器 项目做出贡献！🎉

## 🤝 如何贡献

### 1. Fork 项目
1. 访问 [项目主页](https://github.com/huangzhixin2018-sudo/Article_Generation_Agent)
2. 点击右上角的 "Fork" 按钮
3. 在你的账户下创建项目副本

### 2. 克隆你的 Fork
```bash
git clone https://github.com/你的用户名/Article_Generation_Agent.git
cd Article_Generation_Agent
```

### 3. 创建功能分支
```bash
git checkout -b feature/你的功能名称
# 或者
git checkout -b fix/修复的问题名称
```

### 4. 进行修改
- 编写代码
- 添加测试
- 更新文档
- 确保代码符合项目规范

### 5. 提交更改
```bash
git add .
git commit -m "feat: 添加新功能描述"
# 或者
git commit -m "fix: 修复问题描述"
```

### 6. 推送分支
```bash
git push origin feature/你的功能名称
```

### 7. 创建 Pull Request
1. 访问你的 Fork 页面
2. 点击 "New Pull Request"
3. 选择你的分支
4. 填写 PR 描述
5. 提交 PR

## 📝 提交规范

我们使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

### 提交类型
- `feat`: 新功能
- `fix`: 修复bug
- `docs`: 文档更新
- `style`: 代码格式调整
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

### 示例
```bash
git commit -m "feat: 添加微信公众号平台支持"
git commit -m "fix: 修复任务执行器中的路径问题"
git commit -m "docs: 更新快速开始指南"
```

## 🎯 贡献方向

### 功能扩展
- [ ] 添加新的内容平台支持
- [ ] 集成更多AI服务
- [ ] 开发Web界面
- [ ] 添加批量处理功能

### 性能优化
- [ ] 提升AI调用效率
- [ ] 优化文件处理速度
- [ ] 减少内存占用
- [ ] 改进错误处理

### 文档完善
- [ ] 添加API文档
- [ ] 完善使用教程
- [ ] 翻译文档
- [ ] 添加视频教程

### Bug修复
- [ ] 修复已知问题
- [ ] 改进错误提示
- [ ] 增强稳定性
- [ ] 优化用户体验

## 🔧 开发环境设置

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 配置开发环境
```bash
# 复制配置文件模板
cp 系统配置/api_keys.json.example 系统配置/api_keys.json
# 编辑配置文件
```

### 3. 运行测试
```bash
cd 文章创作
python 任务执行器.py
```

## 📋 代码规范

### Python 代码
- 遵循 PEP 8 规范
- 使用有意义的变量名
- 添加适当的注释
- 编写文档字符串

### 文档
- 使用 Markdown 格式
- 保持文档结构清晰
- 添加适当的示例
- 定期更新文档

### 提交信息
- 使用中文描述
- 简洁明了
- 说明修改原因
- 关联相关Issue

## 🐛 报告问题

### 创建 Issue
1. 访问 [Issues 页面](https://github.com/huangzhixin2018-sudo/Article_Generation_Agent/issues)
2. 点击 "New Issue"
3. 选择 Issue 类型
4. 填写详细信息

### Issue 模板
```markdown
## 问题描述
简要描述遇到的问题

## 重现步骤
1. 第一步
2. 第二步
3. 第三步

## 预期行为
描述你期望看到的结果

## 实际行为
描述实际发生的情况

## 环境信息
- 操作系统：
- Python版本：
- 项目版本：

## 附加信息
任何其他相关信息
```

## 🎉 获得认可

### 贡献者名单
所有贡献者都会被添加到项目的贡献者名单中。

### 特殊贡献
- 重大功能贡献者
- 长期维护者
- 文档贡献者
- 社区活跃者

## 📞 联系我们

如果你有任何问题或建议，欢迎通过以下方式联系：

- [GitHub Issues](https://github.com/huangzhixin2018-sudo/Article_Generation_Agent/issues)
- [GitHub Discussions](https://github.com/huangzhixin2018-sudo/Article_Generation_Agent/discussions)

## 🙏 致谢

感谢所有为这个项目做出贡献的开发者！

---

**让我们一起打造更好的AI Agent文章生成器！** 🚀
