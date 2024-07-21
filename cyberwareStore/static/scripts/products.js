$(document).ready(function(){
    console.log("This is a test") ;

    $(".product").click(function(){
        
        const name = $(this).data('name') ;
        console.log("Product Name is " + " " + name) ;
        if ($(this).data('grade') == 'Military') {
            $(this).css("background-color","green");
        }
        else{
            $(this).css("background-color","pink");
        };

    })
})
