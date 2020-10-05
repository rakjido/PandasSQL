-- MySQL Script generated by MySQL Workbench
-- Mon Oct  5 09:04:15 2020
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema EMPDB
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema EMPDB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `EMPDB` DEFAULT CHARACTER SET utf8 ;
USE `EMPDB` ;

-- -----------------------------------------------------
-- Table `EMPDB`.`EMP`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `EMPDB`.`EMP` ;

CREATE TABLE IF NOT EXISTS `EMPDB`.`EMP` (
  `EMPNO` INT NOT NULL,
  `ENAME` VARCHAR(10) NULL,
  `JOB` VARCHAR(9) NULL,
  `MGR` INT NULL,
  `HIREDATE` DATE NULL,
  `SAL` INT NULL,
  `COM` INT NULL,
  `DEPNO` INT NULL,
  PRIMARY KEY (`EMPNO`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `EMPDB`.`DEPT`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `EMPDB`.`DEPT` ;

CREATE TABLE IF NOT EXISTS `EMPDB`.`DEPT` (
  `DEPTNO` INT NOT NULL,
  `DNAME` VARCHAR(14) NULL,
  `LOC` VARCHAR(13) NULL,
  PRIMARY KEY (`DEPTNO`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `EMPDB`.`SALGRADE`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `EMPDB`.`SALGRADE` ;

CREATE TABLE IF NOT EXISTS `EMPDB`.`SALGRADE` (
  `GRADE` INT NULL,
  `LOSAL` INT NULL,
  `HISAL` INT NULL)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
