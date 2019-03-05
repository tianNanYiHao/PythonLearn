


-- 数据库操作

-----------------------------------------------------------------------------------------------------------------------
-- 1. 库层级的相关操作 -----------------

	-- 链接数据库
  	mysql -uroot -p
  	mysql -uroot -pmysql123
  
 	-- 退出数据库
  	exit/quit

  	--sql语句最后需要分号;结尾--

  	-- 显示数据库版本
  	select version();

  	-- 显示时间
  	select now();

  	-- 查看所有数据库
  	show databases;

  	-- 创建数据库
  	create database python_test1;
  	create database python_test2  charset=utf8;

  	-- 查看创建的数据库
  	show create database python_test2;
 
  	-- 使用数据库
  	use python_test2;

  	-- 删除数据库
  	drop database python_test2;

----------------------------------------------------------------------------------------------------------------------------------------
-- 2. 表层级的相关操作 -----------------
  -- 数据库中,表的操作
  	-- 查看当前数据库中所有的表
  	show tables;

  	-- 查看创建的某个表描述
  	show create table xxxx;
  	show create table xxxx2;

  	-- 创建表
  	-- create table 数据表名字 (字段 类型 约束[, 字段 类型 约束]);
  	-- auto_increment 表示自动增长
  	-- not null 表示不能为空
  	-- primary key 表示主键
  	-- default 默认值
  	create table xxxx(id int, name varchar(30));
  	create table xxxx2(id int, sex varchar(30), age int);
  	create table xxxx3(id int primary key not null auto_increment, title varchar(100));
  	-- 创建一个student表(id, name, age, hight, gender, cls_id)
  	create table student(
  			id int unsigned primary key not null auto_increment,
  			name varchar(30) not null,
  			age tinyint unsigned default 0,
  			height decimal(5,2) ,
  			gender enum("男","女","人妖") default "人妖",
  			cls_id int unsigned
  		);

  	-- 插入一条数据
  	insert into student values(1,"小明",12,1.45,"人妖",0);
  	insert into classes vaules(1,'桔子班');

  	-- 查看某个表的所有数据
  	select * from student;
  	select * from classdes;

  	-- 表结构的增删改查
  	-- 查看表的数据结构
  	desc student;

  	-- 表添加字段
  	alter table student add brithday datetime;

  	-- 修改表字段(不重命名)
  	-- modify 
  	alter table student modify brithday date;
  	-- 修改表字段(重命名)
  	alter table student change brithday date default "1990-01-01";

  	-- 删除表字段
  	alter table student drop date;

  	-- 删除表
  	drop table student;


----------------------------------------------------------------------------------------------------------------------------------------
-- 3.数据层级的相关操作 -----------------

  -- student表
  +----+-----------+------+--------+--------+--------+-----------+
  | id | name      | age  | height | gender | cls_id | is_hidden |
  +----+-----------+------+--------+--------+--------+-----------+
  | 12 | 王五      |   19 |  22.33 | 男     |      3 |           |
  | 13 | 小明      |   14 |  12.89 | 男     |      1 |           |
  | 14 | 小王      |   15 |  13.23 | 女     |      3 |          |
  | 15 | 阿坝      |   12 |  12.09 | 女     |      2 |           |
  | 16 | 春树      |   11 |  12.33 | 女     |      3 |          |
  | 17 | 小秦      |   19 |  22.43 | 男     |      2 |           |
  | 18 | 大白      |   12 |  12.33 | 男     |      1 |           |
  | 19 | 小白      |   15 |  12.83 | 女     |      3 |          |
  | 20 | 小白菜    |   18 |  42.39 | 男     |      1 |           |
  | 21 | 丽斯      |   12 |  12.31 | 女     |      3 |          |
  | 22 | 嘉文瑥    |   28 |  52.52 | 男     |      2 |           |
  | 23 | 长谷川    |   32 |  16.89 | 男     |      2 |           |
  +----+-----------+------+--------+--------+--------+-----------+

  -- classes表
  +----+-----------+
  | id | title     |
  +----+-----------+
  |  1 | 草莓班    |
  |  2 | 香瓜班    |
  |  3 | 蜜糖班    |
  +----+-----------+

   -- 增加 
      -- 全列插入
      -- insert [into] 表名 values(...)
      -- 主键字段 可以用 0 null default 来占位
      -- 向classes表中插入 一个班级
      insert into classes values(0,'桔子班');
      insert into classes values(default,'苹果班');
      -- 枚举中的值对应1/2/3....
      insert into student values(1,"小明",12,1.45,"男(或这里可以用数字1代替)",0);

      -- 部分插入
      insert into student (name,age) values("小平",12);

      -- 多行插入
      insert into student (name,age) values('张三',13),('李四', 13);

   -- 修改
   	  -- update
   	  update student set age=12; --将字段age全部改为12
   	  update student set age=19 where name='小白'; --只要name=小白,全部修改
   	  update student set age=20 where id=3; --只要id为3,进行修改
   	  update student set age=22,name='小明' where id=10; --只要id为10,进行修改

   -- 删除
    -- 物理删除
      delete from student; --整个删除表内数据
      delete from student where name='小白菜';

    -- 逻辑删除
    alter table student add is_hidden bit default 0; --添加一个字段,用于标识是否逻辑删除
    update student set is_hidden=1 where id=4; --逻辑删除(标识)id为6的数据



   -- 查询
   	  -- 查询所有列
   	  select * from student;
   	  -- 指定条件查询
   	  select * from student where name='小白菜'; --查询name为小白菜的所有数据
   	  select * from student where id>3; --查询id大于3的所有信息
   	  
   	  -- 查询指定字段
   	  select name,age from student;
 	
 	  -- 使用as为字段指定别名
 	  select name as 姓名, age as 年龄 from student;


----------------------------------------------------------------------------------------------------------------------------------------
-- 4.sql查询(重点) -----------------

  -- 查询:
    -- 查询所有字段 
    select * from student;
    -- 查询指定字段
    select name from student;
    -- 查询指定字段且字段以别名显示
    select name as '姓名' from student;
    -- 以表名.字段方式查询字段
    select student.name,student.age from student;
    -- 通过 as 给表起别名
    select s.name,s.age from student as s;
    -- 消除重复行
    -- distinct 字段;
    select distinct gender from student;

   -- 条件查询:
    -- > 
    select * from student where age>12;
    -- <
    select * from student where age<19;
    select id,name,age,height from student where age=15;
   
   -- 逻辑运算符
    -- and 
    -- 18到28岁的所有学生信息
    select id,name from student where age<18 and age>12;
    -- 18岁以上的女性
    select * from student where age>18 and gender=2;

    -- or
    -- 18岁以下或则身高大于12.55的所有学生
    select * from student where age<18 or height>12.55;

    -- not 
    -- 不在18岁以上的女性
    select * from student where not (age>18 and gender=2);
    -- 不在18以上,且女性
    select * from student where not age>18 adn gender=2;


   -- 模糊查询
    -- like
    -- % 替换1个或多个
    -- _ 替换一个
    -- 查询姓名中以 '小'开始的名字
    select name from student where name like '小%'; --性能低, 使用比较少
    -- 查询姓名中, 包含 '小'的名字
    select name from student where name like '%小%';
    -- 查询有两个字符的名字
    select name from student where name like '__';
    -- 查询至少两个字符及以上的名字
    select name from student where name like '__%';

   -- rlike正则
    -- 查询 以 长开头的姓名
    select name from student where name rlike '^长.*';
    -- 查询 以 长开头,川结尾的姓名
    select name from student where name rlike '^长.*川$';

   -- 范围查询
    -- in (1,3,5) 表示在一个非连续范围内
    select name,age from student where age in (12,15,19);
    select name,age from student where age not in(12,15);

    -- between...and... 连续范围内查询
    select name,age from student where age between 12 and 20;
    -- not between... and ... 连续范围之外
    select name,age from student where age not between 12 and 20;

   -- 空判断
    -- is null 
    select name,height from student where height is null;
    -- is not null
    select name,height from student where height is not null;


  -- 排序
    -- order by 字段
    -- asc 从小到大,升序
    -- desc 从大到小,降序
    -- 查询age在12到20的男性,按升序排列
    select name,age from student where (age between 12 and 20) and gender=1 order by age;
    -- 查询age在12到20的男性,按降序排列
    select name,age from student where (age between 12 and 20) and gender=2 order by age desc;
    -- 查询年龄在12到20的女性,身高从高道矮(降序)
    select name,age,height from student where (age between 12 and 20) and gender=2 order by height desc;
    -- 查询年龄在12到20的女性,身高从高道矮(降序),如果身高相同则按照年龄从大到小排
    select name,age,height from student where (age between 12 and 20) and gender=2 order by height desc,age desc;



  -- 聚合函数
   -- count 总数
   -- 查询男生多少人,女生多少人
   select count(*) from student where gender=1;
   select count(*) as 男生人数 from student where gender=1;

   -- max 最大值
   select max(age) from student;
   -- 查询名字有小字的学生的最大身高
   select max(height) from student where name like '%小%';

   -- min 最小值
   select min(height) from student;

   -- sum 求和
   select sum(age) from student where gender=1; --求所有男生的年龄总和

   -- avg 平均值
   select avg(height) from student where gender=2; --求所有女生的平均身高
   
   -- round(,) 四舍五入, 保留x位小数
   select round(avg(height),1) from student;



  -- 分组
   -- group by 
   -- 按照性别分组,统计每个性别的人数
   select gender, count(*) from student group by gender;
   -- 按照男性分组,并统计人数
   select gender, count(*) from student where gender=1 group by gender;

   -- group _concat(...)
   -- 按照某个字段分组,并查看各分组的内容
   select gender,group_concat(id,"_",name,"_",age,"_",height) from student group by gender;

   -- having 对分组进行调节判断
   -- 按性别分组,查询平均年龄超过15的姓名
   select gender,group_concat(name),avg(age) from student group by gender having avg(age)>15;

   -- 查询每种性别中,人数多于5个的信息
   select gender,group_concat(name) from student group by gender having count(*)>5;

   -- 小结where与having的区别, 
   -- where是对原始数据表的判断
   -- having是对分组后的数据进行判断



  -- 分页
    -- limit start, count
    -- 限制查询出的数据
    select * from student limit 5;
    select * from student limit 0,5; -- 从零开始, 查询5个数据

  -- 连接查询
    -- inner join ... on
    -- 查询 有能够对应班级的学生及班级信息
    select * from student inner join classes on student.cls_id=classes.id;
    select * from student as s inner join classes as c on s.cls_id=c.id;
    -- 按要求显示姓名,班级
    select student.name, classes.title from student inner join classes on student.cls_id=classes.id;
    select s.name,c.title from student as s inner join classes as c on s.cls_id=c.id;

    -- 以上查询中, 将班级放在第一列, 并将班级分类,且将序号从小到大排列,且将年龄升序,
    +-----------+----+-----------+------+--------+--------+--------+-----------+
    | title     | id | name      | age  | height | gender | cls_id | is_hidden |
    +-----------+----+-----------+------+--------+--------+--------+-----------+
    | 草莓班    | 13 | 小明      |   14 |  12.89 | 男     |      1 |           |
    | 草莓班    | 18 | 大白      |   12 |  12.33 | 男     |      1 |           |
    | 草莓班    | 20 | 小白菜    |   18 |  42.39 | 男     |      1 |           |
    | 蜜糖班    | 12 | 王五      |   19 |  22.33 | 男     |      3 |           |
    | 蜜糖班    | 14 | 小王      |   15 |  13.23 | 女     |      3 |          |
    | 蜜糖班    | 16 | 春树      |   11 |  12.33 | 女     |      3 |          |
    | 蜜糖班    | 19 | 小白      |   15 |  12.83 | 女     |      3 |          |
    | 蜜糖班    | 21 | 丽斯      |   12 |  12.31 | 女     |      3 |          |
    | 香瓜班    | 15 | 阿坝      |   12 |  12.09 | 女     |      2 |           |
    | 香瓜班    | 17 | 小秦      |   19 |  22.43 | 男     |      2 |           |
    | 香瓜班    | 22 | 嘉文瑥    |   28 |  52.52 | 男     |      2 |           |
    | 香瓜班    | 23 | 长谷川    |   32 |  16.89 | 男     |      2 |           |
    +-----------+----+-----------+------+--------+--------+--------+-----------+
    select c.title,s.* from student as s inner join classes as c on s.cls_id=c.id order by c.title asc,s.id asc,s.age asc;


-- left join ... on 左连接查询
  -- 查询每位学生对应的班级信息
  select * from student as s left join classes as c on s.cls_id=c.id;
  -- 查询没有班级的学生
  select * from student as s left join classes as c on s.cls_id=c.id having c.id is null;



-- 自关联
  -- source xxx.sql 即可
  -- 举例: 中国省市地区SQL
+-----------+--------------+
| name      | name         |
+-----------+--------------+
| 江苏省    | 南京市       |
| 江苏省    | 无锡市       |
| 江苏省    | 徐州市       |
| 江苏省    | 常州市       |
| 江苏省    | 苏州市       |
| 江苏省    | 南通市       |
| 江苏省    | 连云港市     |
| 江苏省    | 淮安市       |
| 江苏省    | 盐城市       |
| 江苏省    | 扬州市       |
| 江苏省    | 镇江市       |
| 江苏省    | 泰州市       |
| 江苏省    | 宿迁市       |
+-----------+--------------+
  select state.name,city.name from region_directory as state inner join region_directory as city on state.id=city.pid having state.name='江苏省';

-- 子查询

  -- 查询身高最高的男生信息
  select * from student where height=(select max(height) from student) order by gender=1;

































































 






































































































































































