-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema certificacion4
-- ---------------------------------------------------

-- -----------------------------------------------------
-- Schema certificacion4
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `certificacion4` DEFAULT CHARACTER SET utf8 ;
USE `certificacion4` ;

-- ---------------------------------------------------
-- Table `certificacion4`.`usuarios` 
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `certificacion4`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `apellido` VARCHAR(255) NULL,
  `mail` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `certificacion4`.`libros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `certificacion4`.`libros` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(255) NULL,
  `autor` VARCHAR(255) NULL,
  `sinopsis` TEXT NULL,
  `created_at` DATETIME NULL,
  `usuarios_id` INT NOT NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`, `usuarios_id`),
  INDEX `fk_libros_usuarios_idx` (`usuarios_id` ASC) VISIBLE,
  CONSTRAINT `fk_libros_usuarios`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `certificacion4`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `certificacion4`.`libros_prestados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `certificacion4`.`libros_prestados` (
  `usuarios_id` INT NOT NULL,
  `libros_id` INT NOT NULL,
  `libros_usuarios_id` INT NOT NULL,
  PRIMARY KEY (`usuarios_id`, `libros_id`, `libros_usuarios_id`),
  INDEX `fk_usuarios_has_libros_libros1_idx` (`libros_id` ASC, `libros_usuarios_id` ASC) VISIBLE,
  INDEX `fk_usuarios_has_libros_usuarios1_idx` (`usuarios_id` ASC) VISIBLE,
  CONSTRAINT `fk_usuarios_has_libros_usuarios1`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `certificacion4`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuarios_has_libros_libros1`
    FOREIGN KEY (`libros_id` , `libros_usuarios_id`)
    REFERENCES `certificacion4`.`libros` (`id` , `usuarios_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
