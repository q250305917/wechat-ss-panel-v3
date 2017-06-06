from django.db import models

# Create your models here.
class Magnet(models.Model):
    mgTitle = models.CharField(db_column='mgTitle', max_length=255)  # Field name made lowercase.
    mgSize = models.IntegerField(db_column='mgSize')  # Field name made lowercase.
    mgList = models.CharField(db_column='mgList', max_length=255)  # Field name made lowercase.
    mgCreate = models.DateTimeField(db_column='mgCreate')  # Field name made lowercase.
    mgHot = models.IntegerField(db_column='mgHot')  # Field name made lowercase.
    mgLable = models.CharField(db_column='mgLable', max_length=255)  # Field name made lowercase.
    mgList_1 = models.CharField(db_column='mgList_1', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'app_magnet'


class UserBind(models.Model):
    userid = models.IntegerField()
    openid = models.CharField(max_length=128)
    create = models.DateTimeField()
    modify = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_bind'


class UserCode(models.Model):
    openid = models.CharField(max_length=128)
    code = models.CharField(max_length=128)
    create = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_code'


class NodeSs(models.Model):
    node_name = models.CharField(max_length=128)
    node_type = models.IntegerField()
    node_server = models.CharField(max_length=128)
    node_method = models.CharField(max_length=64)
    node_info = models.CharField(max_length=128)
    node_status = models.CharField(max_length=128)
    node_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'node_ss'



class AliveIp(models.Model):
    id = models.BigAutoField(primary_key=True)
    nodeid = models.IntegerField()
    userid = models.IntegerField()
    ip = models.TextField()
    datetime = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'alive_ip'


class Announcement(models.Model):
    date = models.DateTimeField()
    content = models.TextField()
    markdown = models.TextField()

    class Meta:
        managed = False
        db_table = 'announcement'


class Auto(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField()
    value = models.TextField()
    sign = models.TextField()
    datetime = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'auto'


class Blockip(models.Model):
    id = models.BigAutoField(primary_key=True)
    nodeid = models.IntegerField()
    ip = models.TextField()
    datetime = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'blockip'


class Bought(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    shopid = models.BigIntegerField()
    datetime = models.BigIntegerField()
    renew = models.BigIntegerField()
    coupon = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'bought'


class Code(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.TextField()
    type = models.IntegerField()
    number = models.DecimalField(max_digits=11, decimal_places=2)
    isused = models.IntegerField()
    userid = models.BigIntegerField()
    usedatetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'code'


class Coupon(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.TextField()
    onetime = models.IntegerField()
    expire = models.BigIntegerField()
    shop = models.TextField()
    credit = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coupon'


class DetectList(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    text = models.TextField()
    regex = models.TextField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detect_list'


class DetectLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    list_id = models.BigIntegerField()
    datetime = models.BigIntegerField()
    node_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detect_log'


class DisconnectIp(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    ip = models.TextField()
    datetime = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'disconnect_ip'


class EmailVerify(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.TextField()
    ip = models.TextField()
    code = models.TextField()
    expire_in = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'email_verify'


class Link(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField()
    address = models.TextField()
    port = models.IntegerField()
    token = models.TextField()
    ios = models.IntegerField()
    userid = models.BigIntegerField()
    isp = models.TextField(blank=True, null=True)
    geo = models.IntegerField(blank=True, null=True)
    method = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link'


class LoginIp(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    ip = models.TextField()
    datetime = models.BigIntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login_ip'


class Payback(models.Model):
    id = models.BigAutoField(primary_key=True)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    userid = models.BigIntegerField()
    ref_by = models.BigIntegerField()
    ref_get = models.DecimalField(max_digits=12, decimal_places=2)
    datetime = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'payback'


class Paylist(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    total = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.IntegerField()
    tradeno = models.TextField(blank=True, null=True)
    datetime = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'paylist'


class RadiusBan(models.Model):
    userid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'radius_ban'


class Relay(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    source_node_id = models.BigIntegerField()
    dist_node_id = models.BigIntegerField()
    dist_ip = models.TextField()
    port = models.IntegerField()
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'relay'


class Shop(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    content = models.TextField()
    auto_renew = models.IntegerField()
    auto_reset_bandwidth = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop'


class Speedtest(models.Model):
    id = models.BigAutoField(primary_key=True)
    nodeid = models.IntegerField()
    datetime = models.BigIntegerField()
    telecomping = models.TextField()
    telecomeupload = models.TextField()
    telecomedownload = models.TextField()
    unicomping = models.TextField()
    unicomupload = models.TextField()
    unicomdownload = models.TextField()
    cmccping = models.TextField()
    cmccupload = models.TextField()
    cmccdownload = models.TextField()

    class Meta:
        managed = False
        db_table = 'speedtest'


class SsInviteCode(models.Model):
    code = models.CharField(max_length=128)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ss_invite_code'


class SsNode(models.Model):
    name = models.CharField(max_length=128)
    type = models.IntegerField()
    server = models.CharField(max_length=128)
    method = models.CharField(max_length=64)
    info = models.CharField(max_length=128)
    status = models.CharField(max_length=128)
    sort = models.IntegerField()
    custom_method = models.IntegerField()
    traffic_rate = models.FloatField()
    node_class = models.IntegerField()
    node_speedlimit = models.DecimalField(max_digits=12, decimal_places=2)
    node_connector = models.IntegerField()
    node_bandwidth = models.BigIntegerField()
    node_bandwidth_limit = models.BigIntegerField()
    bandwidthlimit_resetday = models.IntegerField()
    node_heartbeat = models.BigIntegerField()
    node_ip = models.TextField(blank=True, null=True)
    node_group = models.IntegerField()
    custom_rss = models.IntegerField()
    mu_only = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ss_node'


class SsNodeInfo(models.Model):
    node_id = models.IntegerField()
    uptime = models.FloatField()
    load = models.CharField(max_length=32)
    log_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ss_node_info'


class SsNodeOnlineLog(models.Model):
    node_id = models.IntegerField()
    online_user = models.IntegerField()
    log_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ss_node_online_log'


class SsPasswordReset(models.Model):
    email = models.CharField(max_length=32)
    token = models.CharField(max_length=128)
    init_time = models.IntegerField()
    expire_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ss_password_reset'


class TelegramSession(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    type = models.IntegerField()
    session_content = models.TextField()
    datetime = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'telegram_session'


class Ticket(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField()
    rootid = models.BigIntegerField()
    userid = models.BigIntegerField()
    datetime = models.BigIntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ticket'


class Unblockip(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip = models.TextField()
    datetime = models.BigIntegerField()
    userid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'unblockip'


class User(models.Model):
    user_name = models.CharField(max_length=128)
    email = models.CharField(max_length=32)
    pass_field = models.CharField(db_column='pass', max_length=64)  # Field renamed because it was a Python reserved word.
    passwd = models.CharField(max_length=16)
    t = models.IntegerField()
    u = models.BigIntegerField()
    d = models.BigIntegerField()
    plan = models.CharField(max_length=2)
    transfer_enable = models.BigIntegerField()
    port = models.IntegerField()
    switch = models.IntegerField()
    enable = models.IntegerField()
    type = models.IntegerField()
    last_get_gift_time = models.IntegerField()
    last_check_in_time = models.IntegerField()
    last_rest_pass_time = models.IntegerField()
    reg_date = models.DateTimeField()
    invite_num = models.IntegerField()
    money = models.DecimalField(max_digits=12, decimal_places=2)
    ref_by = models.IntegerField()
    expire_time = models.IntegerField()
    method = models.CharField(max_length=64)
    is_email_verify = models.IntegerField()
    reg_ip = models.CharField(max_length=128)
    node_speedlimit = models.DecimalField(max_digits=12, decimal_places=2)
    node_connector = models.IntegerField()
    is_admin = models.IntegerField()
    im_type = models.IntegerField(blank=True, null=True)
    im_value = models.TextField(blank=True, null=True)
    last_day_t = models.BigIntegerField()
    senddailymail = models.IntegerField(db_column='sendDailyMail')  # Field name made lowercase.
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    class_expire = models.DateTimeField()
    expire_in = models.DateTimeField()
    theme = models.TextField()
    ga_token = models.TextField()
    ga_enable = models.IntegerField()
    pac = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    node_group = models.IntegerField()
    auto_reset_day = models.IntegerField()
    auto_reset_bandwidth = models.DecimalField(max_digits=12, decimal_places=2)
    relay_enable = models.IntegerField()
    relay_info = models.TextField(blank=True, null=True)
    protocol = models.CharField(max_length=128, blank=True, null=True)
    protocol_param = models.CharField(max_length=128, blank=True, null=True)
    obfs = models.CharField(max_length=128, blank=True, null=True)
    obfs_param = models.CharField(max_length=128, blank=True, null=True)
    forbidden_ip = models.TextField(blank=True, null=True)
    forbidden_port = models.TextField(blank=True, null=True)
    disconnect_ip = models.TextField(blank=True, null=True)
    is_hide = models.IntegerField()
    is_multi_user = models.IntegerField()
    telegram_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserToken(models.Model):
    token = models.CharField(max_length=256)
    user_id = models.IntegerField()
    create_time = models.IntegerField()
    expire_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_token'


class UserTrafficLog(models.Model):
    user_id = models.IntegerField()
    u = models.IntegerField()
    d = models.IntegerField()
    node_id = models.IntegerField()
    rate = models.FloatField()
    traffic = models.CharField(max_length=32)
    log_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_traffic_log'

