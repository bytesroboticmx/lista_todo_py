-- Tabla para las Listas de Tareas
CREATE TABLE ListasTareas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_creacion DATE NOT NULL,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    usuario_id INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id) -- Suponiendo que tengas una tabla de usuarios
);

-- Tabla para las Tareas
CREATE TABLE Tareas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_creacion DATE NOT NULL,
    fecha_vencimiento DATE,
    completada BOOLEAN NOT NULL DEFAULT FALSE,
    lista_id INT NOT NULL,
    FOREIGN KEY (lista_id) REFERENCES ListasTareas(id)
);
