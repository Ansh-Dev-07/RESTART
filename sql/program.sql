create table student10 (
   id    number primary key,
   name  varchar2(20) not null,
   age   number check ( age > 18 ),
   dept  varchar2(25),
   marks number
);

insert into student10 values ( 1,
                               'Ansh',
                               22,
                               'CSE',
                               80 );
insert into student10 values ( 2,
                               'Ravi',
                               21,
                               'IT',
                               75 );
insert into student10 values ( 3,
                               'Neha',
                               19,
                               'ECE',
                               90 );

select *
  from student10;
select name,
       marks
  from student10;
select *
  from student10
 where marks > 80;
select *
  from student10
 where dept = 'CSE';
select *
  from student10
 order by marks;

select *
  from student10
 where name like '__s%';

create table dept10 (
   dept_id   number primary key,
   dept_name varchar2(25)
);

create table student11 (
   id      number primary key,
   name    varchar2(20) not null,
   dept_id number,
   foreign key ( dept_id )
      references dept10 ( dept_id )
);

insert into dept10 values ( 22,
                            'CSE' );
insert into dept10 values ( 21,
                            'IT' );
insert into dept10 values ( 19,
                            'ECE' );
insert into student11 values ( 1,
                               'Ansh',
                               22 );
insert into student11 values ( 2,
                               'Ravi',
                               21 );
insert into student11 values ( 3,
                               'Neha',
                               19 );

select name,
       dept_name
  from student11 s,
       dept10 d
 where s.dept_id = d.dept_id;
select s.name,
       d.dept_name
  from student11 s
 inner join dept10 d
on s.dept_id = d.dept_id;
select s.name,
       d.dept_name
  from student11 s
  left outer join dept10 d
on s.dept_id = d.dept_id;
select s.name,
       d.dept_name
  from student11 s
 right outer join dept10 d
on s.dept_id = d.dept_id;

select s.name,
       d.dept_name
  from student11 s,
       dept10 d
 where s.dept_id = d.dept_id
   and d.dept_name = 'CSE';

select d.dept_name,
       count(*)
  from student11 s,
       dept10 d
 where s.dept_id = d.dept_id
 group by d.dept_name;

select d.dept_name,
       count(*)
  from student11 s,
       dept10 d
 where s.dept_id = d.dept_id
 group by d.dept_name
having count(*) > 1;

select count(*)
  from student11;

select dept_id,
       count(*)
  from student11
 group by dept_id;

select d.dept_name,
       count(*)
  from student11 s,
       dept10 d
 where s.dept_id = d.dept_id
 group by d.dept_name;

select sum(marks)
  from student10;

--select dept_id, sum(marks) from Student11 group by dept_id;

select avg(marks)
  from student10;

--select dept_id, avg(marks) from Student11 group by dept_id;

select max(marks)
  from student10;

--select dept_id, max(marks) from Student11 group by dept_id;

select min(marks)
  from student10;

--select dept_id, min(marks) from Student11 group by dept_id;

select upper(name)
  from student11;

select lower(name)
  from student11;

select *
  from student11
 where upper(name) = 'RAVI';

select nvl(
   marks,
   0
)
  from student10;

select *
  from student11
 where dept_id in ( 1,
                    2 );

select *
  from student10
 where marks between 50 and 80;

select *
  from student10
 where marks > (
   select avg(marks)
     from student10
);