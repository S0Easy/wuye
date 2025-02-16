from django.db import models

# Create your models here.
class BSIC_INFO(models.Model):
    name = models.CharField(max_length=20, verbose_name='基础信息表',default="基础信息表")
    ip = models.CharField(max_length=20, verbose_name='ip')
    hostname = models.CharField(max_length=20, verbose_name='主机名')
    assset_desc = models.CharField(max_length=20, verbose_name='资产描述')
    os_type = models.CharField(max_length=20, verbose_name='操作系统')
    sys_user = models.CharField(max_length=100, verbose_name='系统用户',default="")
    sys_password = models.CharField(max_length=255, verbose_name='系统密码',default="")
    cpu_cores = models.CharField(max_length=20, verbose_name='cpu核数', default="")

    


    class Meta:
        db_table = 'bsic_info'
        verbose_name = 'BSIC信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name