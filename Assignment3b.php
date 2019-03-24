<form action="" method="POST">
Enter the size of your pizza (Small = 1) (large=2):
<br><br>
<input type="text" name="size_entered" value=''/> <br><br>
Enter the amount of toppings (max=4):
<input type="text" name="top_entered" value=''/> <br><br>
<input type="submit" name="Cost" value="Cost"/><br><br>
</form>

<?php
$pricebutton= $_POST['Cost'];
$size= $_POST['size_entered'];
$top= $_POST['top_entered'];

$HST = 0.13;

if ($pricebutton){
    if ($size ==1){
        $subtotal = 6.00;
    }
    if ($size == 2){
        $subtotal = 10.00;
    }
    
    
    if ($top ==1){
        $subtotal = $subtotal + 1.00;
    }
    if ($top ==2){
        $subtotal = $subtotal + 1.75;
    }
    if ($top ==3){
        $subtotal = $subtotal + 2.50;
    }
    if ($top ==4){
        $subtotal = $subtotal + 3.25;
    }
    
    
    $final_HST= $HST * $subtotal;
    $final_cost = $subtotal + $final_HST;
    
    echo "Subtotal:" . " " . "$" . $subtotal;
    echo " ";
   
    echo "HST:" . " " . "$" . $final_HST;
    echo " ";
    echo "Total Cost:" . " " . "$" . $final_cost;
    
}

?>