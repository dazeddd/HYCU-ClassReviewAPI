create table subject (
    id uuid not null primary key default gen_random_uuid(),
    name text not null,
    professor_id uuid not null
);


create table student (
    id uuid not null primary key default gen_random_uuid(),
    name text not null,
    student_number text not null
);


create table professor (
    id uuid not null primary key default gen_random_uuid(),
    name text not null
);



