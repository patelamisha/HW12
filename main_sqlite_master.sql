INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'majors', 'majors', 7, 'CREATE TABLE majors
(
	Major TEXT,
	"Required/Elective" TEXT,
	Course TEXT
)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'instructors', 'instructors', 2, 'CREATE TABLE instructors
(
	CWID TEXT,
	Name TEXT,
	Dept TEXT
)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'grades', 'grades', 4, 'CREATE TABLE grades
(
	StudentCWID TEXT,
	Course TEXT,
	Grade TEXT,
	InstructorCWID TEXT
)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'students', 'students', 5, 'CREATE TABLE "students"
(
	CWID TEXT
		constraint students_pk
			primary key,
	Name TEXT,
	Major TEXT
)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('index', 'sqlite_autoindex_students_1', 'students', 6, null);