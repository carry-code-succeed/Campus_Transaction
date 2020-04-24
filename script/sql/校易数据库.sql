/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2020/4/24 21:06:12                           */
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
   ADMIN_PICTURE        MEDIUMBLOB,
   primary key (ADMIN_ID)
);

/*==============================================================*/
/* Table: COMMODITY                                             */
/*==============================================================*/
create table COMMODITY
(
   COMMODITY_ID         VARCHAR(20) not null,
   USER_ID              VARCHAR(22) not null,
   COMMODITY_NAME       VARCHAR(40) not null,
   COMMODITY_INFO       VARCHAR(400) not null,
   COMMODITY_PRICE      INT not null,
   COMMODITY_PICTRUE    MEDIUMBLOB not null,
   IS_PUTAWAY           VARCHAR(22) not null,
   primary key (COMMODITY_ID)
);

/*==============================================================*/
/* Table: STUDENT                                               */
/*==============================================================*/
create table STUDENT
(
   STUDENT_ID           VARCHAR(22) not null,
   STUDENT_NAME         VARCHAR(40) not null,
   IS_REGISTER          VARCHAR(22),
   primary key (STUDENT_ID)
);

/*==============================================================*/
/* Table: USER_INFO                                             */
/*==============================================================*/
create table USER_INFO
(
   USER_ID              VARCHAR(22) not null,
   USER_NAME            VARCHAR(40) not null,
   USER_PASSWORD        VARCHAR(40) not null,
   USER_PICTRUE         MEDIUMBLOB,
   primary key (USER_ID),
   unique key UNQ_USER_INFO_USER_NAME (USER_NAME)
);

alter table COMMODITY add constraint FK_USERINFO_COMMODITY foreign key (USER_ID)
      references USER_INFO (USER_ID) on delete restrict on update restrict;

