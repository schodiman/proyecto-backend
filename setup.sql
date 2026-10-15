CREATE DATABASE if NOT EXISTS defaultdb;
CREATE USER 'avnadmin'@'%' IDENTIFIED BY 'tu_contraseña_segura';
GRANT ALL PRIVILEGES ON defaultdb.* TO 'avnadmin'@'%';
FLUSH PRIVILEGES;
