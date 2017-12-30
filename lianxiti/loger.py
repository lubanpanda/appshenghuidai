import logging
import logging.config


# 使用baseConfig()函数,可选参数有filename,filemode,format,datefmt,level,stream
# 有filename是文件日志输出,filemode是'w'的话，文件会被覆盖之前生成的文件会被覆盖。datafmt参数用于格式化日期的输出
def log():
    logging.config.fileConfig ("/Users/yuchengtao/PycharmProjects/shenghuidai/SHD_automation/panda_log/config.conf")
    logging.getLogger ("shenghuidai")
    return logging
if __name__ == '__main__':
    log()