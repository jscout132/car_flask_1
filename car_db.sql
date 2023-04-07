select * from car_info 

alter table car_info 
add column "token" VARCHAR(15) references "user"("token");

alter table car_info 
drop column user_token

alter table car_info 
alter column year_ type VARCHAR(20);

insert into car_info (serial_number, car_make, car_model, cost_, mileage, year_, car_color, "token")
VALUES(111, 'Honda', 'CRV', 19874.23, 24500, 2016, 'Blue', 'a8abb8500756');

select * from "user"