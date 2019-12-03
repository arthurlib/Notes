
*以后将脚本分开写*

> 之前我在Linux上运行代码时，当运行一个sh脚本的时候,出现了如下错误：
> $'\r': 未找到命令
> 未预期的符号 `$'{\r'' 附近有语法错误


解决方案：

```shell
	sudo apt-get install dos2unix
```

然后用 dos2unix命令对所有的用到的sh脚本进行转化即可
例子： 

```shell
	dos2unix hello.sh
```

> 原因：在windows系统下写了一个tomcat重启shell，然后上传到linux中，执行后报错：$'\r': 未找到命令 : 没有那个文件或目录。网上资料搜索后，找到原因：主要原因是shell脚本是我在windows下编辑然后上传到linux系统里执行的。.sh文件的格式为dos格式。而linux只能执行格式为unix格式的脚本。


## ubuntu安装jdk

```shell
	sudo echo y | apt-get install default-jdk
```

## ubuntu安装jdk tomcat(需要手动上传jdk和tomcat，和脚本放在一起，执行脚本)

```bash
#!/bin/bash
# @Date:   2017-02-17 19:39:21
# @Last Modified time: 2017-02-17 19:43:30
#说明：请执行以下命令 ubuntu系统的系统测试成功
# “. 该文件名”
#路径
#如果输入javac没有没有，请执行  source /etc/profile
touch ./retomcat.sh;
echo >> ./retomcat.sh '#!/bin/bash';
echo >> ./retomcat.sh 'shutdowntomcat;';
echo >> ./retomcat.sh 'startomcat;';
path=`pwd`
install_path="/usr/local/"
echo "当前路径为：${path}"
index=0
for tmp in `ls *.tar.gz;`;do
	packages[index]=${tmp}
	index=$((index+1))
done
#输出符合条件的包
#echo ${packages[*]}
echo "发现${#packages[*]}个包"

for package in ${packages[*]};do
	#获取安装目录名
	install_contents_name=`tar tvf ${package} | awk -F " " '{print $6}' | sed -n '1p'`
	#去除多余字符
	install_contents_name=${install_contents_name%%/*}
	#echo ${package} #输出包名
	if test -d ${install_path}${install_contents_name}
	then
		#存在
		echo "${install_contents_name}已存在"
		continue
	else
		echo "${install_path}${install_contents_name}不存在，正在安装${install_contents_name}..."
		tar -zxf ${package}
		sudo mv  ${install_contents_name} ${install_path}
        if [ ${install_contents_name:0:3} = "jdk" ]; then
			sudo echo >> /etc/profile "export JAVA_HOME=${install_path}${install_contents_name}";
			sudo echo >> /etc/profile 'export JRE_HOME=$JAVA_HOME/jre';
			sudo echo >> /etc/profile 'export CLASSPATH=.:$CLASSPATH:$JAVA_HOME/lib:$JRE_HOME/lib';
			sudo echo >> /etc/profile 'export PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin';
        elif [ ${install_contents_name:0:6}="apache" ]; then
			sudo echo >> /etc/profile "export CATALINA_HOME=${install_path}${install_contents_name}";
			sudo ln -s ${install_path}${install_contents_name}/bin/startup.sh ${install_path}/bin/startomcat;
			sudo ln -s ${install_path}${install_contents_name}/bin/shutdown.sh ${install_path}/bin/shutdowntomcat;
			sudo chmod 755 retomcat.sh;
			sudo mv retomcat.sh ${install_path}/bin/retomcat;
		fi
	fi
done
. /etc/profile
#source /etc/profile

```

## 自动下载jdk，tomcat进行配置

```bash
#!/bin/bash
# @Date:   2017-02-17 19:39:21
# @Last Modified time: 2017-02-17 19:43:30
#请在root权限下运行
# 建立了快捷命令如下：
# 关闭：shutdowntomcat
# 启动：startomcat
# 重启：retomcat
sudo echo y | apt-get install default-jdk
touch ./retomcat.sh;
echo >> ./retomcat.sh '#!/bin/bash';
echo >> ./retomcat.sh 'shutdowntomcat;';
echo >> ./retomcat.sh 'startomcat;';
echo "下载apache-tomcat-8.5.23"
wget http://www-us.apache.org/dist/tomcat/tomcat-8/v8.5.23/bin/apache-tomcat-8.5.23.tar.gz
tar  -zxvf apache-tomcat-8.5.23.tar.gz
mv apache-tomcat-8.5.23  /usr/local/apache-tomcat-8.5.23
sudo ln -s /usr/local/apache-tomcat-8.5.23/bin/startup.sh /usr/local/bin/startomcat;
sudo ln -s /usr/local/apache-tomcat-8.5.23/bin/shutdown.sh /usr/local/bin/shutdowntomcat;
sudo chmod 755 retomcat.sh;
sudo mv retomcat.sh /usr/local/bin/retomcat;

```