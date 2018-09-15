drop table if exists inspection;
drop table if exists violation;

PRAGMA foreign_keys = ON;

create table inspection (
    activity_date Date,
    employee_id number(8),
    facility_address char(30),
    facility_city char(30),
    facility_id number(3) PRIMARY KEY,
    facility_name char(30),
    facility_state char(20),
    facility_zip number(3),
    grade number(3),
    owner_id number(3),
    owner_name char(30),
    pe_description char(30),
    program_element_pe number(3),
    program_name char(30),
    program_status
    record_id number(3),
    score number(3),
    serial_number number(3),
    service_code number(3),
    service_description char(30));

create table violation (
points number(8),
serial_number char(30),
violation_code char(3),
violation_description char(30),
violation_status char(20));
