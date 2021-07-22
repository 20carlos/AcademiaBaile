<?php
 class Conexion{
     public static function Conectar(){
         define('servidor','localhost');
         define('nombre_bd','id16574164_login');
         define('usuario','id16574164_arturo');
         define('password','7X7WH|{TnlM_JD4!');         
         $opciones = array(PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES utf8');
         
         try{
            $conexion = new PDO("mysql:host=".servidor.";dbname=".nombre_bd, usuario, password, $opciones);             
            return $conexion; 
         }catch (Exception $e){
             die("El error de Conexión es :".$e->getMessage());
         }         
     }
     
 }
?>