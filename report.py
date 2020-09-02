codinicio = """<!DOCTYPE html>

<head>
<title>Reporte Practica</title>
<style>
body{
    background-image: url("fondo.jpg");
    background-size: cover ;
    font-family:  Helvetica;
    text-align: center;
}
.fondo {
    position: absolute;
	left:50%;
	top:50%;
	transform: translate(-50%,-50%);
    background-color: rgba(255, 255, 255, 0.6);
	border-radius:15px;
    padding:25px 80px;
    }
th, td {
    text-align: left;
    padding: 8px;
    }
    tr:nth-child(even) {background-color: #f2f2f2;}
    </style>
</head>

<body>
    <div class="fondo">
        <form>
        <table  >
                <tr>
                    <td>No.</td> 
                    <td>NOMBRE</td> 
                    <td>EDAD</td>
                    <td>ACTIVO</td>
                    <td>PROMEDIO</td>
                </tr>
                <tr>"""
final_hmtl = """                
                </tr>
        </table>
    </form>
    </div>
</body>
</html>"""
