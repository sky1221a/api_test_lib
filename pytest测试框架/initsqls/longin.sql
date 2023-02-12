--登录接口
--login_01、测试成功登录、把test01写入数据库
delete from info where id=4
delete from users where id=4
insert into users(id,username,password) values(4,'test01',md5('123456'))
insert into info(id, name) values(4, '成功登录用户')

--login_02、测试用户名为空、删除''用户
delete from info where name=''
delete from users where username=''

--login_03、测试密码为空、把test02、123456加密写入数据库
delete from info where id=5
delete from users where id=5
insert into users(id,username,password) values(5,'test02',md5('123456'))
insert into info(id, name) values(5, '登录密码为空用户')

--login_04、测试用户名和密码均为空
--login_05、测试用户名错误、删除数据库中test03
delete from info where name='登录用户名错误用户'
delete from users where username='test03'

--login_06、测试密码错误、把test04、123456加密写入数据库
delete from info where id=6
delete from users where id=6
insert into users(id,username,password) values(6,'test04',md5('123456'))
insert into info(id, name) values(6, '登录密码错误用户')

--login_07、测试用户名和密码均错误、删除数据库中test05
delete from info where name='登录用户名与密码均错误用户'
delete from users where username='test05'
