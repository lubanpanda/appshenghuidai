import logging
import logging.config
from lianxiti import weather
# 使用baseConfig()函数,可选参数有filename,filemode,format,datefmt,level,stream
# 有filename是文件日志输出,filemode是'w'的话，文件会被覆盖之前生成的文件会被覆盖。datafmt参数用于格式化日期的输出
def log():
    # logging.basicConfig (level = logging.DEBUG,
    #                      format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s\n',
    #                      datefmt = '%Y-%m-%d %H:%M:%S', filename = 'myapp.log', filemode = 'a+')
    # #################################################################################################
    # # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
    # console = logging.StreamHandler ()
    # console.setLevel (logging.DEBUG)
    # formatter = logging.Formatter ('%(name)-12s: %(levelname)-8s %(message)s')
    # console.setFormatter (formatter)
    # logging.getLogger ('').addHandler (console)
    # return logging
    logging.config.fileConfig ("config.conf")
    logger = logging.getLogger ("example01")
    return logging
if __name__ == '__main__':
    log()