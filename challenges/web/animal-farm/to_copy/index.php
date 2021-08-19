<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">    
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <style>
            body {background-color: #161616;color:white;}
        </style>
        <title>THE-ANIMAL-RANDOMIZER-1337</title>
    </head>
    <body>
        <div class="p-3 mb-2 text-white">
            <div class="pt-4 d-flex justify-content-center">
                <center><h1>THE-ANIMAL-RANDOMIZER-1337</h1></center>
            </div>
            <div class="container pt-3">
                <h2>Select an animal</h2>
                <form role="form" class="form-horizontal" action="index.php" method="GET">
                <div class="input-group mb-2">
                    <div class="input-group-prepend">
                      <div class="input-group-text">Animal:</div>
                    </div>

                     <select name="page" class="form-control">
                         <option value="horse.php">Horse</option>
                         <option value="cat.php">Cat</option>
                         <option value="dog.php">Dog</option>
                    </select>

                    <div class="col-auto">
                        <button id="sendbutton" type="submit" class="btn btn-primary">Submit</button>
                    </div>
                </div>
                </form>
            </div>
        </div>
            <!-- Optional JavaScript -->
            <!-- jQuery first, then Popper.js, then Bootstrap JS -->
            <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </body>
</html>

<?php

$horse = "horse.php";
$cat = "cat.php";
$dog = "dog.php";

if ( (strpos($_GET["page"], $horse) !== false) || (strpos($_GET["page"], $cat) !== false) || (strpos($_GET["page"], $dog) !== false) ) {
    include($_GET["page"]);
} else {
    echo "<center><h3>INVALID ANIMAL</h3></center>";
}

?>