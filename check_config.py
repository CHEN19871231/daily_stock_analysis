#!/usr/bin/env python3
"""
配置检查脚本
检查daily_stock_analysis项目的基本配置
"""

import os
import sys
from pathlib import Path

def check_env_file():
    """检查.env文件是否存在和基本配置"""
    env_path = Path(".env")
    
    if not env_path.exists():
        print("❌ .env文件不存在")
        print("请运行: cp .env.example .env")
        return False
    
    print("✅ .env文件存在")
    
    # 读取.env文件内容
    with open(env_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查关键配置
    checks = {
        "STOCK_LIST": "股票列表配置",
        "OPENAI_API_KEY": "DeepSeek API Key配置",
        "FEISHU_WEBHOOK_URL": "飞书Webhook配置",
        "SCHEDULE_ENABLED": "定时任务配置",
        "AGENT_MODE": "Agent模式配置"
    }
    
    all_ok = True
    for key, description in checks.items():
        if key in content:
            # 检查是否还是示例值
            lines = content.split('\n')
            for line in lines:
                if line.startswith(f"{key}="):
                    value = line.split('=', 1)[1].strip()
                    if "你的" in value or "your_" in value or not value:
                        print(f"⚠️  {description}: 需要填写实际值")
                        all_ok = False
                    else:
                        print(f"✅  {description}: 已配置")
                    break
        else:
            print(f"⚠️  {description}: 未找到配置项")
            all_ok = False
    
    return all_ok

def check_python_dependencies():
    """检查Python依赖"""
    print("\n📦 检查Python依赖...")
    
    try:
        import pandas
        print("✅ pandas: 可用")
    except ImportError:
        print("❌ pandas: 未安装")
        return False
    
    try:
        import sqlalchemy
        print("✅ sqlalchemy: 可用")
    except ImportError:
        print("❌ sqlalchemy: 未安装")
        return False
    
    try:
        import schedule
        print("✅ schedule: 可用")
    except ImportError:
        print("❌ schedule: 未安装")
        return False
    
    return True

def check_data_sources():
    """检查数据源"""
    print("\n📊 检查数据源...")
    
    try:
        import akshare as ak
        print("✅ akshare: 可用")
    except ImportError:
        print("⚠️  akshare: 未安装（可选）")
    
    try:
        import yfinance as yf
        print("✅ yfinance: 可用")
    except ImportError:
        print("⚠️  yfinance: 未安装（可选）")
    
    return True

def main():
    print("=" * 50)
    print("Daily Stock Analysis 配置检查")
    print("=" * 50)
    
    # 检查当前目录
    current_dir = Path.cwd()
    print(f"当前目录: {current_dir}")
    
    # 检查.env文件
    env_ok = check_env_file()
    
    # 检查Python依赖
    deps_ok = check_python_dependencies()
    
    # 检查数据源
    data_ok = check_data_sources()
    
    print("\n" + "=" * 50)
    print("检查结果汇总:")
    print("=" * 50)
    
    if env_ok and deps_ok:
        print("✅ 基本配置检查通过")
        print("\n下一步:")
        print("1. 填写.env文件中的API Key和Webhook地址")
        print("2. 安装完整依赖: pip install -r requirements.txt")
        print("3. 测试运行: python test_env.py")
        print("4. 手动运行分析: python main.py")
    else:
        print("❌ 配置检查未通过")
        if not env_ok:
            print("- 请完善.env文件配置")
        if not deps_ok:
            print("- 请安装必要的Python依赖")
    
    print("\n💡 提示:")
    print("- 查看配置说明: cat 配置说明.md")
    print("- 查看完整文档: docs/full-guide.md")
    print("- GitHub Actions部署: 参考README.md")

if __name__ == "__main__":
    main()