-- ************************************** `Academias`
CREATE TABLE academias (
    id INT auto_increment NOT NULL,
    nombre varchar(100) NOT NULL,
    telefono varchar(45) NULL,
    web varchar(100) NULL,
    PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;




-- ************************************** `Profesores`

CREATE TABLE `profesores`
(
 `id`          integer NOT NULL ,
 `nombre`      varchar(100) NOT NULL ,
 `apellido`    varchar(100) NOT NULL ,
 `email`       varchar(255) NOT NULL ,
 `telefono`    varchar(45) NOT NULL ,
 `academia_id` integer NOT NULL ,

PRIMARY KEY (`id`),
KEY `FK` (`academia_id`),
CONSTRAINT `FK` FOREIGN KEY `FK` (`academia_id`) REFERENCES `academias` (`id`)
);

-- ************************************** `Alumnos`

CREATE TABLE `alumnos`
(
 `id`          integer NOT NULL ,
 `nombre`      varchar(100) NOT NULL ,
 `appellido`   varchar(100) NOT NULL ,
 `email`       varchar(255) NOT NULL ,
 `telefono`    varchar(45) NOT NULL ,
 `academia_id` integer NOT NULL ,

PRIMARY KEY (`id`),
KEY `FK` (`academia_id`),
CONSTRAINT `FK_2` FOREIGN KEY `FK` (`academia_id`) REFERENCES `academias` (`id`)
);

-- ************************************** `Cursos`

CREATE TABLE `cursos`
(
 `id`          integer NOT NULL ,
 `nombre`      varchar(100) NOT NULL ,
 `descripcion` text NOT NULL ,
 `profesor_id` integer NOT NULL ,

PRIMARY KEY (`id`),
KEY `FK` (`profesor_id`),
CONSTRAINT `FK_3` FOREIGN KEY `FK` (`profesor_id`) REFERENCES `profesores` (`id`)
);

-- ************************************** `Alumnos_cursos`

CREATE TABLE `alumnos_cursos`
(
 `id`        integer NOT NULL ,
 `alumno_id` integer NOT NULL ,
 `cursos_id` integer NOT NULL ,

PRIMARY KEY (`id`),
KEY `FK` (`alumno_id`),
CONSTRAINT `FK_4` FOREIGN KEY `FK` (`alumno_id`) REFERENCES `alumnos` (`id`),
KEY `FK_2` (`cursos_id`),
CONSTRAINT `FK_5` FOREIGN KEY `FK_2` (`cursos_id`) REFERENCES `cursos` (`id`)
);

-- ************************************** `Notas`

CREATE TABLE `notas`
(
 `id`        integer NOT NULL ,
 `nota`      float NOT NULL ,
 `alumno_id` integer NOT NULL ,
 `id_1`      integer NOT NULL ,

PRIMARY KEY (`id`),
KEY `FK` (`alumno_id`),
CONSTRAINT `FK_6` FOREIGN KEY `FK` (`alumno_id`) REFERENCES `alumnos` (`id`),
KEY `FK_2` (`id_1`),
CONSTRAINT `FK_7` FOREIGN KEY `FK_2` (`id_1`) REFERENCES `cursos` (`id`)
);




