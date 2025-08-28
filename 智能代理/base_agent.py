"""
基础Agent类 - 提供AI Agent的核心功能
"""

import os
import json
import logging
from datetime import datetime

class BaseAgent:
    """基础Agent类"""
    
    def __init__(self, config_dir="系统配置"):
        """初始化Agent"""
        self.config_dir = config_dir
        self.settings = self._load_settings()
        self.templates = self._load_templates()
        self.platform_styles = self._load_platform_styles()
        self.setup_logging()
    
    def _load_settings(self):
        """加载系统配置"""
        try:
            settings_path = os.path.join(self.config_dir, "settings.json")
            with open(settings_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ 加载配置失败，使用默认配置: {e}")
            return {
                "material_dir": "素材库",
                "output_dir": "输出结果",
                "target_platform": "wechat_public",
                "article_length": "2000-5000"
            }
    
    def _load_templates(self):
        """加载模板库"""
        templates = {}
        template_dir = "模板库"
        
        try:
            # 加载文章创作模板
            creation_template_path = os.path.join(template_dir, "article_creation.md")
            if os.path.exists(creation_template_path):
                templates['article_creation'] = self.read_file(creation_template_path)
            
            # 加载要素提取模板
            extraction_template_path = os.path.join(template_dir, "article_elements_extraction.md")
            if os.path.exists(extraction_template_path):
                templates['elements_extraction'] = self.read_file(extraction_template_path)
            
            self.logger.info(f"成功加载 {len(templates)} 个模板")
            return templates
            
        except Exception as e:
            self.logger.warning(f"加载模板失败: {e}")
            return {}
    
    def _load_platform_styles(self):
        """加载平台风格库"""
        try:
            styles_path = os.path.join("模板库", "platform_styles_lib.json")
            if os.path.exists(styles_path):
                with open(styles_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            self.logger.warning(f"加载平台风格失败: {e}")
            return {}
    
    def setup_logging(self):
        """设置日志"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def read_file(self, file_path):
        """读取文件内容"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            self.logger.error(f"读取文件失败 {file_path}: {e}")
            return ""
    
    def save_file(self, file_path, content):
        """保存文件内容"""
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            self.logger.info(f"文件已保存: {file_path}")
            return True
        except Exception as e:
            self.logger.error(f"保存文件失败 {file_path}: {e}")
            return False
    
    def save_json(self, file_path, data):
        """保存JSON文件"""
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            self.logger.info(f"JSON文件已保存: {file_path}")
            return True
        except Exception as e:
            self.logger.error(f"保存JSON文件失败 {file_path}: {e}")
            return False
    
    def get_platform_style(self, platform=None):
        """获取平台写作风格"""
        if not platform:
            platform = self.settings.get("target_platform", "wechat_public")
        
        return self.platform_styles.get(platform, {})
    
    def call_ai(self, prompt, task_type="general", platform=None):
        """调用AI模型（模拟）"""
        self.logger.info(f"AI调用: {task_type}")
        
        # 获取平台风格
        platform_style = self.get_platform_style(platform)
        
        # 根据任务类型和模板生成响应
        if task_type == "extract_elements":
            # 使用要素提取模板
            template = self.templates.get('elements_extraction', '')
            prompt = f"基于以下模板和素材，提取文章要素：\n\n模板：\n{template}\n\n素材：{prompt}"
            
            return {
                "basic_info": {
                    "topic": f"基于{platform_style.get('name', '平台')}的文章主题",
                    "target_audience": "目标读者",
                    "article_type": "经验分享"
                },
                "core_points": {
                    "main_argument": "主要论点",
                    "value_proposition": "价值主张",
                    "key_insights": ["关键洞察1", "关键洞察2"]
                }
            }
        
        elif task_type == "generate_outline":
            # 使用平台风格生成大纲
            style = platform_style.get('characteristics', {})
            title_examples = platform_style.get('title_examples', [])
            
            outline = f"""
# 备选标题（{platform_style.get('name', '平台')}风格）
"""
            for i, example in enumerate(title_examples[:3], 1):
                outline += f"{i}. {example}\n"
            
            outline += f"""
# 文章大纲
## 第一章：引言
- 核心要点1
- 核心要点2

## 第二章：主要内容
- 核心要点1
- 核心要点2

## 第三章：总结
- 核心要点1
- 核心要点2

# 写作风格要求
- 标题风格：{style.get('title_style', '')}
- 内容长度：{style.get('content_length', '')}
- 文章结构：{style.get('structure', '')}
- 写作语调：{style.get('tone', '')}
"""
            return outline
        
        elif task_type == "expand_content":
            # 使用文章创作模板
            template = self.templates.get('article_creation', '')
            prompt = f"基于以下模板和大纲，扩写文章内容：\n\n模板：\n{template}\n\n大纲：{prompt}"
            
            return f"基于模板和大纲的完整文章内容...\n\n使用的模板：{template[:100]}..."
        
        else:
            return "AI响应内容"
    
    def get_materials(self):
        """获取素材库中的素材"""
        materials_dir = self.settings.get("material_dir", "素材库")
        materials = []
        
        if not os.path.exists(materials_dir):
            self.logger.warning(f"素材目录不存在: {materials_dir}")
            return materials
        
        for filename in os.listdir(materials_dir):
            if filename.endswith(('.txt', '.md')):
                file_path = os.path.join(materials_dir, filename)
                content = self.read_file(file_path)
                if content:
                    materials.append(f"=== {filename} ===\n{content}\n")
        
        self.logger.info(f"成功加载 {len(materials)} 个素材文件")
        return materials
    
    def save_results(self, results):
        """保存结果到输出目录"""
        output_dir = self.settings.get("output_dir", "输出结果")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # 保存要素
        if 'elements' in results:
            elements_path = os.path.join(output_dir, "extracted_meta.json")
            self.save_json(elements_path, results['elements'])
        
        # 保存大纲
        if 'outline' in results:
            outline_path = os.path.join(output_dir, "article_structure.md")
            self.save_file(outline_path, results['outline'])
        
        # 保存文章
        if 'content' in results:
            content_path = os.path.join(output_dir, "final_article.md")
            self.save_file(content_path, results['content'])
        
        # 保存执行报告
        report = {
            'execution_time': datetime.now().isoformat(),
            'platform_style': self.get_platform_style(),
            'templates_used': list(self.templates.keys()),
            'results': results
        }
        report_path = os.path.join(output_dir, "execution_report.json")
        self.save_json(report_path, report)
