# PROBLEMA PROPUESTO

## Se creará un grupo, donde todo aquel que pertenezca a dicho grupo, podrá rwx

### Crear un grupo llamado "Auditores" cuyo propietario será Él

groupadd Auditores

### Luego creo el usuario ROXS dentro del Grupo "Auditores"

adduser Roxs Auditores

### Editamos los permisos del Directorio /Home para que solo tenga acceso el propietario "u" y Auditores "g"

chmod ug+rwx,o-rwx /home

### Reforzamos la seguridad del archivo en caso logren extraerlo, para que entonces solo pueda ser rwx por el propietario o miembros de Auditores

chmod 770 Lista_Precios


*** Medidas de seguridad implementadas: *** Permisología octal expresada para los bits, en letras.
*** Tipos de usuarios que aplicarán permisos: *** Usuario Proietario, usuario perteneciente a Grupo autorizado, y Otros como no autorizados
*** Tipo de permiso: *** Permisología reforzada a directorio /home , con acceso solo a propietario y miembros de grupo Auditores. Se aplica seguridad a archivo Lista_Precios, para solo ser rwx por propietario y miembro de grupo Auditores.

