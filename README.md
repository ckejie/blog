# blog.ckee.cn with python3-Flash

# Git管理python项目
  1. 生成git公私
```
ssh-keygen -t rsa -C "yourmail@gmail.com"

ls  ~/.ssh/  && cat ~/.ssh/id_rsa.pub
```

  2.上传公钥到Github

  3. 配置Git
```
git config --global user.email "yourmail@example.com"
git config --global user.name "yourname"
```

# 创建项目环境

  1.建立项目目录
```
mkdir projectName && cd projectName

echo "# projectName with Python-Flask" >> README.md
```

  2. 使用virtualenv独立python环境
```
pip install virtualenv    # 安装
virtualenv .envName       # 创建独立环境
source env/bin/activate   # 激活env环境

pip install flask               # 安装python模块
pip freeze > requirements.txt   # 生成当前环境下所需要安装的python软件包列表

deactivate                # 退出沙盒环境
```

  3. 初始化git仓库
```
git init
git add .
git commit -m "commit init Project"
# 将项目发布到github
git remote add origin https://yourname@github.com/yourname/projectName.git  # 添加远程主机
git push -u origin master  # 将本地分支的更新，推送到远程主机
```
