--注册接口
--signup_01、测试成功注册、删除数据库中users表中的test06、info表中的成功注册用户
delete from info where name='成功注册用户'
delete from users where username='test06'

--signup_02、测试注册用户名为空、删除数据库中users表中的''、info表中的注册用户名为空用户
delete from info where name='注册用户名为空用户'
delete from users where username=''

--signup_03、测试注册密码为空、删除数据库中test07、注册密码为空用户
delete from info where name='注册密码为空用户'
delete from users where username='test07'

--signup_04、测试注册确认密码为空、删除数据库中test08、注册确认密码为空用户
delete from info where name='注册确认密码为空用户'
delete from users where username='test08'

--signup_05、测试注册姓名为空、删除数据库中test09、姓名为''用户
delete from info where name=''
delete from users where username='test09'

--signup_06、测试注册所有参数为空、删除数据库中user表中的''、姓名为''用户
delete from info where name=''
delete from users where username=''

--signup_07、测试注册用户名字数超过30、删除数据库中test10test10test10test10test10-、注册用户名31个字用户
delete from info where name='注册用户名31个字用户'
delete from users where username='test10test10test10test10test10-'

--signup_08、测试注册密码字数超过50、删除数据库中test11、注册密码51个字用户
delete from info where name='注册密码51个字用户'
delete from users where username='test11'

--signup_09、测试注册确认密码字数超过50、删除数据库中test12、注册确认密码51个字用户
delete from info where name='注册确认密码51个字用户'
delete from users where username='test12'

--signup_10、测试注册姓名字数超过20、删除数据库中test13、注册姓名字数21用户-注册姓名字数21用户
delete from info where name='注册姓名字数21用户-注册姓名字数21用户'
delete from users where username='test13'

--signup_11、测试注册密码与确认密码不一致、删除数据库中test14、注册两个密码不一致用户
delete from info where name='注册两个密码不一致用户'
delete from users where username='test14'

--signup_12、测试用户名被占用、把test15、123456加密、注册时间2022/8/1、注册用户名已存在用户写入数据库
delete from info where id=7
delete from users where id=7
insert into users(id,username,password,regtime) values(7,'test15',md5('123456'),'2022/08/01')
insert into info(id, name) values(7, '注册用户名已存在用户')