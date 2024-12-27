# 使用官方 Python 3.9 基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 文件
COPY requirements.txt .

# 更新包列表并安装必要的编译工具
RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get install -y libssl-dev && \
    apt-get install -y libffi-dev && \
    apt-get install -y zlib1g-dev && \
    apt-get install -y libncurses5-dev && \
    apt-get install -y libncursesw5-dev && \
    apt-get install -y libreadline-dev && \
    apt-get install -y libsqlite3-dev && \
    apt-get install -y libgdbm-dev && \
    apt-get install -y libdb5.3-dev && \
    apt-get install -y libbz2-dev && \
    apt-get install -y libexpat1-dev && \
    apt-get install -y liblzma-dev && \
    apt-get install -y tk-dev && \
    apt-get install -y liblzma-dev && \
    apt-get install -y libffi-dev && \
    apt-get install -y libssl-dev && \
    apt-get install -y libreadline-dev && \
    apt-get install -y libsqlite3-dev && \
    apt-get install -y libgdbm-dev && \
    apt-get install -y libdb5.3-dev && \
    apt-get install -y libbz2-dev && \
    apt-get install -y libexpat1-dev && \
    apt-get install -y liblzma-dev && \
    apt-get install -y tk-dev && \
    apt-get install -y libffi-dev && \
    apt-get install -y libssl-dev && \
    apt-get install -y libreadline-dev && \
    apt-get install -y libsqlite3-dev && \
    apt-get install -y libgdbm-dev && \
    apt-get install -y libdb5.3-dev && \
    apt-get install -y libbz2-dev && \
    apt-get install -y libexpat1-dev && \
    apt-get install -y liblzma-dev && \
    apt-get install -y tk-dev && \
    apt-get install -y libffi-dev && \
    apt-get install -y libssl-dev && \
    apt-get install -y libreadline-dev && \
    apt-get install -y libsqlite3-dev && \
    apt-get install -y libgdbm-dev && \
    apt-get install -y libdb5.3-dev && \
    apt-get install -y libbz2-dev && \
    apt-get install -y libexpat1-dev && \
    apt-get install -y liblzma-dev && \
    apt-get install -y tk-dev && \
    apt-get install -y libffi-dev && \
    apt-get install -y libssl-dev && \
    apt-get install -y libreadline-dev && \
    apt-get install -y libsqlite3-dev && \
    apt-get install -y libgdbm-dev && \
    apt-get install -y libdb5.3-dev && \
    apt-get install -y libbz2-dev && \
    apt-get install -y libexpat1-dev && \
    apt-get install -y liblzma-dev && \
    apt-get install -y tk-dev

# 升级 pip 并安装依赖项
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 暴露 Streamlit 默认端口
EXPOSE 8501

# 复制项目文件
COPY . .

# 启动 Streamlit 应用
CMD ["streamlit", "run", "app.py", "--server.enableCORS", "false", "--server.enableXsrfProtection", "false"]