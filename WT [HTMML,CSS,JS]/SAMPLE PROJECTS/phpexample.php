<?php

// Create a 2D array to store the board
$board = array(array());

// Set the dimensions of the board
$size = 8;

// Generate the board using nested loops
for ($row = 0; $row < $size; $row++) {
    for ($col = 0; $col < $size; $col++) {
        // Determine the color of the square based on its row and column
        if (($row + $col) % 2 == 0) {
            $board[$row][$col] = 'black';
        } else {
            $board[$row][$col] = 'white';
        }
    }
}

// Print the HTML code for the chessboard
echo '<table border="1">';
for ($row = 0; $row < $size; $row++) {
    echo '<tr>';
    for ($col = 0; $col < $size; $col++) {
        $color = $board[$row][$col];
        echo "<td style='background-color: $color;'></td>";
    }
    echo '</tr>';
}
echo '</table>';

?>