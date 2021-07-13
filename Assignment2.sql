create table student(
	firstName	varChar(20),
	lastName	varChar(20),
	studentID	numeric(10,0),
	gradYear	int,
	major		char(4),
	email		varChar(15));

create table instructor(
	firstName	varChar(20),
	lastName	varChar(20),
	employeeID	numeric(10,0),
	title		varChar(30),
	dept		char(4),
	email		varChar(15),
	yearHired	int);

create table admin(
	firstName	varChar(20),
	lastName	varChar(20),
	employeeID	numeric(10,0),
	office		varChar(10),
	title		varChar(30),
	email		varChar(15));

create table course(
	title 		varChar(30),
	CRN			numeric(8,0),
	dept 		char(4),
	instructor 	varChar(20),
	classTime	numeric(4),
	days		varChar(3),
	semester	char(2),
	courseYear 	int,
	credits	 	int);


insert into student 
	values('A', 'B', 0101010101, 2019, 'BSCO', 'ab@wit.edu');
insert into student 
	values('C', 'D', 0101010102, 2020, 'BSEE', 'cdwit.edu');	
insert into student 
	values('E', 'F', 0101010103, 2021, 'BCOS', 'efwit.edu');
insert into student 
	values('G', 'H', 0101010104, 2022, 'BSME', 'gh@wit.edu');
insert into student 
	values('I', 'J', 0101010105, 2023, 'BELM', 'ij@wit.edu');

insert into instructor
	values('Z', 'Y', 1111111111, 'Prof.', 'BSCO', 'zy@wit.edu',2000);
insert into instructor
	values('X', 'W', 2222222222, 'Asst. Prof.', 'BELM', 'xw@wit.edu',2018);
insert into instructor
	values('V', 'U', 3333333333, 'Assoc. Prof.', 'BSEE', 'vu@wit.edu',2010);

insert into admin
	values('M', 'N', 1234567890, 'WNTW 101', 'Registrar', 'registrar@wit.edu');

insert into course
	values('Intro to Eng.', '00110011', NULL, 'W', 1000, 'MWF', 'Sp', 2019, 4);
insert into course
	values('Computer Architecture', '00220022', 'BSCO', 'Z', 1000, 'TR', 'Su', 2019, 3);
insert into course
	values('Data Structures', '00330033', NULL, 'Z', 1400, 'MW', 'Fa', 2019, 4);
insert into course
	values('Senior Design', '00440044', NULL, 'TBA', 0800, 'MWF', 'Su', 2020, 4);

select lastName, major
from student;