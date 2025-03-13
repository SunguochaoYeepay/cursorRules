#!/usr/bin/env python3
"""
Cursor 项目初始化脚本
用于快速创建新项目并应用配置模板
"""

import argparse
import os
import shutil
import json
from pathlib import Path
import toml
from typing import Optional, Dict, Any

class CursorInitializer:
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.cursor_dir = self.project_path / '.cursor'
        self.template_dir = Path(__file__).parent.parent / 'templates'
        self.rules_dir = Path(__file__).parent.parent / 'rules'

    def init_project(self, project_type: str, use_mysql: bool = True, use_ant: bool = True) -> None:
        """初始化项目结构和配置"""
        print(f"正在初始化项目: {self.project_path}")
        
        # 创建项目目录
        self.project_path.mkdir(parents=True, exist_ok=True)
        
        # 创建.cursor目录结构
        self._create_cursor_structure()
        
        # 复制基础配置
        self._copy_base_config()
        
        # 根据项目类型应用特定配置
        if project_type in ['frontend', 'fullstack']:
            self._setup_frontend(use_ant)
        
        if project_type in ['backend', 'fullstack']:
            self._setup_backend(use_mysql)
        
        # 创建项目依赖文件
        self._create_dependency_files(project_type)
        
        print("✅ 项目初始化完成！")
        self._print_next_steps(project_type)

    def _create_cursor_structure(self) -> None:
        """创建.cursor目录结构"""
        dirs = [
            'config',
            'rules/frontend',
            'rules/backend',
            'rules/common',
            'templates/frontend',
            'templates/backend',
            'templates/common'
        ]
        
        for dir_path in dirs:
            (self.cursor_dir / dir_path).mkdir(parents=True, exist_ok=True)

    def _copy_base_config(self) -> None:
        """复制基础配置文件"""
        shutil.copy2(self.rules_dir / 'common/security.rules.toml',
                    self.cursor_dir / 'rules/common/security.rules.toml')
        shutil.copy2(self.rules_dir / 'common/style.rules.toml',
                    self.cursor_dir / 'rules/common/style.rules.toml')

    def _setup_frontend(self, use_ant: bool) -> None:
        """设置前端配置"""
        vue_rules = self.rules_dir / 'frontend/vue.rules.toml'
        target_rules = self.cursor_dir / 'rules/frontend/vue.rules.toml'
        
        if use_ant:
            shutil.copy2(vue_rules, target_rules)
        else:
            # 读取配置并移除Ant Design相关内容
            config = toml.load(vue_rules)
            self._remove_ant_design_config(config)
            with open(target_rules, 'w') as f:
                toml.dump(config, f)

    def _setup_backend(self, use_mysql: bool) -> None:
        """设置后端配置"""
        python_rules = self.rules_dir / 'backend/python.rules.toml'
        target_rules = self.cursor_dir / 'rules/backend/python.rules.toml'
        
        if use_mysql:
            shutil.copy2(python_rules, target_rules)
        else:
            # 读取配置并移除MySQL相关内容
            config = toml.load(python_rules)
            self._remove_mysql_config(config)
            with open(target_rules, 'w') as f:
                toml.dump(config, f)

    def _create_dependency_files(self, project_type: str) -> None:
        """创建项目依赖文件"""
        if project_type in ['frontend', 'fullstack']:
            self._create_package_json()
        
        if project_type in ['backend', 'fullstack']:
            self._create_requirements_txt()

    def _create_package_json(self) -> None:
        """创建package.json文件"""
        package_config = self._load_template('frontend/package.template.json')
        with open(self.project_path / 'package.json', 'w') as f:
            json.dump(package_config, f, indent=2)

    def _create_requirements_txt(self) -> None:
        """创建requirements.txt文件"""
        requirements = self._load_template('backend/requirements.template.txt')
        with open(self.project_path / 'requirements.txt', 'w') as f:
            f.write(requirements)

    def _print_next_steps(self, project_type: str) -> None:
        """打印后续步骤指南"""
        print("\n📝 后续步骤:")
        if project_type in ['frontend', 'fullstack']:
            print("1. 前端设置:")
            print("   - 运行: pnpm install")
            print("   - 开发: pnpm dev")
            print("   - 构建: pnpm build")
        
        if project_type in ['backend', 'fullstack']:
            print("\n2. 后端设置:")
            print("   - 创建虚拟环境: python -m venv venv")
            print("   - 激活环境: source venv/bin/activate")
            print("   - 安装依赖: pip install -r requirements.txt")
            print("   - 运行开发服务器: uvicorn main:app --reload --port 3000")
        
        print("\n🔧 配置文件位置:")
        print(f"   - 前端配置: {self.cursor_dir}/rules/frontend/")
        print(f"   - 后端配置: {self.cursor_dir}/rules/backend/")
        print(f"   - 通用配置: {self.cursor_dir}/rules/common/")

def main():
    parser = argparse.ArgumentParser(description="Cursor项目初始化工具")
    parser.add_argument("project_path", help="项目路径")
    parser.add_argument("--type", choices=['frontend', 'backend', 'fullstack'],
                      default='fullstack', help="项目类型")
    parser.add_argument("--no-mysql", action="store_false", dest="use_mysql",
                      help="不使用MySQL配置")
    parser.add_argument("--no-ant", action="store_false", dest="use_ant",
                      help="不使用Ant Design配置")

    args = parser.parse_args()
    
    initializer = CursorInitializer(args.project_path)
    initializer.init_project(args.type, args.use_mysql, args.use_ant)

if __name__ == "__main__":
    main() 