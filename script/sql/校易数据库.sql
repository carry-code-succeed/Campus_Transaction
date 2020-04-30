/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2020/4/30 19:51:42                           */
/*==============================================================*/


drop table if exists ADMIN;

drop table if exists COMMODITY;

drop table if exists STUDENT;

drop table if exists USER_INFO;

/*==============================================================*/
/* Table: ADMIN                                                 */
/*==============================================================*/
create table ADMIN
(
   ADMIN_ID             VARCHAR(22) not null,
   ADMIN_NAME           VARCHAR(40) not null,
   ADMIN_PASSWORD       VARCHAR(40) not null,
   ADMIN_PICTURE        VARCHAR(200),
   primary key (ADMIN_ID)
)
charset = utf8mb4;

/*==============================================================*/
/* Table: COMMODITY                                             */
/*==============================================================*/
create table COMMODITY
(
   COMMODITY_ID         VARCHAR(20) not null,
   USER_ID              VARCHAR(22),
   COMMODITY_NAME       VARCHAR(40) not null,
   COMMODITY_INFO       VARCHAR(400) not null,
   COMMODITY_PRICE      INT not null,
   COMMODITY_PICTRUE    VARCHAR(200) not null,
   IS_PUTAWAY           VARCHAR(22) not null,
   primary key (COMMODITY_ID)
)
charset = utf8mb4;

/*==============================================================*/
/* Table: STUDENT                                               */
/*==============================================================*/
create table STUDENT
(
   STUDENT_ID           VARCHAR(22) not null,
   STUDENT_NAME         VARCHAR(40) not null,
   IS_REGISTER          VARCHAR(22),
   primary key (STUDENT_ID)
)
charset = utf8mb4;

/*==============================================================*/
/* Table: USER_INFO                                             */
/*==============================================================*/
create table USER_INFO
(
   USER_ID              VARCHAR(22) not null,
   USER_NAME            VARCHAR(40) not null,
   STUDENT_ID           VARCHAR(22),
   USER_PASSWORD        VARCHAR(40) not null,
   USER_PICTRUE         VARCHAR(200),
   primary key (USER_ID),
   unique key UNQ_USER_INFO_USER_NAME (USER_NAME)
)
charset = utf8mb4;

