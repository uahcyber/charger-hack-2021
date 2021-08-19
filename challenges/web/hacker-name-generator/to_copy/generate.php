<?php

// sudo apt install php-xml

if (empty($_GET['input'])) {
    echo "There's no `input` GET parameter, n00b";
    return;
}

$xmlData = base64_decode($_GET["input"]);
$xmlData = simplexml_load_string($xmlData, null, LIBXML_NOENT) or die ("INVALID XML: " . $xmlData);

$firstName = $xmlData->firstName;
$lastName = $xmlData->lastName;

$leetCharacters = array(
    "A"=>"4",
    "a"=>"4",
    "E"=>"3",
    "e"=>"3",
    "I"=>"1",
    "i"=>"1",
    "O"=>"0",
    "o"=>"0",
    "T"=>"7",
    "t"=>"7",
    "Z"=>"2",
    "z"=>"2",
    "S"=>"5",
    "s"=>"5",
    "G"=>"6",
    "g"=>"6"
); 

$arrayFirstName = str_split($firstName);
$arrayLastName = str_split($lastName);
$leetFirstName = "";
$leetLastName = "";

foreach ($arrayFirstName as $char) { 
    if (array_key_exists($char, $leetCharacters)) {
        $leetFirstName = $leetFirstName . $leetCharacters[$char];
    } else {
        $leetFirstName = $leetFirstName . $char;
    }
};

foreach ($arrayLastName as $char) { 
    if (array_key_exists($char, $leetCharacters)) {
        $leetLastName = $leetLastName. $leetCharacters[$char];
    } else {
        $leetLastName = $leetLastName. $char;
    }
};

echo <<<EOT
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">    
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <style>
            body {background-color: #161616;}
            h2 {font-family: "Lucida Console", "Courier New", monospace;background-color:green;}
        </style>
        <title>Hacker Name Generator</title>
    </head>
    <body>
        <div class="p-3 mb-2 text-white">
            <div class="pt-4 d-flex justify-content-center">
                <center><h1>Welcome to Blue's Hacker Name Generator</h1></center>
            </div>
            <div class="container pt-3">
            <center>
            <h1>Your Hacker Name Is:</h1>
            <h2>$leetFirstName $leetLastName</h2>
            </center>
            </div>
        </div>
            <!-- Optional JavaScript -->
            <!-- jQuery first, then Popper.js, then Bootstrap JS -->
            <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </body>
</html>
EOT;
?>
